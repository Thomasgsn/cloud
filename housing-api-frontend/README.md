# Housing Prediction Frontend

Frontend Streamlit pour interroger l'API FastAPI du projet `housing-api`.

## Codespaces

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Local

### Fonctionnement

- L'interface affiche un formulaire avec les 8 variables du modèle.
- Le bouton `Predict` envoie un `POST /predict` au backend avec `requests`.
- La réponse attendue est un JSON de la forme `{"predicted_house_value": ...}`.
- En cas d'erreur réseau ou HTTP, un message explicite est affiché dans l'UI.

### Configuration du backend

### Installation locale

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Exemple pour lancer en local :

[Décommentez le lien au backend local](./app.py#l20)
[Commentez le lien au backend du codespaces](./app.py#l21)\

```bash
streamlit run app.py
```

### Backend attendu

- `GET /health` pour vérifier l'état du service.
- `POST /predict` avec le JSON suivant :

```json
{
  "MedInc": 8.3252,
  "HouseAge": 41.0,
  "AveRooms": 6.984,
  "AveBedrms": 1.024,
  "Population": 322.0,
  "AveOccup": 2.555,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```
