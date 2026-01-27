---
description: "Contrato obrigatório de citações para respostas do RAG"
---

# RAG & Citations Logic

1. **The Contract**
   - Toda resposta técnica baseada em manual DEVE vir acompanhada de citações.
   - Se o RAG não encontrar a resposta nos chunks recuperados:
     - **Resposta**: "Desculpe, não encontrei essa informação específica nos manuais disponíveis."
     - ** NÃO ALUCINAR **.

2. **Schema de Resposta**
   ```json
   {
     "answer": "O código de erro E7 na Daikin geralmente indica falha no motor do ventilador...",
     "citations": [
       {
         "source": "Manual_Daikin_Split_Inverter.pdf",
         "page": 32,
         "excerpt": "E7: Travamento do motor do ventilador..."
       }
     ]
   }
   ```
   
3. **Fallback**
   - Se o confidence score for baixo, avise o usuário: "Encontrei algo parecido, mas não tenho certeza: ..."

4. **Ingestão**
   - Metadata `page_number` e `filename` são obrigatórios no Qdrant para permitir a citação precisa.
