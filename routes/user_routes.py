from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from account import *
from database import get_session
from user import *
from newclass import *

router = APIRouter(prefix="/user", tags=["User"])

class CreateUser(BaseModel):
    username: str
    password: str

class CreateAccount(BaseModel):
    iban: str

@router.post("/register")
def register_user(body: CreateUser,body_account:CreateAccount, session = Depends(get_session)) -> User:
    account = Account(amount=100, iban=body_account.iban, user_id=getCurrentUserId(),is_main=True)
    user = User(username=body.username, password=body.password)
    session.add(user)
    session.add(account)
    session.commit()
    session.refresh(user)
    session.refresh(account)
    return user

@router.post("/login")
def login(body: CreateUser, session = Depends(get_session)) -> User:
    user = session.query(User).filter_by(username=body.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.password != body.password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    main_account = session.query(Account).filter_by(user_id=getCurrentUserId(),is_main=True).first()

    update_iban(main_account.iban)
    update_account_id(main_account.id)
    update_amount(main_account.amount)

    update_current_id(user.id)
    update_current_name(user.username)
    return user

@router.get("/current_user")
def get_my_user():
    return {"ID": getCurrentUserId(),"username": getCurrentUserName()}

# @router.get("/get_all_accounts")
# def get_all_accounts():
#     ibans = ""
#     for x in get_current_user().get_accounts():
#         ibans += x.get_iban()+" : "+str(x.get_amount())+" zennys ; "
#     return {"All your accounts are": ibans}