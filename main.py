from typing import TypedDict
from fastapi import FastAPI, Depends
from routes import account_routes,user_routes,transaction_routes,beneficiary_routes
import asyncio
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta

app = FastAPI(title="Gooning Factory API")


SECRET_KEY = "Damn"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def periodic_task():
    while True:
        print("Function is running every 10 seconds")
        # Put your actual function code here
        await asyncio.sleep(10)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(periodic_task())

@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(account_routes.router)
app.include_router(user_routes.router)
app.include_router(transaction_routes.router)
app.include_router(beneficiary_routes.router)

