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


@router.get("/community")
async def all_categories(state: State = Depends(get_state)) -> List[Category]:
    return state.community


@router.get("/user/{user_id}")
async def get_user_by_id(user_id: int, state: State = Depends(get_state)) -> User:
    # vrne uporabnika z id = user_id
    for user in state.users:
        if user.id == user_id:
            return user


@router.get("/user/{user_id}/family")
async def get_user_family(user_id: int, state: State = Depends(get_state)) -> List[UserPlus]:
    # vrne seznam userjev, ki so druzina od userja z id=user_id
    fam = []
    for user in state.users:
        if user.id == user_id:
            main_user = user
    for u2 in state.users:
        if main_user and u2.id in main_user.family:
            fam.append(create_user_plus_from_user(u2))
    return fam


@router.get("/bills/{user_id}/family")
async def get_bills_for_user_family(user_id: int, state: State = Depends(get_state)) -> List[Bill]:
    # vrne seznam userjev, ki so druzina od userja z id=user_id
    bills = []
    fam = []
    for user in state.users:
        if user.id == user_id:
            main_user = user
    for u2 in state.users:
        if main_user and u2.id in main_user.family:
            fam.append(u2)
    for bill in state.bills:
        if bill.date_payment == "" and bill.id_payer in main_user.family:
            if bill.visible_family:
                bills.append(bill)
    return bills


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


@router.get("/user/{user_id}/bills/recent")
async def get_bills_recent(user_id: int, state: State = Depends(get_state)) -> List[Bill]:
    user_bills = []
    for bill in state.bills:
        if bill.id_payer == user_id and not bill.date_payment:
            if abs(datetime.strptime(bill.date_due, "%Y-%m-%d") - datetime.today()).days <= 10:
                user_bills.append(bill)
    user_bills.sort(key=lambda x: x.date_due, reverse=False)
    return user_bills


@router.get("/community/active")
async def get_active_community(state: State = Depends(get_state)) -> List[Community]:
    community = []
    for com in state.community:
        if not com.goal:
            community.append(com)
    return community


@router.get("/community/closed")
async def get_active_community(state: State = Depends(get_state)) -> List[CommunityPlus]:
    community = []
    for com in state.community:
        if com.goal:
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


@router.get("/bill/pay/community")
async def bill_community(poor_id: int, amount: float, credits: bool, state: State = Depends(get_state)):
    bill_id = create_community_bill(poor_id, amount)
    set_billPaid(bill_id, credits)
    return "Thank you for your help"


# ----------------------- STATISTIKA
@router.get("/statistics/{user_id}") #vrne seznam
async def get_statistics(user_id:int, state: State = Depends(get_state)) -> List[List[float]]:
    stat1 = get_stat_value_for_month(user_id)
    stat2 = get_stat_value_for_week(user_id)
    stat3 = get_stat_credits(user_id)
    stat4 = get_stat_donations(user_id)
    stat5 = get_stat_transactions(user_id)
    return [stat1, stat2, stat3, stat4, stat5]


@router.get("/statistics/{user_id}/dict") #vrne slovar
async def get_statistics_dict(user_id:int, state: State = Depends(get_state)):
    stat1 = get_stat_value_for_month(user_id)
    stat2 = get_stat_value_for_week(user_id)
    stat3 = get_stat_credits(user_id)
    stat4 = get_stat_donations(user_id)
    stat5 = get_stat_transactions(user_id)
    stat6 = get_stat_byCategory(user_id)
    stat7 = get_stat_byCategory_num(user_id)
    return {
            "for_month": stat1,
            "for_week": stat2,
            "credits": stat3,
            "donations": stat4,
            "transactions": stat5,
            "cake1": stat6,
            "cake2": stat7
            }
