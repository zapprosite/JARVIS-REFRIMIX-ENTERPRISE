from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import logging
import os
from src.graph import app as graph_app

# Logging Setup
logging.basicConfig(level=logging.INFO, format='%(message)s') # JSON logger logic handled by standard logging for now, upgrade to python-json-logger later
logger = logging.getLogger("orchestrator")

app = FastAPI()

class ChatRequest(BaseModel):
    messages: List[Dict[str, str]] # [{"role": "user", "content": "..."}]
    tenant_id: str = "default"
    user_id: str = "default"
    thread_id: Optional[str] = None

@app.get("/health")
async def health():
    return {"status": "ok", "service": "orchestrator-langgraph"}

@app.post("/v1/chat")
async def chat(req: ChatRequest):
    logger.info(f"Received chat for tenant {req.tenant_id} user {req.user_id}")
    
    # Convert messages
    # Simple conversion, production needs better handling of roles
    # But graph expects BaseMessages.
    # The graph invocation handles conversion if we pass dicts usually, but let's see.
    
    config = {"configurable": {"thread_id": req.thread_id or f"{req.tenant_id}:{req.user_id}"}}
    
    # Transform input messages to LangChain format if this is a new run
    # For LangGraph with persistence, we might just pass the NEW user message
    # Assuming the client (adapter) sends the LAST message or the full history?
    # Usually adapter sends just the new message.
    
    # Let's assume req.messages contains ONLY new messages to append
    inputs = {
        "messages": req.messages, # LangGraph handles dicts like {"role": "user", "content": "..."}
        "tenant_id": req.tenant_id,
        "user_id": req.user_id
    }
    
    try:
        # Stream or invoke? Invoke for now.
        final_state = await graph_app.ainvoke(inputs, config=config)
        
        # Extract last AI message
        last_msg = final_state["messages"][-1]
        content = last_msg.content
        
        return {
            "response": content,
            "thread_id": config["configurable"]["thread_id"]
        }
    except Exception as e:
        logger.error(f"Error in graph execution: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
