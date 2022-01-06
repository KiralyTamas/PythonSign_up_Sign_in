import os
import json

def log_in(user_name,password):
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
                return print("Üdvözöllek :)")
        elif user_name not in users:
            return print("Nincs ilyen felhasználó") 
        
log_in("Naruto","Hinata")