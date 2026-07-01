# Housing Prediction API

API REST FastAPI qui prédit la valeur médiane d'un logement en Californie via un modèle Random Forest.

## Codespaces

Si il n'y a pas de model:

```bash
pip install scikit-learn joblib pandas
python train.py
```

Lancer le serveur Backend:

```bash
python -m uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## Local

### Prérequis

- [Docker](https://docs.docker.com/get-docker/) et Docker Compose installés
- Port `8000` disponible sur la machine hôte

---

### Exécution avec Docker Compose

#### Étape 1 — Cloner le dépôt

```bash
git clone git@github.com:Thomasgsn/cloud
cd cloud/housing-api
```

#### Étape 2 — Entraîner le modèle

```bash
pip install scikit-learn joblib pandas
python train.py
```

#### Étape 3 — Construire et lancer le service

```bash
docker compose up --build
```

L'API est disponible sur [http://localhost:8000](http://localhost:8000).

Pour lancer en arrière-plan :

```bash
docker compose up --build -d
```

#### Étape 4 — Vérifier que l'API fonctionne

```bash
curl http://localhost:8000/health
```

Réponse attendue :

```json
{"status": "L'API fonctionne"}
```

#### Étape 5 — Faire une prédiction

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984,
    "AveBedrms": 1.024,
    "Population": 322.0,
    "AveOccup": 2.555,
    "Latitude": 37.88,
    "Longitude": -122.23
  }'
```

Réponse attendue :

```json
{"predicted_house_value": 4.18}
```

#### Étape 6 — Prédiction en lot (`/predict_batch`)

```bash
curl -X POST http://localhost:8000/predict_batch \
  -H "Content-Type: application/json" \
  -d '[
    {"MedInc": 8.3252, "HouseAge": 41.0, "AveRooms": 6.984, "AveBedrms": 1.024, "Population": 322.0, "AveOccup": 2.555, "Latitude": 37.88, "Longitude": -122.23},
    {"MedInc": 3.5, "HouseAge": 25.0, "AveRooms": 5.0, "AveBedrms": 1.1, "Population": 800.0, "AveOccup": 3.0, "Latitude": 34.05, "Longitude": -118.25}
  ]'
```

#### Étape 7 — Arrêter le service

```bash
docker compose down
```

---

### Documentation interactive

FastAPI génère automatiquement une interface Swagger UI :

- **Swagger UI** : [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc** : [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

### Structure du projet

```plaintext
housing-api/
├── app.py              # API FastAPI
├── train.py            # Script d'entraînement du modèle
├── model.joblib        # Modèle Random Forest pré-entraîné
├── requirements.txt    # Dépendances Python
├── dockerfile          # Image Docker
├── docker-compose.yml  # Orchestration du service
└── questions.md        # Réponses aux questions théoriques
```

### Endpoints

| Méthode | Route           | Description                       |
|---------|-----------------|-----------------------------------|
| GET     | `/health`       | Vérifie que l'API est opérationnelle |
| POST    | `/predict`      | Prédit la valeur d'un logement    |
| POST    | `/predict_batch`| Prédit pour une liste de logements |
