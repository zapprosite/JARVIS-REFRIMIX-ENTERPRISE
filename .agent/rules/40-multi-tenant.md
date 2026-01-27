---
description: "Regras para Multi-Tenancy e Rate Limiting"
---

# Multi-Tenant & Rate Limit

1. **Tenant Isolation**
   - Todo dado sensível (conversas, usage) deve ter `tenant_id`.
   - Qdrant: Usar `payload` filters (`filter: { must: [ { key: "tenant_id", match: { value: "..." } } ] }`) se os docs forem privados.
   - Manuais técnicos genéricos (Daikin, LG) podem ser públicos (`tenant_id: "public"`).

2. **Rate Limiting (Redis)**
   - **Token Bucket** ou **Fixed Window** por `tenant_id` ou `user_phonenumber`.
   - Tiers:
     - **Basic**: 50 msgs/dia.
     - **Pro**: 500 msgs/dia.
     - **Agency**: Ilimitado (ou soft limit alto).
   - Quando exceder: Retornar 429 Too Many Requests e mensagem amigável no WhatsApp.

3. **Quota Management**
   - Orchestrator deve checar quota no Redis ANTES de chamar LLM caro (GPT-4/Claude).
   - Se falhar, nem invoca o modelo, economizando $$$.
