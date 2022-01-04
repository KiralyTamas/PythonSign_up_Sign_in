import json
import pandas as pd
import os

def reg(user_name,password):
    if os.path.exists("database")==False:
        os.mkdir("database")
    if os.path.exists("database/user_datas.json")==False:
        open("database/user_datas.json", "x")
    status=False
    raw_data={'password':[password],'gyermek':[status]}
    data=pd.DataFrame(raw_data,columns=['password','status'],index=[user_name])
    data.to_json(r'database/user_datas.json',orient='index')
    print("Készen vagyok")

reg("Sasuke","Sakura")