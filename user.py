from typing import TypedDict
from account import *
from account import account_from_iban
from beneficiary import *

class User:
    username: str
    password: str
    accounts: list[Account]
    mainAccount: Account
    Beneficiaries: list[Beneficiary]

    def __init__(self, username: str, password: str, accounts_list: list[Account], mainAccount: Account, Beneficiaries: list[Beneficiary]):
        self.username = username
        self.password = password
        self.accounts = accounts_list
        self.mainAccount = mainAccount
        self.Beneficiaries = Beneficiaries

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_accounts(self):
        return self.accounts

    def get_main_account(self):
        return self.mainAccount

    def get_beneficiaries(self):
        return self.Beneficiaries


#All users
Liam = User("Liam", "furryfemboy", [LiamAccount],LiamAccount,[GhaziBeneficiary])
Ghazi = User("Ghazi", "jadorelespieds", [GhaziAccount],GhaziAccount,[])
Adam = User("Adam", "futa", [AdamAccount], AdamAccount,[])

CurrentUser = User

users = [Liam, Adam, Ghazi]

def get_users():
    return users

def get_current_user():
    return CurrentUser

def add_user(username: str, password: str, iban: str):
    new_account = add_account(iban)
    new_user = User(username, password, [new_account],new_account,[])
    users.append(new_user)
    return new_user

def update_current_user(new_user):
    global CurrentUser
    CurrentUser = new_user
    return CurrentUser

def user_from_username(username):
    return next((x for x in get_users() if x.get_username() == username), None)

def account_from_username(username):
    account = user_from_username(username).get_main_account()
    return account_from_iban(account.get_iban())
