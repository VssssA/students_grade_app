# Students_grade_app

### Предварительные требования
- Установленный Docker и Docker Compose
- Git для клонирования репозитория

### Запуск проекта

1. **Клонируйте репозиторий:**
```
git clone git@github.com:VssssA/students_grade_app.git
cd students_grade_app
```

Запустите проект через Docker Compose:
```
docker compose up --build
```
После успешного запуска API будет доступно по адресу: http://localhost:8000

1.  Загрузка оценок студентов
POST /upload-grades

Загрузите CSV файл с оценками студентов.

Пример запроса:

```
curl -X POST http://localhost:8000/upload-grades \
  -H "Accept: application/json" \
  -F "file=@students_grades.csv"
```

Формат CSV файла:
Дата;Номер группы;ФИО;Оценка
11.03.2025;101Б;Иванов Иван Иванович;4
18.09.2024;102Б;Иванов Иван Иванович;3
26.09.2024;103М;Иванов Иван Иванович;4
...

2. Получение студентов с более чем 3-мя двойками
GET /students/more-than-3-twos

Возвращает список студентов, у которых количество двоек превышает 3.

Пример запроса:

```
curl -X GET http://localhost:8000/students/more-than-3-twos \
  -H "Accept: application/json"
```
3. Получение студентов с менее чем 5-ю двойками
GET /students/less-than-5-twos

Возвращает список студентов, у которых количество двоек меньше 5.

Пример запроса:
```
curl -X GET http://localhost:8000/students/less-than-5-twos \
  -H "Accept: application/json"
```
Запуск тестов
Для запуска тестов выполните команду:

```
docker compose exec api pytest
```
