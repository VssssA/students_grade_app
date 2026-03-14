from fastapi import FastAPI
from app.api.endpoints.upload_csv import router as upload_csv_router 
from app.api.endpoints.find_more_3_twos import router as find_more_than_3_router 
from app.api.endpoints.find_less_5_twos import router as find_less_than_5_router

app = FastAPI(title="Grades service")

app.include_router(upload_csv_router)
app.include_router(find_more_than_3_router)
app.include_router(find_less_than_5_router)

# @app.get("/")
# async def hello_world():
#     return {"hello": "world"}

