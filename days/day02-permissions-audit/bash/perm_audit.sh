#!/usr/bin/env bash
set -euo pipefail

TARGET_FILE="/tmp/secure_file.txt"

# If file doesn't exist, create it
if [ ! -f "$TARGET_FILE" ]; then
    echo "[INFO] File missing. Creating $TARGET_FILE"
    sudo touch "$TARGET_FILE"
fi

# Get current permission
CURRENT_PERM=$(stat -c "%a" "$TARGET_FILE")

if [ "$CURRENT_PERM" != "600" ]; then
    echo "[ACTION] Fixing permission from $CURRENT_PERM to 600"
    sudo chmod 600 "$TARGET_FILE"
else
    echo "[OK] Permission already 600"
fi
