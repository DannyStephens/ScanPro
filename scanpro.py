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

    print(f"[+] Nmap scan complete. Output saved to: {outfile}")

def run_ffuf(ip):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = "scan_results"
    os.makedirs(out_dir, exist_ok=True)
    outfile = os.path.join(out_dir, f"ffuf_{ip}_{timestamp}.txt")

    print(f"[*] Running FFUF scan on {ip}...")

    wordlist = "/usr/share/dirb/wordlists/common.txt "

    cmd = [
        "ffuf", "-u", f"http://{ip}/FUZZ", "-w", wordlist, "-t", "50", "-o", outfile
    ]

    with open(outfile, "w") as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT)

    print(f"[+] FFUF scan complete. Output saved to: {outfile}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scanpro.py <IP_OR_DOMAIN>")
        sys.exit(1)

    target = sys.argv[1].strip()
    
    run_nmap(target)
    
    print("[*] Checking if the target has HTTP(S) services...")
    run_ffuf(target)

if __name__ == "__main__":
    main()

