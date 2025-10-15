from fastapi import APIRouter, HTTPException
from account import *
from user import *

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/login")
def login(username, password):
    user = user_from_username(username)
    if not user:
        return {"Username not found"}
    if user.get_password() != password:
        return {"Password incorrect"}
    update_current_user(user)
    update_current_account(user.get_main_account())
    return {"Logged in as": user.get_username()}

@router.get("/register")
def register(username, password, iban):
    if username in [x.get_username() for x in users]:
        return {"Username already in use"}
    new_user = add_user(username, password,iban)
    return {"New user created": new_user}

@router.get("/current_user")
def get_my_user():
    current_user = get_current_user()
    return {"Amount": current_user.get_username()}

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