#!/usr/bin/env python3
import re
import json

SAMPLE_THREAT_REPORT = """
C2 IP Addresses identified: 185.220.101.5, 192.0.2.1
Malicious domains involved: update-check-auth.com, malware-c2-node.net
SHA-256 Hashes: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
"""

def extract_iocs(text):
    return {
        "ipv4_addresses": list(set(re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text))),
        "domains": list(set(re.findall(r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b', text))),
        "sha256_hashes": list(set(re.findall(r'\b[a-fA-F0-9]{64}\b', text)))
    }

if __name__ == '__main__':
    print(json.dumps(extract_iocs(SAMPLE_THREAT_REPORT), indent=2))
