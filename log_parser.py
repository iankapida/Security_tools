#!/usr/bin/env python3
import re
from collections import Counter
import sys

def parse_auth_log(file_path, threshold=3):
    failed_attempts = []
    ip_pattern = re.compile(r'Failed password for (?:invalid user )?.*? from (\d{1,3}(?:\.\d{1,3}){3})')

    try:
        with open(file_path, 'r') as file:
            for line in file:
                match = ip_pattern.search(line)
                if match:
                    failed_attempts.append(match.group(1))
        
        ip_counts = Counter(failed_attempts)
        
        print(f"\n[+] Scanning Log File: {file_path}")
        print("-" * 45)
        print(f"{'IP Address':<20} | {'Failed Attempts':<15}")
        print("-" * 45)
        
        for ip, count in ip_counts.items():
            status = " [ALERT: BRUTE-FORCE?]" if count >= threshold else ""
            print(f"{ip:<20} | {count:<15}{status}")
            
        print("-" * 45)
        
    except FileNotFoundError:
        print(f"[-] Error: Log file '{file_path}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    log_file = sys.argv[1] if len(sys.argv) > 1 else "sample_auth.log"
    parse_auth_log(log_file)
# Tampered comment
# Unauthorized modification
