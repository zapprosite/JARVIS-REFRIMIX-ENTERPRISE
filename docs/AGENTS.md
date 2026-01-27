# Governança de Agentes LLM

## Princípios

1. **ZERO ALUCINAÇÃO**: Respostas técnicas devem citar fontes
2. **DELEGAÇÃO**: AI codifica, humano revisa
3. **BOUNDARIES**: AI não toma decisões de arquitetura
4. **TESTES**: Todo código AI-gerado precisa de test

## Agents no Projeto

### 1. RAG HVAC Agent (Produção)
- **Modelo**: Ollama Deepseek Coder v2 (local)
- **Role**: Responder dúvidas técnicas HVAC
- **Constraints**:
  - SEMPRE citar fonte (manual + página)
  - Se não houver match: "Não encontrado" (nunca inventar)
  - Confidence score < 0.7 → avisar usuário
- **Monitoramento**: Grafana dashboard "RAG Accuracy"

### 2. Coding Assistants (Dev)
- **Antigravity (Gemini 3)**: Arquitetura, refactoring
- **Cursor/Copilot**: Code completion
- **Constraints**:
  - Seguir .agent/rules/*
  - Logs sempre JSON
  - Secrets via env
  - Testes obrigatórios

### 3. Browser Automation (Tools)
- **Puppeteer scripts**: Scraping preços, Comet research
- **Constraints**:
  - Rodar em container isolado
  - Timeout 30s max
  - Sanitizar output (XSS)

## Anti-Alucinação Rules

### Para RAG Agent (Produção)
```python
# services/orchestrator-langgraph/src/rag_guard.py
def validate_rag_response(response, citations):
    if not citations or len(citations) == 0:
        return "Desculpe, não encontrei essa informação nos manuais."
    
    if response.confidence < 0.7:
        return f"⚠️ Encontrei algo similar (confiança {response.confidence:.0%}), mas não tenho certeza: {response.answer}"
    
    return response.answer + "\n\n📚 Fontes: " + format_citations(citations)
```

### Para Coding AI (Desenvolvimento)
Ver [.agent/rules/90-anti-hallucination.md](../.agent/rules/90-anti-hallucination.md)
