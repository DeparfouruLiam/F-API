from fastapi import APIRouter, HTTPException
from account import *
from user import CurrentUser, get_current_user

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.get("/read_amount")
def read_amount():
    user = get_iban()
    if user is None:
        return {"No account linked to this IBAN"}
    return {"Amount": user.get_amount()}

@router.get("/choose_current_account")
def choose_current_account(iban):
    if CurrentUser is None:
        return {"Not connected"}
    account = user_account_from_iban(iban,get_current_user().get_accounts())
    if account is None:
        return {"No account linked to this IBAN in your accounts"}
    update_current_account(account)
    return {"Current account successfully updated to": account}

# @router.get("/create_new_account")
# def create_new_account(iban):
#     if iban in [x.get_iban() for x in accounts]:
#         return {"Iban already in use"}
#     new_account = add_account(iban)
#     user = get_current_user()
#     user.get_accounts().append(new_account)
#     return {"New account successfully created to": new_account}

@router.get("/current_account")
def get_my_account():
    return {"Iban": get_iban()}
