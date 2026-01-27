# Deploy to Coolify Runbook

This guide explains how to deploy the JARVIS-REFRIMIX stack to Coolify.

## Prerequisites
- Access to Coolify Dashboard.
- Git repository connected to Coolify.

## Steps

1. **Create Project**
   - In Coolify, create a new Project -> Environment -> Resource.
   - Select "Docker Compose".

2. **Configuration**
   - Paste the content of `ops/compose/docker-compose.prod.yml`.
   - **Crucial**: Ensure `build: context` paths are correct. Coolify clones the repo root.
     - Our compose assumes it runs from `ops/compose/`, so paths are `../../services/xxx`.
     - If Coolify runs from root, you might need to adjust paths to `./services/xxx` OR set the Working Directory in Coolify to `ops/compose`.
   - **Recommendation**: Set Working Directory in Coolify to `.` (root) and update compose paths to `./services/xxx` if needed, OR just set Working Directory to `ops/compose`.

3. **Environment Variables**
   - Add the following secrets in Coolify:
     - `OPENAI_API_KEY`: ...
     - `POSTGRES_PASSWORD`: ...
     - `REDIS_PASSWORD`: ...

4. **Deploy**
   - Click "Deploy".
   - Watch Build Logs.

5. **Verification**
   - Check if all containers are green (Healthchecks passing).
   - Curl the healthcheck endpoints via the Domains configured.
