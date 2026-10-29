import json
import uuid
from datetime import datetime


with open("data.json","r+") as file:
    data=json.load(file)
    # print(data)

def signup():
    dic={} 
    
    
    try:
        while True:
            dic["name"]=input("enter your name : ")
            if len(dic["name"])>=3 and dic["name"].isalpha():
                break
            else:
                with open("error.log", "a") as file:
                 file.write(f"[{datetime.now()}] [ERROR] - invalid name - {dic['name']}\n")
                
            print("invalid name")
    except Exception as name:
        print("error",name)


    dic["studentsid"] = uuid.uuid4().hex[:4]
    print("Student UUID:", dic["studentsid"])
        


    try:        
        while True:
            dic["id"]=input("enter your id : ")
            if len(dic["id"])<5 and dic["id"].isdigit():
                break
            else:
                with open("error.log", "a") as file:
                    file.write(f"[{datetime.now()}] [ERROR] - invalid id - {dic['id']}\n")
                print("invalid id")
    except Exception as id:
        print("error",id)

    try:
        while True:
            dic["age"]=input("enter your age  :")
            if len(dic["age"])>0 and dic["age"].isdigit():
                break        
            else:
                with open("error.log", "a") as file:
                    file.write(f"[{datetime.now()}] [ERROR] - invalid age - {dic['age']}\n")
                print("not exist age")
    except Exception as age:
        print("error",age)



    qul=int(input("enter how many qualification :-"))
    dic["qualification"]=[]
    for i in range(qul):
        q=input("enter qualification :-") 
        dic["qualification"].append(q)
        print(dic["qualification"])


    try:
        while True:
            dic["email"]=input("enter your email : ")
            if "@"  in dic["email"] and  dic["email"].endswith(".com"):
                break
            else:
                with open("error.log", "a") as file:
                    file.write(f"[{datetime.now()}] [ERROR] - invalid email - {dic['email']}\n")
                print("invalid amail") 
    except Exception as email:
        print("error",email)

          
    try:
        while True:
            dic["password"]=input("enter your password : ")
            if len(dic["password"])>=4 and dic["password"].isdigit():
                break
            else:
                with open("error.log", "a") as file:
                    file.write(f"[{datetime.now()}] [ERROR] - invalid password - {dic['password']}\n")
                print("incorrect password , please try again") 
    except Exception as password:
        print("error",password) 
        return           

    dic["signup_time"] = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    now = datetime.now()
    print(now)
    data.append(dic)

    
    with open ("data.json","w") as file:
            
        json.dump(data,file,indent=4)

    print("----signup successfully---- ")
    # print(dic)
