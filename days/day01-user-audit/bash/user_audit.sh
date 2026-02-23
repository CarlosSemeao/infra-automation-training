#!/bin/bash

USER_NAME="devops_user"

if id "$USER_NAME" &>/dev/null; then
    echo "[OK] User $USER_NAME already exists"
else
    echo "[INFO] User $USER_NAME does not exist. Creating..."
    sudo useradd "$USER_NAME"
    echo "[DONE] User $USER_NAME created"
fi
