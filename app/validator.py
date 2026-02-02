import csv

REQUIRED_COLUMNS = {"Дата","Номер группы","ФИО","Оценка"}

def parse_and_validate_csv(file_bytes: bytes):
    decoded = file_bytes.decode("utf-8-sig").splitlines()
    reader = csv.DictReader(decoded,delimiter=';')
    fieldnames = reader.fieldnames
    # print(fieldnames)
    if not REQUIRED_COLUMNS.issubset(fieldnames):
        raise ValueError("Invalid CSV header")


    rows = []
    for row in reader:
        full_name = row["ФИО"]
        # print(full_name)
        grade = int(row["Оценка"])

        if not full_name:
            raise ValueError("Empty full_name")

        if grade < 2 or grade > 5:
            raise ValueError("Invalid grade")

        rows.append((full_name, grade))

    return rows
