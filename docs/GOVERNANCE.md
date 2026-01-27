# Governança do Projeto

## Decisões de Arquitetura (ADRs)
- Toda mudança estrutural requer ADR em `/docs/adr/`
- Template: [adr-template.md](adr/adr-template.md)
- Aprovação: 1 dev sênior + 1 DevOps

## Aprovações

| Mudança              | Aprovação                 |
| -------------------- | ------------------------- |
| Novo service         | ADR + tech lead           |
| Mudança DB schema    | ADR + DBA review          |
| Segredos/credentials | Security + DevOps         |
| Deploy production    | 2 aprovações + smoke test |
| Dependency upgrade   | Trivy scan pass           |

## Branches

- **main**: production (protected)
- **staging**: pre-prod (auto-deploy)
- **feature/***: desenvolvimento

## CI/CD

- PR → CI obrigatório (lint, security, tests)
- Merge → auto-deploy staging
- Tag v* → manual deploy production

## Rollback

- Auto-rollback se healthcheck fail
- Manual: `git revert` + redeploy

## Code Review Checklist

✅ ADR criado (se arquitetura)
✅ Testes adicionados
✅ Docs atualizadas
✅ Secrets não commitados
✅ Logs JSON
✅ Healthcheck funcional
✅ Rate limit considerado
