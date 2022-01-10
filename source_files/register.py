import json
import os
import datetime

def reg(user_name,password):
    reg_time=datetime.datetime.now().strftime("%Y-%m-%d %X")
    status=False
    if os.path.exists("database")==False:
        os.mkdir("database")
    if os.path.exists("database/user_datas.json")==False:
        open("database/user_datas.json", "x")
    with open("database/user_datas.json", "r") as file:
        json_data=json.load(file)
        for i in json_data['user']:
            if user_name == i:
                return print("Már van ilyen felhasználó")
        raw_data={'password':password,'status':status}
        json_data['user'][user_name]=raw_data
        json_data['user'][user_name]['log_in_time']=reg_time
    with open("database/user_datas.json", "w", newline='',encoding='utf-8') as file:
        json.dump(json_data,file,indent=4)
    return ("Felhasználó Regisztrálva")