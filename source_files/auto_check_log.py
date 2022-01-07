import json
import time as tm
from datetime import datetime

def auto():
    with open("database/user_datas.json", "r") as file:
        users_name = []
        present=tm.time()
        jfile = json.load(file)
        for i in jfile['user']:
            users_name.append(i)
        for j in users_name:
            log_date = datetime.strptime(jfile['user'][j]['log_in_time'], "%Y-%m-%d %H:%M:%S")
            log_date_stamp=datetime.timestamp(log_date)
            last_log_in=int((present-log_date_stamp)/60)
            print(last_log_in)
            if last_log_in >= 30:
                jfile['user'][j]['status']=False
    with open("database/user_datas.json", "w",newline='',encoding='utf-8') as file:
        json.dump(jfile, file,indent=4)

auto()
