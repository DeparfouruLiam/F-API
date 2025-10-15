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


users = [Liam, Adam, Ghazi]
