import io
import pytest

def test_upload_csv_success(test_app):
    csv_content = """Дата;Номер группы;ФИО;Оценка
11.03.2025;101Б;Курочкин Антон Владимирович;4
18.09.2024;102Б;Москвичев Андрей;3
26.09.2024;103М;Фомин Глеб Александрович;4
"""

    file = {
        "file": (
            "grades.csv",
            io.BytesIO(csv_content.encode("utf-8-sig")),
            "text/csv"
        )
    }
    response = test_app.post("/upload-grades",files=file)

    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")  # Добавьте для отладки


    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"
    assert data["records_loaded"] == 3
    assert data["students"] == 3

def test_upload_csv_invalid_grade(test_app):
    csv_content = """Дата;Номер группы;ФИО;Оценка
11.03.2025;101Б;Курочкин Антон Владимирович;4
18.09.2024;102Б;Москвичев Андрей;1231425345234
26.09.2024;103М;Фомин Глеб Александрович;4
"""

    file = {
        "file": (
            "bad.csv",
            io.BytesIO(csv_content.encode("utf-8-sig")),
            "text/csv"
        )
    }

    response = test_app.post("/upload-grades", files=file)

    assert response.status_code == 400
    assert "Invalid grade" in response.text

def test_upload_csv_invalid_header(test_app):
    csv_content = """
11.03.2025;101Б;Курочкин Антон Владимирович;4
18.09.2024;102Б;Москвичев Андрей;3
26.09.2024;103М;Фомин Глеб Александрович;4
"""

    file = {
        "file": (
            "bad.csv",
            io.BytesIO(csv_content.encode("utf-8-sig")),
            "text/csv"
        )
    }

    response = test_app.post("/upload-grades", files=file)

    assert response.status_code == 400
    assert "Invalid CSV header" in response.text