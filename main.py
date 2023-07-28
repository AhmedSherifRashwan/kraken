# imported modules and libraries
import argparse
import concurrent
import socket
import sys
import subprocess
import requests
print(''' _              _              
| |            | |             
| | ___ __ __ _| | _____ _ __  
| |/ / '__/ _` | |/ / _ \ '_ \ 
|   <| | | (_| |   <  __/ | | |
|_|\_\_|  \__,_|_|\_\___|_| |_|
--------------------v1.0-------''')
print('   --> Ahmed Rashwan || @Rsasec0x01')

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
# attempt retrieving content of robots.txt file, if found


# script arguments
parser = argparse.ArgumentParser(description='Port Scanner')
parser.add_argument('--host', help='Specify the host for port scanning')
parser.add_argument('--verbose', help='Enable verbose output')

args = parser.parse_args()
if args.host:
    print('<<<------------Port Scan Info---------------->>>')
    print(f"Started a Common Port Scan on host: {args.host}")
    open_ports = []
    for port_no in range(1, 10000):
        port = scan_host(args.host, port_no)
        open_ports.append(port)
    print('FOUND OPEN PORTS:')
    for i in range(len(open_ports)):
        print(open_ports[i])
    for open_port in open_ports:
        if open_port == 80:
            print(f"Web Server Detected on Port 80 for host {args.host}")
            print('<<<-----------------Gobuster Results---------------->>>')
            subprocess.run(["gobuster", "dir", "-u", f"http://{args.hosts}:80", "-w", "/usr/share/wordlists/dirb/common.txt"])
            subprocess.run(["gobuster", "dir", "-u", f"http://{args.hosts}:80", "-w",
                            "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"])
            print('Attempting to Retrieve Robots.txt file')
            robots_url = f"{args.hosts}/robots.txt"

            # Send a GET request to the URL
            response = requests.get(robots_url)

            if response.status_code == 200:
                print('<<<------------Retrieved Content of Robots.txt File---------------->>>')
                print(response.text)
            else:
                print("No robots.txt file found.")
        elif open_port == 8080:
            print(f"Web Server Detected on Port 8080 for host {args.host}")
            print('<<<-----------------Gobuster Results---------------->>>')
            subprocess.run(["gobuster", "dir", "-u", f"http://{args.hosts}:8080", "-w", "/usr/share/wordlists/dirb/common.txt"])
            subprocess.run(["gobuster", "dir", "-u", f"http://{args.hosts}:8080", "-w",
                            "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"])
            print('Attempting to Retrieve Robots.txt file')
            robots_url = f"{args.hosts}:8080/robots.txt"

            # Send a GET request to the URL
            response = requests.get(robots_url)

            if response.status_code == 200:
                print('<<<------------Retrieved Content of Robots.txt File---------------->>>')
                print(response.text)
            else:
                print("No robots.txt file found.")
    print('<<<-----------------Nmap Service Scan Results---------------->>>')
    print('running nmap service scan on host...')
    run_nmap_service_scan(args.host)