# Incident: Rate Limit Spikes

How to diagnose and handle rate limit complaints.

## Diagnosis

1. **Check Redis**:
   - Exec into redis container: `docker exec -it <redis-id> redis-cli`
   - Check keys: `KEYS rate_limit:*`
   - Check value: `GET rate_limit:<tenant_id>`

2. **Check Logs**:
   - `docker logs whatsapp-adapter | grep "Rate limit exceeded"`

## Mitigation

1. **Reset Limit**:
   - `DEL rate_limit:<tenant_id>`

2. **Increase Limit**:
   - Edit `services/whatsapp-adapter/src/index.js` (or env var if configured) to increase default limit.
   - Ideally, implement Tier logic correctly in database and have Adapter read from it.
