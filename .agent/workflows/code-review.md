# Workflow: Code Review

## Trigger
Desenvolvedor solicita: "Revise este código/PR"

## Steps

1. **Ler contexto**
   - Ler ADRs relevantes (docs/adr/*)
   - Ler rules (.agent/rules/*)
   - Ler ARCHITECTURE.md

2. **Checklist Governança** (docs/GOVERNANCE.md)
   - [ ] ADR criado se mudança arquitetural?
   - [ ] Testes adicionados?
   - [ ] Docs atualizadas?
   - [ ] Secrets via env?
   - [ ] Logs JSON?

3. **Checklist Segurança**
   - [ ] Input validation?
   - [ ] Rate limit considerado?
   - [ ] Sem hardcoded secrets?
   - [ ] Network isolation OK?

4. **Checklist Anti-Alucinação**
   - [ ] APIs existem nas docs oficiais?
   - [ ] Citações de fonte presentes?
   - [ ] Error handling explícito?

5. **Output**
   ```
   ✅ APROVADO com sugestões
   ou
   ⚠️ MUDANÇAS NECESSÁRIAS

   Feedback:
   - [Item 1]
   - [Item 2]

   Próximos passos:
   - [Ação 1]
   ```
