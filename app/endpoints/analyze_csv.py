from fastapi import APIRouter

from app.schemas import StudentTwos
from app.services.services import less_than_5, more_than_3

router = APIRouter(prefix="/students")

@router.get(
    "/less-than-5-twos",
    response_model=list[StudentTwos],
)
async def less_than_5_twos() -> list[dict[str,int]]:
    rows = await less_than_5()
    return rows

@router.get(
    "/more-than-3-twos",
    response_model=list[StudentTwos],
)
async def more_than_3_twos() -> list[dict[str,int]]:
    rows = await more_than_3()
    return rows
