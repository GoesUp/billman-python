from pydantic import BaseModel
from typing import List, Set


class User(BaseModel):
    id: int
    desc: str = ""
    name: str
    surname: str
    address: str
    banc_acc_number: str
    local_credit: float = 0.0
    family: Set[int]

      
class Category(BaseModel):
    name: str


class Cause(BaseModel):
    cause: str
    value: float


class Community(BaseModel):
    id: int
    poor: User
    bills: List[Cause]
    total: float
    collected: float = 0.0
    goal: bool


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


class UserPlus(BaseModel):
    id: int
    name: str
    surname: str
    address: str
    banc_acc_number: str
    local_credit: float = 0.0
    family: Set[int]
    family_bills: List[Bill]


class CommunityPlus(BaseModel):
    poor: User
    goal: bool
    collected: float = 0.0
    cause: str


class State(BaseModel):
    users: List[User]
    categories: List[Category]
    community: List[Community]
    bills: List[Bill]

