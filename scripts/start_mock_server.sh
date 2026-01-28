#!/bin/bash
# Starts the Orchestrator in Credentialless Mock Mode
export MOCK_LLM=true
export TEST_MODE=true
export MOCK_REDIS=true
export REDIS_URL=redis://mock:6379 
# The application tries to connect to Redis on startup for RateLimiter.
# If we want FULL credentialless without docker, we need to Mock Redis too.
# But RateLimiter is in main.py.

echo "Starting Orchestrator in MOCK_LLM + TEST_MODE..."
echo "Note: This requires a running Redis or we need to patch RateLimiter in main.py to allow loose connection."

# For true credentialless, main.py should conditionally skip RateLimiter if MOCK_REDIS is set.
# Let's assume we can skip RateLimiter for now or the user has a local redis.
# If not, we might fail on startup.

# Let's check main.py again.
# Navigate to service directory to simplify imports logic
cd "$(dirname "$0")/../services/orchestrator-langgraph"

# Run uvicorn assuming we are in service root
PYTHONPATH=. uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload --log-level debug
