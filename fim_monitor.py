#!/usr/bin/env python3
import hashlib
import os

def get_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for block in iter(lambda: f.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

if __name__ == '__main__':
    target = "incident_triage.py"
    if os.path.exists(target):
        print(f"[+] SHA-256 for {target}: {get_hash(target)}")
    else:
        print("[-] Target file not found.")
