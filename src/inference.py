from pathlib import Path

import joblib
from sklearn.base import ClassifierMixin
from sklearn.datasets import load_iris

from training import MODEL_PATH

CLASS_NAMES = load_iris().target_names
FEATURE_NAMES = ["sepal_length", "sepal_width", "petal_length", "petal_width"]


def load_model(path: Path = MODEL_PATH) -> ClassifierMixin:
    """Load the trained model from a file."""
    if not path.is_file():
        raise FileNotFoundError(f"Model file not found: {path}")
    return joblib.load(path)


def predict_iris_class(model: ClassifierMixin, features: dict[str, float]) -> str:
    """Predict the iris class name for one sample (feature values in cm)."""
    row = [features[name] for name in FEATURE_NAMES]
    class_index = model.predict([row])[0]
    return str(CLASS_NAMES[class_index])


if __name__ == "__main__":
    model = load_model()
    sample = {
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
    }
    print(predict_iris_class(model, sample))
