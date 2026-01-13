import time
import re
from collections import defaultdict

LOG_FILE = "auth.log"
BLOCKLIST_FILE = "blocked_ips.txt"
FAILED_LIMIT = 5
TIME_WINDOW = 60

failed_attempts = defaultdict(list)
blocked_ips = set()

def load_blocked_ips():
    try:
        with open(BLOCKLIST_FILE, "r") as f:
            for line in f:
                blocked_ips.add(line.strip())
    except FileNotFoundError:
        pass

def block_ip(ip):
    if ip not in blocked_ips:
        blocked_ips.add(ip)
        with open(BLOCKLIST_FILE, "a") as f:
            f.write(ip + "\n")
        print(f"[BLOCKED] {ip}")

def parse_log():
    with open(LOG_FILE, "r") as log:
        for line in log:
            match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ip = match.group(1)
                failed_attempts[ip].append(time.time())
                evaluate_ip(ip)

def evaluate_ip(ip):
    now = time.time()
    attempts = [t for t in failed_attempts[ip] if now - t <= TIME_WINDOW]
    failed_attempts[ip] = attempts

    if len(attempts) >= FAILED_LIMIT:
        respond(ip)

def respond(ip):
    print(f"\n🚨 BRUTE FORCE DETECTED from {ip}")
    print("[ACTION] Blocking IP & locking account\n")
    block_ip(ip)

def main():
    print("[INFO] Starting Brute Force Detection Engine")
    load_blocked_ips()
    parse_log()

if __name__ == "__main__":
    main()
