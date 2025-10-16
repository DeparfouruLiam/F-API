from sqlmodel import Field, SQLModel
from typing import TypedDict

# class Beneficiary:
#     username: str
#     iban: str

class Beneficiary(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: int = Field(index=True)
    iban: str = Field(index=True)
    user_id: int = Field(index=True)


