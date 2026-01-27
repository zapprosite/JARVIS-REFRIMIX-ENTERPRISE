---
name: hvac_rag_answerer
description: "Gera respostas técnicas baseadas em chunks recuperados com citações obrigatórias"
---

# HVAC RAG Answerer Skill

Crie uma função/utilitário que:

1. **Receba**: `query` (str) e `retrieved_chunks` (list[dict]).
2. **Contexto**: Formate os chunks em um prompt:
   ```text
   Use ONLY the following context to answer. If not found, say "I don't know".
   
   Context:
   [1] (File: manual_daikin.pdf, Page: 32) ...text...
   [2] (File: manual_lg.pdf, Page: 10) ...text...
   ```
3. **Prompt System**:
   - Enforce JSON output: `{ answer: string, citations: [{ source, page, excerpt }] }`.
   - Regra: Só inclua citação se usada na resposta.
4. **Output**: Retorne o objeto parseado.
