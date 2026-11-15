#!/usr/init/env python3
import os
from datetime import datetime

REPORTS_DIR = "reports"

def generate_report(incident_type, details, severity="HIGH"):
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)
        
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"incident_{timestamp}.md"
    filepath = os.path.join(REPORTS_DIR, filename)
    
    report_content = f"""# 🛡️ SOC Incident Report
- **Timestamp:** {datetime.now()}
- **Incident Type:** {incident_type}
- **Severity Level:** {severity}

## Description & Findings
{details}

## Recommended Actions
1. Isolate the affected asset or IP address.
2. Review raw system logs and correlated alerts.
3. Document post-incident remediation and rule updates.
"""
    
    with open(filepath, "w") as f:
        f.write(report_content)
        
    print(f"[+] Incident report successfully generated: {filepath}")

if __name__ == "__main__":
    import sys
    inc_type = sys.argv[1] if len(sys.argv) > 1 else "File Integrity Violation"
    inc_details = sys.argv[2] if len(sys.argv) > 2 else "Unauthorized modification detected in script file via FIM."
    severity_level = sys.argv[3] if len(sys.argv) > 3 else "HIGH"
    generate_report(inc_type, inc_details, severity_level)
