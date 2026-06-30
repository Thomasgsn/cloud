import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def main():
    # Charger le dataset
    print("Chargement du dataset California Housing...")
    california = fetch_california_housing(as_frame=True)
    
    X = california.data
    y = california.target
    
    # Conserver uniquement les variables demandées
    features = ["MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup", "Latitude", "Longitude"]
    X = X[features]

    # Créer un jeu d'entraînement et un jeu de test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraînement
    print("Entraînement de la Random Forest...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Sauvegarde
    joblib.dump(model, "model.joblib")
    print("Modèle sauvegardé dans model.joblib")

if __name__ == "__main__":
    main()