# JARVIS REFRIMIX ENTERPRISE ❄️

> **Enterprise Neural Backbone for HVAC Technical Support**
> _Not just a chatbot. A Distributed Cognitive System._

---

## 🦅 Executive Summary

This repository hosts a production-grade **Vertical AI Platform** designed for the HVAC-R (Heating, Ventilation, Air Conditioning, and Refrigeration) industry. Unlike standard "LLM Wrappers", this system implements a **Cognitive Architecture** using LangGraph to perform reasoning, tool use, and self-correction before responding.

It is architected to be **Vendor-Agnostic**, **Credentialless-Resilient**, and **Observability-First**.

### 🏗️ Why this is "Senior-Grade" Engineering
1.  **Event-Driven Microservices**: Decoupled Adapters (WhatsApp/Web) from the Cognitive Core (Orchestrator).
2.  **LangGraph Cognitive Loops**: Implements "ReAct" patterns with **Self-Correction**. If the AI hallucinates or fails a validation check, it retries automatically.
3.  **Defensive Architecture**:
    *   **RAG Citations Validator**: Blocks answers that cannot be traced back to ingested technical manuals.
    *   **Guardrails Sidecar**: API Gateway middleware that acts as a WAF against Prompt Injection and Payload abuse.
    *   **Credentialless Mode**: Capable of booting and passing contract tests even without external API Keys (Mock-First Development).
4.  **Semantic Caching**: Utilizes Redis Stack for vector-based caching, reducing costs and latency for recurring technical queries.

---

## 🛠️ Tech Stack & Architecture

| Component            | Technology                       | Responsibility                                                  |
| -------------------- | -------------------------------- | --------------------------------------------------------------- |
| **Orchestrator**     | **Python (FastAPI + LangGraph)** | The "Brain". Manages state, routing, and tool execution.        |
| **Cognitive Engine** | **LangChain + OpenAI/LiteLLM**   | Reasoning and generation (Model Agnostic via LiteLLM).          |
| **RAG Store**        | **Qdrant**                       | Vector database for Technical Manuals (Daikin, LG, Mitsubishi). |
| **Persistence**      | **PostgreSQL (Async)**           | Long-term memory of conversation states and checkpoints.        |
| **Cache & Queue**    | **Redis Stack**                  | Rate Limiting, Semantic Cache, and Pub/Sub.                     |
| **Observability**    | **OpenTelemetry (OTel)**         | Distributed tracing of agent thought processes.                 |
| **Edge Security**    | **Node.js Gateway**              | Guardrails, WAF, and Protocol Translation.                      |

---

## ⚡ Quick Start (Developer Mode)

### Prerequisites
- Docker & Docker Compose
- (Optional) OpenAI API Key (or run in Mock Mode)

### 1. Bootstrap
```bash
git clone https://github.com/zapprosite/JARVIS-REFRIMIX-ENTERPRISE
cd JARVIS-REFRIMIX-ENTERPRISE
# Sets up .env, permissions, and initial data
./ops/scripts/bootstrap.sh
```

### 2. Run (Mock Mode - No Keys Needed)
```bash
# Validates the architecture without spending 1 cent
./scripts/start_mock_server.sh
```

### 3. Run (Production)
```bash
docker-compose up --build -d
```

---

## 🧩 Modularity & Governance

This project follows **Google Antigravity** principles for AI-Assisted Development via strictly typed context rules.

*   `/services`: Isolated microservices.
*   `/ops`: Infrastructure as Code (Docker, Nginx, Grafana).
*   `/.agent`: AI Governance Rules (The "Constitution" of the project).
    *   `GEMINI.md`: Global instructions.
    *   `AGENTS.md`: Agent specific roles.

---

## 🔮 Roadmap & 2026 Vision

See [TASKMASTER.md](TASKMASTER.md) for the active sprint board.

**Current Innovation Focus:**
*   **Proactive Agents**: Shifting from "Reactive Chat" to "Proactive Support" (Cron-based health checks).
*   **Self-Healing**: Automated error reflection and retry loops.
*   **Local-First AI**: Capable of running entirely on premise (LocalLLM + LocalVectorDB).

---

## 📞 Support & Documentation
*   **Architecture**: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
*   **Deployment**: [docs/runbooks/deploy-coolify.md](docs/runbooks/deploy-coolify.md)
*   **API Contracts**: [docs/api](docs/api)
