from typing import TypedDict
from fastapi import FastAPI, Depends

from database import create_db_and_tables
from routes import account_routes, user_routes, transaction_routes, beneficiary_routes, database_routes

app = FastAPI(title="Gooning Factory API")

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(account_routes.router)
app.include_router(user_routes.router)
app.include_router(transaction_routes.router)
app.include_router(beneficiary_routes.router)

app.include_router(database_routes.router)