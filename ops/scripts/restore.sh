#!/bin/bash
set -e

BACKUP_DIR=$1

if [ -z "$BACKUP_DIR" ]; then
    echo "Usage: ./restore.sh <backup_directory>"
    exit 1
fi

echo "⚠️ Restoring from $BACKUP_DIR..."
read -p "Are you sure? This will overwrite data. (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    exit 1
fi

# Postgres
if [ -f "$BACKUP_DIR/zappro_pg.sql" ]; then
    echo "♻️ Restoring Postgres..."
    cat "$BACKUP_DIR/zappro_pg.sql" | docker compose -f ops/compose/docker-compose.prod.yml exec -T postgres psql -U user zappro
fi

# Redis
if [ -f "$BACKUP_DIR/redis_dump.rdb" ]; then
    echo "♻️ Restoring Redis..."
    # Redis needs to be stopped to replace dump
    docker compose -f ops/compose/docker-compose.prod.yml stop redis
    docker cp "$BACKUP_DIR/redis_dump.rdb" $(docker compose -f ops/compose/docker-compose.prod.yml ps -aq redis):/data/dump.rdb
    docker compose -f ops/compose/docker-compose.prod.yml start redis
fi

echo "✅ Restore complete!"
