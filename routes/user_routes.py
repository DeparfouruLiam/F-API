from fastapi import APIRouter, HTTPException
from account import *
from user import *

router = APIRouter(prefix="/user", tags=["User"] )

@router.get("/read_amount_username")
def read_amount_dos(username):
    user = account_from_username(username)
    if user is None:
        return {"No account linked to this IBAN"}
    return {"Amount": user.amount }