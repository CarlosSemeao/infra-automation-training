#!/usr/bin/env python3
import subprocess

TARGET_FILE = "/tmp/secure_file.txt"

def run(cmd):
    return subprocess.run(cmd, text=True, capture_output=True)

def file_exists():
    result = run(["test", "-f", TARGET_FILE])
    return result.returncode == 0

def create_file():
    print("[INFO] File missing. Creating...")
    subprocess.run(["sudo", "touch", TARGET_FILE])

def get_perm():
    result = run(["stat", "-c", "%a", TARGET_FILE])
    return result.stdout.strip()

def fix_perm():
    print("[ACTION] Fixing permission to 600")
    subprocess.run(["sudo", "chmod", "600", TARGET_FILE])

def main():
    if not file_exists():
        create_file()

    perm = get_perm()

    if perm != "600":
        fix_perm()
    else:
        print("[OK] Permission already 600")

if __name__ == "__main__":
    main()
