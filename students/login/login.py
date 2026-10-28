import json
def login():
    email=input("enter your email : ")
    password=input("enter your password : ") 
    try:
        with open("data.json","r") as file:
            data=json.load(file)
        found=False
    
        for i in data:
            if i["email"]==email and i["password"]==password:
                print("-----login succesfull-----")
                found=True
                return
        if not found:
            print("invalid email or password:")
    except Exception as login:
        print("error",login)            
