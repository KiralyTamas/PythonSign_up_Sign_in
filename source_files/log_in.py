import json
import datetime

def log(user_name,password):
    with open("database/user_datas.json", "r") as file:
        json_data=json.load(file)
        users=[]
        for i in json_data['user']:
            users.append(i)
        if (user_name in users) and (json_data['user'][user_name]['password'] != password):
            return print("Rosszúl adtad meg a jelszavad!")
        elif  (user_name in users) and (json_data['user'][user_name]['password'] == password):
            if json_data['user'][user_name]['status']==True:
                return print("Már be vagy jelentkezve")
            else:
                json_data['user'][user_name]['status']=True
                time=datetime.datetime.now()
                json_data['user'][user_name]['log_in_time']=time.strftime("%Y-%m-%d %X")
                with open("database/user_datas.json","w",newline='',encoding='utf-8')as new_file:
                    json.dump(json_data, new_file,indent=4)
                return print(f"Üdvözöllek {user_name}")
        elif user_name not in users:
            return print("Nincs ilyen felhasználó") 