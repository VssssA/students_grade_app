from app.db import get_pool


async def insert_grades(rows: list[tuple[str, int]]) -> tuple[int, int]:
    pool = await get_pool()

    students_cache: dict[str, int] = {}
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
                        full_name,
                    )

                    if not student_id:
                        student_id = await conn.fetchval(
                            "SELECT id FROM students WHERE full_name=$1",
                            full_name,
                        )

                    students_cache[full_name] = student_id

                await conn.execute(
                    "INSERT INTO grades (student_id, grade) VALUES ($1, $2)",
                    students_cache[full_name],
                    grade,
                )

                records_loaded += 1

    return records_loaded, len(students_cache)


async def get_students_with_twos(condition: str):
    pool = await get_pool()

    async with pool.acquire() as conn:
        rows = await conn.fetch(
            f"""
            SELECT s.full_name, COUNT(*) AS count_twos
            FROM grades g
            JOIN students s ON s.id = g.student_id
            WHERE g.grade = 2
            GROUP BY s.full_name
            HAVING COUNT(*) {condition}
            """
        )

    return [dict(r) for r in rows]  # ⭐ ВОТ ЭТО КЛЮЧ

