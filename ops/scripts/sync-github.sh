#!/bin/bash

# Sync script for JARVIS-REFRIMIX-ENTERPRISE
echo "🔄 Starting GitHub Sync..."

# Ensure we are in the root
cd "$(dirname "$0")/../.."

# Add changes
git add .

# Commit (timestamped)
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
git commit -m "chore: sync at $TIMESTAMP"

# Push
echo "⬆️ Pushing to origin/main..."
git push origin main

echo "✅ Sync complete!"
