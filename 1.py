import subprocess
import time
import os
import re
import platform
import concurrent.futures





def get_network_ip_prefix():
    """
    Extract the network IP prefix from the Wi-Fi (Wireless LAN) connection.
    """
    try:
        # Get the output from the ipconfig command
        result = subprocess.check_output(['ipconfig']).decode()

        # Regex pattern to find the Wi-Fi adapter section and extract the IPv4 address
        wifi_section = re.search(r'Wireless LAN adapter Wi-Fi.*?IPv4 Address.*?:\s*([\d.]+)', result, re.S)
        
        if wifi_section:
            ip_address = wifi_section.group(1)
            # Return the first three octets as the IP prefix
            return '.'.join(ip_address.split('.')[:3])
        else:
            print("No Wi-Fi connection detected.")
            return None
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving IP prefix: {e}")
        return None
    





def send_packets_to_network(network_prefix):
    """
    Sends a ping to every IP in the provided network prefix.
    """
    def send_packet(ip):
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '1', ip]
        subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    ip_range = [f"{network_prefix}.{i}" for i in range(1, 255)]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(send_packet, ip_range)



import re
import subprocess
import platform

def save_dynamic_mac_addresses(ip_prefix, output_file="macd.txt"):
    """
    Extracts dynamic MAC addresses from the ARP table for IP addresses matching the given prefix
    and saves them to a file, skipping IP addresses ending in .1 and .255. 
    Checks if the MAC address already exists in the file, if so, skips it.
    
    Parameters:
    ip_prefix (str): The prefix of the IP addresses to match (e.g., "192.168.1").
    output_file (str): The file to save valid MAC addresses (default is "macd.txt").
    """
    try:
        # Use appropriate command for the platform
        command = ['arp', '-a'] if platform.system().lower() == 'windows' else ['ip', 'neigh']
        arp_output = subprocess.check_output(command).decode()

        # Regex to extract IP addresses and corresponding MAC addresses
        ip_mac_regex = r'((?:\d{1,3}\.){3}\d{1,3})\s.*?((?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2})'
        matches = re.findall(ip_mac_regex, arp_output)

        # Load existing MAC addresses from the file
        existing_macs = set()
        try:
            with open(output_file, "r") as file:
                existing_macs = {line.strip() for line in file}
        except FileNotFoundError:
            pass  # File doesn't exist, so proceed with an empty set

        # Filter MAC addresses by IP prefix and skip .1 and .255 IPs
        valid_mac_addresses = []
        for ip, mac in matches:
            if ip.startswith(ip_prefix) and not (ip.endswith(".1") or ip.endswith(".255")):
                mac_cleaned = mac.replace(":", "").replace("-", "")  # Clean MAC address format
                if mac_cleaned not in existing_macs:  # Check if it's already in the file
                    valid_mac_addresses.append(mac_cleaned)

        # Write valid MAC addresses to the file
        if valid_mac_addresses:  # Only open file if there are new MAC addresses
            with open(output_file, "a") as file:
                for mac in valid_mac_addresses:
                    file.write(f"{mac}\n")

        print(f"MAC addresses for IPs with prefix {ip_prefix}, saved to {output_file}.")
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving MAC addresses: {e}")




print("hi")
network_prefix = get_network_ip_prefix()
print(network_prefix)
send_packets_to_network(network_prefix)
save_dynamic_mac_addresses(network_prefix,"macd.txt")

