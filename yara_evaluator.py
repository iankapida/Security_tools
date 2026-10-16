#!/usr/bin/env python3
import os

YARA_RULES = {
    "Suspicious_Exec": [b"os.system(", b"subprocess.Popen(", b"eval("]
}

if __name__ == '__main__':
    test_target = "test_script.py"
    with open(test_target, "w") as f:
        f.write("import os\nos.system('echo test')\n")

    with open(test_target, "rb") as f:
        content = f.read()

    for rule, sigs in YARA_RULES.items():
        if any(s in content for s in sigs):
            print(f"[!] RULE MATCH: {rule}")
    os.remove(test_target)
