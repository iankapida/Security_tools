#!/usr/bin/env python3
import hashlib
import json
import os
import sys

HASH_STORE = "baseline.json"

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4048), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def create_baseline(file_paths):
    baseline = {}
    for path in file_paths:
        file_hash = calculate_sha256(path)
        if file_hash:
            baseline[path] = file_hash
            print(f"[+] Baseline set for: {path}")
        else:
            print(f"[-] File not found: {path}")
            
    with open(HASH_STORE, "w") as f:
        json.dump(baseline, f, indent=4)
    print(f"[+] Baseline saved to {HASH_STORE}")

def check_integrity():
    if not os.path.exists(HASH_STORE):
        print(f"[-] No baseline file found ({HASH_STORE}). Create one first.")
        return

    with open(HASH_STORE, "r") as f:
        baseline = json.load(f)

    print("\n[+] Checking File Integrity...")
    print("-" * 50)
    for path, old_hash in baseline.items():
        current_hash = calculate_sha256(path)
        if current_hash is None:
            print(f"[!] WARNING: File missing -> {path}")
        elif current_hash != old_hash:
            print(f"[!] ALERT: File modified/tampered -> {path}")
        else:
            print(f"[OK] Unchanged -> {path}")
    print("-" * 50)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "init":
        create_baseline(sys.argv[2:])
    else:
        check_integrity()
