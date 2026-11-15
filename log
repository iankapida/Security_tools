#!/usr/bin/env python3
import json

LOGS = [
    "[AUTH] Failed login for root",
    "[WEB] GET /admin/config.php - Status: 403"
]

if __name__ == '__main__':
    parsed = [{"event": log, "severity": "HIGH" if "root" in log or "403" in log else "INFO"} for log in LOGS]
    print(json.dumps(parsed, indent=2))
