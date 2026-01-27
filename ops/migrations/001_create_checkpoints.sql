-- ops/migrations/001_create_checkpoints.sql
-- Note: langgraph-checkpoint-postgres handles its own schema if we call .setup(),
-- but having a manual migration is safer for production environments.

CREATE TABLE IF NOT EXISTS checkpoints (
    thread_id TEXT PRIMARY KEY,
    checkpoint JSONB NOT NULL,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_checkpoints_thread ON checkpoints(thread_id);
CREATE INDEX IF NOT EXISTS idx_checkpoints_created ON checkpoints(created_at);
