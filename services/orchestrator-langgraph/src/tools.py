import httpx
import os
from langchain_core.tools import tool
from typing import List, Dict, Any, Optional

RAG_HVAC_URL = os.getenv("RAG_HVAC_URL", "http://rag-hvac:8000")
BROWSER_TOOLS_URL = os.getenv("BROWSER_TOOLS_URL", "http://browser-tools:3000")

@tool
async def query_hvac_manuals(query: str) -> Dict[str, Any]:
    """
    Consults technical manuals for HVAC equipment (Daikin, LG, Samsung, etc).
    Use this for any technical questions about error codes, installation, or specs.
    
    Args:
        query: The user's technical question.
        
    Returns:
        A dictionary with "answer" and "citations".
    """
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(f"{RAG_HVAC_URL}/query", json={"query": query}, timeout=30.0)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            return {"answer": f"Error querying manuals: {str(e)}", "citations": []}

@tool
async def search_web(query: str) -> str:
    """
    Searches the web for information using a browser agent.
    Use this if the info is likely not in the manuals (e.g. current weather, news, competitor prices).
    """
    async with httpx.AsyncClient() as client:
        try:
            # Assuming browser-tools has a compatible endpoint
            resp = await client.post(f"{BROWSER_TOOLS_URL}/search", json={"query": query}, timeout=60.0)
            return resp.text
        except Exception as e:
            return f"Error searching web: {str(e)}"
