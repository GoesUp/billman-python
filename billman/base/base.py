from fastapi.params import Depends
from fastapi.routing import APIRouter
from billman.state_management.get_state import *
from billman.state_management.state import State


router = APIRouter()


@router.get("/")
async def test(state: State = Depends(get_state)) -> State:
    return state

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