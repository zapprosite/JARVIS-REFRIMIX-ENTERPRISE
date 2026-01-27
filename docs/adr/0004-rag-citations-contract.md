# ADR 0004: Contrato de Citações RAG

## Status
Aceito

## Contexto
O sistema fornece suporte técnico crítico para HVAC. Informações incorretas (alucinações) podem causar danos a equipamentos ou risco à segurança.
Precisamos garantir que o modelo não invente procedimentos.

## Decisão
1. **Regra "Sem Citação, Sem Resposta"**:
   - Toda resposta de cunho técnico gerada pelo RAG deve incluir explicitamente a fonte.
   - Formato obrigatório: `[Manual X, pág Y]` ou similar.
   - O prompt do sistema (System Prompt) deve instruir o modelo a responder "Não encontrei essa informação nos manuais disponíveis" caso a busca vetorial não retorne evidências suficientes com score alto.

2. **Estrutura de Retorno do RAG**:
   - O serviço `rag-hvac` retornará não apenas o texto, mas o objeto de citação completo (`doc_id`, `page_number`, `figure_id` se houver).
   - O Orquestrador deve validar se a resposta gerada usou esses contextos.

## Consequências
- **Positivo**: Aumenta drasticamente a confiabilidade e confiança do usuário profissional.
- **Negativo**: O bot pode parecer "menos inteligente" em perguntas gerais fora do manual (trade-off aceitável).
- **Negativo**: Requer pipeline de ingestão robusto que preserve números de página e estrutura de documentos.
