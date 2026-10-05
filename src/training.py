from pathlib import Path

import joblib
from sklearn.base import ClassifierMixin
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

MODEL_PATH = Path("models") / "iris_model.joblib"


def load_data():
    """Load the iris dataset and return features and labels (X, y)."""
    return load_iris(return_X_y=True)


def train_model(X, y) -> ClassifierMixin:
    """Train a simple classifier on the given data and return it."""
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model


def save_model(model: ClassifierMixin, path: Path = MODEL_PATH) -> None:
    """Save the trained model to a file using joblib."""
    path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)


if __name__ == "__main__":
    X, y = load_data()
    model = train_model(X, y)
    save_model(model)
    print(f"Model saved to {MODEL_PATH} (train accuracy: {model.score(X, y):.3f})")
