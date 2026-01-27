---
description: "Processo para adicionar uma nova tool MCP"
---

# Add MCP Tool Workflow

1. **Definition**
   - Edite `data-contracts/mcp/tools.json`.
   - Adicione a definição JSON Schema da tool (name, description, inputSchema).

2. **Implementation**
   - No serviço alvo (ex: `orchestrator-langgraph` ou `api-gateway`), implemente a função correspondente.
   - Garanta que ela receba os argumentos tipados corretamente.

3. **Mapping**
   - Atualize o mapa de tools no orchestrator para vincular `tool_name` -> `function_implementation`.

4. **Test**
   - Use o script de teste do orchestrator para forçar a chamada da tool via prompt.
