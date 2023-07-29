# imported modules and libraries
import argparse
import concurrent
import socket
import sys
import subprocess
import requests
# --------------------------------
def banner():
    print(''' _              _              
    | |            | |             
    | | ___ __ __ _| | _____ _ __  
    | |/ / '__/ _` | |/ / _ \ '_ \ 
    |   <| | | (_| |   <  __/ | | |
    |_|\_\_|  \__,_|_|\_\___|_| |_|
    --------------------v1.0-------''')
    print('   --> Ahmed Rashwan || @Rsasec0x01')


def test_connection(ip_address):
    try:
        # Test connection to the given IP address on a common port (e.g., HTTP on port 80)
        status = False
        target_port = 80
        timeout = 5  # seconds
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((ip_address, target_port))
        s.close()
        print(f"Connection to {ip_address} on port {target_port} is SUCCESSFUL."), status == True
    except socket.error as e:
        print(f"Connection to {ip_address} on port {target_port} failed: {e}") , status == False
def is_port_open(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set timeout to 1 second for connection attempt
            s.connect((ip, port))
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False
def run_nmap_service_scan(target):
    cmd = f"nmap -sV {target}"
    try:
        output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running Nmap: {e.output}")
def check_robots_txt(target_ip, port):
    # Check if robots.txt exists
    response = requests.get(f"http://{target_ip}:{port}/robots.txt")
    if response.status_code == 200:
        print("robots.txt found! Contents:")
        print(response.text)

port_data = {
    1: "TCP Port Service Multiplexer (TCPMUX)",
    5: "Remote Job Entry (RJE)",
    7: "ECHO",
    18: "Message Send Protocol (MSP)",
    20: "FTP -- Data  -- File Transfer Protocol (FTP): used for uploading and downloading files to and from a server.",
    21: "FTP -- Control -- File Transfer Protocol (FTP): used for uploading and downloading files to and from a server.",
    22: "SSH Remote Login Protocol",
    23: "Telnet",
    25: "Simple Mail Transfer Protocol (SMTP): used for sending emails through a server.",
    29: "MSG ICP",
    37: "Time",
    42: "Host Name Server (Nameserv)",
    43: "WhoIs",
    49: "Login Host Protocol (Login)",
    53: "Domain Name System (DNS): Used for the translation of domain names to the IP addresses they are assigned to, employing the use of Name Servers.",
    69: "Trivial File Transfer Protocol (TFTP)",
    70: "Gopher Services",
    79: "Finger",
    80: "Hyper-Text Transfer Protocol (HTTP): used for (HTML) based web pages, and other types of web site files, such as Active Server Pages (ASP).",
    103: "X.400 Standard",
    108: "SNA Gateway Access Server",
    109: "POP2",
    110: "POP3 Post Office Protocol (POP): Used for receiving emails from a server.",
    115: "Simple File Transfer Protocol (SFTP)",
    118: "SQL Services",
    119: "Newsgroup (NNTP)",
    137: "NetBIOS Name Service Network Basic Input/Output System NetBIOS allows applications on separate computers to communicate over a local area network.",
    143: "Interim Mail Access Protocol (IMAP) Alternate method used for receiving emails from a server, similar to the POP protocol.",
    150: "NetBIOS Session Service",
    156: "SQL Server",
    161: "SNMP",
    179: "Border Gateway Protocol (BGP)",
    190: "Gateway Access Control Protocol (GACP)",
    194: "Internet Relay Chat (IRC)",
    197: "Directory Location Service (DLS)",
    389: "Lightweight Directory Access Protocol (LDAP)",
    396: "Novell Netware over IP",
    443: "HTTPS Secure Socket Layer (SSL): Used for securing and encrypting the connection from a user’s computer to a server in order to protect the packet data being transmitted.",
    444: "Simple Network Paging Protocol (SNPP)",
    445: "Microsoft-DS -- Server Message Block (SMB): Used for Microsoft Windows Networking communication.",
    458: "Apple QuickTime",
    546: "DHCP Client",
    547: "DHCP Server",
    563: "SNEWS",
    569: "MSN",
    587: "Alternate SMTP: Commonly used as a viable alternative to port 25, as some Internet Service Providers choose to block connectivity on port 25.",
    1080: "Socks",
    1167: "Continuous Data Protection (CDP): Used for the R1Soft Backup Agent for processing automated off-site server backups.",
    1443: "Microsoft Structured Query Language Server (SQL Server)",
    2433: "Microsoft Structured Query Language Server (SQL Server): Used for database connectivity between server and client computers",
    3389: "Remote Desktop Protocol (RDP): Used for connecting remotely to a server or client computer via Windows Remote Desktop."
}

if __name__ == "__main__":
    banner()

    # enter target ip and run port scan
    target_ip = input("enter target IP: ")
    # test connection to target IP
    test_connection(target_ip)
    if test_connection(target_ip):
        open_ports = []
        # Test each port from the dictionary and print open ports
        for port, description in port_data.items():
            if is_port_open(target_ip, port):
                open_ports.append((port, description))

        # Print open ports
        if open_ports:
            print("Open ports on", target_ip, ":")
            for port, description in open_ports:
                print(f"Port {port}: {description}")
        else:
            print("No open ports found on", target_ip)

        # run nmap service scan
        print("Running nmap service scan on target IP...")
        run_nmap_service_scan(target_ip)
        # run gobuster
        print("Running gobuster using the Common.txt wordlist...")
        for port, description in open_ports:
            if port == 80:
                # Run gobuster for port 80
                subprocess.run(["gobuster", "dir", "-u", f"http://{target_ip}:{port}", "-w", "/usr/share/wordlists/common.txt"])
                check_robots_txt(target_ip, port)
            elif port == 443:
                # Run gobuster for port 443
                subprocess.run(["gobuster", "dir", "-u", f"https://{target_ip}:{port}", "-w", "/usr/share/wordlists/common.txt"])
                check_robots_txt(target_ip, port)
            elif port == 8080:
                # Run gobuster for port 8080
                subprocess.run(["gobuster", "dir", "-u", f"http://{target_ip}:{port}", "-w", "/usr/share/wordlists/common.txt"])
                check_robots_txt(target_ip, port)
    else:
        print("Ending script")
        sys.exit()
    # --------------------------
