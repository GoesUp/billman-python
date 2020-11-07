from datetime import timedelta
from datetime import datetime

from fastapi.params import Depends
from fastapi.routing import APIRouter
from billman.state_management.get_state import *

router = APIRouter()


@router.get("/")
async def test(state: State = Depends(get_state)) -> State:
    return state


@router.get("/users")
async def all_users(state: State = Depends(get_state)) -> List[User]:
    return state.users


@router.get("/bills")
async def all_bills(state: State = Depends(get_state)) -> List[Bill]:
    return state.bills


@router.get("/categories")
async def all_categories(state: State = Depends(get_state)) -> List[Category]:
    return state.categories


@router.get("/user/{user_id}")
async def get_user_by_id(user_id: int, state: State = Depends(get_state)) -> User:
    for user in state.users:
        if user.id == user_id:
            return user


@router.get("/user/{user_id}/family")
async def get_user_family(user_id: int, state: State = Depends(get_state)) -> Family:
    for user in state.users:
        if user.id == user_id:
            return user.family


@router.get("/user/{user_id}/bills/all")
async def get_bills_for_user_id(user_id: int, state: State = Depends(get_state)) -> List[Bill]:
    user_bills = []
    for bill in state.bills:
        if bill.id_payer == user_id:
            user_bills.append(bill)
    user_bills.sort(key=lambda x: x.recipient, reverse=False)
    return user_bills


@router.get("/user/{user_id}/bills/paid")
async def get_bills_for_user_id(user_id: int, state: State = Depends(get_state)) -> List[Bill]:
    user_bills = []
    for bill in state.bills:
        if bill.id_payer == user_id and bill.date_payment != "":
            user_bills.append(bill)
    user_bills.sort(key=lambda x: x.date_payment, reverse=False)
    return user_bills


@router.get("/user/{user_id}/bills")
async def get_bills_for_user_id(user_id: int, state: State = Depends(get_state)) -> List[Bill]:
    user_bills = []
    for bill in state.bills:
        if bill.id_payer == user_id and not bill.date_payment:
            user_bills.append(bill)
    user_bills.sort(key=lambda x: x.date_due, reverse=False)
    return user_bills


@router.get("/community/active")
async def get_active_community(state: State = Depends(get_state)) -> List[Community]:
    community = []
    for com in state.community:
        if com.collected < com.goal:
            community.append(com)
    return community


@router.get("/community/closed")
async def get_active_community(state: State = Depends(get_state)) -> List[Community]:
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


@router.get("/bill/pay")
async  def bill_pay(id_bill: int, credits: bool, state: State = Depends(get_state)):
    set_billPaid(id_bill, credits)
    return


@router.post("/bill/transaction")
async def bill_transactFam(id_recipient: int, amount: float, state: State = Depends(get_state)):
    set_transactCredits(id_recipient, amount)
    return


# ----------------------- STATISTIKA

@router.get("/statistics/{user_id}/value-for-month")
async def get_stat_value_for_month(user_id: int, state: State = Depends(get_state)) -> List[float]:
    stats = {}
    base = datetime.today()
    date_list = [(base - timedelta(days=x)) for x in range(30)]
    date_list.reverse()

    for datum in date_list:
        stats["{year}-{month}-{day}".format(year=datum.year, month=datum.month, day=datum.day)] = 0
    for bill in state.bills:
        if bill.id_payer == user_id:
            stats[bill.date_payment] = bill.total
    return list(stats.values())


@router.get("/statistics/{user_id}/value-for-week")
async def get_stat_value_for_week(user_id: int, state: State = Depends(get_state)) -> List[float]:
    stats = {}
    base = datetime.today()
    date_list = [(base - timedelta(days=x)) for x in range(7)]
    date_list.reverse()

    for datum in date_list:
        stats["{year}-{month}-{day}".format(year=datum.year, month=datum.month, day=datum.day)] = 0
    for bill in state.bills:
        if bill.id_payer == user_id and bill.date_payment in date_list:
            stats[bill.date_payment] = stats[bill.date_payment] + bill.total
    return list(stats.values())


@router.get("/statistics/{user_id}/donations")
async def get_stat_donations(user_id: int, state: State = Depends(get_state)) -> List[float]:
    stats = {}
    base = datetime.today()
    date_list = [(base - timedelta(days=x)) for x in range(30)]
    date_list.reverse()

    for datum in date_list:
        stats["{year}-{month}-{day}".format(year=datum.year, month=datum.month, day=datum.day)] = 0
    for bill in state.bills:
        if bill.id_payer == user_id and bill.category == "Community":
            stats[bill.date_payment] = bill.total
    return list(stats.values())



# @router.get("/statistics/{user_id}/credits")
# async def get_stat_credits(user_id: int, state: State = Depends(get_state)) -> List[float]:
#     stats = {}
#     base = datetime.today()
#     date_list = [(base - timedelta(days=x)) for x in range(30)]
#     date_list.reverse()
#
#     credits_today = 0
#     for datum in date_list:
#         stats["{year}-{month}-{day}".format(year=datum.year, month=datum.month, day=datum.day)] = 0
#
#     user = get_user_by_id(user_id)
#     credits_today = user.local_credit
#     statistics = [credits_today] * 30
#
#     datumi = []
#     for bill in state.bills:
#         if bill.id_payer == user_id:
#             datumi.append([bill.date_payment, bill.total])
#     datumi.sort(reverse=True)
#     map(lambda x: datetime.fromisoformat(x[0]), datumi)
#     print(datumi)
#
#     today = datetime.today()
#     for d2 in datumi:
#         delta = abs((today - d2[0]).days)
#         for day in range(delta):
#
#     datetime_obj = datetime.fromisoformat(datum)
#     credits_today = state.users.get
#     for bill in state.bills:
#         if bill.id_payer == user_id and bill.category == "Community":
#             stats[bill.date_payment] = bill.total
#     return list(stats.values())