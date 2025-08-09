import schedule
import time
import csv
import pprint
import handler
from datetime import datetime

# Job execution function
def job():
    if ((d.minute==0)or(d.minute==30))&(d.second==0):
        with open('shuukei.csv',"a") as f:
            now = time.ctime()
            writer = csv.writer(f)
            writer.writerow([time.strftime("%m/%d %H:%M", time.strptime(now)),dict(handler.get_total_number_user())["result"] ,dict(handler.get_total_number_ticket())["result"], dict(handler.get_total_number_entry())["result"], dict(handler.get_total_number_exit())["result"]])
            print("job executed")



if __name__ == "__main__":
    print("counting start")

    while True:
        schedule.run_pending()
        time.sleep(1)
