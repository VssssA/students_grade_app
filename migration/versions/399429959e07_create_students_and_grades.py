"""create_students_and_grades

Revision ID: 399429959e07
Revises: 
Create Date: 2026-03-26 16:18:52.591388

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '399429959e07'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            full_name TEXT UNIQUE NOT NULL
        );
    """)

    op.execute("""
        CREATE TABLE IF NOT EXISTS grades (
            id SERIAL PRIMARY KEY,
            student_id INTEGER REFERENCES students(id),
            grade INTEGER NOT NULL
        );
    """)

    op.execute("""
        CREATE INDEX IF NOT EXISTS idx_grades_student_id
        ON grades(student_id);
    """)


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS grades;")
    op.execute("DROP TABLE IF EXISTS students;")
