# Lab 5 (Advanced): Continuous Deployment to EC2 with Docker Compose
**Duration:** 50 minutes  
**Track:** Advanced (after Labs 1–4)  
**Goal:** Deploy application updates to EC2 automatically using GitHub Actions, self-hosted runner, feature-branch workflow, and GitHub Secrets.

---

## Learning Objectives

By the end of this lab, students should be able to:
- Use a feature-branch + pull-request flow for safe deployment.
- Run deployment jobs on a self-hosted runner.
- Manage deployment configuration through GitHub Secrets.
- Deploy/redeploy app containers on EC2 using Docker Compose.

## Delivery Pattern Used in This Lab

1. Create feature branch (`feature/*`)
2. Open PR to `main`
3. CI validates PR
4. Merge PR into `main`
5. CD workflow runs on `main` and deploys on EC2 via self-hosted runner

---

## Files in this Lab

```
lab5-cd-ec2-compose/
├── README.md
├── cd-ec2-compose.yml.template
├── docker-compose.prod.yml.template
└── .env.prod.example
```

---

## Prerequisites

- EC2 instance created (Lab 4).
- Docker and Docker Compose installed on EC2.
- Self-hosted GitHub Actions runner installed on EC2 and online.
- Repository contains a Dockerfile for your app.

## Required GitHub Secrets

Create these in **Settings → Secrets and variables → Actions**:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
- `APP_IMAGE_NAME` (example: `iris-classifier`)
- `APP_PORT` (example: `8000`)
- `APP_ENV` (example: `production`)

---

## Instructions

### Step 1: Prepare deployment files in your app repo

Copy:
- `docker-compose.prod.yml.template` → `docker-compose.prod.yml`
- `cd-ec2-compose.yml.template` → `.github/workflows/cd.yml`

Use `.env.prod.example` as a local reference only.  
In CI/CD, `.env.prod` is generated automatically from GitHub Secrets by the workflow.

### Step 2: Configure the self-hosted runner labels

The template uses:
- `self-hosted`
- `linux`
- `x64`
- `ec2-prod`

If needed, adjust labels in workflow to match your runner.

### Step 3: Use feature-branch workflow

```bash
git checkout -b feature/improve-predict-endpoint
# make changes
git add .
git commit -m "Improve prediction endpoint"
git push origin feature/improve-predict-endpoint
```

Open PR to `main`, pass CI, then merge.

### Step 4: Watch CD deployment

After merge to `main`, deployment runs automatically:
1. Open Actions tab
2. Open `Deploy to EC2 with Docker Compose` workflow run started by push to `main`
3. Confirm deploy job runs on self-hosted runner
4. Verify app is reachable on EC2 public IP + app port

If needed for testing, you can also trigger the same workflow manually using **Run workflow** (`workflow_dispatch`).

---

## Success Criteria (Checkpoint)

- PR-based feature branch flow is used (no direct push to main for features).
- CD workflow runs on self-hosted EC2 runner after merge to main.
- New image is pulled and container restarted with Docker Compose.
- Application is reachable after deployment.

---

## Common Troubleshooting Path

1. Confirm self-hosted runner is online and has matching labels.
2. Confirm all required GitHub Secrets are set.
3. Check Docker login/pull errors in workflow logs.
4. Validate EC2 security group allows app port.
5. Run `docker compose ps` and `docker compose logs` on EC2.

## Reflection Questions

1. Why is PR merge to main a safer deployment trigger than pushing directly?
2. What are the risks of running deployment on a self-hosted runner?
3. Which additional gate would you add before production deploy?
