# Lab 1: Your First Container
**Duration:** 25 minutes  
**Session:** 1 (end of session)  
**Goal:** Get a Python script running inside a Docker container.

---

## What's in this folder

```
lab1-first-container/
├── app.py              ← pre-written Python script
├── requirements.txt    ← one dependency
├── Dockerfile          ← INCOMPLETE — you fill this in
└── Dockerfile.solution ← check your work after
```

---

## Instructions

### Step 1: Read the existing files
Before writing anything, read `app.py` and `requirements.txt`. Understand what the script does.

### Step 2: Write the Dockerfile
Open `Dockerfile`. It has comments guiding you. Fill in each instruction.

Hints:
- Base image: `python:3.11-slim`
- Working directory: `/app`
- Copy `requirements.txt` first, then install, then copy the rest
- The script runs with `python app.py`

### Step 3: Build the image
```bash
docker build -t lab1-app .
```

You should see each Dockerfile instruction run as a step.

### Step 4: Run the container
```bash
docker run lab1-app
```

**Expected output:**
```
Hello from inside Docker!
Running Python 3.11.x
Today is: 2026-06-19
```

### Step 5: Bonus — Observe layer caching
1. Change a line in `app.py` (e.g., change the greeting text)
2. Run `docker build -t lab1-app .` again
3. Notice which steps say `CACHED` — only the last layers rebuild
4. This is why we copy `requirements.txt` before the rest of the code

### Step 6: Check your solution
Compare your `Dockerfile` with `Dockerfile.solution`.

---

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `COPY failed: file not found` | Wrong filename in COPY | Check exact filename spelling |
| `python: not found` | Wrong CMD syntax | Use `["python", "app.py"]` not `python app.py` |
| `ModuleNotFoundError` | pip install didn't run | Make sure `RUN pip install` is before `COPY . .` |
| Image builds but runs nothing | Missing CMD | Add `CMD ["python", "app.py"]` at the end |
