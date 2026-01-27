from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.ingest import process_pdf, client, model, COLLECTION_NAME, init_collection
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("rag-hvac")

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    tenant_id: Optional[str] = "public"
    top_k: int = 3

@app.on_event("startup")
def startup():
    try:
        init_collection()
    except Exception as e:
        logger.error(f"Failed to init Qdrant: {e}")

@app.get("/health")
def health():
    return {"status": "ok", "service": "rag-hvac"}

@app.post("/ingest")
async def ingest(file: UploadFile = File(...), tenant_id: str = "public"):
    try:
        content = await file.read()
        num_chunks = process_pdf(content, file.filename, tenant_id)
        return {"status": "success", "chunks_ingested": num_chunks, "filename": file.filename}
    except Exception as e:
        logger.error(f"Ingest error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
async def query(req: QueryRequest):
    try:
        vector = model.encode(req.query).tolist()
        
        # Filter by tenant_id?
        # For now, simplistic search
        hits = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=vector,
            limit=req.top_k
        )
        
        results = []
        for hit in hits:
            results.append({
                "answer": hit.payload["text"], # Orchestrator uses this field as context
                "citations": [{
                    "source": hit.payload["filename"],
                    "page": hit.payload["page"],
                    "score": hit.score,
                    "excerpt": hit.payload["text"][:200]
                }]
            })
            
        # The Orchestrator expects a slightly different format from standard tool calling
        # But our tool wrapper `query_hvac_manuals` just returns the json.
        # We need to return a combined structure for the LLM to consume.
        
        return {
            "answer": "Use the context below.", # Placeholder
            "citations": results # The LLM will use this list to form the final answer
        }
        
    except Exception as e:
        logger.error(f"Query error: {e}")
        return {"answer": "Error querying database.", "citations": []}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
