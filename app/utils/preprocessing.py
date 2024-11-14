import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def preprocess_input_data(df: pd.DataFrame, target_encoder):
    """Aplica o pré-processamento necessário ao Dataframe de entrada"""

    ohe_columns = ['gender', 'smoking_history', 'hypertension', 'heart_disease']
    ohe = OneHotEncoder(sparse_output=False)

    for col in ohe_columns:
        if col in df.columns:
            encoded = ohe.fit_transform(df[[col]])
            col_names = [f"{col}_{cat}" for cat in ohe.categories_[0]]
            encoded_df = pd.DataFrame(encoded, columns=col_names, index=df.index)
            df = pd.concat([df, encoded_df], axis=1)
            df.drop(columns=[col], inplace=True)

    if 'location' in df.columns:
        df['location'] = target_encoder.transform(df['location'])

    return df