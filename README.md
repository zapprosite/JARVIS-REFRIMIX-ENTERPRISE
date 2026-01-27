# JARVIS REFRIMIX ENTERPRISE

WhatsApp SaaS multi-tenant com RAG técnico HVAC-R (ar-condicionado inverter Brasil).

## 🎯 Quick Start (5min)
```bash
git clone https://github.com/zapprosite/JARVIS-REFRIMIX-ENTERPRISE
cd JARVIS-REFRIMIX-ENTERPRISE
./ops/scripts/bootstrap.sh
```

## 🏗️ Arquitetura
Ver [ARCHITECTURE.md](docs/ARCHITECTURE.md)

## 📋 Roadmap
Ver [TASKMASTER.md](TASKMASTER.md)

## 🤖 AI-Assisted Development
Este projeto usa Antigravity IDE (Gemini 3). Ver [GEMINI.md](.agent/GEMINI.md) e [AGENTS.md](docs/AGENTS.md).

## 🛡️ Segurança
- Secrets via env (nunca commit)
- Rate limit Redis (multi-tenant)
- Input validation (anti-prompt injection)
- RAG citations obrigatórias (zero alucinação)

## 🚀 Deploy
Coolify 4.0 (Docker Compose). Ver [docs/runbooks/deploy-coolify.md](docs/runbooks/deploy-coolify.md)

## 📞 Suporte
- Issues: GitHub Issues
- Docs: /docs
- ADRs: /docs/adr
