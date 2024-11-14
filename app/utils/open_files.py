import pickle
import os

def load_pickle_file(file_path):
    """Carrega um arquivo pickle de um caminho especificado."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"O arquivo {file_path} não foi encontrado")
    with open(file_path, "rb") as file:
        return pickle.load(file)
    

def load_pipeline():
    """Carrega o pipeline salvo."""
    return load_pickle_file("app/models/pipeline.pkl")

def load_target_encoder():
    """Carrega o encoder de alvo salvo."""
    return load_pickle_file("app/models/target_encoder.pkl")