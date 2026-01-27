# ADR 0003: Rate Limiting Multi-Tenant

## Status
Aceito

## Decisão
Implementar Token Bucket algorithm no `api-gateway`.
Chaves: `tenant:{id}` e `user:{phone}`.

## Motivação
Evitar que um único tenant consuma toda a quota de LLM ou sobrecarregue o Qdrant.
