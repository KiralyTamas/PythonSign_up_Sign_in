import time

date1="2022 1 7 12:20:00"
date2="2022 1 7 12:55:00"
boj1=time.strptime(date1, "%Y %m %d %H:%M:%S" )
boj2=time.strptime(date2, "%Y %m %d %H:%M:%S" )
time1=time.mktime(boj1)
time2=time.mktime(boj2)
minute=time2-time1
print(int(minute/60))