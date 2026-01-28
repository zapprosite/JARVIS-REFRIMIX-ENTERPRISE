-- 002_create_user_profiles.sql
-- Stores long-term "Episodic Memory" about users in JSONB format.
-- Allows the Agent to "remember" facts like "User X has a Daikin VRV".

CREATE TABLE IF NOT EXISTS user_profiles (
    tenant_id VARCHAR(50) NOT NULL,
    user_id VARCHAR(50) NOT NULL,
    profile_data JSONB DEFAULT '{}'::jsonb,
    last_updated TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    PRIMARY KEY (tenant_id, user_id)
);

-- Index for fast lookup
CREATE INDEX IF NOT EXISTS idx_user_profiles_gin ON user_profiles USING gin (profile_data);
