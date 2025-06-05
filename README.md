# Simple Python Packet Sniffer

A beginner-friendly Python tool for capturing and analyzing TCP network packets using Scapy.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Ethics & Legal Notice](#ethics--legal-notice)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)
- [What I Learned](#what-i-learned)
- [References](#references)

---

## Project Overview

This project is a simple packet sniffer built in Python using the Scapy library. It captures TCP packets on your local network interface, displays source and destination IP addresses and ports, and flags potential HTTP traffic. The tool is designed for educational purposes and aids beginners in understanding how network traffic can be monitored and analyzed.

---

## Features

- Captures real-time TCP packets
- Displays source/destination IPs and ports with timestamps
- Flags potential HTTP (port 80) traffic
- Lightweight and easy to use
- No sensitive data stored

---

## Installation

1. **Clone the repository:**
   
git clone https://github.com/Bailey7220/basic_packet_sniffer.git

cd sniffer.py


2. **Set up a Python environment (optional but recommended):**

python3 -m venv venv
source venv/bin/activate


3. **Install dependencies:**

pip install scapy

---

## Usage

**Run the script with administrative privileges (required for packet sniffing):**

sudo python3 packet_sniffer.py


**Stop the sniffer at any time with `Ctrl+C`.**



---

## How It Works

- Uses Scapy to sniff TCP packets on the default network interface.
- For each packet, extracts and prints:
  - Timestamp
  - Source and destination IP addresses
  - Source and destination ports
- Flags packets on port 80 as potential HTTP traffic.

---

## Ethics & Legal Notice

**This tool is for educational use only.**  
- Only run it on networks you own or have explicit permission to monitor.
- Do not use this tool to capture or analyze traffic on public or unauthorized networks.
- No sensitive data is stored or logged by this script.

---

## Troubleshooting

- **Permission denied:**  
  Run the script with `sudo` or as an administrator.

- **No output:**  
  - Ensure your network has active TCP traffic.
  - Try running the script on a different interface (see Scapy docs for `iface` parameter).

- **Scapy not found:**  
  - Make sure you installed it with `pip install scapy`.

---

## Future Improvements

- Add packet capture to a log file (with anonymization).
- Expand protocol detection (e.g., DNS, HTTPS, ARP).
- Integrate with a simple web dashboard for real-time monitoring.
- Add automated alerts for suspicious patterns (e.g., port scans, repeated failed logins).

---

## What I Learned

- How to use Scapy for packet sniffing and protocol analysis.
- The risks of unencrypted network traffic.
- The basics of TCP/IP networking and port usage.
- The importance of ethical and legal considerations.

---

## References

- [Scapy Documentation](https://scapy.readthedocs.io/en/latest/)
- [Python.org](https://www.python.org/)
- [Wireshark](https://www.wireshark.org/)

---

