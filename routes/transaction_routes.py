from fastapi import APIRouter, HTTPException
from account import *
from user import *

router = APIRouter(prefix="/transaction", tags=["Transaction"])

@router.post("/transfer")
def transfer_amount(receiveriban,amount):
    current_account = get_current_account()
    sender = account_from_iban(current_account.get_iban())
    if sender is None:
        return {"No account linked to the IBAN of the sender"}
    receiver = account_from_iban(receiveriban)
    if receiver is None:
        return {"No account linked to the IBAN of the receiver"}
    if sender is receiver:
        return {"Transfer must be from one account to another"}
    if int(amount) > sender.get_amount():
        return {"Sender doesn't have enough to transfer the amount"}
    sender.take_amount(amount)
    receiver.add_amount(amount)

    current_transaction = Transaction(sender.get_iban(), receiveriban, amount)
    sender.get_transactions().append(current_transaction)
    receiver.get_transactions().append(current_transaction)

    return {"The transfer was successful. "+sender.get_iban()+" new amount": sender.get_amount(), receiveriban+" new amount": receiver.get_amount()}
