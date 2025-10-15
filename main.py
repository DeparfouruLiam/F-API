from typing import TypedDict
from fastapi import FastAPI, Depends
from user import *
from routes import account_routes,user_routes,transaction_routes,beneficiary_routes
app = FastAPI(title="Gooning Factory API")


app.include_router(account_routes.router)
app.include_router(user_routes.router)
app.include_router(transaction_routes.router)
app.include_router(beneficiary_routes.router)




@app.get("/read_amount")
def read_amount(iban):
    user = account_from_iban(iban)
    if user is None:
        return {"No account linked to this IBAN"}
    return {"Amount": user["amount"]}

@app.get("/read_amount_username")
def read_amount_dos(username):
    user = account_from_username(username)
    if user is None:
        return {"No account linked to this IBAN"}
    return {"Amount": user["amount"]}