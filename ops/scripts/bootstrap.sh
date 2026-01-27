#!/bin/bash
set -e

echo "🚀 Starting Zappro Bootstrap..."

# 1. Check dependencies
if ! command -v docker &> /dev/null; then
    echo "❌ Docker not found!"
    exit 1
fi

# 2. Network creation (if not exists)
if [ -z "$(docker network ls -q -f name=jarvis-net)" ]; then
    echo "🌐 Creating jarvis-net..."
    docker network create jarvis-net
else
    echo "✅ Network jarvis-net exists."
fi

# 3. Build & Up
echo "🏗️ Building services..."
docker compose -f ops/compose/docker-compose.prod.yml build

echo "⬆️ Starting services..."
docker compose -f ops/compose/docker-compose.prod.yml up -d

# 4. Wait for health
echo "⏳ Waiting for services to be healthy..."
sleep 10
./ops/scripts/healthcheck.sh

echo "🎉 Bootstrap complete! System is running."
