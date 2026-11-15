#!/usr/bin/env python3
import re
import json

LOG_DATA = """
2026-10-16 22:10:01 192.168.1.105 Failed password for invalid user admin
2026-10-16 22:10:15 192.168.1.105 Failed password for invalid user root
2026-10-16 22:10:22 192.168.1.105 Failed password for user deploy
2026-10-16 22:10:30 192.168.1.105 Failed password for user admin
2026-10-16 22:10:45 192.168.1.105 Failed password for user admin
2026-10-16 22:11:00 10.0.0.12 Accepted password for user analyst
"""

def parse_and_triage(log_content, threshold=4, window_seconds=60):
    pattern = re.compile(r'(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<ip>\d{1,3}(?:\.\d{1,3}){3}) (?P<msg>Failed password.*)')
    attempts = {}

    for line in log_content.strip().split('\n'):
        match = pattern.search(line)
        if match:
            from datetime import datetime
            ts = datetime.strptime(match.group('time'), "%Y-%m-%d %H:%M:%S")
            ip = match.group('ip')
            attempts.setdefault(ip, []).append(ts)

    alerts = []
    for ip, timestamps in attempts.items():
        timestamps.sort()
        for i in range(len(timestamps)):
            window = [t for t in timestamps if 0 <= (t - timestamps[i]).total_seconds() <= window_seconds]
            if len(window) >= threshold:
                alerts.append({
                    "severity": "HIGH",
                    "ip": ip,
                    "event_count": len(window),
                    "action": "Escalated to L2 / Block IP"
                })
                break
    return alerts

if __name__ == '__main__':
    print(json.dumps(parse_and_triage(LOG_DATA), indent=2))
