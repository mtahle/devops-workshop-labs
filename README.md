# Workshop: From Notebook to Production
## DevOps & MLOps for CS/SE Graduation Projects

**Audience:** Final-year CS/SE students with ML/DS graduation projects  
**Format:** 2 sessions × 3 hours (fully remote, live coding)  
**Language:** English slides, Arabic instruction  
**Level:** Foundation — not a complete MLOps training  
**Instructor:** Mujahed Al-Tahleh  

---

## Session Overview

| Session | Title | Core Topics |
|---------|-------|-------------|
| **Session 1** | The Foundation | DevOps intro, Cloud basics, Docker fundamentals, Lab 1 |
| **Session 2** | Ship and Automate | ML API in Docker, CI/CD, GitHub Actions, Labs 2–3, Model versioning, Serverless |

## Labs

| Lab | What students build | Duration |
|-----|---------------------|----------|
| **Lab 1** | Containerize a Python script | 25 min |
| **Lab 2** | ML inference API — FastAPI + scikit-learn Iris classifier | 30 min |
| **Lab 3** | CI/CD pipeline — GitHub Actions for the ML repo | 25 min |

## Self-Learning Assignments

See [ASSIGNMENTS.md](./ASSIGNMENTS.md):
- MLflow experiment tracking on their own project
- Containerize their graduation project model
- TensorFlow Serving (reference pattern)
- Cloud deployment: AWS ECS or Lambda

## Repository Structure

```
workshops/mlops-for-students/
├── README.md
├── SESSION_1.md          ← Full instructor script, Session 1
├── SESSION_2.md          ← Full instructor script, Session 2
├── ASSIGNMENTS.md        ← Self-learning tasks + resources
└── labs/
    ├── lab1-first-container/
    ├── lab2-ml-api/
    └── lab3-github-actions/
```

## Student Prerequisites (must verify before Session 1 starts)

```
✅ Docker Desktop installed and running  →  docker run hello-world
✅ Git installed                         →  git --version
✅ VS Code installed
✅ Python 3.10 or 3.11                   →  python --version
✅ GitHub account ready
✅ AWS account (free tier) or shared account provided by instructor
```

Send students a setup guide and ask them to verify all 5 before the session.
