# Anti-Hallucination Rules (Coding AI)

## Para Gemini / Cursor / Copilot

### 1. SEMPRE citar fonte
❌ "Este é o padrão do LangGraph"
✅ "Segundo docs LangGraph v0.2.5 (link), o padrão é..."

### 2. NUNCA inventar APIs
❌ `litellm.get_models()` (não existe)
✅ Consultar: https://docs.litellm.ai/docs/proxy/configs antes de usar

### 3. Secrets SEMPRE via env
❌ `API_KEY = "sk-abc123"`
✅ `API_KEY = os.getenv("OPENAI_API_KEY")`

### 4. Validar antes de codar
❌ Assumir que biblioteca X tem método Y
✅ "Verifique na doc se X.Y existe antes de usar"

### 5. Testes obrigatórios
❌ Gerar código sem test
✅ Gerar código + test de integração mínimo

### 6. Logs estruturados
❌ `print("erro")`
✅ `logger.error({"event": "error", "details": ...})`

### 7. Error handling explícito
❌ `response = api.call()`
✅ 
```python
try:
    response = api.call()
except TimeoutError:
    logger.error(...)
    raise HTTPException(504, "Timeout")
```

### 8. Não modificar arquivos sem contexto
❌ Alterar docker-compose.prod.yml sem ler atual
✅ Ler arquivo atual + aplicar diff mínimo

### 9. Citar ADRs relevantes
Se mudança arquitetural:
✅ "Esta mudança segue ADR 0003 (multi-tenant rate limit)"

### 10. Confidence score
Se incerto:
✅ "⚠️ Não tenho certeza, sugiro verificar docs oficiais"
