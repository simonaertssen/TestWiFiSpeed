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
        try:
            file_to_open = os.path.join(directory, file_name)
            with open(file_to_open, 'r') as filereader:
                network_names.append(file_name.rstrip("\n"))
                passwords.append(filereader.readline().rstrip("\n"))
        except Error as e:
            print(f"Error opening {file_name}:", e)
    return network_names, passwords

def GetActiveNetworkName():
    active_network_name = ""
    try:
        subprocess_result = subprocess.Popen("/Sy*/L*/Priv*/Apple8*/V*/C*/R*/airport -I | awk '/ SSID:/ {print $2}'",shell=True,stdout=subprocess.PIPE)
        subprocess_output = subprocess_result.communicate()[0],subprocess_result.returncode
        active_network_name = subprocess_output[0].decode('utf-8')
    except Error as e:
        print("Could not get current network name:", e)
    finally:
        return active_network_name

def ConnectTo(ssid, passphrase):
    command_on = "networksetup -setairportpower en0 on"
    subprocess_result = subprocess.Popen(command_on,shell=True,stdout=subprocess.PIPE)
    command_conn = f"networksetup -setairportnetwork en0 {ssid} {passphrase}"
    subprocess_result = subprocess.Popen(command_conn,shell=True,stdout=subprocess.PIPE)
    time.sleep(30)  # Wait for connection to be established:
    print(f"Connected to {GetActiveNetworkName()}..")

if __name__ == '__main__':
    for ssid, passwrd in GetNetworkData():
        ConnectTo(ssid, passwrd)
