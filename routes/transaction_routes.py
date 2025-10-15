from fastapi import APIRouter, HTTPException
from account import *
from user import account_from_username, CurrentUser

router = APIRouter(prefix="/transaction", tags=["Transaction"])


@router.get("/transfer")
def transfer_amount(receiveriban,amount):
    sender = account_from_username(CurrentUser["username"])
    if sender is None:
        return {"No account linked to the IBAN of the sender"}
    receiver = account_from_iban(receiveriban)
    if receiver is None:
        return {"No account linked to the IBAN of the receiver"}
    if int(amount) > sender["amount"]:
        return {"Sender doesn't have enough to transfer the amount"}
    sender.update({"amount": get_amount(sender) - int(amount)})
    receiver.update({"amount": get_amount(receiver) + int(amount)})

    current_transaction: Transaction = {"ibanSender": sender["iban"], "ibanReceiver": receiveriban, "amount": amount}
    sender["transactions"].append(current_transaction)
    receiver["transactions"].append(current_transaction)

    return {"The transfer was successful. "+sender["iban"]+" new amount": sender["amount"], receiveriban+" new amount": receiver["amount"]}
