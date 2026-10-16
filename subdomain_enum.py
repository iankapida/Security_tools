#!/usr/bin/env python3
import socket

TARGET_DOMAIN = "example.com"
WORDLIST = ["www", "api", "mail", "dev", "vpn", "admin"]

if __name__ == '__main__':
    print(f"[*] Enumerating {TARGET_DOMAIN}...")
    for sub in WORDLIST:
        target = f"{sub}.{TARGET_DOMAIN}"
        try:
            ip = socket.gethostbyname(target)
            print(f"[+] RESOLVED: {target} -> {ip}")
        except socket.gaierror:
            pass
