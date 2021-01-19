import re
import time
import schedule
from speedtest import Speedtest

from Storage import AddResultsToDataBaseTable
from WiFi import GetNetworkData, GetActiveNetworkName, ConnectTo


def PerformSpeedtest():
    s = Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    return s.results.dict()

def RunTest():
    try:
        for desired_ssid, passwrd in GetNetworkData():
            ConnectTo(desired_ssid, passwrd)
            try:
                data = PerformSpeedtest()
            except Error as e:
                continue
            ssid_raw = GetActiveNetworkName() # Should be same as desired but connection might have failed
            ssid = re.sub(r'\W+', '', ssid_raw)

            results = {}
            results["TIMESTAMP"]     = data["timestamp"]
            results["WIFINAME"]      = ssid
            results["HOSTNAME"]      = data["server"]["host"]
            results["HOSTID"]        = data["server"]["id"]
            results["DOWNLOADSPEED"] = data["download"]
            results["UPLOADSPEED"]   = data["upload"]
            results["LATENCY"]       = data["ping"]

            AddResultsToDataBaseTable(desired_ssid, results)
            print(f"Test on {ssid} successful: DOWNLOADSPEED {results['DOWNLOADSPEED']/1024} KiB/s")
    except Exception as e:
        print("Unforeseen error caught:", e)

def ScheduleAllTests():
    schedule.every(30).minutes.do(RunTest)
    while True:
        schedule.run_pending()
        time.sleep(10)

if __name__ == '__main__':
    ScheduleAllTests()
