from fastapi.params import Depends
from fastapi.routing import APIRouter
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
    user_bills.sort(key=lambda x: x.recipient, reverse=False)
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
def cat_family(state: State = Depends(get_state)):
    return get_byCategory("Family")


@router.get("/category/community")
def cat_community(state: State = Depends(get_state)):
    return get_byCategory("Community")


@router.get("/category/education")
def cat_education(state: State = Depends(get_state)):
    return get_byCategory("Education")


@router.get("/category/fun")
def cat_fun(state: State = Depends(get_state)):
    return get_byCategory("Fun")


@router.get("/category/food")
def cat_food(state: State = Depends(get_state)):
    return get_byCategory("Food")


@router.get("/category/sport")
def cat_sport(state: State = Depends(get_state)):
    return get_byCategory("Sport")


@router.get("/category/transport")
def cat_transport(state: State = Depends(get_state)):
    return get_byCategory("Transport")


@router.get("/category/fixedExpenses")
def cat_fixedExpenses(state: State = Depends(get_state)):
    return get_byCategory("FixedExpenses")


@router.get("/category/other")
def cat_other(state: State = Depends(get_state)):
    return get_byCategory("Other")


@router.get("/bill/dateDue")
def bill_dateDue(state: State = Depends(get_state)):
    return get_billDateDue()


@router.get("/bill/datePayed")
def bill_datePayed(state: State = Depends(get_state)):
    return get_billDatePayed()


@router.get("/bill/totalAsc")
def bill_totalAsc(state: State = Depends(get_state)):
    return get_byTotalAsc()


@router.get("/bill/totalDesc")
def bill_totalDesc(state: State = Depends(get_state)):
    return get_byTotalDesc()


@router.get("/bill/familyYes")
def bill_familyYes(state: State = Depends(get_state)):
    return get_family(True)


@router.get("/bill/familyNo")
def bill_familyNo(state: State = Depends(get_state)):
    return get_family(False)

@router.post("/bill/pay")
def bill_pay(id_bill: int, amount, credits: float, state: State = Depends(get_state)):
    set_billPaid(id_bill, amount, credits)
    return

@router.post("/bill/transaction")
def bill_transactFam(id_recipient: int, amount: float, state: State = Depends(get_state)):
    set_transactCredits(id_recipient, amount)
    return