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
        Community(id=0, goal=100.5, collected=50.25, cause="Družini vidmajer je toča uničila streho. Pomagajte!"),
        Community(id=1, goal=800.0, cause="Omogočimo otrokom izlet v Črno goro!"),
        Community(id=2, goal=150, cause="Zbiramo sredstva za male živali..."),
        Community(id=3, goal=1054.52, collected=72, cause="Gregor, Maja in Barbara so lačni. Darujte!"),
        Community(id=4, goal=100, collected=100, cause="Stara mama Helga zbira denar za flamethrower7000"),
    ]
)


async def get_state() -> State:
    return state
