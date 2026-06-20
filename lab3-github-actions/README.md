# Lab 3: CI/CD with GitHub Actions
**Duration:** 25 minutes  
**Session:** 2 (second lab)  
**Prerequisite:** Lab 2 completed and pushed to your own GitHub repository

**Goal:** Add a GitHub Actions CI pipeline that automatically runs tests and builds the Docker image on every push.

---

## Setup

This lab assumes you have:
- Your `iris-classifier` repo (from Lab 2) on GitHub
- A personal GitHub account

---

## Instructions

### Step 1: Create the workflow file
In your `iris-classifier` project (from Lab 2):

```bash
mkdir -p .github/workflows
```

Copy the `ci.yml.template` file from this folder to `.github/workflows/ci.yml` in your project.

### Step 2: Review the workflow
Open `.github/workflows/ci.yml` and read it. Identify:
- What triggers the workflow
- How many jobs it has
- What each step does

### Step 3: Commit and push
```bash
git add .github/
git commit -m "Add GitHub Actions CI pipeline"
git push origin main
```

### Step 4: Watch it run
1. Go to your GitHub repo
2. Click the **Actions** tab
3. Click the running workflow
4. Watch each step complete in real time

A green checkmark = your CI pipeline passed.

### Step 5: Break it intentionally
1. Open `tests/test_model.py`
2. Change this line:
   ```python
   assert model.predict(features)[0] == 0  # setosa
   ```
   to:
   ```python
   assert model.predict(features)[0] == 1  # WRONG on purpose
   ```
3. Commit and push
4. Watch the pipeline go red
5. Fix it and push again — watch it go green

This is the CI feedback loop.

### Step 6: Add a status badge to your README
Add this to your README.md (replace `USERNAME` and `REPO`):
```markdown
![CI](https://github.com/USERNAME/REPO/actions/workflows/ci.yml/badge.svg)
```

---

## Bonus: Push Docker image to Docker Hub on success
See the `ci-with-docker-push.yml.template` for an extended workflow that:
1. Runs CI tests
2. On success, builds and pushes the Docker image to Docker Hub
3. Tags the image with the git commit SHA for traceability
