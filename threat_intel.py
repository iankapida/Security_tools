#!/usr/bin/env python3
import urllib.request
import json
import sys

def enrich_ip(ip_address):
    """
    Queries free public threat intelligence API for IP geolocation and ASN data.
    """
    if ip_address in ("127.0.0.1", "localhost", "0.0.0.0", "192.168.1.50"):
        return {
            "ip": ip_address,
            "country": "Local / Private Network",
            "org": "Internal Lab Asset",
            "threat_score": "SUSPICIOUS (Simulated)"
        }
        
    url = f"https://ipapi.co/{ip_address}/json/"
    req = urllib.request.Request(url, headers={'User-Agent': 'SOC-ThreatIntel-Bot'})
    
    try:
        with urllib.request.urlopen(req, timeout=4) as response:
            data = json.loads(response.read().decode())
            return {
                "ip": ip_address,
                "country": data.get("country_name", "Unknown"),
                "org": data.get("org", "Unknown"),
                "city": data.get("city", "Unknown"),
                "threat_score": "EVALUATED"
            }
    except Exception as e:
        return {"ip": ip_address, "error": str(e), "threat_score": "UNKNOWN"}

def generate_active_response(ip_address):
    """
    Active Response: Generates Linux UFW/Iptables firewall rules to isolate threats.
    """
    print(f"\n[🛡️ ACTIVE RESPONSE AUTOMATION]")
    print("-" * 50)
    print(f"[-] Threat identified from IP: {ip_address}")
    print(f"[+] Generating OS Firewall Containment Rule:")
    
    # Generate Linux UFW drop command
    ufw_command = f"sudo ufw deny from {ip_address} to any port 22 proto tcp"
    print(f"    > {ufw_command}")
    print(f"[+] Action: Firewall drop rule formulated for deployment.")
    print("-" * 50)
    return ufw_command

if __name__ == "__main__":
    target_ip = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.50"
    print(f"\n[+] Running Threat Intelligence Lookup for: {target_ip}")
    intel = enrich_ip(target_ip)
    print(json.dumps(intel, indent=4))
    
    generate_active_response(target_ip)
