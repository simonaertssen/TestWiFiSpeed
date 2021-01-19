import os

def GetNetworkData():
    files_to_open = os.listdir("path/to/directory")
    with open("WiFi Network Data/password.txt", 'r') as filereader:
def GetPassword():
    with open("WiFi Network Data/password.txt", 'r') as filereader:
        print(filereader.read())


def GetActiveWiFiNetworkName():
    subprocess_result = subprocess.Popen("/Sy*/L*/Priv*/Apple8*/V*/C*/R*/airport -I | awk '/ SSID:/ {print $2}'",shell=True,stdout=subprocess.PIPE)
    subprocess_output = subprocess_result.communicate()[0],subprocess_result.returncode
    return subprocess_output[0].decode('utf-8')

# def Connect()
#
#     command = """sudo iwlist wlp2s0 scan | grep -ioE 'ssid:"(.*{}.*)'"""
#     result = os.popen(command.format(self.server_name))
#     result = list(result)


if __name__ == '__main__':
    GetPassword()
