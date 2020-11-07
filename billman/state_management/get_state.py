from functools import lru_cache
from billman.state_management.state import *


state = State(
    users=[
        User(
            id=0,
            name="Gregor",
            surname="Gabrovšek",
            address="Čokoladna ulica nekje",
            bancAccNumber="SI56293847932865923",
            localCredit="3.1",
            family=Family(relations={1, 10})
        ),
        User(
            id=1,
            name="Miki",
            surname="Miška",
            address="Disneyland 16a",
            bancAccNumber="SI563548463245356",
            localCredit="8327947197",
            family=Family(relations={0})
        ),
        User(
            id=2,
            name="Mojca",
            surname="Pokrajculja",
            address="Lonček 113",
            bancAccNumber="SI563453636865923",
            localCredit="50.50",
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
    ]
)


async def get_state() -> State:
    return state
