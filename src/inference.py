from pathlib import Path

import joblib
from sklearn.base import ClassifierMixin
from sklearn.datasets import load_iris

from training import MODEL_PATH

CLASS_NAMES = load_iris().target_names


def load_model(path: Path = MODEL_PATH) -> ClassifierMixin:
    """Load the trained model from a file."""
    if not path.is_file():
        raise FileNotFoundError(f"Model file not found: {path}")
    return joblib.load(path)


def predict(model: ClassifierMixin, features: list[float]) -> str:
    """Predict the iris class name for one sample.

    features: [sepal length, sepal width, petal length, petal width] in cm.
    """
    class_index = model.predict([features])[0]
    return str(CLASS_NAMES[class_index])


if __name__ == "__main__":
    model = load_model()
    print(predict(model, [5.1, 3.5, 1.4, 0.2]))
