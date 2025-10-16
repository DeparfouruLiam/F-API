from sqlmodel import Field, SQLModel

class AccountA(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    amount: int = Field(index=True)
    iban: str = Field(index=True)
    user_id: int = Field(index=True)