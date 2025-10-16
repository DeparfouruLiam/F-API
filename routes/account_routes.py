from fastapi import APIRouter, HTTPException, Depends
from account import *
from database import get_session
from user import CurrentUser, get_current_user, getCurrentUserId
from pydantic import BaseModel

router = APIRouter(prefix="/accounts", tags=["Accounts"])

class CreateAccount(BaseModel):
    iban: str

@router.get("/current_account_amount")
def read_amount(session = Depends(get_session)):
    account = get_iban()
    if account is "":
        return {"No account linked to this IBAN"}
    amount = session.query(Account).filter_by(user_id=getCurrentUserId()).first()
    return {"Amount": amount.amount}

@router.get("/choose_current_account")
def choose_current_account(iban, session=Depends(get_session)):
    if getCurrentUserId() is 0:
        return {"Not connected"}
    new_account = session.query(Account).filter_by(iban=iban).first()
    if new_account is None:
        return {"No account linked to this IBAN in your accounts"}
    update_account_id(new_account.id)
    return {"Current account successfully updated to": new_account.iban}

@router.post("/create_account", response_model=CreateAccount)
def create_account(body: CreateAccount, session = Depends(get_session)) -> Account:
    if getCurrentUserId() == 0:
        raise HTTPException(status_code=404, detail="User not connected")
    account = Account(amount=100, iban=body.iban, user_id=getCurrentUserId())
    session.add(account)
    session.commit()
    session.refresh(account)
    return account

@router.get("/current_account")
def get_my_account():
    return {"Iban": get_iban()}
