#!/usr/bin/env python3
import os

def load_env(env_path=".env"):
    """
    Lightweight native .env configuration loader 
    without requiring external python packages like python-dotenv.
    """
    if not os.path.exists(env_path):
        print(f"[-] Warning: {env_path} file not found. Copy .env.example to .env to configure secrets.")
        return False
        
    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, val = line.split("=", 1)
                os.environ[key.strip()] = val.strip()
    return True

if __name__ == "__main__":
    if load_env():
        print("[+] Environment variables loaded securely from .env")
        webhook = os.getenv("DISCORD_WEBHOOK_URL", "Not Configured")
        print(f"[*] Loaded Webhook target prefix: {webhook[:30]}...")
    else:
        # Create a local default .env for testing
        with open(".env", "w") as f:
            f.write("DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/TEST/TEST\n")
        print("[+] Created default local .env file for testing.")
        load_env()
