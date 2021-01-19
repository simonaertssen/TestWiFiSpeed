import time
import schedule
from speedtest import Speedtest

def PerformSpeedtest():
    s = Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    return s.results.timestamp, s.results.download, s.results.upload, s.results.ping

def GetWiFiNetworkName():
    subprocess_result = subprocess.Popen("/Sy*/L*/Priv*/Apple8*/V*/C*/R*/airport -I | awk '/ SSID:/ {print $2}'",shell=True,stdout=subprocess.PIPE)
    subprocess_output = subprocess_result.communicate()[0],subprocess_result.returncode
    return subprocess_output[0].decode('utf-8')

def TestSchedule():
    print("Testing Schedule")

if __name__ == '__main__':
    PerformSpeedtest()
    # schedule.every(1).seconds.do(TestSchedule)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(0.1)
