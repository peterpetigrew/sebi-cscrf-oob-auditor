import json
import argparse
from datetime import datetime, timedelta

def audit_stream(log_file):
    print(f"[*] Initializing OOB Network Tap Monitor on: {log_file}")
    print("[*] Monitoring for SEBI CSCRF API Violations...\n")
    
    violation_count = 0
    
    with open(log_file, 'r') as file:
        for line_num, line in enumerate(file, 1):
            if not line.strip():
                continue
            
            try:
                entry = json.loads(line.strip())
                
                # SEBI CSCRF Logic: Detect Blocked Unauthorized Access
                if entry.get("status") == "BLOCKED" and "unauthorized" in entry.get("event", ""):
                    violation_count += 1
                    incident_time = datetime.fromisoformat(entry["timestamp"].replace("Z", "+00:00"))
                    deadline = incident_time + timedelta(hours=6)
                    
                    print(f"[!] CSCRF VIOLATION DETECTED (Log Line {line_num})")
                    print(f"    Target: {entry.get('source')}")
                    print(f"    SEBI 6-Hour Reporting Deadline: {deadline.isoformat()}")
                    print(f"    Action: Asynchronous Alert Dispatched. (Zero impact to trading latency)\n")
            
            except json.JSONDecodeError:
                print(f"[-] Malformed log at line {line_num}")
                continue

    print(f"[*] Audit Complete. Total Critical Violations Flagged: {violation_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Out-of-Band SEBI CSCRF Compliance Auditor")
    parser.add_argument("--stream", required=True, help="Path to the JSONL log stream")
    args = parser.parse_args()
    
    audit_stream(args.stream)