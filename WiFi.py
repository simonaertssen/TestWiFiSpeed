import os

def GetNetworkData():
    directory = "WiFi Network Data"
    network_names = []
    passwords = []
    for file_name in os.listdir("WiFi Network Data"):
        file_to_open = os.path.join(directory, file_name)
        with open(file_to_open, 'r') as filereader:
            network_names.append(filereader.readline().strip())
            passwords.append(filereader.readline().strip())
    return network_names, passwords


def GetActiveNetworkName():
    subprocess_result = subprocess.Popen("/Sy*/L*/Priv*/Apple8*/V*/C*/R*/airport -I | awk '/ SSID:/ {print $2}'",shell=True,stdout=subprocess.PIPE)
    subprocess_output = subprocess_result.communicate()[0],subprocess_result.returncode
    return subprocess_output[0].decode('utf-8')

def Connect()
    command = """sudo iwlist wlp2s0 scan | grep -ioE 'ssid:"(.*{}.*)'"""
    result = os.popen(command.format(self.server_name))
    result = list(result)


if __name__ == '__main__':
    print(GetNetworkData())
