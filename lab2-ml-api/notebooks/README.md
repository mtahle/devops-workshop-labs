# Lab 2 – ML API Notebooks

These notebooks are the **student-first version** of Lab 2.
They teach the ML project flow in notebook format first, then transition to a real REST API web app.

## Learning Path

1. **`model.ipynb`** — train and save the model artifact (`../model.pkl`)
2. **`test_model.ipynb`** — validate model behavior and accuracy
3. **`main.ipynb`** — convert notebook logic into production REST API code (`../main.py`)

---

## Prerequisites

From `/home/runner/work/devops-workshop-labs/devops-workshop-labs/lab2-ml-api`:

```bash
pip install -r requirements.txt
```

---

## Notebook-first workflow

From `/home/runner/work/devops-workshop-labs/devops-workshop-labs/lab2-ml-api/notebooks`:

```bash
jupyter notebook model.ipynb
jupyter notebook test_model.ipynb
jupyter notebook main.ipynb
```

After running all cells:
- `../model.pkl` is created for inference.
- `../main.py` is generated as the REST API app file.

---

## Move from notebook to web app (REST API)

From `/home/runner/work/devops-workshop-labs/devops-workshop-labs/lab2-ml-api`:

```bash
uvicorn main:app --reload
```

Then test via:
- Swagger UI: `http://localhost:8000/docs`
- or curl:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
```

Expected response includes `"prediction": "setosa"`.

---

## Optional CI-aligned validation

From `/home/runner/work/devops-workshop-labs/devops-workshop-labs/lab2-ml-api`:

```bash
python model.py
pytest tests/ -v
```
