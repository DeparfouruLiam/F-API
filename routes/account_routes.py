from fastapi import APIRouter, HTTPException
from account import *

router = APIRouter(prefix="/accounts", tags=["Accounts"])

@router.get("/read_amount")
def read_amount(iban):
    user = account_from_iban(iban)
    if user is None:
        return {"No account linked to this IBAN"}
    return {"Amount": user["amount"]}