# Lab 3: CI/CD with GitHub Actions
**Duration:** 25 minutes  
**Session:** 2 (second lab)  
**Prerequisite:** Lab 2 completed and pushed to your own GitHub repository

**Goal:** Add a GitHub Actions CI pipeline that automatically runs tests and builds the Docker image on every push.

---

## Learning Objectives

By the end of this lab, students should be able to:
- Explain CI trigger conditions and workflow job structure.
- Validate ML project quality with automated tests on push.
- Interpret pass/fail workflow runs and use them as feedback loops.

## Success Criteria (Checkpoint)

Students are successful when all of the following are true:
- Workflow file is added at `.github/workflows/ci.yml`.
- A push triggers a workflow run in the Actions tab.
- Students can identify one passing run and one failing run reason.
- After fixing the intentional failure, workflow returns to green.

---

## Template Reliability Notes

The provided CI templates are aligned with Lab 2 behavior:
- install dependencies from `requirements.txt`
- train model with `python model.py`
- run tests with `pytest tests/ -v`
- build Docker image and verify container startup using the root endpoint (`/`)

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

## Common Troubleshooting Path

Use this order when diagnosing issues:
1. Confirm workflow location is exactly `.github/workflows/ci.yml`.
2. Check workflow trigger conditions match your push branch.
3. Open failed job logs and identify the first failing step.
4. Fix code/tests locally, commit, then push again.

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| Workflow not appearing in Actions | Wrong file path/name | Move file to `.github/workflows/ci.yml` |
| Workflow not triggered on push | Branch mismatch in trigger | Align trigger branch with active branch |
| Tests fail unexpectedly | Local code diverged from tested assumptions | Re-run local test sequence from Lab 2 before push |
| Badge always broken | Wrong repo/workflow URL | Rebuild badge URL with correct username/repo/workflow |

---

## Wrap-Up Reflection Questions

1. Why is a failing CI pipeline useful even when it blocks merges?
2. What should run in CI for your graduation project first: tests, lint, or security checks?
3. What would you add next to move from CI to full CD?

---

## Bonus: Push Docker image to Docker Hub on success
See the `ci-with-docker-push.yml.template` for an extended workflow that:
1. Runs CI tests
2. On success, builds and pushes the Docker image to Docker Hub
3. Tags the image with the git commit SHA for traceability
