import os

import requests
import streamlit as st


FEATURE_DEFAULTS = {
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.984,
    "AveBedrms": 1.024,
    "Population": 322.0,
    "AveOccup": 2.555,
    "Latitude": 37.88,
    "Longitude": -122.23,
}


def get_backend_url() -> str:
    # backend_url = "http://localhost:8000"
    backend_url = "https://verbose-tribble-x764p9jr76p2v4r9-8000.app.github.dev/"
    return backend_url.rstrip("/")


def build_payload(values: dict[str, float]) -> dict[str, float]:
    return {
        "MedInc": float(values["MedInc"]),
        "HouseAge": float(values["HouseAge"]),
        "AveRooms": float(values["AveRooms"]),
        "AveBedrms": float(values["AveBedrms"]),
        "Population": float(values["Population"]),
        "AveOccup": float(values["AveOccup"]),
        "Latitude": float(values["Latitude"]),
        "Longitude": float(values["Longitude"]),
    }


def predict(backend_url: str, payload: dict[str, float]) -> float:
    response = requests.post(f"{backend_url}/predict", json=payload, timeout=15)
    response.raise_for_status()
    data = response.json()
    return float(data["predicted_house_value"])


st.set_page_config(page_title="Housing Predictor", page_icon="🏠", layout="centered")

st.title("Housing Price Predictor")

backend_url = get_backend_url()

with st.sidebar:
    st.header("Configuration")
    st.caption("Streamlit lit d'abord `BACKEND_URL` depuis les secrets, puis depuis les variables d'environnement.")
    st.code(backend_url, language="text")
    if st.button("Vérifier l'état du back"):
        try:
            health_response = requests.get(f"{backend_url}/health", timeout=10)
            health_response.raise_for_status()
            st.success(health_response.json().get("status", "Backend reachable"))
        except requests.RequestException as exc:
            st.error(f"Backend inaccessible: {exc}")

with st.form("prediction_form"):
    st.subheader("Housing features")
    col1, col2 = st.columns(2)

    with col1:
        med_inc = st.number_input(
            "MedInc", value=float(FEATURE_DEFAULTS["MedInc"]), format="%.4f"
        )
        house_age = st.number_input(
            "HouseAge", value=float(FEATURE_DEFAULTS["HouseAge"]), format="%.1f"
        )
        ave_rooms = st.number_input(
            "AveRooms", value=float(FEATURE_DEFAULTS["AveRooms"]), format="%.4f"
        )
        ave_bedrms = st.number_input(
            "AveBedrms", value=float(FEATURE_DEFAULTS["AveBedrms"]), format="%.4f"
        )

    with col2:
        population = st.number_input(
            "Population", value=float(FEATURE_DEFAULTS["Population"]), format="%.1f"
        )
        ave_occup = st.number_input(
            "AveOccup", value=float(FEATURE_DEFAULTS["AveOccup"]), format="%.4f"
        )
        latitude = st.number_input(
            "Latitude", value=float(FEATURE_DEFAULTS["Latitude"]), format="%.4f"
        )
        longitude = st.number_input(
            "Longitude", value=float(FEATURE_DEFAULTS["Longitude"]), format="%.4f"
        )

    submit = st.form_submit_button("Predict")

if submit:
    payload = build_payload(
        {
            "MedInc": med_inc,
            "HouseAge": house_age,
            "AveRooms": ave_rooms,
            "AveBedrms": ave_bedrms,
            "Population": population,
            "AveOccup": ave_occup,
            "Latitude": latitude,
            "Longitude": longitude,
        }
    )

    try:
        prediction = predict(backend_url, payload)
        st.success(f"Predicted house value: {prediction:.2f}")
        st.json({"input": payload, "prediction": prediction})
    except requests.HTTPError as exc:
        detail = ""
        if exc.response is not None:
            try:
                detail = exc.response.json()
            except ValueError:
                detail = exc.response.text
        st.error(f"Backend returned an error: {detail or exc}")
    except requests.RequestException as exc:
        st.error(f"Unable to contact backend: {exc}")
    except (KeyError, TypeError, ValueError) as exc:
        st.error(f"Unexpected response from backend: {exc}")
