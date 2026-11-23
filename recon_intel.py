#!/usr/bin/env python3
"""
Passive Reconnaissance & DNS Intelligence Gatherer
Part of the Offensive Security & Telemetry Toolkit
"""

import socket
import urllib.request
import json
import sys

def get_dns_info(domain):
    print(f"\n[*] Querying Core DNS Records for: {domain}")
    print("-" * 50)
    
    # Resolve IPv4
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] A Record (IPv4): {ip}")
    except socket.gaierror:
        print("[-] A Record: Could not resolve IP address.")

def inspect_http_headers(domain):
    print(f"\n[*] Inspecting HTTP Response Headers for: {domain}")
    print("-" * 50)
    url = f"http://{domain}"
    
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Security Intelligence Scanner)'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            headers = response.info()
            
            # Key headers revealing technology stacks
            sensitive_headers = ['Server', 'X-Powered-By', 'X-AspNet-Version', 'Set-Cookie']
            
            for header in sensitive_headers:
                val = headers.get(header)
                if val:
                    print(f"[!] Info Disclosed -> {header}: {val}")
                else:
                    print(f"[+] Protected -> {header}: Not disclosed")
                    
    except Exception as e:
        print(f"[-] HTTP Inspection Failed: {e}")

def main():
    if len(sys.argv) > 1:
        target = sys.argv[1].strip()
    else:
        target = input("Enter target domain (e.g., example.com): ").strip()

    if not target:
        print("[-] No target specified.")
        sys.exit(1)

    print("=" * 60)
    print(f"      PASSIVE RECONNAISSANCE MODULE: {target}")
    print("=" * 60)

    get_dns_info(target)
    inspect_http_headers(target)

if __name__ == "__main__":
    main()
