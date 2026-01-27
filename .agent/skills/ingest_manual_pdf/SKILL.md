---
name: ingest_manual_pdf
description: "Pipeline para ingerir PDF de manual técnico"
---

# Ingest Manual PDF Skill

Crie script/função que:

1. **Parse**: Use `pypdf` ou `unstructured` para extrair texto + metadados (page_number).
2. **Chunking**: RecursiveCharacterTextSplitter (chunk_size=1000, overlap=200).
3. **Embedding**: Gere embeddings (OpenAI ou local).
4. **Upsert Qdrant**:
   - Collection: `manuals`
   - Payload: `{ "filename": "...", "page_number": int, "text": "...", "tenant_id": "public" }`
   - UUID: Gere determinístico (hash do texto) para evitar duplicatas.
