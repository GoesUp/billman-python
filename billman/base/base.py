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


@router.post("/bill/pay/community")
async def bill_community(cause_id: int, amount: float, credits: bool, state: State = Depends(get_state)):
    bill_id = create_community_bill(cause_id, amount)
    set_billPaid(bill_id, credits)
    return "Thank you for your help"


# ----------------------- STATISTIKA

@router.get("/statistics/{user_id}/value-for-month")
async def get_stat_value_for_month(user_id: int, state: State = Depends(get_state)) -> List[float]:
    stats = {}
    base = datetime.today()
    date_list = [(base - timedelta(days=x)) for x in range(30)]
    date_list.reverse()

    for datum in date_list:
        stats["{year}-{x}{month}-{y}{day}".format(year=datum.year, month=datum.month, day=datum.day, x="0" if datum.month < 10 else "", y="0" if datum.day < 10 else "")] = 0
    for bill in state.bills:
        if bill.id_payer == user_id and bill.date_payment in stats.keys():
            stats[bill.date_payment] = bill.total
    return list(stats.values())


@router.get("/statistics/{user_id}/value-for-week")
async def get_stat_value_for_week(user_id: int, state: State = Depends(get_state)) -> List[float]:
    stats = {}
    base = datetime.today()
    date_list = [(base - timedelta(days=x)) for x in range(7)]
    date_list.reverse()

    for datum in date_list:
        stats["{year}-{x}{month}-{y}{day}".format(year=datum.year, month=datum.month, day=datum.day, x="0" if datum.month < 10 else "", y="0" if datum.day < 10 else "")] = 0
    for bill in state.bills:
        if bill.id_payer == user_id and bill.date_payment in stats.keys():
            stats[bill.date_payment] += bill.total
    return list(stats.values())


@router.get("/statistics/{user_id}/donations")
async def get_stat_donations(user_id: int, state: State = Depends(get_state)) -> List[float]:
    stats = {}
    base = datetime.today()
    date_list = [(base - timedelta(days=x)) for x in range(30)]
    date_list.reverse()

    for datum in date_list:
        stats["{year}-{x}{month}-{y}{day}".format(year=datum.year, month=datum.month, day=datum.day, x="0" if datum.month < 10 else "", y="0" if datum.day < 10 else "")] = 0
    for bill in state.bills:
        if bill.id_payer == user_id and bill.category == "Community" and bill.date_payment in stats.keys():
            stats[bill.date_payment] += bill.total
    return list(stats.values())



@router.get("/statistics/{user_id}/credits")
async def get_stat_credits(user_id: int, state: State = Depends(get_state)) -> List[float]:
    stats = {}
    base = datetime.today()
    date_list = [(base - timedelta(days=x)) for x in range(30)]
    date_list.reverse()
    for datum in date_list:
        stats["{year}-{month}-{day}".format(year=datum.year, month=datum.month, day=datum.day)] = 0
    for user in state.users:
        if user.id == user_id:
            main_user = user
            break
    credits_today = main_user.local_credit
    credits_daily = [credits_today] * 30
    datumi = []
    for bill in state.bills:
        if bill.id_payer == user_id and bill.date_payment != "":
            datumi.append([bill.date_payment, bill.total])
    datumi.sort(reverse=True)
    map(lambda x: datetime.fromisoformat(x[0]), datumi)
    print("datumi",  datumi)

    dnevi = []
    today = datetime.today()
    for d2 in datumi:
        delta = abs(today - datetime.strptime(d2[0], '%Y-%m-%d')).days
        dnevi.append((delta, d2[1]))
    print("dnevi", dnevi)

    for obj in dnevi:
        for i in range(obj[0], len(credits_daily)):
            credits_daily[i] += obj[1]
    credits_daily.reverse()
    return credits_daily


@router.get("/statistics/{user_id}/transactions")
async def get_stat_transactions(user_id: int, state: State = Depends(get_state)) -> List[float]:
    stats = {}
    base = datetime.today()
    date_list = [(base - timedelta(days=x)) for x in range(30)]
    date_list.reverse()

    for datum in date_list:
        stats["{year}-{x}{month}-{y}{day}".format(year=datum.year, month=datum.month, day=datum.day, x="0" if datum.month < 10 else "", y="0" if datum.day < 10 else "")] = 0
    for bill in state.bills:
        if bill.id_payer == user_id and bill.date_payment in stats.keys():
            stats[bill.date_payment] = bill.total
    return list(stats.values())

@router.get("/statistics/{user_id}/categoryNumber")  #po stevilu
async def get_stat_byCategory(user_id: int, state: State = Depends(get_state)):
    cat = {
        "Community": 0,
        "Family": 0,
        "Education": 0,
        "Food": 0,
        "Fun": 0,
        "Sport": 0,
        "Transport": 0,
        "Fixed expenses": 0,
        "Other": 0
    }

    total_amount = 0

    for bill in state.bills:
        if bill.id_payer == user_id:
            cat[bill.category] += 1
            total_amount += 1

    return cat

@router.get("/statistics/{user_id}/categoryAmount") #po denarju
async def get_stat_byCategory(user_id: int, state: State = Depends(get_state)):
    cat = {
        "Community": 0,
        "Family": 0,
        "Education": 0,
        "Food": 0,
        "Fun": 0,
        "Sport": 0,
        "Transport": 0,
        "Fixed expenses": 0,
        "Other": 0
    }

    for bill in state.bills:
        if bill.id_payer == user_id:
            cat[bill.category] += bill.total

    return cat