#!/usr/bin/env python3
import sqlite3

DB_NAME = "soc_siem.db"

def run_correlation_rules():
    print("[+] Running SIEM Cross-Module Correlation Engine...")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Query event counts grouped by severity to detect threat spikes
    cursor.execute('''
        SELECT severity, COUNT(*) as count 
        FROM security_events 
        GROUP BY severity
    ''')
    results = cursor.fetchall()
    conn.close()
    
    print("-" * 50)
    print("[*] Cross-Module Event Correlation Summary:")
    for row in results:
        sev, count = row
        print(f"    Severity: {sev} | Total Triggered: {count}")
        if sev in ("HIGH", "CRITICAL") and count > 0:
            print(f"    [!] CORRELATION ALERT: Elevated threat cluster detected for level {sev}!")
    print("-" * 50)

if __name__ == "__main__":
    run_correlation_rules()
