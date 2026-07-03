from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model.joblib"
REPORTS_DIR = BASE_DIR / "reports"
REPORT_PATH = REPORTS_DIR / "evaluation.txt"


def evaluate_model() -> float:
    if not MODEL_PATH.exists():
        raise FileNotFoundError("model.joblib introuvable. Lancer train.py.")

    iris = load_iris(as_frame=True)
    X = iris.data
    y = iris.target

    _, X_test, _, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    model = joblib.load(MODEL_PATH)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(f"Accuracy={accuracy:.2f}\n", encoding="utf-8")
    print(f"[EVALUATE]Accuracy={accuracy:.2f}")
    return accuracy


if __name__ == "__main__":
    evaluate_model()
