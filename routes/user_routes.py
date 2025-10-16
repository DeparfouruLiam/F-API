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

@router.post("/login")
def login(user: CreateUser):
    return {"token": generate_token(user)}

@router.get("/meme")
def me(user=Depends(get_user)):
    return user
@router.get("/a", response_model=str)
async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    username: str
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username

@router.post("/Login")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    user = user_from_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="Username not found")
    if not verify_password(user.get_password(), password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}
@router.get("/me")
def get_current_user_info(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    username = payload.get("sub")
    user = user_from_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"username": user.get_username()}
@router.get("/register")
def register(username: str, password: str, iban: Optional[str] = None):
    # Critère : l'email doit être unique
    if username in [x.get_username() for x in users]:
        return {"error": "Username  already in use"}
    hashed = hash_password(password)
    new_user = add_user(username, hashed, iban)
    return {"message": "New user created", "email": new_user.password}

@router.get("/current_user")
def get_my_user():
    current_user = get_current_user()
    return {"Amount": current_user.get_username()}, current_user.get_password()

@router.get("/read_amount_username")
def read_amount_dos(username):
    user = account_from_username(username)
    if user is None:
        return {"No account linked to this IBAN"}
    return {"Amount": user.get_amount()}

@router.get("/get_all_accounts")
def get_all_accounts():
    ibans = ""
    for x in get_current_user().get_accounts():
        ibans += x.get_iban()+" : "+str(x.get_amount())+" zennys ; "
    return {"All your accounts are": ibans}
@router.post("/addBeneficiary")
def add_Beneficiary(name: str, iban: str):
    if not account_from_iban(iban) is None:
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


