CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    full_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS grades (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id),
    grade INTEGER NOT NULL CHECK (grade BETWEEN 2 AND 5)
);

CREATE INDEX IF NOT EXISTS idx_grades_student_id ON grades(student_id);
CREATE INDEX IF NOT EXISTS idx_grades_grade ON grades(grade);
