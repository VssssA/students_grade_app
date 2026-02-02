from fastapi import FastAPI, UploadFile, File, HTTPException
from app.db import get_pool
from app.validator import parse_and_validate_csv

app = FastAPI(title="Grades service")

@app.get("/")
async def hello_world():
    return {"hello":"world"}

@app.post("/upload-grades")
async def upload_grades(file: UploadFile = File(...)):
    try:
        print(file)
        content = await file.read()
        rows = parse_and_validate_csv(content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    pool = await get_pool()
    students_cache = {}
    records_loaded = 0

    async with pool.acquire() as conn:
        async with conn.transaction():
            for full_name, grade in rows:
                if full_name not in students_cache:
                    student_id = await conn.fetchval(
                        """
                        INSERT INTO students (full_name)
                        VALUES ($1)
                        ON CONFLICT DO NOTHING
                        RETURNING id
                        """,
                        full_name
                    )

                    if not student_id:
                        student_id = await conn.fetchval(
                            "SELECT id FROM students WHERE full_name=$1",
                            full_name
                        )

                    students_cache[full_name] = student_id

                await conn.execute(
                    "INSERT INTO grades (student_id, grade) VALUES ($1, $2)",
                    students_cache[full_name],
                    grade
                )
                records_loaded += 1

    return {
        "status": "ok",
        "records_loaded": records_loaded,
        "students": len(students_cache),
    }


@app.get("/students/more-than-3-twos")
async def more_than_3_twos():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            """
            SELECT s.full_name, COUNT(*) AS count_twos
            FROM grades g
            JOIN students s ON s.id = g.student_id
            WHERE g.grade = 2
            GROUP BY s.full_name
            HAVING COUNT(*) > 3
            """
        )

    return [
        {"full_name": r["full_name"], "count_twos": r["count_twos"]}
        for r in rows
    ]


@app.get("/students/less-than-5-twos")
async def less_than_5_twos():
    pool = await get_pool()
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            """
            SELECT s.full_name, COUNT(*) AS count_twos
            FROM grades g
            JOIN students s ON s.id = g.student_id
            WHERE g.grade = 2
            GROUP BY s.full_name
            HAVING COUNT(*) < 5
            """
        )

    return [
        {"full_name": r["full_name"], "count_twos": r["count_twos"]}
        for r in rows
    ]
