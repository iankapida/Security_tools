#!/usr/bin/env python3
import socket
import threading
import sys
from datetime import datetime

def scan_port(target_ip, port, results):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            results.append(port)
        s.close()
    except Exception:
        pass

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    ports_to_scan = [21, 22, 23, 25, 53, 80, 443, 445, 3306, 3389, 8080]
    
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[-] Hostname could not be resolved: {target}")
        sys.exit(1)

    print(f"\n[+] Starting scan on target: {target_ip}")
    print(f"[+] Time started: {datetime.now()}")
    print("-" * 40)

    threads = []
    results = []

    for port in ports_to_scan:
        t = threading.Thread(target=scan_port, args=(target_ip, port, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n[+] Scan Completed.")
    print("-" * 40)
    if results:
        for port in sorted(results):
            print(f"[*] Port {port}: OPEN")
    else:
        print("[-] No specified ports open.")
    print("-" * 40)

if __name__ == "__main__":
    main()
