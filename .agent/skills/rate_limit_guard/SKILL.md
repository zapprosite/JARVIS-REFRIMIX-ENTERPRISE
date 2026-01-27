---
name: rate_limit_guard
description: "Implementa lógica de Token Bucket com Redis"
---

# Rate Limit Guard Skill

Crie Middleware/Decorator que:

1. **Check**:
   - Key: `rate_limit:{tenant_id}`.
   - Se chave não existe, set `MAX_TOKENS` com expire 24h.
   - Decrement `DECR`.
2. **Decision**:
   - Se valor < 0: Raise `429 Too Many Requests`.
3. **Reset**:
   - Script diário ou TTL do Redis para resetar quotas.
