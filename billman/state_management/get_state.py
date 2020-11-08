from billman.state_management.state import *
from datetime import datetime, timedelta

state = State(
    users=[
        User(
            id=0,
            name="Peppa",
            surname="Pig",
            address="Čokoladna ulica nekje",
            banc_acc_number="SI56293847932865923",
            local_credit=3.1,
            family={1, 2}
        ),
        User(
            id=1,
            name="George",
            surname="Pig",
            address="Disneyland 16a",
            banc_acc_number="SI563548463245356",
            local_credit=8327.94,
            family={0, 2}
        ),
        User(
            id=2,
            name="Mummy",
            surname="Pig",
            address="Lonček 113",
            banc_acc_number="SI563453636865923",
            local_credit=50.50,
            family={0, 1}
        ),
        User(
            id=3,
            name="Mr.",
            surname="Dinosaur",
            address="Barn 121",
            banc_acc_number="452",
            local_credit=-97.0,
            family=set()
        ),
        User(
            id=4,
            name="Danny",
            surname="Dog",
            address="Barn 113",
            banc_acc_number="SI56334536865923",
            local_credit=1.0,
            family=set()
        ),
        User(
            id=5,
            name="Mrs.",
            surname="Rabbit",
            address="Barn 16a",
            banc_acc_number="SI563548456765356",
            local_credit=17.0,
            family=set()
        )

    ],
    categories=[
        Category(name="Family"),
        Category(name="Food"),
        Category(name="Fun"),
        Category(name="Education"),
        Category(name="Sport"),
        Category(name="Transport"),
        Category(name="Fixed expenses"),
        Category(name="Community"),
        Category(name="Other"),
    ],
    community=[
        Community(id=0,
                  poor=User(
                      id=3,
                      desc="Izgubil celotno družino in premoženje v hudi nesreči, ko je asteroid zadel Zemljo.",
                      name="Mr.",
                      surname="Dinosaur",
                      address="Barn 121",
                      banc_acc_number="452",
                      local_credit=-97.0,
                      family=set()
                  ),
                  goal=False,
                  bills=[
                      Cause(cause="Račun za elektriko", value=30.0),
                      Cause(cause="Najemnina", value=150.0),
                      Cause(cause="Zdravila za miltiplo sklerozo", value=15.0)
                  ],
                  total=195.0,
                  collected=10.0),
        Community(id=1,
                  poor=User(
                      id=4,
                      desc="Lastnik ga je zapustil in ostal je brez vsega.",
                      name="Danny",
                      surname="Dog",
                      address="Barn 113",
                      banc_acc_number="SI56334536865923",
                      local_credit=1,
                      family=set()
                  ),
                  goal=False,
                  bills=[
                      Cause(cause="Popravilo avtomobila po nesreči", value=95.0),
                      Cause(cause="Komunalne storitve", value=25.0),
                      Cause(cause="Sanacija vodovodne napeljave", value=40.0)
                  ],
                  total=160.0,
                  collected=85.0),
        Community(id=2,
                  poor=User(
                      id=5,
                      desc="Letina je bila slaba zaradi povodni, kmetija je šla v stečaj, ni več korenja, rubeži grozijo, da ji bodo odvzeli hišo.",
                      name="Mrs.",
                      surname="Rabbit",
                      address="Barn 16a",
                      banc_acc_number="SI563548456765356",
                      local_credit=17,
                      family=set()
                  ),
                  goal=False,
                  bills=[
                      Cause(cause="Pripomočki za šolanje na daljavo", value=55.0),
                      Cause(cause="Račun za plin", value=210.0),
                  ],
                  total=265.0,
                  collected=45.0)
    ],
    bills=[
        Bill(
            id=0,
            id_payer=0,
            short_name="univerzalj",
            category="Education",
            reference="SI12",
            date_payment="",  # ni placan - prazen string
            date_due="2020-11-12",
            date_issued="2020-10-12",
            total=21.02,
            purpose="Vpisnina",
            code_purpose="STDY",
            recipient="Univerza v Ljubljani",
            recipient_address="Kongresni trg 12, 1000 Ljubljana",
            BIC_bank_recipient="ABCD1234",
            IBAN_recipient="SI32124578563456789",
            visible_family="True"
        ),
        Bill(
            id=1,
            id_payer=0,
            short_name="ilirija",
            category="Sport",
            reference="SI15",
            date_payment="2020-11-05",
            date_due="2020-12-11",
            date_issued="2020-10-12",
            total=32.00,
            purpose="Članarina za plavalni klub",
            code_purpose="MDCS",
            recipient="Plavalni klub Ilirija",
            recipient_address="Celovška cesta 3, 1000 Ljubljana",
            BIC_bank_recipient="ABCD7634",
            IBAN_recipient="SI32124578563443210",
            visible_family="True"
        ),
        Bill(
            id=2,
            id_payer=0,
            short_name="lpp",
            category="Transport",
            reference="SI20",
            date_payment="2020-11-01",
            date_due="2021-01-01",
            date_issued="2020-11-06",
            total=210.00,
            purpose="IJPP",
            code_purpose="BUSB",
            recipient="LPP d.o.o.",
            recipient_address="Celovška cesta 160, 1000 Ljubljana",
            BIC_bank_recipient="EFGH3134",
            IBAN_recipient="SI32134988563443210",
            visible_family="True"
        ),
        Bill(
            id=3,
            id_payer=2,
            short_name="petrol",
            category="Fun",
            reference="SI20",
            date_payment="",  # ni placan - prazen string
            date_due="2021-11-11",
            date_issued="2020-07-12",
            total=17.64,
            purpose="Concert tickets",
            code_purpose="OTHR",
            recipient="Petrol d.d.",
            recipient_address="Dunajska cesta 50, 1000 Ljubljana",
            BIC_bank_recipient="EX6K3134",
            IBAN_recipient="SI32134988563654321",
            visible_family="True"
        ),
        Bill(
            id=4,
            id_payer=1,
            short_name="t2",
            category="Other",
            reference="SI11",
            date_payment="",
            date_due="2021-03-04",
            date_issued="2020-05-12",
            total=5560.69,
            purpose="Internetne storitve",
            code_purpose="OTHR",
            recipient="T-2 d.o.o.",
            recipient_address="Verovškova 64a, 1000 Ljubljana",
            BIC_bank_recipient="XLBA5174",
            IBAN_recipient="SI54789885636543218",
            visible_family="True"
        ),
        Bill(
            id=5,
            id_payer=0,
            short_name="petrol",
            category="Transport",
            reference="SI20",
            date_payment="",  # ni placan - prazen string
            date_due="2020-11-08",
            date_issued="2020-10-12",
            total=112.00,
            purpose="Letna vinjeta",
            code_purpose="OTHR",
            recipient="Petrol d.d.",
            recipient_address="Dunajska cesta 50, 1000 Ljubljana",
            BIC_bank_recipient="EX6K3134",
            IBAN_recipient="SI32134988563654321",
            visible_family="True"
        ),
        Bill(
            id=6,
            id_payer=0,
            short_name="t2",
            category="Other",
            reference="SI11",
            date_payment="",
            date_due="2021-11-08",
            date_issued="2020-08-12",
            total=5560.69,
            purpose="Nakup opreme",
            code_purpose="OTHR",
            recipient="T-2 d.o.o.",
            recipient_address="Verovškova 64a, 1000 Ljubljana",
            BIC_bank_recipient="XLBA5174",
            IBAN_recipient="SI54789885636543218",
            visible_family="True"
        )
    ],
)


async def get_state() -> State:
    return state


def get_byCategory(cat):
    categoryBills = []
    for bill in state.bills:
        if bill.category == cat:
            categoryBills.append(bill)
    return categoryBills


def get_billDateDue():
    dueDateBills = []
    for bill in state.bills:
        if bill.date_payment == "":
            dueDateBills.append(bill)
    dueDateBills.sort(key=lambda r: r.date_due, reverse=True)
    return dueDateBills


def get_billDatePayed():
    payedDateBills = []
    for bill in state.bills:
        if bill.date_payment != "":
            payedDateBills.append(bill)
    payedDateBills.sort(key=lambda r: r.date_payment, reverse=True)
    return payedDateBills


def get_byTotalAsc():
    billsAsc = state.bills
    billsAsc.sort(key=lambda r: r.total)
    return billsAsc


def get_byTotalDesc():
    billsDesc = state.bills
    billsDesc.sort(key=lambda r: r.total, reverse=True)
    return billsDesc


def get_family(option):
    seen = []
    for bill in state.bills:
        if bill.visible_family == option:
            seen.append(bill)
    seen.sort(key=lambda r: r.date_due)
    return seen


def set_billPaid(id_bill, credits):
    for bill in state.bills:
        if bill.id == id_bill:
            if credits:
                state.users[0].local_credit -= bill.total
            bill.date_payment = str(datetime.today().strftime('%Y-%m-%d'))
            bill.id_payer=0
            break
    return


def set_transactCredits(id_recipient, amount):
    for user in state.users:
        if user.id == id_recipient:
            user.local_credit += amount
            state.users[0].local_credit -= amount
            break
    return


def create_community_bill(poor_id, amount) -> int:
    today = datetime.now()
    date_today = today.strftime("%Y-%m-%d")
    date_due = (today + timedelta(14)).strftime("%Y-%m-%d")
    cause = "Provide help"
    for com in state.community:
        if com.poor.id == poor_id:
            # ker bomo takoj placali ta racun, lahko ze v community povisamo zbrani znesek
            com.collected += amount

    new_bill = Bill(id=len(state.bills),
                    id_payer=0,
                    short_name="community",
                    category="Community",
                    reference="SI11",
                    date_payment="",
                    date_due=date_due,
                    date_issued=date_today,
                    total=amount,
                    purpose="Provide help",
                    code_purpose="HELP",
                    recipient="Humanitarno društvo",
                    recipient_address="Ozka ulica 54, 1200 Moravče",
                    BIC_bank_recipient="ERG23422",
                    IBAN_recipient="SI5614134325235",
                    visible_family=False
                    )
    state.bills.append(new_bill)
    return new_bill.id


def make_com_plus(com) -> CommunityPlus:
    for user in state.users:
        if user.id == com.poor:
            revni = user
            break
    new_com = CommunityPlus(poor=revni, goal=com.goal, collected=com.collected, cause=com.cause)
    return new_com


def create_user_plus_from_user(user) -> UserPlus:
    new_user_plus = UserPlus(
        id=user.id,
        name=user.name,
        surname=user.surname,
        address=user.address,
        banc_acc_number=user.banc_acc_number,
        local_credit=user.local_credit,
        family=user.family,
        family_bills=[]
    )
    for bill in state.bills:
        if bill.id_payer == user.id and bill.date_payment == "" and bill.visible_family:
            new_user_plus.family_bills.append(bill)
    return new_user_plus

def get_stat_value_for_month(user_id):
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


def get_stat_value_for_week(user_id):
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

def get_stat_donations(user_id):
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

def get_stat_credits(user_id):
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

def get_stat_transactions(user_id):
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

def get_stat_byCategory(user_id):
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

def get_stat_byCategory(user_id):
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