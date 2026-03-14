from app.services.repo import get_students_with_twos, insert_grades
from app.services.validator import parse_and_validate_csv


async def upload_grades_service(content: bytes) -> dict[str,object]:
    rows = parse_and_validate_csv(content)
    records, students = await insert_grades(rows)

    return {
        "status": "ok",
        "records_loaded": records,
        "students": students,
    }


async def more_than_3() -> list[dict[str,int]]:
    return await get_students_with_twos("> 3")


async def less_than_5() -> list[dict[str,int]]:
    return await get_students_with_twos("< 5")
