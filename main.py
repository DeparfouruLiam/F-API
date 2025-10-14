from typing import TypedDict
from fastapi import FastAPI, Depends
app = FastAPI()

class Transaction(TypedDict):
    ibanSender: str
    ibanReceiver: str
    amount: int

class Account(TypedDict):
    amount: int
    iban: str
    transactions: list[Transaction]

class Beneficiary(TypedDict):
    username: str
    iban: str

class Users(TypedDict):
    username: str
    password: str
    accounts: list[Account]
    mainAccount: Account
    Beneficiaries: list[Beneficiary]



users = [{"username": "Liam", "password": "furryfemboy", "accounts": [],"mainAccount":None,"Beneficiary": []},{"username": "Ghazi", "password": "jadorelespieds", "accounts": [],"mainAccount":None,"Beneficiary": []},{"username": "Adam", "password":"futa", "accounts": [],"mainAccount": None,"Beneficiary": []}]
accounts = [{"amount": 100, "iban": "Aled", "transactions": []},{"amount": 10, "iban": "Yiouiuh", "transactions": []},{"amount": 50, "iban": "Buranyah", "transactions": []}]
beneficiaries = [{"username": "Ghazi","iban": "Buranyah"}]
transactions = [{"ibanSender": "Aled", "ibanReceiver": "Yiouiuh", "Amount":20}]



def get_accounts():
    return accounts

def get_amount(account):
    return account["amount"]


def account_from_iban(iban):
    return next((x for x in get_accounts() if x["iban"] == iban), None)

@app.get("/transfer")
def transfer_amount(sender,receiver,amount):
    sender = account_from_iban(sender)
    receiver = account_from_iban(receiver)
    sender.update({"amount": get_amount(sender) - int(amount)})
    receiver.update({"amount": get_amount(receiver) + int(amount)})

@app.get("/read_amount")
def read_amount(user):
    user = account_from_iban(user)
    return {"Amount": user["amount"]}