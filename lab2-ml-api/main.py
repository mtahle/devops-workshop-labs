from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
import pickle
import numpy as np
from fastapi.responses import HTMLResponse
app = FastAPI(
    title="Iris Classifier API",
    description="Predict Iris flower species from measurements",
    version="1.0.0",
)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

SPECIES = ["setosa", "versicolor", "virginica"]


class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2,
            }
        }
    )


class PredictionOutput(BaseModel):
    prediction: str
    class_index: int


@app.get("/", response_class=HTMLResponse)
def root():
        # Return a small Bootstrap landing page for quick API onboarding.
    return """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <title>Iris Classifier API</title>
                <link
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
                    rel="stylesheet"
                />
                <style>
                    body {
                        min-height: 100vh;
                        background: linear-gradient(120deg, #e0f7fa 0%, #f5f7ff 45%, #e8f5e9 100%);
                    }
                    .hero-card {
                        border: 0;
                        border-radius: 1.25rem;
                        box-shadow: 0 0.75rem 2rem rgba(32, 33, 36, 0.1);
                    }
                    .pill {
                        border-radius: 999px;
                        padding: 0.4rem 0.9rem;
                        font-size: 0.85rem;
                    }
                </style>
            </head>
            <body class="d-flex align-items-center py-5">
                <main class="container">
                    <div class="row justify-content-center">
                        <div class="col-12 col-lg-9">
                            <div class="card hero-card">
                                <div class="card-body p-4 p-md-5">
                                    <span class="badge text-bg-success pill mb-3">FastAPI + scikit-learn</span>
                                    <h1 class="display-6 fw-bold mb-3">Iris Classifier API</h1>
                                    <p class="lead text-secondary mb-4">
                                        Predict Iris flower species from sepal and petal measurements.
                                    </p>

                                    <div class="d-flex flex-wrap gap-2 mb-4">
                                        <span class="badge text-bg-light border">setosa</span>
                                        <span class="badge text-bg-light border">versicolor</span>
                                        <span class="badge text-bg-light border">virginica</span>
                                    </div>

                                    <div class="d-grid gap-2 d-md-flex">
                                        <a class="btn btn-primary btn-lg" href="/docs">Open API Docs</a>
                                        <a class="btn btn-outline-dark btn-lg" href="/redoc">Open ReDoc</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </main>
            </body>
        </html>
    """
        

@app.post("/predict", response_model=PredictionOutput)
def predict(data: IrisInput):
    features = np.array(
        [[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]]
    )
    class_index = int(model.predict(features)[0])
    return PredictionOutput(
        prediction=SPECIES[class_index],
        class_index=class_index,
    )
