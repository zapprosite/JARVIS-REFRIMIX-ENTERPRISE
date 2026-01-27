---
name: service_scaffold
description: "Gera boilerplate para novo microserviço"
---

# Service Scaffold Skill

Gere a estrutura básica:

1. `Dockerfile`:
   ```dockerfile
   FROM node:18-alpine
   WORKDIR /app
   COPY package*.json ./
   RUN npm ci --only=production
   COPY . .
   CMD ["node", "src/index.js"]
   ```

2. `src/index.js`:
   - Express/Fastify server.
   - `GET /health` endpoint.
   - JSON Logger setup (pino/winston).
