## Contexto (fonte de verdade)
- Deploy target: Coolify 4.0 + Docker Compose.
- Produto: ZapPRO WhatsApp bot (multi-tenant) com RAG HVAC (Qdrant).
- Requisito de qualidade: toda resposta técnica deve citar fonte (manual + página / figura).
- Sem achismo: se não houver evidência no manual ou inferência suportada por procedimento, responder “não encontrado” + próximos passos.
- Segurança: rate limit por tenant + por número WhatsApp + por user_id.
- Observabilidade: logs estruturados + métricas de latência RAG + erro 429.

## Backlog
(Tarefas anteriores preservadas aqui)

## Concluído (Bootstrap Phase)
- [x] **Antigravity Setup**: Criada estrutura de pastas, rules, workflows e skills.
- [x] **Service Refinement**:
  - API Gateway: Logging JSON, proxy `/v1/messages`.
  - WhatsApp Adapter: Stub com Rate Limit (Redis).
  - Orchestrator: LangGraph com tools RAG e Browser.
  - RAG HVAC: Ingest pipeline PDF -> Qdrant.
  - Browser Tools: Puppeteer service.
  - LiteLLM: Config com Redis.
- [x] **DevOps**:
  - `docker-compose.prod.yml` completo com healthchecks e volumes.
  - Scripts: bootstrap, backup, healthcheck, smoke-test.
  - Runbooks: Deploy Coolify, Ingest Manuals, Incident Rate Limit.
- [x] **Quality**: Tests integration flow.

## Próximos Passos
- Implementar UI Dashboard (Next.js/React).
- Configurar CI/CD no GitHub Actions/Coolify Webhooks real.
- Ingerir manuais reais de produção.
