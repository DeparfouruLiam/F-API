import time
from threading import Thread
from tokenize import String

from fastapi import APIRouter, HTTPException
from account import *
from config import transactionCount

router = APIRouter(prefix="/transaction", tags=["Transaction"] )



def transfer_amount_reverse(senderiban,receiveriban,amount):
    sender = account_from_iban(senderiban)
    receiver = account_from_iban(receiveriban)
    if int(amount) > sender.amount :
        return {"Sender doesn't have enough to transfer the amount"}
    sender.amount-= int(amount)
    receiver.amount+= int(amount)
    return {"The transfer was successful. "+senderiban+" new amount": sender.amount , receiveriban+" new amount": receiver.amount }


@router.get("/Addmoney")
def add_money(amount):
    if CurrentAccount is None:
        return {"pute"}
    if int(amount) < 0:
        return {"Sender 'doesnt have enough to transfer the amount"}
    #sender.update({"amount": get_amount(sender) - int(amount)})
    #receiver.update({"amount": get_amount(receiver) + int(amount)})
    CurrentAccount.amount+=int(amount)
    add_transaction_self(amount)
    return { get_amount(CurrentAccount) }

@router.get("/showTransactions")
def show_transaction():
    return  CurrentAccount.transactions 
def show_transaction(id:int):
    for accounts in CurrentAccount.accounts:
        for transaction in accounts.transactions:
            if transaction.id == id:
                return transaction
    return{"No transaction found"}
@router.get("/cancelTransaction")
def cancel_transaction():
    i:int  =0
    for transaction in CurrentAccount.transactions :
        if transaction.ibanSender  == CurrentAccount.iban :
            if transaction.ibanReceiver  != CurrentAccount.iban :
                if not transaction.cancelled:
                    if datetime.now(timezone.utc) - transaction.date .replace(tzinfo=timezone.utc)+timedelta(seconds=7200) <= timedelta(seconds=10):
                        transfer_amount_reverse(transaction.ibanReceiver ,transaction.ibanSender ,transaction.amount )
                        CurrentAccount.transactions[i].cancelled=True
                        return transaction.ibanReceiver ,transaction.ibanSender ,transaction.amount ,datetime.now(timezone.utc) - transaction.date .replace(tzinfo=timezone.utc)+timedelta(seconds=7200)
        i=i+1
    return  "No valid transaction to cancel"

@router.get("/transfer")
def transfer_amount(receiveriban,amount):
    if CurrentAccount is None:
        return {"No account linked to the IBAN of the sender"}
    receiver = account_from_iban(receiveriban)
    if receiver is None:
        return {"No account linked to the IBAN of the receiver"}
    if int(amount) > CurrentAccount.amount :

        return {"Sender doesn't have enough to transfer the amount"}
    tmpTransaction: Transaction = Transaction(ibanSender= CurrentAccount.iban , ibanReceiver= receiveriban,
                                       amount= amount, date= datetime.now(UTC), cancelled= False ,id= config.transactionCount )
    create_thread(tmpTransaction)
    config.transactionCount+=1
    return {"The transfer was successful. "+CurrentAccount.iban +" new amount": CurrentAccount.amount , receiveriban+" new amount": receiver.amount }

def create_thread(trs: Transaction):
    thread = Thread(target=check_flag_later, args=(trs,))
    account_from_iban(trs.ibanSender).transactions.append(trs)
    account_from_iban(trs.ibanReceiver).transactions.append(trs)
    thread.start()
    return {"message": "Object created and background check started."}


def check_flag_later(trs:Transaction  ):
    time.sleep(5)
    if not trs.cancelled :
        account_from_iban(trs.ibanSender).amount -=  int(trs.amount )
        account_from_iban(trs.ibanReceiver).amount+=  int(trs.amount )
        print("Flag is still False after 5 seconds!")
    else:
        print("Flag was set to True before 5 seconds.")
