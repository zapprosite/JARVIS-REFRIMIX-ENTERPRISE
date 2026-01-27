# Arquitetura JARVIS REFRIMIX

## Diagrama de Serviços
```
┌─────────────┐
│ WhatsApp    │
│ Cloud API   │
└──────┬──────┘
       │
┌──────▼──────────────┐
│  api-gateway        │ (Node.js, rate limit)
│  :3000              │
└──────┬──────────────┘
       │
┌──────▼──────────────┐
│ whatsapp-adapter    │ (Baileys, Redis session)
│ :3001               │
└──────┬──────────────┘
       │
┌──────▼────────────────────┐
│ orchestrator-langgraph    │ (Python, LangGraph MCP)
│ :8000                     │
│ ├─ Router de decisão      │
│ ├─ Tools: RAG, Browser    │
│ └─ Persistência: Postgres │
└──────┬────────────────────┘
       │
   ┌───┴────┬──────────┬─────────┐
   │        │          │         │
┌──▼───┐ ┌─▼──────┐ ┌─▼──────┐ ┌▼──────┐
│ RAG  │ │Browser │ │LiteLLM │ │Postgres│
│HVAC  │ │Tools   │ │:4000   │ │:5432   │
│:8000 │ │:3000   │ │        │ │        │
│      │ │        │ │Ollama  │ │pgvector│
│Qdrant│ │Puppeter│ │4090+   │ │tenants │
└──────┘ └────────┘ │3060    │ │billing │
                    └────────┘ └────────┘
```

## Boundaries de Serviços

### api-gateway (External)
- **Responsabilidade**: Entry point HTTP, CORS, rate limit global
- **Não faz**: Lógica de negócio
- **Depende**: whatsapp-adapter

### whatsapp-adapter (Adapter)
- **Responsabilidade**: Protocol conversion (WhatsApp ↔ Internal API)
- **Não faz**: IA, decisões
- **Depende**: orchestrator-langgraph, Redis

### orchestrator-langgraph (Core)
- **Responsabilidade**: Router de decisão, invoke tools, persistência
- **Não faz**: RAG direto (delega para rag-hvac)
- **Depende**: rag-hvac, browser-tools, litellm, postgres, redis

### rag-hvac (Domain)
- **Responsabilidade**: Ingest manuais, query semântico, citations
- **Não faz**: LLM generation (só retrieval)
- **Depende**: Qdrant

### browser-tools (Tools)
- **Responsabilidade**: Automação navegador (Comet, Antigravity, Kabum)
- **Não faz**: AI
- **Depende**: Puppeteer

## Data Stores

| Store    | Uso                         | Backup            |
| -------- | --------------------------- | ----------------- |
| Qdrant   | Embeddings HVAC             | Snapshot diário   |
| Postgres | Tenants, billing, threads   | pg_dump 4x/dia    |
| Redis    | Rate limit, cache, sessions | RDB 1x/dia        |
| MongoDB  | (Opcional) Raw docs         | mongodump semanal |

## Networks

- **external**: api-gateway, whatsapp-adapter (exposto)
- **internal**: orchestrator, rag, dbs (isolado)

Ver [docker-compose.prod.yml](../ops/compose/docker-compose.prod.yml)
