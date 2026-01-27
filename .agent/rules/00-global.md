---
description: "Regras globais de estilo, arquitetura e qualidade para o JARVIS-REFRIMIX-ENTERPRISE"
---

# Global Rules

1. **Architecture & Style**
   - **Monorepo**: Tudo vive neste repo. `services/` para backends, `ops/` para infra.
   - **Language**: Backend em Python (FastAPI/LangChain) ou Node.js (se necessário).
   - **Style**: Siga PEP8 para Python, ESLint/Prettier padrão para JS/TS.
   - **No Magic**: Sem configurações ocultas. Tudo via env vars (documentadas em `.env.example`).

2. **Logging & Observability**
   - **JSON Logs**: TODOS os serviços devem logar em JSON (stdout/stderr) para ingestão fácil.
   - **Campos Obrigatórios**: `timestamp`, `level`, `service`, `trace_id` (se houver), `message`.
   - **Healthcheck**: Todo serviço deve ter `GET /health` retornando 200 OK `{ "status": "ok" }`.

3. **Testing**
   - **Unit**: Pytest/Jest para lógica de negócio.
   - **Smoke**: Scripts bash simples em `ops/scripts/smoke-test.sh` são obrigatórios antes de commit.
   - **Coverage**: Foco em caminhos críticos (billing, rag accuracy), não 100% cego.

4. **GitOps**
   - Commits pequenos e descritivos.
   - Não commitar segredos (use `.gitignore`).
