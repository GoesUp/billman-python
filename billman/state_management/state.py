from pydantic import BaseModel
from typing import List
# from datetime import datetime
#from pydantic.schema import datetime


class User(BaseModel):
    name: str
    surname: str

class Bill(BaseModel):
    category: str
    reference: str
    date_payment: str
    date_due: str
    total: float
    purpose: str
    code_purpose: str
    recipient_and_address: str
    BIC_bank_recipient: str
    IBAN_recipient: str
    visible_family: bool


class State(BaseModel):
    users: List[User]
    bills: List[Bill]

