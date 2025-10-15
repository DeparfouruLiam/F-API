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

CurrentUser: User = Liam


users = [Liam, Adam, Ghazi]


def get_users():
    return users


def account_from_username(username):
    account = next((x for x in get_users() if x["username"] == username), None)["mainAccount"]
    return account_from_iban(account["iban"])
