import os
import logging
from langchain.globals import set_llm_cache
from langchain_community.cache import RedisSemanticCache
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import FakeEmbeddings

logger = logging.getLogger(__name__)

def setup_semantic_cache(redis_url: str):
    """
    Configures Semantic Caching for LLM responses.
    Requires Redis Stack (for vector search).
    """
    try:
        if os.getenv("MOCK_LLM") == "true":
             embeddings = FakeEmbeddings(size=1536)
             logger.info("Semantic Cache: Using FakeEmbeddings (Mock Mode)")
        else:
             embeddings = OpenAIEmbeddings()
             
        # Check if we should enable semantic cache
        # Using a distinct index name to avoid collision
        set_llm_cache(
            RedisSemanticCache(
                redis_url=redis_url,
                embedding=embeddings,
                score_threshold=0.90
            )
        )
        logger.info("Semantic Cache: Enabled via Redis Stack")
    except Exception as e:
        logger.warning(f"Failed to enable Semantic Cache: {e}")
        # Fallback to standard (in-memory) or no cache if Redis fails
