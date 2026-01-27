## Contexto (fonte de verdade)
- Deploy target: Coolify 4.0 + Docker Compose.
- Produto: ZapPRO WhatsApp bot (multi-tenant) com RAG HVAC (Qdrant).
- Requisito de qualidade: toda resposta técnica deve citar fonte (manual + página / figura).
- Sem achismo: se não houver evidência no manual ou inferência suportada por procedimento, responder “não encontrado” + próximos passos.
- Segurança: rate limit por tenant + por número WhatsApp + por user_id.
- Observabilidade: logs estruturados + métricas de latência RAG + erro 429.

## Concluído (DevOps Audit Phase)
- [x] **CI/CD**: Workflows de CI (Security/Tests) e CD (Webhook) criados.
- [x] **Secrets**: Removido hardcode, implementado padrão env var.
- [x] **Rate Limit**: Implementado Redis Token Bucket no Orchestrator.
- [x] **Volumes**: Bind mounts para `/nvme/*` configurados.
- [x] **Validation**: Prompt Injection Protection ativo.
- [x] **Logs**: JSON estruturado implementado.
- [x] **Network**: Segregação External/Internal aplicada.

## Concluído (Bootstrap Phase)
- [x] **Antigravity Setup**: Criada estrutura de pastas, rules, workflows e skills.
- [x] **Service Refinement**: Services básicos funcionais.
- [x] **DevOps Basics**: Docker Compose v1, Scripts básicos.

## Next Steps (Feature Phase)
- Implementar UI Dashboard (Next.js/React).
- Ingerir manuais reais de produção.
- Configurar monitoramento (Prometheus/Grafana) para consumir logs JSON.
