# ADR 0001: Fronteiras de Seriços

## Status
Aceito

## Contexto
Necessidade de desacoplar a lógica de conexão com WhatsApp (que muda frequentemente/instável) da inteligência do bot (estável).

## Decisão
Separar em microserviços:
1. `whatsapp-adapter`: Apenas I/O. Não toma decisões.
2. `orchestrator-langgraph`: Mantém o estado e decisão.
3. `api-gateway`: Controla acesso e quotas.

## Consequências
- Isolamento de falhas do WhatsApp.
- Possibilidade de troca de provider (Baileys -> Meta API) sem tocar no orquestrador.
