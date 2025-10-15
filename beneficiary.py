from typing import TypedDict

class Beneficiary(TypedDict):
    username: str
    iban: str


GhaziBeneficiary: Beneficiary = {"username": "Ghazi","iban": "Yiouiuh"}
