#!/usr/bin/env python3
"""
Active Service Enumeration & Banner Grabbing Tool
Part of the Offensive Security & Telemetry Toolkit
"""

import socket
import sys

# Common service ports and their standard protocols
TARGET_PORTS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}

def grab_banner(ip, port):
    try:
        # Create a socket connection with a short timeout
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2.0)
        s.connect((ip, port))
        
        # For HTTP, send a basic request to trigger a response header
        if port in [80, 443]:
            s.sendall(b"HEAD / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
        
        banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
        s.close()
        
        if banner:
            print(f"[+] Port {port} ({TARGET_PORTS.get('port', 'Service')}): OPEN")
            print(f"    [->] Banner: {banner.splitlines()[0] if banner else 'No banner text'}")
        else:
            print(f"[+] Port {port}: OPEN (No banner returned)")
            
    except socket.timeout:
        print(f"[-] Port {port}: Filtered or Timeout")
    except ConnectionRefusedError:
        print(f"[-] Port {port}: Closed")
    except Exception as e:
        print(f"[-] Port {port}: Error ({e})")

def main():
    if len(sys.argv) > 1:
        target_host = sys.argv[1].strip()
    else:
        target_host = input("Enter target IP or hostname: ").strip()

    if not target_host:
        print("[-] No target specified.")
        sys.exit(1)

    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("[-] Could not resolve host.")
        sys.exit(1)

    print("=" * 60)
    print(f"      ACTIVE ENUMERATION & BANNER GRABBER: {target_ip}")
    print("=" * 60)

    for port in TARGET_PORTS.keys():
        grab_banner(target_ip, port)

if __name__ == "__main__":
    main()
