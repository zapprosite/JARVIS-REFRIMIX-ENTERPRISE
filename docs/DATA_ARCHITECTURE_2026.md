# 🧠 The Unified Data Fabric (2026 Architecture)

> **Philosophy**: "Polyglot Persistence for Cognitive Systems".
> Instead of forcing all data into one DB, we assign each "Cognitive Function" to its ideal substrate.

---

## 🏗️ The 4 Pillars of Agent Memory

| Memory Type  |       Cognitive Role        |   Technology    | Why? (2026 Standard)                                                                                                       |
| :----------: | :-------------------------: | :-------------: | :------------------------------------------------------------------------------------------------------------------------- |
| **Episodic** | **Stream of Consciousness** |   **MongoDB**   | Logs complex nested "Thought Traces" (LangGraph steps) without strict schema. Fast ingestion of massive logs.              |
| **Semantic** |   **Long-Term Knowledge**   |   **Qdrant**    | Dedicated Vector Engine. Handles Hybrid Search (Keyword + Vector) and aggressive Quantization for billion-scale retrieval. |
| **Identity** | **Core Truth & Relations**  | **PostgreSQL**  | ACID Compliance. Users, Tenants, Billing, Permissions. The "Adult" in the room ensuring data integrity.                    |
| **Working**  | **Hot Context & Reflexes**  | **Redis Stack** | Semantic Cache, Rate Limiting, Pub/Sub for Real-time Agent coordination. Sub-millisecond latency.                          |

---

## 🔄 Data Flow: "The Memory Consolidation Loop"

1.  **Awake (Working Memory)**:
    *   User queries hit **Redis Semantic Cache** first.
    *   If miss, Agent starts thinking.
    
2.  **Recall (Semantic Memory)**:
    *   Agent queries **Qdrant** for Manuals (Docs) AND Past User Preferences (Profile).
    *   *Innovation*: "Active Retrieval" -> Qdrant filters by Tenant ID (Metadata).

3.  **Reasoning (Episodic Memory)**:
    *   Every step (Tool Call, LLM Token, Error) is streamed to **MongoDB**.
    *   This creates a perfect "Black Box" recording for debugging and fine-tuning later.

4.  **Commit (Identity Memory)**:
    *   Final result (ex: "Ticket Created #123") is written to **PostgreSQL**.
    *   This triggers a webhook to WhatsApp via **Redis Pub/Sub**.

---

## 🛠️ Implementation Strategy

### Phase 1: The "Black Box" (MongoDB Tracing)
*   Deploy MongoDB Container.
*   Create a `LangGraphTracer` that pushes every step to Mongo.
*   **Goal**: Full observability of "Why did the agent say that?".

### Phase 2: Hybrid Search (Qdrant Upgrade)
*   Enable `Sparse Vectors` (BM25) in Qdrant alongside Dense Vectors.
*   **Goal**: Better accuracy for specific part numbers (e.g., "Error code E7-44"). Standard vectors perform poorly on strict alphanumeric codes; Hybrid fixes this.

### Phase 3: Semantic Cache (Redis Stack)
*   (Already Implemented in Sprint 2).
*   **Next Level**: Add "User-Specific Cache" (Cache partitions per Tenant).

---

## 🏆 Reference Examples (Open Source)
*   **LangChain Templates**: Uses Mongo for Chat History + Postgres for Vectors (pgvector). We upgrade this by using Qdrant for better scale.
*   **Microsoft Semantic Kernel**: Heavy use of Qdrant + Redis.
*   **AutoGPT**: Uses JSON/File based memory, evolving to Mongo/Qdrant.

---

## 📝 Governance
*   **PII Rules**: No User PII in Qdrant (Vectors must be anonymized). PII lives in Postgres only.
*   **Retention**: MongoDB Logs TTL = 90 Days. Important interactions summarized to Postgres.
