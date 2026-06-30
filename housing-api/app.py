from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import pandas as pd

# Chargement du modèle au démarrage
model = joblib.load("model.joblib")

app = FastAPI(title="Housing Prediction API")

# Schéma d'entrée basé sur les variables du dataset
class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/health")
def health_check():
    return {"status": "L'API fonctionne"}

@app.post("/predict")
def predict(features: HouseFeatures):
    # Convertir l'entrée pour le modèle
    input_data = pd.DataFrame([features.dict()])
    prediction = model.predict(input_data)[0]
    
    # Format de sortie attendu
    return {"predicted_house_value": round(prediction, 2)}

# Bonus : Endpoint pour les prédictions en lot
@app.post("/predict_batch")
def predict_batch(features_list: List[HouseFeatures]):
    input_data = pd.DataFrame([f.dict() for f in features_list])
    predictions = model.predict(input_data)
    
    return {"predicted_house_values": predictions.tolist()}