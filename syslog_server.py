#!/usr/bin/env python3
import socket
import sys
import os

# Import our SIEM database logger safely
try:
    from siem_db import log_event
except ImportError:
    def log_event(source_tool, severity, message, remediation="None"):
        print(f"[DB Stub] {source_tool} | {severity} | {message}")

HOST = "0.0.0.0"
PORT = 5140  # Standard unprivileged port for lab testing

def start_syslog_listener():
    print(f"[+] Starting Network Syslog Ingestion Server on {HOST}:{PORT}...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))
    
    try:
        while True:
            data, addr = sock.recvfrom(1024)
            message = data.decode('utf-8', errors='ignore').strip()
            print(f"[!] Syslog Packet Captured from {addr[0]}: {message}")
            
            # Automatically ingest into SQLite SIEM database
            log_event(
                source_tool="SyslogListener",
                severity="MEDIUM",
                message=f"Remote telemetry from {addr[0]}: {message}",
                remediation="Evaluate packet headers and verify source asset."
            )
    except KeyboardInterrupt:
        print("\n[-] Shutting down Syslog server gracefully.")
    finally:
        sock.close()

if __name__ == "__main__":
    start_syslog_listener()
