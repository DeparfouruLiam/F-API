from datetime import datetime, timedelta, UTC, timezone
import config
from pydantic import BaseModel

transactions = []
class Transaction(BaseModel):
    ibanSender: str
class Transaction(BaseModel):
    ibanSender: str
    ibanReceiver: str
    amount: int
    date : datetime
    cancelled: bool
    id:int
#All transactions
transaction_lg = Transaction(ibanSender="Aled", ibanReceiver="Yiouiuh", amount=20, date= datetime.now(), cancelled=False, id=config.transactionCount)
config.transactionCount+=1
