---
description: "Diretrizes de segurança para LLMs e Infraestrutura"
---

# Security Rules

1. **Zero Trust Input**
   - Todo input do usuário (WhatsApp, Web) deve ser sanitizado.
   - Não concatenar strings de usuário diretamente em queries SQL ou comandos Shell.

2. **LLM & Prompt Injection**
   - Usar delimitadores claros (ex: `"""USER INPUT"""`) nos prompts.
   - Validar output do LLM antes de executar ações (especialmente tools).
   - Rate Limit é mandatório para proteger custos (Wallet Exhaustion).

3. **Secrets Management**
   - **NUNCA** commitar `.env` ou chaves de API.
   - Em dev: use `.env.local`.
   - Em prod (Coolify): injetar via UI do Coolify.

4. **Infraestrutura**
   - Containers não devem rodar como `root` se possível.
   - Expor apenas portas estritamente necessárias no `docker-compose.prod.yml`.
