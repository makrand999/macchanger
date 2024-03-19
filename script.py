import subprocess
import time

# Function to check if ping is successful
def ping(host):
    return subprocess.call(['ping', '-n', '1', host], stdout=subprocess.PIPE) == 0

# Function to read values from a text file
def read_values(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Function to connect to a Wi-Fi network
def connect_to_wifi(ssid):
    subprocess.call(['netsh', 'wlan', 'connect', 'name=', ssid])

# File containing list of values
values_file = r'C:\Users\makar\Desktop\mac\macd.txt'

# Read values from the file
values = read_values(values_file)

# Try each value until ping to amazon.com succeeds
for value in values:
    # Connect to the Wi-Fi network MIT_TEST (replace with the actual SSID)
   # Wait for a few seconds for the connection to establish
   
   
    connect_to_wifi('MIT_Test')  # Replace 'MIT_TEST' with the actual SSID of the Wi-Fi network
    time.sleep(5) 
    
    if not ping('amazon.com'):
        # Command to change registry value
        reg_command = f'reg add "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4d36e972-e325-11ce-bfc1-08002be10318}}\\0003" /v NetworkAddress /t REG_SZ /d "{value}" /f'
        # Execute registry command
        subprocess.call(reg_command, shell=True)
        # Disable and enable Wi-Fi interface
        subprocess.call('netsh interface set interface "Wi-Fi" disable', shell=True)
        subprocess.call('netsh interface set interface "Wi-Fi" enable', shell=True)
        print(f'changed to {value}')
    else:
        print(f'Ping to amazon.com successful with value: {value}')
        break
else:
    print('All values tried but unable to ping amazon.com.')
