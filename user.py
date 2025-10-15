from typing import TypedDict
from account import *
from beneficiary import *

class User(TypedDict):
    username: str
    password: str
    accounts: list[Account]
    mainAccount: Account
    Beneficiaries: list[Beneficiary]

#All users
Liam: User = {"username": "Liam", "password": "furryfemboy", "accounts": [LiamAccount],"mainAccount":LiamAccount,"Beneficiaries": [GhaziBeneficiary]}
Ghazi: User = {"username": "Ghazi", "password": "jadorelespieds", "accounts": [GhaziAccount],"mainAccount":GhaziAccount,"Beneficiaries": []}
Adam: User = {"username": "Adam", "password":"futa", "accounts": [AdamAccount],"mainAccount": AdamAccount,"Beneficiaries": []}

CurrentUser: User = {"username": "Not connected", "password": "jspgros", "accounts": [],"mainAccount":None,"Beneficiaries": []}

users = [Liam, Adam, Ghazi]

def get_users():
    return users

def get_current_user():
    return CurrentUser

def add_user(username: str, password: str, iban: str):
    new_account = add_account(iban)
    new_user: User = {"username": username, "password": password, "accounts": [new_account],"mainAccount":new_account,"Beneficiaries": []}
    users.append(new_user)
    return new_user

def update_current_user(new_user):
    CurrentUser.update(new_user)
    return CurrentUser

def user_from_username(username):
    return next((x for x in get_users() if x["username"] == username), None)

def account_from_username(username):
    account = user_from_username(username)["mainAccount"]
    return account_from_iban(account["iban"])
