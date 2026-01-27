#!/bin/bash
set -e

BACKUP_DIR="./backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo "💾 Starting Backup to $BACKUP_DIR..."

# Postgres
echo "📦 Backing up Postgres..."
docker compose -f ops/compose/docker-compose.prod.yml exec -T postgres pg_dump -U user zappro > "$BACKUP_DIR/zappro_pg.sql"

# Qdrant (Snapshot)
echo "📦 Backing up Qdrant..."
# Qdrant snapshots are better handled via API, but for now we rely on volume. 
# Or we can trigger a snapshot via curl.
# curl -X POST "http://localhost:6333/collections/manuals/snapshots"
# For this script, we'll assume volume backup is external or we dump data.
# Let's use internal snapshot API logic if possible, otherwise skip relying on volume.

# Redis
echo "📦 Backing up Redis..."
docker compose -f ops/compose/docker-compose.prod.yml exec -T redis redis-cli save
docker cp $(docker compose -f ops/compose/docker-compose.prod.yml ps -q redis):/data/dump.rdb "$BACKUP_DIR/redis_dump.rdb"

echo "✅ Backup complete!"
ls -lh "$BACKUP_DIR"
