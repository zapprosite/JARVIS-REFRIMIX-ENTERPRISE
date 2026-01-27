# Ingest Manuals Runbook

How to ingest new HVAC manuals into the RAG system.

## Via API

1. **Endpoint**: `POST /ingest` (on `rag-hvac` service).
2. **Method**:
   ```bash
   curl -X POST -F "file=@manual_daikin.pdf" -F "tenant_id=public" http://rag-hvac:8000/ingest
   ```
3. **Response**:
   ```json
   { "status": "success", "chunks_ingested": 150 }
   ```

## Verification

1. Query via Qdrant UI/API or `rag-hvac`:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"query": "error E7 daikin"}' http://rag-hvac:8000/query
   ```
