import subprocess
import time
import os


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

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# File containing list of values
values_file = os.path.join(script_dir, 'macd.txt')

# Read values from the file
values = read_values(values_file)

for value in values:
  
   
   
    connect_to_wifi('MIT_Test')  
    time.sleep(5) 
    
    if not ping('amazon.com'):
        # Command to change registry value
        # Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4d36e972-e325-11ce-bfc1-08002be10318}\0003
        # string file with name NetworkAddress
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
