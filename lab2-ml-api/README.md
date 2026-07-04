# Lab 2: ML Inference API
**Duration:** 30 minutes  
**Session:** 2 (first lab)  
**Goal:** Build and run a machine learning inference API in Docker using FastAPI and scikit-learn.

---

## Learning Objectives

By the end of this lab, students should be able to:
- Train and persist a simple ML model artifact.
- Serve model inference through a FastAPI endpoint.
- Package model training + API serving into one Docker image.

## Success Criteria (Checkpoint)

Students are successful when all of the following are true:
- Docker image builds and includes a trained `model.pkl`.
- API runs at `http://localhost:8000/docs`.
- `/predict` returns the expected species for sample inputs.
- Local tests pass when running `python model.py` then `pytest tests/ -v`.

---

## What you're building

```
model.py   → train Iris classifier → save model.pkl (at Docker build time)
main.py    → FastAPI app with /predict endpoint (loads model.pkl)
Dockerfile → packages both → Docker image

docker run → http://localhost:8000/docs → click to test predictions in browser
```

---

## Files

```
lab2-ml-api/
├── model.py            ← train + save the sklearn model
├── main.py             ← FastAPI inference server
├── requirements.txt    ← pinned dependencies
├── Dockerfile          ← complete, ready to build
└── tests/
    └── test_model.py   ← model validation tests
```

---

## Instructions

### Step 1: Read all files before running anything
Open each file and understand what it does. Pay attention to:
- How `model.py` saves the model
- How `main.py` loads it
- Where in the `Dockerfile` the model gets trained

### Step 2: Build the image
```bash
docker build -t iris-classifier .
```

During the build you should see:
```
Step X/Y : RUN python model.py
 ---> Model trained and saved.
```

### Step 3: Run the container
```bash
docker run -p 8000:8000 iris-classifier
```

Expected output:
```
INFO:     Started server process [1]
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 4: Test your API
Open `http://localhost:8000/docs` in your browser.

1. Click **POST /predict**
2. Click **Try it out**
3. Paste this request body:
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```
4. Click **Execute**
5. Expected response: `{"prediction": "setosa"}`

### Step 5: Explore
Try these inputs and predict the species before clicking Execute:

| sepal_length | sepal_width | petal_length | petal_width | Expected |
|---|---|---|---|---|
| 5.1 | 3.5 | 1.4 | 0.2 | setosa |
| 6.3 | 3.3 | 4.7 | 1.6 | versicolor |
| 6.7 | 3.0 | 5.2 | 2.3 | virginica |

### Step 6: Run the tests (optional, needed for Lab 3)
```bash
# Outside Docker — install deps locally first
pip install -r requirements.txt
python model.py
pytest tests/ -v
```

### Step 7: Bonus — Push to Docker Hub
```bash
docker tag iris-classifier yourusername/iris-classifier:v1
docker push yourusername/iris-classifier:v1
```

---

## Common Troubleshooting Path

Use this order when diagnosing issues:
1. Confirm `model.py` can run locally and generates `model.pkl`.
2. Rebuild image and verify `RUN python model.py` succeeds during build.
3. Confirm container port mapping is `-p 8000:8000`.
4. Use `/docs` first before testing raw curl requests.
5. Re-run local tests before retrying CI in Lab 3.

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `FileNotFoundError: model.pkl` | Model was not trained before app startup | Ensure `RUN python model.py` executes in Docker build |
| `Connection refused on localhost:8000` | Container not running or port not mapped | Re-run with `docker run -p 8000:8000 iris-classifier` |
| Validation/test failures | Dependency or model artifact mismatch | Reinstall requirements, rerun `python model.py`, then `pytest tests/ -v` |
| Wrong prediction label | Input values malformed | Use numeric fields and known iris examples first |

---

## Discussion Questions
1. What happens if you change the model (e.g., set `n_estimators=100`) and rebuild?
2. Why do we train the model in the Dockerfile (`RUN python model.py`) instead of at startup?
3. How would you modify this for your own graduation project model?

## Wrap-Up Reflection Questions

1. What was the most important contract between `model.py` and `main.py`?
2. Which step would likely fail first in a real team CI pipeline?
3. How would you adapt this API to return confidence scores?
