from pydantic import BaseModel

class Beneficiary(BaseModel):
    username: str
    iban: str

#All beneficiaries
ghazi_beneficiary = Beneficiary(username="Ghazi", iban="Yiouiuh")
