# 🔮 Proposta de Inovação: A Mudança "Moltbot" (Era 2026)

Baseado na análise de Agentes Proativos de Estado da Arte (ex: Moltbot, Claude Code), aqui está a proposta para atualizar o JARVIS-REFRIMIX-ENTERPRISE de um **Chatbot Reativo** para um **Funcionário de IA Proativo**.

## 1. Heartbeat Proativo (O "Pulso")
**Conceito**: Bots tradicionais dormem até serem chamados. Agentes "Moltbot" têm um batimento cardíaco.
**Implementação**:
- Criar um `Serviço Agendador` (Python/Celery ou cron simples).
- **Gatilho**: A cada 1h.
- **Ação**: Invocar o `Orchestrator` com um evento especial de sistema (não input de usuário).
- **Objetivo**: "Verificar integridade do sistema", "Checar status de chamados ativos", "Enviar follow-up proativo ao usuário se ele parou de responder durante um diagnóstico".

## 2. Memória Episódica e Perfilamento
**Conceito**: LLMs têm janelas de contexto limitadas. Precisamos de "Memória Condensada de Longo Prazo".
**Implementação**:
- **Job Noturno**: `Consolidador de Memória`.
- **Processo**: Lê todos os chats do dia -> Resume -> Atualiza tabela `user_profile` (JSONB) no Postgres.
- **Uso**: Quando o Usuário X falar semana que vem, injetar o `user_profile` no Prompt de Sistema ("Usuário X tem um sistema VRV Daikin e prefere linguagem técnica").
- **Diferencial**: O bot não pergunta a mesma coisa duas vezes.

## 3. Ferramentas de Ação Local (Mãos Reais)
**Conceito**: Dar "mãos" para a IA.
**Implementação**:
- Tool segura `run_diagnostic` exposta ao Agente.
- Comandos permitidos: `tail logs`, `check disk usage`, `restart service`.
- **Segurança**: Disparável apenas por Usuários Admin (verificados via Metadados do WhatsApp).

## 4. UI Generativa (para Dashboards)
**Conceito**: Em vez de dashboards estáticos, a IA *gera* a visualização.
**Implementação**:
- Usando estilo `v0` ou React Server Components.
- O `Orchestrator` retorna não apenas texto, mas uma definição JSON de um Componente UI (ex: "Mostrar Gráfico de Manômetro para Pressão").
- O Frontend renderiza este componente dinâmico.

## 🚧 Próximos Passos
Para implementar essa visão, recomendamos começar com o **#1 Heartbeat Proativo**.
Adicionar ao Roadmap?
