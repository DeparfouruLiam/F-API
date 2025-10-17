from fastapi import APIRouter, HTTPException
from account import *
from user import *

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.get("/read_amount")
def read_amount(iban):
    user = account_from_iban(iban)
    if user is None:
        return {"No account linked to this IBAN"}
    return {"Amount": user.get_amount()}


@router.get("/choose_current_account")
def choose_current_account(iban):
    if CurrentUser is None:
        return {"Not connected"}
    account = user_account_from_iban(iban, get_current_user().get_accounts())
    if account is None:
        return {"No account linked to this IBAN in your accounts"}
    update_current_account(account)
    return {"Current account successfully updated to": account}


@router.get("/create_new_account")
def create_new_account(iban):
    if iban in [x.get_iban() for x in accounts]:
        return {"Iban already in use"}
    new_account = add_account(iban)
    user = get_current_user()
    user.get_accounts().append(new_account)
    return {"New account successfully created to": new_account}


@router.get("/current_account")
def get_my_account():
    current_account = get_current_account()
    return {"Amount": current_account.get_iban()}


@router.delete("/delete_account")
def delete_account(iban: str):
    user = get_current_user()
    if user is None:
        raise HTTPException(status_code=401, detail="Not connected")

    account = account_from_iban(iban)
    if account is None:
        raise HTTPException(status_code=404, detail="No account linked to this IBAN")

    if account not in user.get_accounts():
        raise HTTPException(status_code=403, detail="You do not own this account")

    # On définit le compte principal (le premier dans la liste)
    main_account = user.get_accounts()[0]

    # On empêche la suppression du compte principal
    if account == main_account:
        raise HTTPException(status_code=400, detail="You cannot delete your main account")

    # 🔁 Transfert du solde vers le compte principal
    if account.get_amount() > 0:
        main_account.add_amount(account.get_amount())
        account.take_amount(account.get_amount())

    # 🔄 Si le compte supprimé était le compte courant, on repasse au principal
    global CurrentAccount
    if CurrentAccount.get_iban() == iban:
        update_current_account(main_account)

    # 🗑️ Suppression du compte
    accounts.remove(account)
    user.get_accounts().remove(account)

    return {
        "message": f"Account {iban} successfully deleted. Balance transferred to main account {main_account.get_iban()}",
        "main_account_new_balance": main_account.get_amount()
    }
