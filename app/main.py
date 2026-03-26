from fastapi import FastAPI

from app.endpoints.analyze_csv import router as analyze_csv_router
from app.endpoints.upload_csv import router as upload_csv_router

app = FastAPI(title="Grades service")

app.include_router(upload_csv_router)
app.include_router(analyze_csv_router)
