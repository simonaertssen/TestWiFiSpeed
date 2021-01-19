import time
import schedule
from speedtest import Speedtest

def PerformSpeedtest():
    s = Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    return s.results.timestamp,
           s.results.download,
           s.results.upload,
           s.results.ping

def TestSchedule():
    print("Testing Schedule")

if __name__ == '__main__':
    PerformSpeedtest()
    # schedule.every(1).seconds.do(TestSchedule)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(0.1)
