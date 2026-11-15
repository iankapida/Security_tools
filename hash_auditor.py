#!/usr/bin/env python3
import hashlib
import sys
import re

def evaluate_password(password):
    print(f"\n[+] Auditing Password Strength...")
    print("-" * 40)
    score = 0
    feedback = []
    
    if len(password) >= 10:
        score += 1
    else:
        feedback.append("[-] Length is under 10 characters (Recommendation: 12+).")
        
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("[-] Missing uppercase and/or lowercase character mix.")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("[-] Missing numeric digits.")
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("[-] Missing special symbols.")
        
    print(f"[*] Complexity Score: {score}/4")
    if feedback:
        print("\n[!] Recommendations:")
        for tip in feedback:
            print(f"  {tip}")
    else:
        print("[+] Strong password criteria met!")
    print("-" * 40)

def compute_hashes(text):
    print(f"\n[+] Computing Cryptographic Hashes:")
    print("-" * 40)
    print(f"MD5    : {hashlib.md5(text.encode()).hexdigest()}")
    print(f"SHA-1  : {hashlib.sha1(text.encode()).hexdigest()}")
    print(f"SHA-256: {hashlib.sha256(text.encode()).hexdigest()}")
    print("-" * 40)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "TestPassword123!"
    evaluate_password(target)
    compute_hashes(target)
