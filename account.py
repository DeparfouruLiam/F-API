from transaction import *
from pydantic import BaseModel
from datetime import datetime


class Account(BaseModel):
    amount: int
    iban: str
    transactions: list[Transaction]


#All accounts
liam_account = Account(amount= 100, iban="Aled", transactions= [transaction_lg])
ghazi_account = Account(amount= 200, iban="Yiouiuh", transactions= [transaction_lg])
adam_account = Account(amount= 50, iban="Buranyah", transactions= [])

CurrentAccount: Account = liam_account

accounts = [liam_account, ghazi_account, adam_account]
def get_amount(account):
    return account.amount 

def get_accounts():
    return accounts

def account_from_iban(iban):
    return next((x for x in get_accounts() if x.iban  == iban), None)

def add_transaction(receiver:Account, amount):
    tmpTransaction:Transaction = Transaction(ibanSender= CurrentAccount.iban , ibanReceiver= receiver.iban , amount= amount, date= datetime.now(UTC).isoformat(), cancelled=False)
    CurrentAccount.transactions .append(tmpTransaction)
    receiver.transactions .append(tmpTransaction)
    return

def add_transaction_self(amount):
    tmpTransaction:Transaction = Transaction(ibanSender= CurrentAccount.iban , ibanReceiver= CurrentAccount.iban , amount= amount, date= datetime.now(UTC).isoformat(), cancelled=False)
    CurrentAccount.transactions .append(tmpTransaction)
    return
