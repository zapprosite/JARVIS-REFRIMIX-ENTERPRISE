#!/bin/bash

# Tests basic flow: Gateway receiving message -> orchestrator
echo "🔥 Running Smoke Test..."

URL="http://localhost:3000/v1/messages"

RESPONSE=$(curl -s -X POST "$URL" \
    -H "Content-Type: application/json" \
    -d '{ "from": "123456", "body": "test smoke", "tenantId": "smoke_test" }')

echo "Response: $RESPONSE"

if [[ "$RESPONSE" == *"queued"* ]]; then
    echo "✅ Gateway accepted message."
    exit 0
else
    echo "❌ Smoke test failed."
    exit 1
fi
