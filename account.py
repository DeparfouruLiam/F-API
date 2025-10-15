from typing import TypedDict
from transaction import *
from user import *

class Account(TypedDict):
    amount: int
    iban: str
    transactions: list[Transaction]


#All accounts
LiamAccount: Account = {"amount": 100, "iban": "Aled", "transactions": [TransactionLG]}
GhaziAccount: Account = {"amount": 10, "iban": "Yiouiuh", "transactions": [TransactionLG]}
AdamAccount: Account = {"amount": 50, "iban": "Buranyah", "transactions": []}

CurrentAccount: Account = {"amount": 0, "iban": "", "transactions": []}

accounts = [LiamAccount, GhaziAccount, AdamAccount]

def get_amount(account):
    return account["amount"]

def get_accounts():
    return accounts

def get_current_account():
    return CurrentAccount["iban"]

def add_account(iban: str):
    new_account: Account = {"amount": 0, "iban": iban, "transactions": []}
    accounts.append(new_account)
    return new_account


def update_current_account(new_account):
    CurrentAccount.update(new_account)
    return CurrentAccount

def account_from_iban(iban):
    return next((x for x in get_accounts() if x["iban"] == iban), None)

def user_account_from_iban(iban,user_accounts):
    return next((x for x in user_accounts if x["iban"] == iban), None)