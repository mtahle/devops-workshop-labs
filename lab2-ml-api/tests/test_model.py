import pickle
import numpy as np
import pytest


@pytest.fixture
def model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)


def test_model_loads(model):
    assert model is not None


def test_prediction_returns_valid_class(model):
    features = np.array([[5.1, 3.5, 1.4, 0.2]])
    prediction = model.predict(features)
    assert prediction[0] in [0, 1, 2]


def test_setosa_prediction(model):
    # Known setosa sample
    features = np.array([[5.1, 3.5, 1.4, 0.2]])
    assert model.predict(features)[0] == 0


def test_versicolor_prediction(model):
    # Known versicolor sample
    features = np.array([[6.3, 3.3, 4.7, 1.6]])
    assert model.predict(features)[0] == 1


def test_virginica_prediction(model):
    # Known virginica sample
    features = np.array([[6.7, 3.0, 5.2, 2.3]])
    assert model.predict(features)[0] == 2


def test_model_accuracy(model):
    from sklearn.datasets import load_iris
    from sklearn.metrics import accuracy_score

    X, y = load_iris(return_X_y=True)
    predictions = model.predict(X)
    accuracy = accuracy_score(y, predictions)
    assert accuracy >= 0.90, f"Accuracy {accuracy:.2%} is below the 90% threshold"
