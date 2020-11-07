from typing import List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from billman.state_management.get_state import get_state
from billman.state_management.state import State, User, Bill, Category, Family, Community

router = APIRouter()


@router.get("/")
async def test(state: State = Depends(get_state)) -> State:
    return state


@router.get("/users")
def all_users(state: State = Depends(get_state)) -> List[User]:
    return state.users


@router.get("/bills")
def all_bills(state: State = Depends(get_state)) -> List[Bill]:
    return state.bills


@router.get("/categories")
def all_categories(state: State = Depends(get_state)) -> List[Category]:
    return state.categories


@router.get("/user/{user_id}")
def get_user_by_id(user_id: int, state: State = Depends(get_state)) -> User:
    for user in state.users:
        if user.id == user_id:
            return user


@router.get("/user/{user_id}/family")
def get_user_family(user_id: int, state: State = Depends(get_state)) -> Family:
    for user in state.users:
        if user.id == user_id:
            return user.family


@router.get("/user/{user_id}/bills")
def get_bills_for_user_id(user_id: int, state: State = Depends(get_state)) -> List[Bill]:
    user_bills = []
    for bill in state.bills:
        if bill.id_payer == user_id:
            user_bills.append(bill)
    return user_bills


@router.get("/user/{user_id}/bills")
def get_bills_for_user_id(user_id: int, state: State = Depends(get_state)) -> List[Bill]:
    user_bills = []
    for bill in state.bills:
        if bill.id_payer == user_id:
            user_bills.append(bill)
    return user_bills


@router.get("/user/{user_id}/bills")
def get_bills_for_user_id(user_id: int, state: State = Depends(get_state)) -> List[Bill]:
    user_bills = []
    for bill in state.bills:
        if bill.id_payer == user_id:
            user_bills.append(bill)
    return user_bills


@router.get("/community/active")
def get_active_community(state: State = Depends(get_state)) -> List[Community]:
    community = []
    for com in state.community:
        if com.collected < com.goal:
            community.append(com)
    return community


@router.get("/community/closed")
def get_active_community(state: State = Depends(get_state)) -> List[Community]:
    community = []
    for com in state.community:
        if com.collected >= com.goal:
            community.append(com)
    return community


