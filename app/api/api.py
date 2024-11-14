from fastapi import APIRouter
from app.dtos.predict_request import PredictionRequest
from app.services.predict import predict

router = APIRouter()

@router.get("/")
async def isWorking():
    return "Okay"

@router.post("/predict")
async def predict_endpoint(req: PredictionRequest):
    prediction = predict(req.model_dump())
    return {"prediction": prediction}