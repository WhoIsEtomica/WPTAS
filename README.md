# WPTAS (Wi-Fi Penetration Testing Automation Script)

WPTAS is a Python script designed to automate various steps involved in Wi-Fi penetration testing using tools like `airmon-ng`, `airodump-ng`, `aireplay-ng`, and `aircrack-ng` on Kali Linux.

## Features
- Automatically switches Wi-Fi interface to monitor mode.
- Scans for nearby Wi-Fi networks and captures necessary details.
- Performs deauthentication attacks on specified clients.
- Cracks WPA/WPA2-PSK passwords using a provided wordlist.

## Requirements
- Kali Linux (recommended)
- Python 3.x
- Necessary Wi-Fi adapter capable of monitor mode (e.g., Alfa AWUS036NHA)

## Installation
1. Clone the repository:
   git clone https://github.com/WhoIsEtomica/WPTAS.git
   cd WPTAS

Usage
Ensure your Wi-Fi adapter is plugged in and recognized by Kali Linux.

Run the script as root (administrator):

sudo python wptas.py
Follow the on-screen instructions:

Choose your Wi-Fi adapter and switch it to monitor mode.
Scan for nearby Wi-Fi networks and select your target.
Perform deauthentication attacks on desired clients.
Provide the path to your wordlist file for password cracking.
Monitor the output for progress and results.

Disclaimer
This script is intended for educational and authorized penetration testing purposes only. Misuse of this tool on networks without explicit permission is illegal and unethical. Use it responsibly and at your own risk.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
