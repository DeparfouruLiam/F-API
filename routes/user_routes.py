from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from account import *
from database import get_session
from user import *
from newclass import *
from fastapi import APIRouter, HTTPException,Depends,status,Form
from pydantic import BaseModel

from user import *
from auth import *
from fastapi.security import OAuth2PasswordBearer
from typing import List, Optional
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status


bearer_scheme = HTTPBearer()
router = APIRouter(prefix="/user", tags=["User"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="Login")

import jwt
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

secret_key = "very_secret_key"
algorithm = "HS256"
security = HTTPBearer()

class CreateUser(BaseModel):
    username: str
    password: str
class CreateAccount(BaseModel):
    iban: str

def get_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)
):
    try:
        payload = jwt.decode(credentials.credentials, secret_key, algorithms=[algorithm])
        return payload  # You can also return a user object or dict here
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
def generate_token(user: CreateUser):
    return jwt.encode(user.dict(), secret_key, algorithm=algorithm)


@router.post("/register")
def register_user(body: CreateUser,body_account:CreateAccount, session = Depends(get_session)) -> str:
    user = session.query(User).filter_by(username=body.username).first()
    if user:
        raise HTTPException(status_code=404, detail="Username already used")
    user = User(username=body.username, password=body.password)
    session.add(user)
    session.commit()
    session.refresh(user)
    account = Account(amount=100, iban=body_account.iban, user_id=user.id, is_main=True)
    session.add(account)
    session.commit()
    session.refresh(account)
    login(CreateUser(username=body.username, password=body.password),session)
    return "Account created"
@router.post("/login")
def login(user: CreateUser):
    return {"token": generate_token(user)}

@router.get("/meme")
def me(user=Depends(get_user)):
    return user
@router.get("/current_user")
def get_my_user():
    return {"ID": getCurrentUserId(),"username": getCurrentUserName()}

@router.get("/get_all_accounts")
def get_all_accounts(session = Depends(get_session)):
    ibans = ""
    all_accounts = session.query(Account).filter_by(user_id=getCurrentUserId()).all()
    for x in all_accounts:
        ibans += x.iban+" : "+str(x.amount)+" zennys ; "
    return {"All your accounts are": ibans}

@router.post("/addBeneficiary")
def add_Beneficiary(name: str, iban: str):
    if not account_from_iban(iban) is None: #chercher avec bdd
        for bene in get_current_user().get_beneficiaries():
            if bene.get_iban() == iban:
                return "Beneficiary already exists"
        beneficiary = Beneficiary(iban, name)
        get_current_user().add_beneficiaries(beneficiary)
        return "beneficiary added successfully",get_current_user().get_beneficiaries(),iban
    else:
        return "beneficiary could not be added"

@router.get("/showBeneficiary")
def show_Beneficiary():
    return get_current_user().get_beneficiaries()


