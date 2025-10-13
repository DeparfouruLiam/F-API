from fastapi import FastAPI
from pydantic import BaseModel
from typing import TypedDict
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Gooning world"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

class Item(BaseModel):
    name: str
    price: float

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

class Config(TypedDict):
    version :str
    name: str