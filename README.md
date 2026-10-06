Introduction to building a production-ready machine learning application while learning essential MLOps practices and tools, culminating in a local server for ML model predictions.

# Setup
To run the web application:

    uv run uvicorn app:app --app-dir src --reload --port 8000

To train and save the model:

    uv run python src/training.py