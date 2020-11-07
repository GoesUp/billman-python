from fastapi.params import Depends
from fastapi.routing import APIRouter
from billman.state_management.get_state import get_state
from billman.state_management.state import State


router = APIRouter()


@router.get("/")
async def test(state: State = Depends(get_state)):
    return "ayooo"
