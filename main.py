# imported modules and libraries
import argparse
import socket
import sys
import subprocess
import multiprocessing
print(''' _              _              
| |            | |             
| | ___ __ __ _| | _____ _ __  
| |/ / '__/ _` | |/ / _ \ '_ \ 
|   <| | | (_| |   <  __/ | | |
|_|\_\_|  \__,_|_|\_\___|_| |_|
--------------------v1.0-------''')


# scanning the host for ports
def scan_host(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Adjust timeout as needed
    result = sock.connect_ex((host, port))
    if result == 0:
        return port
    sock.close()
# run gobuster
def run_gobuster(host):
    print('running gobuster with common.txt:')
    subprocess.run(["gobuster", "dir", "-u", f"http://{host}", "-w", "/usr/share/wordlists/dirb/common.txt"])
    print('running gobuster with directory-list-2.3-medium.txt:')
    subprocess.run(["gobuster", "dir", "-u", f"http://{host}", "-w", "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"])
# service scan
def run_nmap_service_scan(target):
    cmd = f"nmap -sV {target}"
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Nmap: {e.output}")

# Usage example
target_ip = "192.168.0.1"  # Replace with your target IP address
run_nmap_service_scan(target_ip)

# script arguments
parser = argparse.ArgumentParser(description='Port Scanner')
parser.add_argument('--host', help='Specify the host for port scanning')


args = parser.parse_args()
if args.host:
    print(f"Started a Common Port Scan on host: {args.host}")
    open_ports = []
    for port_no in range(1, 1001):
        port = scan_host(args.host, port_no)
        open_ports.append(port)
    for open_port in open_ports:
        if open_port == 80:
            print(f"Web Server Detected on Port 80 for host {args.host}")
            run_gobuster(args.host)
    print('running nmap service scan on host...')
    run_nmap_service_scan(args.host)
