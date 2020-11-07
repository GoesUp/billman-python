from typing import List

from fastapi.params import Depends
from fastapi.routing import APIRouter
from billman.state_management.state import State, User, Bill, Category, Family, Community
from billman.state_management.get_state import *

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

  
@router.get("/category/family")
async def cat_family(state: State = Depends(get_state)):
    return get_byCategory("Family")

@router.get("/category/community")
async def cat_community(state: State = Depends(get_state)):
    return get_byCategory("Community")

@router.get("/category/education")
async def cat_education(state: State = Depends(get_state)):
    return get_byCategory("Education")

@router.get("/category/fun")
async def cat_fun(state: State = Depends(get_state)):
    return get_byCategory("Fun")

@router.get("/category/food")
async def cat_food(state: State = Depends(get_state)):
    return get_byCategory("Food")

@router.get("/category/sport")
async def cat_sport(state: State = Depends(get_state)):
    return get_byCategory("Sport")

@router.get("/category/transport")
async def cat_transport(state: State = Depends(get_state)):
    return get_byCategory("Transport")

@router.get("/category/fixedExpenses")
async def cat_fixedExpenses(state: State = Depends(get_state)):
    return get_byCategory("FixedExpenses")

@router.get("/category/other")
async def cat_other(state: State = Depends(get_state)):
    return get_byCategory("Other")

@router.get("/bill/dateDue")
async def bill_dateDue(state: State = Depends(get_state)):
    return get_billDateDue()

@router.get("/bill/datePayed")
async def bill_datePayed(state: State = Depends(get_state)):
    return get_billDatePayed()

@router.get("/bill/totalAsc")
async def bill_totalAsc(state: State = Depends(get_state)):
    return get_byTotalAsc()

@router.get("/bill/totalDesc")
async def bill_totalDesc(state: State = Depends(get_state)):
    return get_byTotalDesc()

@router.get("/bill/familyYes")
async def bill_familyYes(state: State = Depends(get_state)):
    return get_family(True)

@router.get("/bill/familyNo")
async def bill_familyNo(state: State = Depends(get_state)):
    return get_family(False)

