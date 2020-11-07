from pydantic import BaseModel
from typing import List, Set


class Family(BaseModel):
    relations: Set[int] = None


class User(BaseModel):
    id: int
    name: str
    surname: str
    address: str
    bancAccNumber: str
    localCredit: float
    family: Family


class Category(BaseModel):
    name: str


class Community(BaseModel):
    id: int
    amount: float = 0.0
    cause: str


class State(BaseModel):
    users: List[User]
    categories: List[Category]
    community: List[Community]
