# Workshop: From Notebook to Production
## DevOps & MLOps for CS/SE Graduation Projects

**Audience:** Final-year CS/SE students with ML/DS graduation projects  
**Format:** 2 sessions × 3 hours (fully remote, live coding)  
**Language:** English slides, Arabic instruction  
**Level:** Foundation — not a complete MLOps training  
**Instructor:** Mujahed Al-Tahleh  

---

## Delivery Model (Trainer Best-Practice Alignment)

- **Flipped setup:** Send setup + pre-read before Session 1 so live time is used for guided practice.
- **Hands-on-first pacing:** Prioritize labs and troubleshooting over long lecture blocks.
- **Checkpoint-based flow:** Add explicit success checks after each major step.
- **Feedback loop:** Collect quick learner feedback at the end of each session and adjust pacing.

## Session Overview

| Session | Title | Core Topics |
|---------|-------|-------------|
| **Session 1** | The Foundation | DevOps intro, Cloud basics, Docker fundamentals, Lab 1 |
| **Session 2** | Ship and Automate | ML API in Docker, CI/CD, GitHub Actions, Labs 2–3, Model versioning, Serverless |

## Facilitation Flow per Session

1. **Warm-up (10–15 min):** recap objectives + verify student environment.
2. **Concept burst (15–20 min):** short explanation with live demo.
3. **Guided lab block:** students build while instructor narrates decisions.
4. **Checkpoint pause:** verify outputs before moving forward.
5. **Wrap-up (10 min):** reflection, common mistakes, and next-step assignment.

## Learner Support Model During Labs

- Keep a dedicated Q&A channel and answer blocking issues quickly.
- Use the same command sequence for everyone before branching into troubleshooting.
- Escalate repeated issues into a quick live fix so all learners benefit.
- Reserve 5 minutes after each lab for “what failed and why” discussion.

## Labs

| Lab | What students build | Duration |
|-----|---------------------|----------|
| **Lab 1** | Containerize a Python script | 25 min |
| **Lab 2** | ML inference API — FastAPI + scikit-learn Iris classifier | 30 min |
| **Lab 3** | CI/CD pipeline — GitHub Actions for the ML repo | 25 min |

## Post-Session Follow-Up Expectations

- Share recording/slides and key commands within 24 hours.
- Assign one practical follow-up task per session.
- Ask students to submit one blocker and one takeaway.
- Review common blockers before the next session starts.

## Self-Learning Assignments

See [ASSIGNMENTS.md](./ASSIGNMENTS.md):
- MLflow experiment tracking on their own project
- Containerize their graduation project model
- TensorFlow Serving (reference pattern)
- Cloud deployment: AWS ECS or Lambda

## Repository Structure

```
devops-workshop-labs/
├── README.md
├── lab1-first-container/
├── lab2-ml-api/
├── lab3-github-actions/
└── slides/
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

Send students a setup guide and ask them to verify all prerequisites before the session.
