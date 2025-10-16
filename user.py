from typing import TypedDict
from account import account_from_iban, Account, liam_account,ghazi_account,adam_account
from beneficiary import *
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    accounts: list[Account]
    mainAccount: Account
    Beneficiaries: list[Beneficiary]

    def getUsername(self) -> str:
        return self.username
#All users
liam = User(username="Liam", password ="furryfemboy", accounts= [liam_account], mainAccount=liam_account, Beneficiaries= [ghazi_beneficiary])
ghazi = User(username="Ghazi", password="jadorelespieds", accounts= [ghazi_account], mainAccount=ghazi_account, Beneficiaries= [])
adam = User(username="Adam", password="futa", accounts= [adam_account], mainAccount= adam_account, Beneficiaries= [])

current_user = liam


users = [liam, adam, ghazi]

def get_users():
    return users



def account_from_username(username):
    user = next((x for x in get_users() if x.getUsername() == username), None)
    if not user:
        return None
    return account_from_iban(user.mainAccount.iban)