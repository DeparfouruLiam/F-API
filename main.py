from typing import TypedDict
from fastapi import FastAPI, Depends
from routes import account_routes,user_routes,transaction_routes,beneficiary_routes
app = FastAPI(title="Gooning Factory API")


app.include_router(account_routes.router)
app.include_router(user_routes.router)
app.include_router(transaction_routes.router)
app.include_router(beneficiary_routes.router)

