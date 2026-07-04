# Lab 1: Your First Container
**Duration:** 25 minutes  
**Session:** 1 (end of session)  
**Goal:** Get a Python script running inside a Docker container.

---

## Learning Objectives

By the end of this lab, students should be able to:
- Explain what each Dockerfile instruction does.
- Build a Python image with dependency caching in mind.
- Run a container and validate expected runtime output.

## Success Criteria (Checkpoint)

Students are successful when all of the following are true:
- `docker build -t lab1-app .` completes without errors.
- `docker run lab1-app` prints the greeting + Python version + date.
- Student can explain why `requirements.txt` is copied before app files.

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

## Common Troubleshooting Path

Use this order when diagnosing issues:
1. Confirm file names and Dockerfile paths are exact.
2. Rebuild image and watch the first failing step.
3. Validate CMD uses JSON array form.
4. Confirm dependencies were installed before app copy.

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `COPY failed: file not found` | Wrong filename in COPY | Check exact filename spelling |
| `python: not found` | Wrong CMD syntax | Use `["python", "app.py"]` not `python app.py` |
| `ModuleNotFoundError` | pip install didn't run | Make sure `RUN pip install` is before `COPY . .` |
| Image builds but runs nothing | Missing CMD | Add `CMD ["python", "app.py"]` at the end |

---

## Wrap-Up Reflection Questions

1. Which Dockerfile step changed most often while iterating?
2. What benefit did you observe from Docker layer caching?
3. What would you change first to containerize your own project?
