from functools import lru_cache
from billman.state_management.state import State, User

state = State(
    users=[
        User(
            name="Gregor",
            surname="Gabrovšek",
        )
    ]
)


async def get_state() -> State:
    return state
