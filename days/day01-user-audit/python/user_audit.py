import subprocess

user = "devops_user"

result = subprocess.run(["id", user], capture_output=True, text=True)

if result.returncode == 0:
    print(f"[OK] User {user} already exists")
else:
    print(f"[INFO] User {user} does not exist. Creating...")
    subprocess.run(["sudo", "useradd", user])
    print(f"[DONE] User {user} created")
