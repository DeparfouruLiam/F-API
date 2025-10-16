from typing import TypedDict

class Beneficiary:
    username: str
    iban: str

    def __init__(self, username: str, iban: str):
        self.username = username
        self.iban = iban

#All beneficiaries
GhaziBeneficiary = Beneficiary( "Ghazi", "Yiouiuh")
