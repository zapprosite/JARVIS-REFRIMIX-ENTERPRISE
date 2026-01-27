# Skill: Rate Limit Guard

## Propósito
Validar quota antes de processar request

## Logic
```python
async def guard(tenant_id, user_id, redis_client):
    tier = await get_tier(tenant_id)  # basic/pro/agency
    limits = {"basic": 100, "pro": 1000, "agency": 5000}
    
    key = f"quota:{tenant_id}:{user_id}"
    count = await redis_client.incr(key)
    if count == 1:
        await redis_client.expire(key, 60)
    
    if count > limits[tier]:
        raise HTTPException(429, f"Quota exceeded: {count}/{limits[tier]}")
```

## Integration
Adicionar ANTES de graph_app.ainvoke:
```python
await rate_limit_guard(req.tenant_id, req.user_id)
```
