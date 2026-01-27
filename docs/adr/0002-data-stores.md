# ADR 0002: Estratégia de Dados

## Status
Aceito

## Decisão
- **Vetores (RAG)**: Qdrant. Motivo: Performance, Facilidade de uso com Docker, Filtragem robusta de metadados.
- **Cache/Rate Limit**: Redis.
- **Histórico/Sessão**: Postgres (ou SQLite no início, mas Postgres para prod).
- **Transient Files**: Volume Docker local para uploads temporários antes da ingestão.

## Consequências
Stack padrão, fácil de manter e escalar.
