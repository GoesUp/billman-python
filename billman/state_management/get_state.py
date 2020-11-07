from functools import lru_cache
from billman.state_management.state import State, User, Bill

state = State(
    users=[
        User(
            name="Gregor",
            surname="Gabrovšek",
        )
    ],
    bills=[
        Bill(
            category="Education",
            reference="SI12",
            date_payment="2020-01-12",
            date_due="2020-11-12",
            total="121.02",
            purpose="Tečaj za kotalkanje po vodi",
            code_purpose="07DA",
            recipient_and_address="Društvo diabetikov Slovenije, Cesta na grad 12, 1000 Koper",
            BIC_bank_recipient="ABCD1234",
            IBAN_recipient="SI32124578563456789",
            visible_family="true"
        ),
        Bill(
            category="Sport",
            reference="SI15",
            date_payment="2020-19-11",
            date_due="2020-20-11",
            total="32.00",
            purpose="Članarina za plavalni klub",
            code_purpose="H2OO",
            recipient_and_address="Društvo paraplegikov Slovenije, Zmajski most 10, 1270 Ljubljana-Moste",
            BIC_bank_recipient="ABCD7634",
            IBAN_recipient="SI32124578563443210",
            visible_family="false"
        ),
        Bill(
            category="Transport",
            reference="SI20",
            date_payment="2020-30-12",
            date_due="2021-01-01",
            total="210.00",
            purpose="IJPP",
            code_purpose="KL21",
            recipient_and_address="LPP d.o.o., Celovška cesta 160, 1000 Ljubljana",
            BIC_bank_recipient="EFGH3134",
            IBAN_recipient="SI32134988563443210",
            visible_family="true"
        ),
        Bill(
            category="Fun",
            reference="SI20",
            date_payment="2020-12-11",
            date_due="2021-15-11",
            total="17.64",
            purpose="Concert tickets",
            code_purpose="CON0",
            recipient_and_address="LPP d.o.o., Celovška cesta 160, 1000 Ljubljana",
            BIC_bank_recipient="EX6K3134",
            IBAN_recipient="SI32134988563654321",
            visible_family="false"
        ),
        Bill(
            category="Other",
            reference="SI11",
            date_payment="2020-08-11",
            date_due="2021-03-04",
            total="5560.69",
            purpose="Bathroom renovation",
            code_purpose="BA7H",
            recipient_and_address="TheNicestBathroomEvr, Kopališka ulica 3, 1000 Ljubljana",
            BIC_bank_recipient="XLBA5174",
            IBAN_recipient="SI54789885636543218",
            visible_family="false"
        )
    ]
)


async def get_state() -> State:
    return state
