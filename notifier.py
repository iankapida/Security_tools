#!/usr/bin/env python3
import urllib.request
import json
import sys

def send_alert(message, webhook_url):
    """
    Sends a real-time security alert to a Discord webhook or custom endpoint.
    """
    payload = {
        "content": f"🚨 **SOC SECURITY ALERT** 🚨\n{message}"
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={'Content-Type': 'application/json', 'User-Agent': 'SOC-Bot'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status in (200, 204):
                print("[+] Alert successfully dispatched via webhook!")
            else:
                print(f"[-] Warning: Webhook returned status code {response.status}")
    except Exception as e:
        print(f"[-] Failed to send webhook alert: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        if "YOUR_DISCORD_WEBHOOK_URL" in url or not url.startswith("http"):
            print("[-] Error: Please replace placeholder with a valid webhook URL starting with https://")
        else:
            send_alert("Test alert from Termux SOC Toolkit!", url)
    else:
        print("[-] Usage: python3 notifier.py <YOUR_DISCORD_WEBHOOK_URL>")
