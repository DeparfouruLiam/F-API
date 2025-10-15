from fastapi import APIRouter, HTTPException
from account import *

router = APIRouter(prefix="/transaction", tags=["transaction"])


@router.get("/transfer")
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
