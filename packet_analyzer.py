#!/usr/bin/env python3
import json

PACKET_LOGS = "2026-10-16 185.220.101.5 4444 TCP 512"
SUSPICIOUS_PORTS = {4444: "Metasploit Default C2"}

if __name__ == '__main__':
    alerts = []
    for line in PACKET_LOGS.strip().split('\n'):
        parts = line.split()
        port = int(parts[2])  # Index 2 is the port number
        if port in SUSPICIOUS_PORTS:
            alerts.append({"port": port, "risk": SUSPICIOUS_PORTS[port]})
    print(json.dumps(alerts, indent=2))
