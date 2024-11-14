import pandas as pd
from app.utils.open_files import load_pipeline, load_target_encoder
from app.utils.preprocessing import preprocess_input_data

pipeline = load_pipeline()
target_encoder = load_target_encoder()

def predict(data: dict):
    df = pd.DataFrame([data])

    df = preprocess_input_data(df, target_encoder)

    prediction = pipeline.predict(df)
    return prediction[0]