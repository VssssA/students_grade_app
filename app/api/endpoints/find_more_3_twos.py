from fastapi import APIRouter

from app.schemas.schemas import StudentTwos
from app.services.services import more_than_3

router = APIRouter()

@router.get(
    "/students/more-than-3-twos",
    response_model=list[StudentTwos],
)
async def more_than_3_twos():
    rows = await more_than_3()
    return rows
