from pydantic import BaseModel

class PredictionRequest(BaseModel):
    age: float
    location: str
    race: str
    bmi: float
    hba1c: float
    blood_glucose: float
    gender: str
    smoking_history: str
    hypertension: bool
    heart_disease: bool