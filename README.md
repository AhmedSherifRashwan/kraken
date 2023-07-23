# KraKen

## Port Scanner and Service Detection

This is a simple Python script that performs port scanning on a specified host and then attempts to detect the services running on the open ports using Nmap. Additionally, it runs Gobuster to search for common directories and attempts to retrieve the content of the robots.txt file if found.

## Requirements

To run the script, you need to have the following tools and libraries installed on your system:

- Python 3
- Nmap (Network Mapper) tool
- Gobuster
- requests library (You can install it using `pip install requests`)

## Usage

1. Clone the repository to your local machine using the following command: `git clone <repository_url>`
2. Change into the cloned directory: `cd <repository_name>`
3. Make sure you have the required tools installed (Python 3, Nmap, Gobuster) and the `requests` library.
4. Run the script with the following command: `python port_scanner.py --host <target_host>`

Replace `<target_host>` with the IP address or hostname of the target host you want to scan for open ports and services.

## Script Output

The script will first perform a common port scan on the target host and display the list of open ports, if any are found. If port 80, 8080, or 443 is open, it will run Gobuster to search for common directories on the web server. It will also attempt to retrieve the content of the robots.txt file, if available.

Afterward, it will run an Nmap service scan on the target host to detect the services running on the open ports.

**Note**: Running a port scan or service detection against a target without proper authorization may violate the target's terms of service and local laws. Use this script responsibly and only on systems you own or have explicit permission to scan.

## Credits

This script was created by Ahmed Rashwan (@Rsasec0x01).

---

Please ensure to provide proper attribution if you are using this script or its contents in your projects. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.



