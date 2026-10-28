import json
def search():
    with open("data.json","r") as file:
        data=json.load(file)
    print("---------welcome student data search----- :")
    print("1. email ")
    print("2. id")
    print("3. name")

    try:
        choice=int(input("enter your choice : "))

    
        # while True:  
        if choice==1:
                email=input("enter your email : ")
                found=False
                for i in data:
                        if i["email"]==email:
                            print(i)
                            found=True
                            break
                if not found:
                            print("not found ")
                        

        elif choice==2:
                id=input("enter your id :")
                found=False
                for i in data:
                        if i["id"]==id:
                            print(i)
                            found=True
                            break
                if not found:
                            print("not found ")
                        
        elif choice==3:
                name=input("enter your name : ")
                found=False
                for i in data:
                        if i["name"]==name:
                            print(i)
                            found=True
                            break
                if not found:
                            print("not found ")
        else:
               print("invalid choice")

    except ValueError:
        print("please enter a valid number")           

    except Exception as search:
        print("error",search)                        
