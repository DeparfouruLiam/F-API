from typing import TypedDict

class Transaction(TypedDict):
    ibanSender: str
    ibanReceiver: str
    amount: int

#All transactions
TransactionLG: Transaction = {"ibanSender": "Aled", "ibanReceiver": "Yiouiuh", "amount":20}
