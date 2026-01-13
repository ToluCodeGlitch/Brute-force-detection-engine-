# Automated Brute-Force Detection & Response
# Author: Tolulope Oni

logs = [
    "IP=192.168.1.10 user=admin status=failed",
    "IP=192.168.1.10 user=admin status=failed",
    "IP=192.168.1.10 user=admin status=failed",
    "IP=192.168.1.10 user=admin status=failed",
    "IP=192.168.1.10 user=admin status=failed",
    "IP=192.168.1.10 user=admin status=failed"
]

THRESHOLD = 5
failed_attempts = {}

for entry in logs:
    parts = entry.split()
    ip = parts[0].split("=")[1]
    user = parts[1].split("=")[1]
    status = parts[2].split("=")[1]

    if status == "failed":
        failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

for ip, count in failed_attempts.items():
    if count > THRESHOLD:
        print(f"[ALERT] Brute-force detected from {ip}")
        print(f"[ACTION] Blocking IP: {ip}")
        print("[ACTION] Locking affected account(s)")
