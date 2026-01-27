# Secrets Management in Coolify

## Overview
We strictly avoid hardcoding secrets in `docker-compose.yml`. Instead, we use Coolify's Environment Variables feature.

## Required Secrets
The following variables must be set in Coolify (Project -> Environment -> Secrets):

| Variable            | Description                      | Example           |
| ------------------- | -------------------------------- | ----------------- |
| `POSTGRES_PASSWORD` | Database password                | `StrongP@ssw0rd!` |
| `OPENAI_API_KEY`    | Key for LLM                      | `sk-proj-...`     |
| `REDIS_PASSWORD`    | (Optional) If Redis Auth enabled | `...`             |

## How to Set
1. Go to your Resource (Docker Compose) in Coolify.
2. Click **Environment Variables**.
3. Add the keys listed above.
4. Redeploy.

## Local Development
For local testing, create a `.env` file based on `ops/coolify/env/prod.env.example`.
**NEVER COMMIT .env TO GIT.**
