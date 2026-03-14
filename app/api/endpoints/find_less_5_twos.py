from fastapi import APIRouter

from app.schemas.schemas import StudentTwos
from app.services.services import less_than_5

router = APIRouter()

@router.get(
    "/students/less-than-5-twos",
    response_model=list[StudentTwos],
)
async def less_than_5_twos() -> list[dict[str,int]]:
    rows = await less_than_5()
    return rows
