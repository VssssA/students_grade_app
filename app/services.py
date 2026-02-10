from app.validator import parse_and_validate_csv
from app.repo import insert_grades, get_students_with_twos


async def upload_grades_service(content: bytes):
    rows = parse_and_validate_csv(content)
    records, students = await insert_grades(rows)

    return {
        "status": "ok",
        "records_loaded": records,
        "students": students,
    }


async def more_than_3():
    return await get_students_with_twos("> 3")


async def less_than_5():
    return await get_students_with_twos("< 5")
