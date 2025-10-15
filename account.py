from typing import TypedDict
from transaction import *

class Account(TypedDict):
    amount: int
    iban: str
    transactions: list[Transaction]


#All accounts
LiamAccount: Account = {"amount": 100, "iban": "Aled", "transactions": [TransactionLG]}
GhaziAccount: Account = {"amount": 10, "iban": "Yiouiuh", "transactions": [TransactionLG]}
AdamAccount: Account = {"amount": 50, "iban": "Buranyah", "transactions": []}

accounts = [LiamAccount, GhaziAccount, AdamAccount]
def get_amount(account):
    return account["amount"]

def get_accounts():
    return accounts

def account_from_iban(iban):
    return next((x for x in get_accounts() if x["iban"] == iban), None)

