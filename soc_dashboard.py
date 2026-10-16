#!/usr/bin/env python3
import os
import sys
import subprocess

def clear_screen():
    os.system('clear')

def show_banner():
    print("=" * 60)
    print("      SOC ANALYST COMMAND CENTER - SECURITY TOOLKIT")
    print("=" * 60)

def main_menu():
    while True:
        clear_screen()
        show_banner()
        print("\nSelect a security automation module to execute:\n")
        print("  [1] Automated Incident Triage & Alert Escalation")
        print("  [2] Threat Intel Scraper & IOC Extractor")
        print("  [3] Subdomain & Active DNS Enumerator")
        print("  [4] YARA-Style File Signature Evaluator")
        print("  [5] Packet Analyzer & Protocol Inspector")
        print("  [6] File Integrity Monitor (FIM)")
        print("  [7] Multi-Threaded TCP Port Scanner")
        print("  [8] Centralized Log Aggregator & Parser")
        print("  [9] Run Full Automated System Audit (All Tools)")
        print("  [0] Exit Console\n")

        choice = input("Select an option [0-9]: ").strip()

        tools = {
            "1": "incident_triage.py",
            "2": "ioc_extractor.py",
            "3": "subdomain_enum.py",
            "4": "yara_evaluator.py",
            "5": "packet_analyzer.py",
            "6": "fim_monitor.py",
            "7": "port_scanner.py",
            "8": "log_aggregator.py"
        }

        if choice in tools:
            run_script(tools[choice])
        elif choice == "9":
            run_all(tools)
        elif choice == "0":
            print("\nExiting SOC Dashboard. Stay secure!")
            sys.exit(0)
        else:
            input("\n[!] Invalid selection. Press Enter to try again...")

def run_script(script_name):
    clear_screen()
    print(f"[*] Executing Module: {script_name}")
    print("-" * 60 + "\n")
    if os.path.exists(script_name):
        subprocess.run([sys.executable, script_name])
    else:
        print(f"[-] Error: {script_name} not found in current directory.")
    print("\n" + "-" * 60)
    input("\n[+] Execution complete. Press Enter to return to main menu...")

def run_all(tools):
    clear_screen()
    print("[*] Initiating Full System Security Audit...")
    print("=" * 60 + "\n")
    for key, script in tools.items():
        print(f"\n---> Running [{key}] {script}")
        print("-" * 40)
        if os.path.exists(script):
            subprocess.run([sys.executable, script])
        else:
            print(f"[-] Missing script: {script}")
    print("\n" + "=" * 60)
    input("\n[+] Full audit cycle finished. Press Enter to return to main menu...")

if __name__ == '__main__':
    main_menu()
