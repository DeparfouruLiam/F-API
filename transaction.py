from typing import TypedDict

class Transaction(TypedDict):
    ibanSender: str
    ibanReceiver: str
    amount: int

TransactionLG: Transaction = {"ibanSender": "Aled", "ibanReceiver": "Yiouiuh", "amount":20}
