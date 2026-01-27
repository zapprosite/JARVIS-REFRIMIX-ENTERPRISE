# Gemini 3 Antigravity - Regras Específicas

Este projeto usa **Google Antigravity IDE** (Gemini 3) para AI-assisted development.

## Configuração

### Workspace Rules
Localização: `.agent/rules/*`

Ordem de aplicação:
1. `00-global.md` (estilo, logs)
2. `10-security.md` (secrets, validation)
3. `20-docker-coolify.md` (compose, volumes)
4. `30-rag-citations.md` (RAG contract)
5. `40-multi-tenant.md` (isolation, quotas)
6. `90-anti-hallucination.md` (AI safety)

### Workflows
Localização: `.agent/workflows/*`

Disponíveis:
- `add-service.md`: Scaffold novo service
- `add-mcp-tool.md`: Registrar tool no LangGraph
- `ci-cd-update.md`: Atualizar pipeline

### Skills
Localização: `.agent/skills/*`

Custom skills:
- `hvac_rag_answerer`: Formata resposta + citations
- `rate_limit_guard`: Valida quota antes de processar
- `service_scaffold`: Gera Dockerfile + healthcheck

## Comandos Úteis

### Criar novo service
```
@workflow add-service --name=sms-adapter
```

### Refatorar com context
```
Refatore services/orchestrator-langgraph/src/main.py seguindo .agent/rules/00-global.md
```

### Code review
```
Revise este PR: [link] aplicando todas as rules e checklist de docs/GOVERNANCE.md
```

## Limitações

❌ **Não usar Gemini para**:
- Decisões de arquitetura (humano decide, AI sugere)
- Secrets/credentials (nunca expor)
- Deploy production (humano aprova)

✅ **Usar Gemini para**:
- Scaffold de código
- Refactoring
- Testes
- Documentação
- Bug fixes
