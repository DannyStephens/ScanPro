import subprocess
import os
import sys
from datetime import datetime


def run_nmap(ip):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = "scan_results"
    os.makedirs(out_dir, exist_ok=True)
    outfile = os.path.join(out_dir, f"nmap_{ip}_{timestamp}.txt")

    print(f"[*] Running Nmap scan on {ip}...")

    cmd = ["nmap", "-sS", "-sV", "-O", "-Pn", ip]

    with open(outfile, "w") as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT)

    print(f"[+] Scan complete. Output saved to: {outfile}")


def main():
    if len(sys.argv) != 2:
        print("INCORRECT INPUT. Corrected Input: python3 scanpro.py <IP_OR_DOMAIN>")
        sys.exit(1)

    target = sys.argv[1].strip()
    run_nmap(target)

if __name__ == "__main__":
    main()

