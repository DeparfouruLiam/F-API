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
