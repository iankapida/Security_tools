#!/usr/init/env python3
"""
Service Vulnerability & Risk Analyzer
Part of the Offensive Security & Telemetry Toolkit
"""

import sys

# Simulated local vulnerability database mapping software signatures to known risks
KNOWN_VULNERABILITIES = {
    "OpenSSH_6.6.1": {
        "cve": "CVE-2015-5600 / CVE-2016-0777",
        "severity": "HIGH",
        "description": "Potential information disclosure or keyboard-interactive brute force risks in older OpenSSH builds."
    },
    "vsftpd_2.3.4": {
        "cve": "CVE-2011-2523",
        "severity": "CRITICAL",
        "description": "Backdoor command execution vulnerability triggered by a smiley face (:^) username."
    },
    "Apache_2.4.49": {
        "cve": "CVE-2021-42013",
        "severity": "CRITICAL",
        "description": "Path traversal and remote code execution vulnerability."
    }
}

def analyze_banner(banner):
    print(f"\n[*] Analyzing Banner String: '{banner}'")
    print("-" * 50)
    
    match_found = False
    for signature, data in KNOWN_VULNERABILITIES.items():
        if signature.lower() in banner.lower():
            match_found = True
            print(f"[!] VULNERABILITY DETECTED!")
            print(f"    [->] Associated CVE: {data['cve']}")
            print(f"    [->] Risk Severity:  {data['severity']}")
            print(f"    [->] Details:        {data['description']}")
            
    if not match_found:
        print("[+] No direct critical CVE signatures matched in local database for this string.")
        print("    (Note: Always cross-reference manually with NVD / CVSS databases)")

def main():
    if len(sys.argv) > 1:
        banner_input = " ".join(sys.argv[1:])
    else:
        banner_input = input("Enter service banner or version string to analyze: ").strip()

    if not banner_input:
        print("[-] No input provided.")
        sys.exit(1)

    print("=" * 60)
    print("      VULNERABILITY ANALYSIS & CVE MAPPING MODULE")
    print("=" * 60)

    analyze_banner(banner_input)

if __name__ == "__main__":
    main()
