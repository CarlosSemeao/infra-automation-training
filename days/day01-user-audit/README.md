# Day 01 — User existence audit + create if missing

## Objective
Ensure a target Linux user exists on the system. If the user does not exist, create it in an idempotent way.

## Scope
- Target: Linux system user (e.g. devops_user)
- Assumption: Fedora VM, local execution

---

## Bash

### File
bash/user_audit.sh

### Run
```bash
cd days/day01-user-audit/bash
chmod +x user_audit.sh
./user_audit.sh
