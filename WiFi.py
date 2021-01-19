import os
import time
import subprocess


def GetNetworkData():
    directory = "WiFi Network Data"
    network_names = []
    passwords = []
    for file_name in os.listdir("WiFi Network Data"):
        if file_name == '.DS_Store':
            continue
        file_to_open = os.path.join(directory, file_name)
        with open(file_to_open, 'r') as filereader:
            network_names.append(filereader.readline().strip())
            passwords.append(filereader.readline().strip())
    return network_names, passwords

def GetActiveNetworkName():
    subprocess_result = subprocess.Popen("/Sy*/L*/Priv*/Apple8*/V*/C*/R*/airport -I | awk '/ SSID:/ {print $2}'",shell=True,stdout=subprocess.PIPE)
    subprocess_output = subprocess_result.communicate()[0],subprocess_result.returncode
    return subprocess_output[0].decode('utf-8')

def ConnectTo(ssid, passphrase):
    command_on = "networksetup -setairportpower en0 on"
    subprocess_result = subprocess.Popen(command_on,shell=True,stdout=subprocess.PIPE)
    command_conn = f"networksetup -setairportnetwork en0 {ssid} {passphrase}"
    subprocess_result = subprocess.Popen(command_conn,shell=True,stdout=subprocess.PIPE)
    time.sleep(20)  # Wait for connection to be established:
    print(f"Connected to {ssid}")

if __name__ == '__main__':
    for ssid, passwrd in GetNetworkData():
        ConnectTo(ssid, passwrd)
