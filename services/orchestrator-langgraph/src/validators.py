from typing import Dict, Any, List

def validate_rag_response(response: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validates that the RAG response contains necessary citation fields.
    If citations are missing but answer suggests success, flags it.
    
    Args:
        response: Dictionary with 'answer' and 'citations'.
        
    Returns:
        The validated response, potentially with warnings appended.
    """
    if not isinstance(response, dict):
         return {"answer": "Error: Invalid response format from RAG service.", "citations": []}
         
    citations = response.get("citations", [])
    answer = response.get("answer", "")
    
    # If the answer implies we found something "According to...", we MUST have citations.
    # This is a basic heuristic.
    
    if answer and not citations:
        # If the answer is "I couldn't find...", then no citations is fine.
        negative_phrases = ["not found", "no information", "couldn't find", "cannot find", "could not find", "did not find"]
        if not any(phrase in answer.lower() for phrase in negative_phrases):
             # We found an answer but no citations? suspicious.
             response["warning"] = "Low Confidence: Source citations missing."
             # Ideally we might strip the answer or ask to retry, but for now we flag it.
    
    # Validate citation structure
    valid_citations = []
    for cit in citations:
        if isinstance(cit, dict) and cit.get("source"):
            valid_citations.append(cit)
            
    response["citations"] = valid_citations
    return response
