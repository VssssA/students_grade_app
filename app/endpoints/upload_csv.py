from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas import UploadResponse
from app.services.services import upload_grades_service

router = APIRouter()

@router.post("/upload-grades", response_model=UploadResponse)
async def upload_grades(file: UploadFile = File(...)) -> dict[str,object]:
    try:
        content = await file.read()
        return await upload_grades_service(content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
