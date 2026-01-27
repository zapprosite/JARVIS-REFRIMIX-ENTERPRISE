

def sanitize_prompt(content: str) -> str:
    """
    Sanitizes user input to prevent common prompt injection attacks.
    """
    if not content:
        return ""
        
    # lower case for checking but we return original casing usually? 
    # For blocking, we check lower.
    content_lower = content.lower()
    
    # 1. Block common injection keywords
    # "Ignore previous instructions", "System override", etc.
    # Be careful not to block legitimate queries.
    blocked_phrases = [
        "ignore previous instructions",
        "ignore the above",
        "system:", 
        "assistant:",
        "user:", # preventing role spoofing if we concat strings
        # "you are now" # maybe too aggressive
    ]
    
    for phrase in blocked_phrases:
        if phrase in content_lower:
            # We can raise error or strip. Raising error is safer.
            raise ValueError(f"Potential prompt injection detected: '{phrase}'")
            
    # 2. Length limit to prevent context exhaustion
    MAX_LENGTH = 4000
    if len(content) > MAX_LENGTH:
        content = content[:MAX_LENGTH]
        
    # 3. Strip null bytes or other weird control chars if needed
    
    return content
