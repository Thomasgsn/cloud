from __future__ import annotations

import shutil
import sys
from importlib.util import find_spec
from pathlib import Path

from evaluate import evaluate_model
from train import train_model


BASE_DIR = Path(__file__).resolve().parent
PIPELINE_PATH = BASE_DIR / "pipeline.yml"
PRODUCTION_DIR = BASE_DIR / "production"
MODEL_PATH = BASE_DIR / "model.joblib"
REPORT_PATH = BASE_DIR / "reports" / "evaluation.txt"
THRESHOLD_DEFAULT = 0.90


def load_pipeline_definition() -> dict:
    pipeline = {"steps": []}
    current_step: dict[str, str] | None = None

    for raw_line in PIPELINE_PATH.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("threshold:"):
            pipeline["threshold"] = float(stripped.split(":", 1)[1].strip())
            continue
        if stripped == "steps:":
            continue
        if stripped.startswith("- "):
            if current_step:
                pipeline["steps"].append(current_step)
            current_step = {}
            remainder = stripped[2:].strip()
            if remainder and ":" in remainder:
                key, value = remainder.split(":", 1)
                current_step[key.strip()] = value.strip()
            continue
        if current_step is None or ":" not in stripped:
            raise ValueError(f"Format YAML non supporté: {raw_line}")

        key, value = stripped.split(":", 1)
        current_step[key.strip()] = value.strip()

    if current_step:
        pipeline["steps"].append(current_step)

    return pipeline


def install_dependencies() -> None:
    requirements_path = BASE_DIR / "requirements.txt"
    if not requirements_path.exists():
        raise FileNotFoundError("requirements.txt introuvable.")

    required_modules = {
        "joblib": "joblib",
        "pandas": "pandas",
        "scikit-learn": "sklearn",
    }

    missing_modules = [
        requirement
        for requirement, module_name in required_modules.items()
        if find_spec(module_name) is None
    ]

    if missing_modules:
        raise ImportError(
            "Dépendances manquantes: " + ", ".join(sorted(missing_modules))
        )

    print("[INSTALL]OK")


def validate_model(threshold: float) -> float:
    if not REPORT_PATH.exists():
        raise FileNotFoundError("Rapport d'évaluation introuvable.")

    content = REPORT_PATH.read_text(encoding="utf-8").strip()
    if "=" not in content:
        raise ValueError("Format du rapport invalide.")

    _, value = content.split("=", 1)
    accuracy = float(value)
    if accuracy < threshold:
        raise ValueError(
            f"Score insuffisant: {accuracy:.2f} < seuil {threshold:.2f}"
        )

    print("[VALIDATE]OK")
    return accuracy


def deploy_model() -> None:
    PRODUCTION_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(MODEL_PATH, PRODUCTION_DIR / "model.joblib")
    print("[DEPLOY]OK")


def run_step(step_type: str, threshold: float) -> None:
    if step_type == "install":
        install_dependencies()
    elif step_type == "train":
        train_model()
    elif step_type == "evaluate":
        evaluate_model()
    elif step_type == "validate":
        validate_model(threshold)
    elif step_type == "deploy":
        deploy_model()
    else:
        raise ValueError(f"Étape inconnue: {step_type}")


def main() -> None:
    pipeline = load_pipeline_definition()
    threshold = float(pipeline.get("threshold", THRESHOLD_DEFAULT))
    steps = pipeline.get("steps", [])

    for step in steps:
        step_type = step.get("type")
        run_step(step_type, threshold)

    print("[PIPELINE]SUCCESS")


if __name__ == "__main__":
    main()
