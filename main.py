from typing import TypedDict
from fastapi import FastAPI, Depends
from user import *
from account import *
app = FastAPI()

def get_accounts():
    return accounts

def get_users():
    return users

def get_amount(account):
    return account["amount"]

def account_from_iban(iban):
    return next((x for x in get_accounts() if x["iban"] == iban), None)

def account_from_username(username):
    account = next((x for x in get_users() if x["username"] == username), None)["mainAccount"]
    return account_from_iban(account["iban"])

@app.get("/transfer")
def transfer_amount(senderiban,receiveriban,amount):
    sender = account_from_iban(senderiban)
    if sender is None:
        return {"No account linked to the IBAN of the sender"}
    receiver = account_from_iban(receiveriban)
    if receiver is None:
        return {"No account linked to the IBAN of the receiver"}
    if int(amount) > sender["amount"]:
        return {"Sender doesn't have enough to transfer the amount"}
    sender.update({"amount": get_amount(sender) - int(amount)})
    receiver.update({"amount": get_amount(receiver) + int(amount)})
    return {"The transfer was successful. "+senderiban+" new amount": sender["amount"], receiveriban+" new amount": receiver["amount"]}

@app.get("/read_amount")
def read_amount(iban):
    user = account_from_iban(iban)
    if user is None:
        return {"No account linked to this IBAN"}
    return {"Amount": user["amount"]}

@app.get("/read_amount_username")
def read_amount_dos(username):
    user = account_from_username(username)
    if user is None:
        return {"No account linked to this IBAN"}
    return {"Amount": user["amount"]}