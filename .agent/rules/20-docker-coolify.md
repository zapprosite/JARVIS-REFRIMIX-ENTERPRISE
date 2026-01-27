---
description: "Padrões para Docker Compose e Deploy no Coolify"
---

# Docker & Coolify Rules

1. **Docker Compose**
   - Arquivo oficial de prod: `ops/compose/docker-compose.prod.yml`.
   - Serviços devem ter `restart: always` ou `unless-stopped`.
   - Networks: Usar networks segregadas (ex: `backend`, `database`) se necessário, mas Coolify geralmente lida com uma net default.
   - **Healthchecks**: OBRIGATÓRIOS. O Coolify usa para saber se o deploy rolou.
     ```yaml
     healthcheck:
       test: ["CMD", "curl", "-f", "http://localhost:port/health"]
       interval: 30s
       timeout: 10s
       retries: 3
     ```

2. **Volumes**
   - Usar volumes nomeados para persistência (Postgres, Redis, Qdrant).
   - Mapear volumes de host APENAS se estritamente necessário (ex: backups).
   - Em produção (Coolify), garantir permissões de escrita.

3. **Environment**
   - Não hardcoded. Usar `${VAR_NAME}` no compose.
   - Services devem falhar fast se variáveis críticas faltarem.

4. **Build**
   - Dockerfiles multi-stage para imagens menores.
   - Evitar buildar no target se puder usar imagem pré-buildada (poupando CPU do server), mas para este repo usaremos `build: .` context.
