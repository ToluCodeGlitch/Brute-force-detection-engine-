import time
from collections import defaultdict

# ==============================
# CONFIGURATION (Hardening Rules)
# ==============================

FAILED_ATTEMPT_LIMIT = 5        # Max failed attempts allowed
TIME_WINDOW = 60                # Time window in seconds
BLOCKED_IPS = set()             # Store blocked IPs

# Track failed login attempts per IP
login_attempts = defaultdict(list)

# ==============================
# CORE SECURITY LOGIC
# ==============================

def log_login_attempt(ip_address, success=False):
    """
    Logs failed login attempts and checks for brute-force behavior
    """
    if ip_address in BLOCKED_IPS:
        print(f"[DENIED] Login attempt from blocked IP: {ip_address}")
        return

    if not success:
        login_attempts[ip_address].append(time.time())
        print(f"[LOG] Failed login attempt from {ip_address}")
        detect_bruteforce(ip_address)
    else:
        print(f"[SUCCESS] Successful login from {ip_address}")
        login_attempts[ip_address].clear()


def detect_bruteforce(ip_address):
    """
    Detects brute-force attacks based on failed attempts within time window
    """
    current_time = time.time()
    recent_attempts = [
        t for t in login_attempts[ip_address]
        if current_time - t <= TIME_WINDOW
    ]

    login_attempts[ip_address] = recent_attempts

    if len(recent_attempts) >= FAILED_ATTEMPT_LIMIT:
        respond_to_attack(ip_address)


def respond_to_attack(ip_address):
    """
    Automated security response
    """
    print("\n🚨 [ALERT] BRUTE FORCE ATTACK DETECTED 🚨")
    print(f"Source IP: {ip_address}")
    print("[ACTION] Blocking IP and locking account\n")

    BLOCKED_IPS.add(ip_address)

    # Simulated responses
    lock_account(ip_address)
    send_alert(ip_address)


def lock_account(ip_address):
    print(f"[LOCKOUT] Account locked due to suspicious activity from {ip_address}")


def send_alert(ip_address):
    print(f"[NOTIFICATION] Security team alerted about IP: {ip_address}")


# ==============================
# ATTACK SIMULATION
# ==============================

def simulate_attack():
    attacker_ip = "192.168.10.23"

    print("\n--- Simulating Brute Force Attack ---\n")

    for attempt in range(6):
        log_login_attempt(attacker_ip, success=False)
        time.sleep(5)

    print("\n--- Attack Simulation Complete ---\n")


# ==============================
# MAIN EXECUTION
# ==============================

if __name__ == "__main__":
    simulate_attack()
