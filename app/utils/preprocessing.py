import pandas as pd

def preprocess_input_data(df: pd.DataFrame, target_encoder):
    """Aplica o pré-processamento necessário ao DataFrame de entrada."""
    # Mapeando colunas manualmente pq eu sou masoquista
    race_columns = ["race:AfricanAmerican", "race:Asian", "race:Caucasian", "race:Hispanic", "race:Other"]
    gender_columns = ["gender_Female", "gender_Male", "gender_Other"]
    smoking_columns = [
        "smoking_history_No Info",
        "smoking_history_current",
        "smoking_history_ever",
        "smoking_history_former",
        "smoking_history_never",
        "smoking_history_not current",
    ]
    hypertension_columns = ["hypertension_0", "hypertension_1"]
    heart_disease_columns = ["heart_disease_0", "heart_disease_1"]

    # One-hot encoding para as colunas necessárias
    race_row = {col: 0 for col in race_columns}
    race_row[f"race:{df.at[0, 'race']}"] = 1
    race_df = pd.DataFrame([race_row])

    gender_row = {col: 0 for col in gender_columns}
    gender_row[f"gender_{df.at[0, 'gender']}"] = 1
    gender_df = pd.DataFrame([gender_row])

    smoking_row = {col: 0 for col in smoking_columns}
    smoking_row[f"smoking_history_{df.at[0, 'smoking_history']}"] = 1
    smoking_df = pd.DataFrame([smoking_row])

    hypertension_row = {hypertension_columns[0]: int(not df.at[0, 'hypertension']),
                        hypertension_columns[1]: int(df.at[0, 'hypertension'])}
    hypertension_df = pd.DataFrame([hypertension_row])

    heart_disease_row = {heart_disease_columns[0]: int(not df.at[0, 'heart_disease']),
                         heart_disease_columns[1]: int(df.at[0, 'heart_disease'])}
    heart_disease_df = pd.DataFrame([heart_disease_row])

    # TargetEncoding pra 'location'
    location_encoded = pd.DataFrame({"location": target_encoder.transform(df["location"]).to_numpy().ravel()}, index=df.index)

    # Manter colunas numéricas
    numeric_columns = df[["age", "bmi", "hba1c", "blood_glucose"]]

    # Concatenar tudo
    processed_data = pd.concat(
        [numeric_columns, location_encoded, race_df, gender_df, smoking_df, hypertension_df, heart_disease_df],
        axis=1
    )

    # Renomear e garantit a ordem
    processed_data.rename(columns={
    "hba1c": "hbA1c_level",
    "blood_glucose": "blood_glucose_level"
    }, inplace=True)

    desired_order = [
    "age", "location", "race:AfricanAmerican", "race:Asian", "race:Caucasian",
    "race:Hispanic", "race:Other", "bmi", "hbA1c_level", "blood_glucose_level",
    "gender_Female", "gender_Male", "gender_Other",
    "smoking_history_No Info", "smoking_history_current",
    "smoking_history_ever", "smoking_history_former",
    "smoking_history_never", "smoking_history_not current",
    "hypertension_0", "hypertension_1", "heart_disease_0", "heart_disease_1"
    ]

    processed_data = processed_data[desired_order]

    return processed_data