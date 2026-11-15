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

