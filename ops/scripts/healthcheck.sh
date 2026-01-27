#!/bin/bash

# Configuration
SERVICES=("api-gateway:3000" "whatsapp-adapter:3001" "orchestrator-langgraph:8000" "rag-hvac:8000" "browser-tools:3000" "litellm:4000")

echo "🏥 Checking Endpoint Health..."

ALL_GOOD=true

for svc in "${SERVICES[@]}"; do
    IFS=":" read -r NAME PORT <<< "$svc"
    URL="http://localhost:$PORT/health"
    
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
    
    if [ "$HTTP_CODE" == "200" ]; then
        echo "✅ $NAME is OK"
    else
        echo "❌ $NAME returned $HTTP_CODE"
        ALL_GOOD=false
    fi
done

if [ "$ALL_GOOD" = true ]; then
    echo "🟢 All systems operational."
    exit 0
else
    echo "🔴 Some systems are down."
    exit 1
fi
