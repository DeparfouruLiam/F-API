from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from database import *
from newclass import *
from user import *

router = APIRouter(prefix="/database", tags=["Database"])

class CreateAccount(BaseModel):
    iban: str

@router.post("/create_account_db", response_model=CreateAccount)
def create_account(body: CreateAccount, session = Depends(get_session)) -> Account:
    account = Account(amount=100, iban=body.iban, user_id=getCurrentUserId())
    session.add(account)
    session.commit()
    session.refresh(account)
    return account

@router.get("/aaaaaaaaa")
def get_user_id():
    return {"ID": getCurrentUserId()}
