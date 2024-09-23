import time

def home():
    homeInput = input("Enter input: ")
    if("./app session" in homeInput):
        appWelcome()
    else:
        print("Welcome to the App!\n")
        print("login: ./'login <username> <password>")

        #code that displays default home menu

def appLogin():
    i = 0
    while i == 0:
        print("Welcome to the app!\n\nlogin: ./'login <username> <password>")
        input1 = input()
        x = input1.split()

        if ("./login" in input1) and (len(x)==3):
            i= 1
            inputUsername = x[1] 
            appWelcome(inputUsername)  
        else:
            print("Invalid input try again\n")

def appLogout():
    print("[you are now logged out\n")
    home()

#def appPeople():

def appWelcome(inputUsername):
    print("Welcome back to the app ",inputUsername,"!\n")
    
def accountCreated(name,username,status,updated):
    print("[account created]\nPerson\n------")
    print("name: ",name,"\nusername: ",username,"\nstatus: ",status,"\nupdated: ",time.ctime())
    


#where main code will be executed         
name = input("Enter your name: ")
print ("Your name is ", name)
home()