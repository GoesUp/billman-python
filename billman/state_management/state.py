from pydantic import BaseModel
from typing import List


class User(BaseModel):
    name: str
    surname: str


class State(BaseModel):
    users: List[User]
