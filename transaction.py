from typing import TypedDict

class Transaction:
    ibanSender: str
    ibanReceiver: str
    amount: int

    def __init__(self, iban_sender: str, iban_receiver: str, amount: int) -> None:
        self.ibanSender = iban_sender
        self.ibanReceiver = iban_receiver
        self.amount = amount

#All transactions
TransactionLG= Transaction("Aled", "Yiouiuh", 20)