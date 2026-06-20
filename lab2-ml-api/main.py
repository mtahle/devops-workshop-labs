from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

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

    class Config:
        json_schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2,
            }
        }


class PredictionOutput(BaseModel):
    prediction: str
    class_index: int


@app.get("/")
def root():
    return {"message": "Iris Classifier API is running. Visit /docs to test."}


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
