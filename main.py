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

class User(TypedDict):
    username: str
    password: str
    accounts: list[Account]
    mainAccount: Account
    Beneficiaries: list[Beneficiary]

#All transactions
TransactionLG: Transaction = {"ibanSender": "Aled", "ibanReceiver": "Yiouiuh", "amount":20}

#All beneficiaries
GhaziBeneficiary: Beneficiary = {"username": "Ghazi","iban": "Yiouiuh"}

#All accounts
LiamAccount: Account = {"amount": 100, "iban": "Aled", "transactions": [TransactionLG]}
GhaziAccount: Account = {"amount": 10, "iban": "Yiouiuh", "transactions": [TransactionLG]}
AdamAccount: Account = {"amount": 50, "iban": "Buranyah", "transactions": []}

#All users
Liam: User = {"username": "Liam", "password": "furryfemboy", "accounts": [LiamAccount],"mainAccount":LiamAccount,"Beneficiaries": [GhaziBeneficiary]}
Ghazi: User = {"username": "Ghazi", "password": "jadorelespieds", "accounts": [GhaziAccount],"mainAccount":GhaziAccount,"Beneficiaries": []}
Adam: User = {"username": "Adam", "password":"futa", "accounts": [AdamAccount],"mainAccount": AdamAccount,"Beneficiaries": []}

#Lists created
users = [Liam, Adam, Ghazi]
accounts = [LiamAccount, GhaziAccount, AdamAccount]

# users = [{"username": "Liam", "password": "furryfemboy", "accounts": [],"mainAccount":None,"Beneficiaries": []},{"username": "Ghazi", "password": "jadorelespieds", "accounts": [],"mainAccount":None,"Beneficiaries": []},{"username": "Adam", "password":"futa", "accounts": [],"mainAccount": None,"Beneficiaries": []}]
# accounts = [{"amount": 100, "iban": "Aled", "transactions": []},{"amount": 10, "iban": "Yiouiuh", "transactions": []},{"amount": 50, "iban": "Buranyah", "transactions": []}]
# beneficiaries = [{"username": "Ghazi","iban": "Yiouiuh"}]
# transactions = [{"ibanSender": "Aled", "ibanReceiver": "Yiouiuh", "Amount":20}]
#
# accounts[0]["transactions"].append(transactions[0])
#
# users[0]["accounts"].append(accounts[0])
# users[1]["accounts"].append(accounts[2])
# users[3]["accounts"].append(accounts[3])
#
# users[0]["Beneficiaries"].append(accounts[0])


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
def transfer_amount(sender,receiver,amount):
    sender = account_from_iban(sender)
    receiver = account_from_iban(receiver)
    sender.update({"amount": get_amount(sender) - int(amount)})
    receiver.update({"amount": get_amount(receiver) + int(amount)})

@app.get("/read_amount")
def read_amount(iban):
    user = account_from_iban(iban)
    if user is None:
        return {"No account linked to this IBAN"}
    return {"Amount": user["amount"]}

@app.get("/read_amount_dos")
def read_amount_dos(username):
    user = account_from_username(username)
    if user is None:
        return {"No account linked to this IBAN"}
    return {"Amount": user["amount"]}