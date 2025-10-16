from fastapi import APIRouter, HTTPException
from account import *
from user import *

import os
import hashlib
import binascii
import hmac
from dataclasses import dataclass, field
from typing import List, Optional

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/login")
def login(username, password):
    user = user_from_username(username)
    if not user:
        return {"Username not found"}
    if not verify_password(user.get_password(), password):
        return {"Password incorrect"}
    update_current_user(user)
    update_current_account(user.get_main_account())
    return {"message": "Logged in as", "username": user.get_username()}

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


