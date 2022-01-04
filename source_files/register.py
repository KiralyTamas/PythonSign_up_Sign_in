import pandas as pd
import os

def reg(name):
    if os.path.exists("database")==False:
        os.mkdir("database")
    if os.path.exists("database/user_datas.json")==False:
        open("database/user_datas.json", "x")
    data = pd.read_json("database/user_datas.json")
    nevek=data['user_name'].values
    for index,row in enumerate(nevek):
        if name in row:
            print(row)
            print(index)
        else:
            continue
        
reg("Minato")