import os
import redis.asyncio as redis
from fastapi import HTTPException
import logging

logger = logging.getLogger(__name__)

class RateLimiter:
    def __init__(self, redis_url: str):
        self.mock_mode = os.getenv("MOCK_REDIS") == "true"
        if self.mock_mode:
            logger.info("RateLimiter running in MOCK mode (bypassed).")
            self.redis = None
        else:
            self.redis = redis.from_url(redis_url, decode_responses=True)
    
    async def check_quota(self, tenant_id: str, user_id: str):
        if self.mock_mode:
            return

        # Key schema: quota:{tenant_id}:{user_id}
        key = f"quota:{tenant_id}:{user_id}"
        
        # Increment returns the new value
        try:
            count = await self.redis.incr(key)
        except Exception as e:
            logger.error(f"Redis error: {e}")
            # Fail open or closed? Fail open for now if redis dies.
            return
        
        # If first request (count == 1), set expiration
        if count == 1:
            await self.redis.expire(key, 60)  # 1 minute window
        
        # Hardcoded limits for now, should be dynamic based on Tenant DB
        # Basic: 20 req/min
        limit = 20 
        
        if count > limit:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
