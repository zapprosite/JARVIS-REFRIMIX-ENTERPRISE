# Skill: HVAC RAG Answerer

## Propósito
Formatar respostas técnicas HVAC com citations obrigatórias

## Input
```json
{
  "query": "Daikin E7 error",
  "rag_results": [
    {"content": "E7: motor fan failure", "source": "daikin_manual.pdf", "page": 47}
  ]
}
```

## Output
```json
{
  "answer": "O código E7 na Daikin indica falha no motor do ventilador. Verifique: 1) Travamento mecânico, 2) Capacitor, 3) Conector.",
  "citations": [
    {"source": "daikin_manual.pdf", "page": 47, "excerpt": "E7: motor fan failure"}
  ],
  "confidence": 0.95
}
```

## Rules
- Se confidence < 0.7: prefixar "⚠️ Não tenho certeza..."
- Se citations vazio: retornar "Não encontrado nos manuais"
- NUNCA inventar valores técnicos (tensão, corrente, ohms)
