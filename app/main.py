from fastapi import FastAPI, UploadFile, File, HTTPException

from app.schemas import UploadResponse, StudentTwos
from app.services import upload_grades_service, more_than_3, less_than_5

app = FastAPI(title="Grades service")


@app.get("/")
async def hello_world():
    return {"hello": "world"}


@app.post("/upload-grades", response_model=UploadResponse)
async def upload_grades(file: UploadFile = File(...)):
    try:
        content = await file.read()
        return await upload_grades_service(content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get(
    "/students/more-than-3-twos",
    response_model=list[StudentTwos],
)
async def more_than_3_twos():
    rows = await more_than_3()
    return rows


@app.get(
    "/students/less-than-5-twos",
    response_model=list[StudentTwos],
)
async def less_than_5_twos():
    rows = await less_than_5()
    return rows
