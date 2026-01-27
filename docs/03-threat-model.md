# Threat Model

## Visão Geral
Análise de ameaças focada na interação via WhatsApp e processamento de documentos externos.

## Superfície de Ataque
1. **Entrada de Texto (WhatsApp)**: Prompt Injection, Jailbreak.
2. **Upload de Arquivos (Ingestão)**: Malicious PDF, XSS via metadados.
3. **Browser Tools**: SSRF, vazamento de dados de sessão, acesso a sites maliciosos por instrução do usuário.
4. **API Gateway**: DDoS, Brute Force em tenants, Bypass de Rate Limit.

## Ameaças e Mitigações

### 1. Prompt Injection / Jailbreak
- **Risco**: Usuário tenta fazer o bot ignorar instruções ou revelar system prompt.
- **Mitigação**:
  - `safety.md` prompt com instruções rígidas de não-desvio.
  - Validação pós-processamento (Output Guardrails) para verificar se a resposta obedece ao formato e tom.

### 2. Execução de Código Remoto (Browser Tools)
- **Risco**: Agente acessa site malicioso que explora vulnerabilidade no engine do browser.
- **Mitigação**:
  - `browser-tools` roda em container isolado, sem privilégios (rootless), com rede restrita (allowlist de domínios se possível, ou egress filter).
  - Sandboxing estrito do Puppeteer/Playwright.

### 3. Exaustão de Recursos (DDoS / Rate Limit)
- **Risco**: Um tenant ou usuário inunda o sistema, elevando custos de LLM e travando o banco vetorial.
- **Mitigação**:
  - Implementação de Token Bucket Rate Limit no `api-gateway`.
  - Limites rígidos por Tenant e por User ID.
  - Cache de respostas frequentes.

### 4. Envenenamento de RAG
- **Risco**: Documentos ingeridos contendo informações falsas ou maliciosas.
- **Mitigação**:
  - Ingestão restrita a administradores autenticados.
  - Validação humana por amostragem.
