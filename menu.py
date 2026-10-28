from students.signup.signup import signup
from students.login.login import login
from students.search.search import search



def menu():
    try:        
        while True:
            print("======== menu =========")
            print("1. signup")
            print("2. login")
            print("3. search")
            print("4. exit")
            choice=int(input("enter your choice :"))           
            if choice==1:
                signup()    
            elif choice==2:
                login()
            elif choice==3:
                search()
            elif choice==4:
                print("exit")  
                break
            else:
                print("not exist")   

    # except ValueError:
    #     print("please enter a valid number")

    except Exception as menu:
        print("error",menu)
menu()        
