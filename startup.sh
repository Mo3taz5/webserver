#!/bin/bash

echo "============================================================"
echo "Mo3taz Cloud Save API - Startup"
echo "============================================================"

# Download server code from HuggingFace dataset
echo "Step 1: Loading server code from private dataset..."
python github_loader.py

if [ $? -ne 0 ]; then
    echo "❌ Failed to load server code"
    exit 1
fi

# Now run the actual startup script
echo ""
echo "Step 2: Starting server..."
bash startup.sh
