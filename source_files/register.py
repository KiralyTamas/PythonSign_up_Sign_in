import json
import pandas as pd
import os

def reg(user_name,password):
    status=False
    if os.path.exists("database")==False:
        os.mkdir("database")
    if os.path.exists("database/user_datas.json")==False:
        open("database/user_datas.json", "x")
    with open("database/user_datas.json", "r") as file:
        json_data=json.load(file)
        raw_data={'password':password,'status':status}
        json_data['user'][user_name]=raw_data
    with open("database/user_datas.json", "w", newline='',encoding='utf-8') as file:
        json.dump(json_data,file,indent=4)