from datetime import datetime, timedelta, UTC, timezone
from typing import TypedDict

from pydantic import BaseModel


class Transaction(BaseModel):
    ibanSender: str
    ibanReceiver: str
    amount: int
    date : datetime
    cancelled: bool
#All transactions
transaction_lg = Transaction(ibanSender="Aled", ibanReceiver="Yiouiuh", amount=20, date= datetime.now(), cancelled=False)

