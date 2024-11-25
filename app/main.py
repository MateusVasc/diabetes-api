from fastapi import FastAPI
from app.api.api import router as api_router

app = FastAPI()

app.include_router(router=api_router)