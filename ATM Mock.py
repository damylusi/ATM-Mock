from datetime import datetime
import random


# Initailizing the System


dataBase = {}

now = datetime.now()
currentdate = now.strftime("%d of %m, %y.")
currenttime = now.strftime("%H:%M:%S")

def generatedaccountno():
    return random.randrange(1111111111, 9999999999)


def login():
    print("Login here \n")
    
    accountNumberFromUser = int(input("Your account number: \n"))
    password = input("Your Password \n")
   
    for accountNumber, userdetails in dataBase.items():
        if(accountNumber == accountNumberFromUser):
            if(userdetails[3] == password):
                bankOperations(userdetails)
                isLoginSuccessful = True
            else:
                print("\nInvalid account or Password")
                login()
        else:
            print("\nInvalid account or Password")
            login()



def bankOperations(user):

    print (f" Welcome %s , You logged in on the {currentdate} {currenttime} \n" %user[1])
    Selectedoption =  int(input("What do you want to do? (1) Withdrawal (2) Deposit (3)Complaint (4)Logout \n"))
    if (Selectedoption == 1):
        Withdrawal()
    elif (Selectedoption == 2):
        Deposit()
    elif (Selectedoption == 3):
        Complaint()
    elif (Selectedoption == 4):
        Logout()
    else:
        print("Invalid Option")
        bankOperations()


def init():
    
    isValidOptionSelected = False
    print("Welcome to Zenith Bank")

    while isValidOptionSelected == False:

        haveAccount = int(input("Do you have account with us: 1 (Yes) 2 (no)"))
    
        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            print(register())
        else:
            print("You have selected invalid option")


def register():

    print("REGISTER HERE")
    first_name = input("Enter your first name: \n")
    last_name = input("Enter your last name: \n")
    email = input("Enter your Email Address: \n")
    password = input("Create password: \n")
    
    accountNumber = generatedaccountno()

    print("Your account has been created successfully")
    print("*****************")
    print("Your account number is: ",  accountNumber)
    print("Keep it Safe, especially your password \n")
    dataBase[accountNumber] = [first_name, last_name, email, password]    
    login()



def Withdrawal():
    money = input("How much would you like to withdraw: \n")
    print("take your cash")
    done()

def Deposit():
    Deposit = input("How much would you like to deposit: \n")
    print("Transaction Successful..")
    print('Your current balance is:  %s '%Deposit)
    done()

def Complaint():
    Complaint = input("What issue will you like to report?: \n")
    print("Thank you for contacting us.")
    done()

def done():
    print("\nHello, would you like to do make another transaction or logout. \n")
    choose = int(input("Press 1 to continue\nPress 2 to logout\n"))    
    if (choose == 1):
        select = int(input("Welcome \n 1. Withdrawal \n 2. Deposit \n 3. Complaint\n"))
        if (select == 1):
            withdrawal()
        elif (select == 2):
            Deposit()
        elif (select == 3):
            Complaint
        else:
            print("Invalid Option")
            done()
    elif (choose == 2):
        print("Thank you for banking with us")
        logout()
    else:
        print("Invalid")
        done()

def logout():
    login()
    
def exit():
    exit()

init()
register()
login()
bankOperations()
        



