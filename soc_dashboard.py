import subprocess
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

THREAT_LOGS = [
    {"time": "21:10:04", "severity": "HIGH", "source": "185.220.101.4", "event": "SSH Brute Force Attempt"},
    {"time": "21:14:22", "severity": "MEDIUM", "source": "192.168.1.45", "event": "Unusual Outbound Port 4444"},
    {"time": "21:22:19", "severity": "LOW", "source": "10.0.0.12", "event": "Port Sweep Detected"},
]

def show_header():
    console.clear()
    console.print(Panel(
        "[bold cyan]SOC Operator CLI Console v3.0[/bold cyan]",
        subtitle=f"Ubuntu PRoot | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    ))

def view_status():
    table = Table(title="System & Threat Telemetry")
    table.add_column("Metric", style="magenta")
    table.add_column("Status", style="green")
    table.add_column("Details", style="yellow")

    table.add_row("IDS / Filter Engine", "[bold green]ONLINE[/bold green]", "Monitoring active interfaces")
    table.add_row("Anomaly Scoring", "[bold yellow]ACTIVE[/bold yellow]", "Threshold: 85/100")
    table.add_row("Active Alerts", f"[bold red]{len(THREAT_LOGS)}[/bold red]", "Unacknowledged events in queue")
    table.add_row("Environment", "Ubuntu PRoot", "Isolated Python venv active")

    console.print(table)

def view_logs():
    table = Table(title="Recent Threat Alerts")
    table.add_column("Time", style="cyan")
    table.add_column("Severity", style="bold")
    table.add_column("Source IP", style="yellow")
    table.add_column("Event Description", style="white")

    for log in THREAT_LOGS:
        sev_color = "red" if log["severity"] == "HIGH" else ("yellow" if log["severity"] == "MEDIUM" else "green")
        table.add_row(log["time"], f"[{sev_color}]{log['severity']}[/{sev_color}]", log["source"], log["event"])

    console.print(table)

def run_scan_module():
    target = Prompt.ask("\n[bold cyan]Enter target IP or domain[/bold cyan]", default="scanme.nmap.org")
    console.print("\n[bold]Select Scan Profile:[/bold]")
    console.print("  [cyan][1][/cyan] Fast Top-100 Port Sweep (-sT -Pn -F)")
    console.print("  [cyan][2][/cyan] Service & Version Audit (-sT -Pn -sV -p 21,22,80,443)")
    
    profile = Prompt.ask("Profile", choices=["1", "2"], default="2")
    
    if profile == "1":
        cmd = ["nmap", "-sT", "-Pn", "-F", target]
        scan_name = "Fast Sweep"
    else:
        cmd = ["nmap", "-sT", "-Pn", "-sV", "-p", "21,22,80,443", target]
        scan_name = "Service Version Audit"

    console.print(f"\n[dim]Executing: {' '.join(cmd)} ...[/dim]\n")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=45)
        output = result.stdout.strip() or "No output returned."
        console.print(Panel(output, title=f"{scan_name}: {target}", border_style="green"))
        
        save = Prompt.ask("\n[cyan]Save scan report to file?[/cyan]", choices=["y", "n"], default="y")
        if save == "y":
            filename = f"scan_{target.replace('.', '_')}_{datetime.now().strftime('%H%M%S')}.txt"
            with open(filename, "w") as f:
                f.write(output)
            console.print(f"[bold green]Saved report to {filename}[/bold green]")
            
    except Exception as e:
        console.print(f"[bold red]Scan failed:[/bold red] {e}")

def main():
    while True:
        show_header()
        view_status()
        console.print("\n[bold]Operator Actions:[/bold]")
        console.print("  [cyan][1][/cyan] View Threat Alert Logs")
        console.print("  [cyan][2][/cyan] Run Nmap Audit Module")
        console.print("  [cyan][3][/cyan] Refresh Telemetry")
        console.print("  [cyan][0][/cyan] Exit Console\n")

        choice = Prompt.ask("Select an option", choices=["1", "2", "3", "0"], default="2")

        if choice == "1":
            show_header()
            view_logs()
            Prompt.ask("\n[dim]Press Enter to return to main menu[/dim]")
        elif choice == "2":
            run_scan_module()
            Prompt.ask("\n[dim]Press Enter to return to main menu[/dim]")
        elif choice == "3":
            continue
        elif choice == "0":
            console.print("[bold green]Session closed. Stay secure![/bold green]")
            break

if __name__ == "__main__":
    main()
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
