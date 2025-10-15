from fastapi import APIRouter, HTTPException
from account import *
from user import *

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/login")
def login(username, password):
    user = user_from_username(username)
    if not user:
        return {"Username not found"}
    if user["password"] != password:
        return {"Password incorrect"}
    update_current_user(user)
    return {"Logged in as": user["username"]}

@router.get("/register")
def register(username, password, iban):
    new_user = add_user(username, password,iban)
    return {"New user created": new_user}

@router.get("/current_user")
def get_my_user():
    current_user = get_current_user()
    return {"Amount": current_user["username"]}

@router.get("/all_users")
def login():
    return {"Amount": users[0]["username"],"Amount1": users[1]["username"],"Amount2": users[2]["username"]}

@router.get("/read_amount_username")
def read_amount_dos(username):
    user = account_from_username(username)
    if user is None:
        return {"No account linked to this IBAN"}
    return {"Amount": user["amount"]}

@router.get("/get_all_accounts")
def get_all_accounts():
    ibans = ""
    for x in get_current_user()["accounts"]:
        ibans += x["iban"]+";"
    return {"All your accounts are": ibans}