from typing import TypedDict

class Beneficiary:
    username: str
    iban: str

    def __init__(self, username: str, iban: str):
        self.username = username
        self.iban = iban

    def get_iban(self) -> str:
        return self.iban

    def get_username(self) -> str:
        return self.username


#All beneficiaries
GhaziBeneficiary = Beneficiary( "Ghazi", "Yiouiuh")
