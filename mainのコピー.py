import os
import re
import csv
import pprint
import time

import handler
shuukei={'aaaastart': 1}
if False:
    with open('shuukei.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        print(l)
    with open('shuukei.csv',"a") as f:
        now = time.ctime()
        writer = csv.writer(f)
        writer.writerow([time.strftime("%H:%M", time.strptime(now)),dict(handler.get_total_number_user())["result"] ,dict(handler.get_total_number_ticket())["result"], dict(handler.get_total_number_entry())["result"], dict(handler.get_total_number_exit())["result"]])
elif False:
    with open('shuukei.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        print(str(int(l[-1][1])-int(l[-2][1])))
else:
    shuukei["aaab"+"start"]=dict(handler.get_total_number_entry())["result"]
    print(shuukei)
    print(dict(handler.get_total_number_entry())["result"]-shuukei["aaaa"+"start"])
