from account import *
from beneficiary import *
import os
import hashlib
import binascii
import hmac
from dataclasses import dataclass, field
from typing import List, Optional
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

    def add_beneficiaries(self,bene: Beneficiary):
        self.Beneficiaries.append(bene)


#All users
def hash_password(password):
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    salt = os.urandom(16)  # 128-bit salt
    dk = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt,  100_000)
    return f"{ 100_000}${binascii.hexlify(salt).decode()}${binascii.hexlify(dk).decode()}"


Liam = User("Liam", hash_password("furryfemboy"), [LiamAccount],LiamAccount,[GhaziBeneficiary])
Ghazi = User("Ghazi", hash_password("jadorelespieds"), [GhaziAccount],GhaziAccount,[])
Adam = User("Adam", hash_password("futa"), [AdamAccount], AdamAccount,[])

CurrentUser = Liam

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


def verify_password(stored_hash: str, password_attempt: str) -> bool:
    try:
        iterations_str, salt_hex, hash_hex = stored_hash.split('$')
        iterations = int(iterations_str)
        salt = binascii.unhexlify(salt_hex)
        expected_hash = binascii.unhexlify(hash_hex)
    except Exception:
        return False

    derived = hashlib.pbkdf2_hmac('sha256', password_attempt.encode('utf-8'), salt, iterations)
    return hmac.compare_digest(derived, expected_hash)
