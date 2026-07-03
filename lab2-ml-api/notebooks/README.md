# Lab 2 – ML API Notebooks

These notebooks walk you through the full lifecycle of building an ML-powered REST API: training a model, defining the API, and validating predictions.

## Use Case

Train a **Random Forest** classifier on the classic [Iris dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-dataset) and serve it as a **FastAPI** inference endpoint that predicts the flower species (`setosa`, `versicolor`, or `virginica`) from four measurements (sepal/petal length and width).

---

## Notebooks

| Notebook | Purpose |
|---|---|
| `model.ipynb` | Train the classifier and export `model.pkl` |
| `main.ipynb` | Define the FastAPI application and `/predict` endpoint |
| `test_model.ipynb` | Run pytest tests to validate model accuracy and predictions |

---

## Prerequisites

Install the required packages (from the `lab2-ml-api` directory):

```bash
pip install -r requirements.txt
```

---

## How to Run

### 1. Train the model — `model.ipynb`

Open and run all cells in order. The notebook:
1. Loads the Iris dataset.
2. Splits data into train/test sets.
3. Trains a `RandomForestClassifier`.
4. Prints test accuracy.
5. Saves the model to `model.pkl`.

```bash
jupyter notebook model.ipynb
```

> **Output:** `model.pkl` saved in the same directory.

---

### 2. Explore the API definition — `main.ipynb`

Open and run all cells to see how the FastAPI app is structured. The notebook defines:
- `GET /` – health check endpoint.
- `POST /predict` – accepts four flower measurements and returns the predicted species.

```bash
jupyter notebook main.ipynb
```

> **Note:** This notebook is for exploration. The actual running API lives in `../main.py` and is started with `uvicorn`.

---

### 3. Validate the model — `test_model.ipynb`

Open and run all cells to execute pytest tests inline. The tests verify:
- The model file loads correctly.
- Predictions return a valid class index (0, 1, or 2).
- Known samples map to the correct species.
- Overall accuracy is ≥ 90 %.

```bash
jupyter notebook test_model.ipynb
```

Alternatively, run the tests directly from the terminal (from `lab2-ml-api/notebooks`):

```bash
pytest test_model.ipynb --nbmake
```

---

## Quick Start (full flow)

```bash
# 1. Install dependencies
cd lab2-ml-api
pip install -r requirements.txt

# 2. Train the model
cd notebooks
jupyter nbconvert --to notebook --execute model.ipynb

# 3. Start the API
cd ..
uvicorn main:app --reload

# 4. Test a prediction
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
# Expected: {"prediction": "setosa", "class_index": 0}
```

Interactive API docs are available at **http://localhost:8000/docs** once the server is running.
