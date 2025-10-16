from typing import TypedDict
from transaction import *
from user import *

class Account:
    amount: int
    iban: str
    transactions: list[Transaction]
    
    def __init__(self, amount: int, iban: str,transaction: list[Transaction]) -> None:
        self.amount = amount
        self.iban = iban
        self.transactions = transaction

    def get_iban(self) -> str:
        return self.iban

    def get_amount(self) -> int:
        return self.amount

    def get_transactions(self) -> list[Transaction]:
        return self.transactions

    def add_amount(self, amount: int) -> None:
        self.amount += int(amount)
    def take_amount(self, amount: int) -> None:
        self.amount -= int(amount)

#All accounts
LiamAccount = Account (100, "Aled", [TransactionLG])
GhaziAccount = Account (10, "Yiouiuh", [TransactionLG])
AdamAccount = Account (50, "Buranyah", [])

CurrentAccount = Account (0,  "",  [])

accounts = [LiamAccount, GhaziAccount, AdamAccount]

def get_amount(account):
    return account.get_amount()

def get_accounts():
    return accounts

def get_current_account():
    return CurrentAccount

def add_account(iban: str):
    new_account = Account(0, iban, [])
    accounts.append(new_account)
    return new_account

def update_current_account(new_account):
    global CurrentAccount
    CurrentAccount = new_account
    return CurrentAccount

def account_from_iban(iban):
    return next((x for x in get_accounts() if x.get_iban() == iban), None)

def user_account_from_iban(iban,user_accounts):
    return next((x for x in user_accounts if x.get_iban() == iban), None)