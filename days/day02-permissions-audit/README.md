# Day 02 — File permission audit + fix

## Objective
Ensure a target file has secure permissions (600). If not, fix it.

## Scope
- Target: /tmp/secure_file.txt
- Assumption: Fedora VM, local execution

---

## Bash

### File
`bash/perm_audit.sh`

### Run
```bash
cd days/day02-permissions-audit/bash
chmod +x perm_audit.sh
./perm_audit.sh
./perm_audit.sh
