from pydantic import BaseModel
from typing import List, Set


class Family(BaseModel):
    relations: Set[int] = None

      
class User(BaseModel):
    id: int
    name: str
    surname: str
    address: str
    banc_acc_number: str
    local_credit: float = 0.0
    family: Family

      
class Category(BaseModel):
    name: str

      
class Community(BaseModel):
    id: int
    goal: float
    collected: float = 0.0
    cause: str


class Bill(BaseModel):
    id: int
    id_payer: int
    short_name: str
    category: str
    reference: str
    date_payment: str
    date_due: str
    date_issued: str
    total: float
    purpose: str
    code_purpose: str
    recipient: str
    recipient_address: str
    BIC_bank_recipient: str
    IBAN_recipient: str
    visible_family: bool

      
class State(BaseModel):
    users: List[User]
    categories: List[Category]
    community: List[Community]
    bills: List[Bill]

