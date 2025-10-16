from datetime import  timedelta, timezone, datetime
from threading import Thread
import time
from fastapi import APIRouter, HTTPException
from account import *
from user import *
import config

router = APIRouter(prefix="/transaction", tags=["Transaction"])

@router.post("/transfer")
def transfer_amount(receiveriban,amount):
    sender = get_current_account()
    if sender.get_iban() is None:
        return {"No account linked to the IBAN of the sender"}
    receiver = account_from_iban(receiveriban)
    if receiver is None:
        return {"No account linked to the IBAN of the receiver"}
    if sender is receiver:
        return {"Transfer must be from one account to another"}
    if int(amount) > sender.get_amount():
        return {"Sender doesn't have enough to transfer the amount"}
    current_transaction = Transaction(sender.get_iban(), receiveriban, amount)

    config.transactionCount+=1
    create_thread(current_transaction)

    return {"The transfer was successful. "+sender.get_iban()+" new amount": sender.get_amount(), receiveriban+" new amount": receiver.get_amount()}

def create_thread(trs: Transaction):
    thread = Thread(target=check_flag_later, args=(trs.id,))
    account_from_iban(trs.ibanSender).transactions.append(trs)
    account_from_iban(trs.ibanReceiver).transactions.append(trs)
    thread.start()
    return {"message": "Object created and background check started."}


def check_flag_later(id:int  ):
    time.sleep(5)
    for trs in get_current_account().get_transactions():
        if trs.id == id:
            if not trs.cancelled :
                account_from_iban(trs.ibanSender).take_amount( int(trs.amount) )
                account_from_iban(trs.ibanReceiver).add_amount( int(trs.amount ))
                print("Flag is still False after 5 seconds!")
            else:
                print("Flag was set to True before 5 seconds.")

@router.get("/cancelTransaction")
def cancel_transaction():
    i:int  =0
    for transaction in get_current_account().get_transactions() :
        if transaction.ibanSender  == get_current_account().iban :
            if transaction.ibanReceiver  != get_current_account().iban :
                if not transaction.cancelled:
                    if datetime.now(timezone.utc) - transaction.date.replace(tzinfo=timezone.utc) <= timedelta(seconds=10):
                        get_current_account().transactions[i].cancelled=True
                        return transaction.ibanReceiver ,transaction.ibanSender ,transaction.amount ,datetime.now(timezone.utc) - transaction.date .replace(tzinfo=timezone.utc)
        i=i+1
    return  datetime.now(timezone.utc)

@router.get("/ShowTransaction")
def show_transaction():
    current_account = get_current_account()
    return {"transactions": current_account.get_transactions()}


@router.get("/Addmoney")
def add_money(amount: int):
    current_account = get_current_account()
    if current_account is None:
        raise HTTPException(status_code=400, detail="No account found")

    if amount < 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    current_account.add_amount(amount)
    add_transaction_self(amount)

    return {"new_balance": current_account.get_amount()}
