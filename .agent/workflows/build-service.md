---
description: "Workflow para criar/buildar um novo serviço"
---

# Build New Service Workflow

1. **Scaffold**
   - Execute o skill `service_scaffold` passando o nome do serviço.
   - Isso criará `Dockerfile`, `src/index.js` (ou `main.py`) e `.dockerignore`.

2. **Add to Compose**
   - Adicione o serviço ao `ops/compose/docker-compose.prod.yml`.
   - Adicione `healthcheck`.

3. **Validate**
   - Rode `docker compose build <service_name>`.
   - Rode `docker compose up -d <service_name>`.
   - Verifique `curl localhost:<port>/health`.
