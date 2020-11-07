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
        Community(id=0, goal=100.5, collected=50.25, cause="Družini vidmajer je toča uničila streho. Pomagajte!"),
        Community(id=1, goal=800.0, cause="Omogočimo otrokom izlet v Črno goro!"),
        Community(id=2, goal=150, cause="Zbiramo sredstva za male živali..."),
        Community(id=3, goal=1054.52, collected=72, cause="Gregor, Maja in Barbara so lačni. Darujte!"),
        Community(id=4, goal=100, collected=100, cause="Stara mama Helga zbira denar za flamethrower7000"),
    ],
    bills=[
        Bill(
            id=0,
            id_payer=2,
            category="Education",
            reference="SI12",
            date_payment="2020-01-12",
            date_due="2020-11-12",
            total="121.02",
            purpose="Tečaj za kotalkanje po vodi",
            code_purpose="07DA",
            recipient="Društvo diabetikov Slovenije",
            recipient_address="Cesta na grad 12, 1000 Koper",
            BIC_bank_recipient="ABCD1234",
            IBAN_recipient="SI32124578563456789",
            visible_family="true"
        ),
        Bill(
            id=1,
            id_payer=0,
            category="Sport",
            reference="SI15",
            date_payment="2020-19-11",
            date_due="2020-20-11",
            total="32.00",
            purpose="Članarina za plavalni klub",
            code_purpose="H2OO",
            recipient="Društvo paraplegikov Slovenije",
            recipient_address="Zmajski most 10, 1270 Ljubljana-Moste",
            BIC_bank_recipient="ABCD7634",
            IBAN_recipient="SI32124578563443210",
            visible_family="false"
        ),
        Bill(
            id=2,
            id_payer=2,
            category="Transport",
            reference="SI20",
            date_payment="2020-30-12",
            date_due="2021-01-01",
            total="210.00",
            purpose="IJPP",
            code_purpose="KL21",
            recipient="LPP d.o.o.",
            recipient_address="Celovška cesta 160, 1000 Ljubljana",
            BIC_bank_recipient="EFGH3134",
            IBAN_recipient="SI32134988563443210",
            visible_family="true"
        ),
        Bill(
            id=3,
            id_payer=1,
            category="Fun",
            reference="SI20",
            date_payment="2020-12-11",
            date_due="2021-15-11",
            total="17.64",
            purpose="Concert tickets",
            code_purpose="CON0",
            recipient="LPP d.o.o.",
            recipient_address="Celovška cesta 160, 1000 Ljubljana",
            BIC_bank_recipient="EX6K3134",
            IBAN_recipient="SI32134988563654321",
            visible_family="false"
        ),
        Bill(
            id=4,
            id_payer=0,
            category="Other",
            reference="SI11",
            date_payment="2020-08-11",
            date_due="2021-03-04",
            total="5560.69",
            purpose="Bathroom renovation",
            code_purpose="BA7H",
            recipient="TheNicestBathroomEvr",
            recipient_address="Kopališka ulica 3, 1000 Ljubljana",
            BIC_bank_recipient="XLBA5174",
            IBAN_recipient="SI54789885636543218",
            visible_family="false"
        )
    ],
)


async def get_state() -> State:
    return state
