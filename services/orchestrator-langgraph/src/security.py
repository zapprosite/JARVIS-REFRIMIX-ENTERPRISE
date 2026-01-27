import re
import unicodedata
import logging

logger = logging.getLogger(__name__)

def sanitize_text(text: str) -> str:
    """
    Performs general text sanitization:
    - Normalizes unicode (NFKC)
    - Removes control characters (prevents weird terminal/display issues)
    - Basic HTML tag stripping
    - Strips leading/trailing whitespace
    """
    if not text:
        return ""
    
    # 1. Normalize unicode
    text = unicodedata.normalize("NFKC", text)
    
    # 2. Remove control characters (except newline and tab)
    # This prevents various terminal-based or hidden char attacks
    text = "".join(ch for ch in text if unicodedata.category(ch)[0] != "C" or ch in "\n\t")
    
    # 3. Strip HTML tags (rudimentary but effective for simple text)
    text = re.sub(r'<[^>]*?>', '', text)
    
    # 4. Escape common template/injection characters if necessary
    # For LangChain/LLM, {{ and }} can be dangerous in templates
    text = text.replace("{{", "{").replace("}}", "}") # Or just strip them? 
    # Let's just escape or replace to be safe.
    
    return text.strip()

def sanitize_prompt(content: str) -> str:
    """
    Sanitizes user input to prevent common prompt injection attacks 
    and role spoofing.
    """
    if not content:
        return ""
        
    # First, run general text sanitization
    content = sanitize_text(content)
    
    content_lower = content.lower()
    
    # 1. Block common injection keywords and role spoofing attempts
    # We use regex for better matching (word boundaries)
    blocked_patterns = [
        r"ignore previous instructions",
        r"ignore the above",
        r"system:", 
        r"assistant:",
        r"user:",
        r"developer:",
        r"strictly follow",
        r"you are now",
        r"forget everything",
        r"markdown code for everything",
    ]
    
    for pattern in blocked_patterns:
        if re.search(pattern, content_lower):
            logger.warning(f"Potential prompt injection detected with pattern: {pattern}")
            raise ValueError("Security Alert: Input contains forbidden phrases or potential role spoofing.")
            
    # 2. Prevent PII exposure (Simple regex example for emails/cards)
    # This is a 'real-world' feature usually requested in enterprise bots.
    email_regex = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    if re.search(email_regex, content):
        # We can either mask it or block. Let's mask it for demo.
        content = re.sub(email_regex, "[EMAIL_REDACTED]", content)

    # 3. Length limit to prevent context exhaustion
    MAX_LENGTH = 4000
    if len(content) > MAX_LENGTH:
        logger.info(f"Input truncated from {len(content)} to {MAX_LENGTH}")
        content = content[:MAX_LENGTH]
        
    return content
