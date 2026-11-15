#!/usr/bin/env python3
import sqlite3
from datetime import datetime

DB_NAME = "soc_siem.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS security_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            source_tool TEXT,
            severity TEXT,
            message TEXT,
            remediation TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_event(source_tool, severity, message, remediation="None"):
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO security_events (timestamp, source_tool, severity, message, remediation)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, source_tool, severity, message, remediation))
    conn.commit()
    conn.close()
    print(f"[+] SIEM DB: Event securely logged from {source_tool}")

def view_events():
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM security_events ORDER BY id DESC LIMIT 5')
    rows = cursor.fetchall()
    conn.close()
    
    print("\n[+] Recent SIEM Security Events (Database Audit):")
    print("-" * 60)
    for row in rows:
        print(f"ID: {row[0]} | Time: {row[1]} | Tool: {row[2]} | Sev: {row[3]}")
        print(f"Msg: {row[4]}")
        print(f"Action: {row[5]}")
        print("-" * 60)

if __name__ == "__main__":
    init_db()
    print("[+] SIEM Database initialized successfully (`soc_siem.db`)")
    view_events()
