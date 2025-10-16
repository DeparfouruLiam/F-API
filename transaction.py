import datetime
from typing import TypedDict
from datetime import datetime, timedelta, UTC, timezone

import config


class Transaction:
    ibanSender: str
    ibanReceiver: str
    amount: int
    cancelled: bool = False
    id:int
    date: datetime

    def __init__(self, iban_sender: str, iban_receiver: str, amount: int) -> None:
        self.cancelled = None
        self.ibanSender = iban_sender
        self.ibanReceiver = iban_receiver
        self.amount = amount
        self.date = datetime.now(timezone.utc)
        self.id = config.transactionCount
        config.transactionCount += 1

#All transactions
TransactionLG= Transaction("Aled", "Yiouiuh", 20)