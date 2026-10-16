#!/usr/bin/env python3
import socket
from concurrent.futures import ThreadPoolExecutor

def scan(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    if sock.connect_ex((ip, port)) == 0:
        print(f"[+] PORT OPEN: {port}")
    sock.close()

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as executor:
        for p in [22, 80, 443, 8080]:
            executor.submit(scan, "127.0.0.1", p)
