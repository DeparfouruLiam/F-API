from typing import TypedDict

class Beneficiary(TypedDict):
    username: str
    iban: str

#All beneficiaries
GhaziBeneficiary: Beneficiary = {"username": "Ghazi","iban": "Yiouiuh"}
