<<<<<<< HEAD
# SOC Operator CLI Console

A modular command-line security operations dashboard built in Python for mobile/PRoot Linux environments.

## Features
- **Real-Time Telemetry View:** Displays active engine status and unacknowledged threat alert queues using `rich`.
- **Threat Alert Log Viewer:** Color-coded severity triage for simulated network events.
- **Automated Nmap Audit Module:** Wraps Nmap (`-sT -Pn`) for non-root container environments with Fast Sweep and Service/Version (`-sV`) detection profiles, plus automated report exporting.

## Setup & Usage
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 soc_dashboard.py

=======
# Security Automation Toolkit

A collection of lightweight, pure Python security automation and telemetry tools designed to run natively in mobile environments like Termux without external dependencies. Built to support incident response, threat intelligence analysis, network monitoring, and system auditing.

## Command Center Dashboard

The toolkit includes a centralized command-line dashboard (`soc_dashboard.py`) that provides an interactive menu interface to launch individual modules or execute a full automated system audit.

## Included Tools

1. **Incident Triage & Alert Escalation (`incident_triage.py`)**
   - Parses authentication logs, detects brute-force patterns within a sliding time window, and flags high-severity IPs for automated escalation.

2. **Threat Intel Scraper & IOC Extractor (`ioc_extractor.py`)**
   - Extracts Indicators of Compromise (IOCs)—including IPv4 addresses, domains, and SHA-256 hashes—from unstructured threat reports.

3. **Subdomain & Active DNS Enumerator (`subdomain_enum.py`)**
   - Performs rapid DNS resolution lookups against common wordlists to discover active subdomains.

4. **YARA-Style File Signature Evaluator (`yara_evaluator.py`)**
   - Scans files for suspicious code patterns, function calls, and potential backdoor signatures.

5. **Packet Analyzer & Protocol Inspector (`packet_analyzer.py`)**
   - Inspects simulated firewall and packet flow logs to flag unauthorized ports and protocol anomalies.

6. **File Integrity Monitor - FIM (`fim_monitor.py`)**
   - Computes and tracks SHA-256 cryptographic file hashes to detect unauthorized modifications or tampering.

7. **Multi-Threaded TCP Port Scanner (`port_scanner.py`)**
   - Scans target IP addresses across specified ports using concurrent threads for rapid service discovery and banner grabbing.

8. **Centralized Log Aggregator & Parser (`log_aggregator.py`)**
   - Normalizes multi-source logs (auth, web, firewall) into a unified JSON telemetry feed with automated severity scoring.

## Usage

Clone the repository and launch the interactive SOC dashboard:

```bash
git clone [https://github.com/iankapida/Security_tools.git](https://github.com/iankapida/Security_tools.git)
cd Security_tools
python3 soc_dashboard.py
>>>>>>> 285ed65d52e6af15c9c8d900ac8255624baee82d
