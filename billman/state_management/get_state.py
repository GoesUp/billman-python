from functools import lru_cache
from billman.state_management.state import *

state = State(
    users=[
        User(
            id=0,
            name="Gregor",
            surname="Gabrovšek",
            address="Čokoladna ulica nekje",
            banc_acc_number="SI56293847932865923",
            local_credit="3.1",
            family=Family(relations={1, 10})
        ),
        User(
            id=1,
            name="Miki",
            surname="Miška",
            address="Disneyland 16a",
            banc_acc_number="SI563548463245356",
            local_credit="8327947197",
            family=Family(relations={0})
        ),
        User(
            id=2,
            name="Mojca",
            surname="Pokrajculja",
            address="Lonček 113",
            banc_acc_number="SI563453636865923",
            local_credit="50.50",
            family=Family(relations=set())
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
        Community(id=0, amount=10.5, cause="Družini vidmajer je toča uničila streho. Pomagajte!"),
        Community(id=0, cause="Omogočimo otrokom izlet v Črno goro!"),
        Community(id=0, cause="Zbiramo sredstva za male živali..."),
        Community(id=0, amount=1054.52, cause="Gregor, Maja in Barbara so lačni. Darujte!"),
    ],
    bills=[
        Bill(
            id="0",
            category="Education",
            reference="SI12",
            date_payment="", #ni placan - prazen string
            date_due="2020-11-12",
            total="121.02",
            purpose="Tečaj za kotalkanje po vodi",
            code_purpose="07DA",
            recipient_and_address="Društvo diabetikov Slovenije, Cesta na grad 12, 1000 Koper",
            BIC_bank_recipient="ABCD1234",
            IBAN_recipient="SI32124578563456789",
            visible_family="True"
        ),
        Bill(
            id="1",
            category="Sport",
            reference="SI15",
            date_payment="2020-11-05",
            date_due="2020-12-11",
            total="32.00",
            purpose="Članarina za plavalni klub",
            code_purpose="H2OO",
            recipient_and_address="Društvo paraplegikov Slovenije, Zmajski most 10, 1270 Ljubljana-Moste",
            BIC_bank_recipient="ABCD7634",
            IBAN_recipient="SI32124578563443210",
            visible_family="False"
        ),
        Bill(
            id="2",
            category="Transport",
            reference="SI20",
            date_payment="2020-12-12",
            date_due="2021-01-01",
            total="210.00",
            purpose="IJPP",
            code_purpose="KL21",
            recipient_and_address="LPP d.o.o., Celovška cesta 160, 1000 Ljubljana",
            BIC_bank_recipient="EFGH3134",
            IBAN_recipient="SI32134988563443210",
            visible_family="True"
        ),
        Bill(
            id="3",
            category="Fun",
            reference="SI20",
            date_payment="", #ni placan - prazen string
            date_due="2021-11-11",
            total="17.64",
            purpose="Concert tickets",
            code_purpose="CON0",
            recipient_and_address="LPP d.o.o., Celovška cesta 160, 1000 Ljubljana",
            BIC_bank_recipient="EX6K3134",
            IBAN_recipient="SI32134988563654321",
            visible_family="False"
        ),
        Bill(
            id="4",
            category="Other",
            reference="SI11",
            date_payment="2020-11-08",
            date_due="2021-03-04",
            total="5560.69",
            purpose="Bathroom renovation",
            code_purpose="BA7H",
            recipient_and_address="TheNicestBathroomEvr, Kopališka ulica 3, 1000 Ljubljana",
            BIC_bank_recipient="XLBA5174",
            IBAN_recipient="SI54789885636543218",
            visible_family="False"
        )
    ]
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