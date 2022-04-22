import os
import time
import pyfiglet as big
import mysql.connector

class CB:
        def progressBar(self,iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
            """
            Call in a loop to create terminal progress bar
            @params:
                iterable    - Required  :  iterable object (Iterable)
                prefix      - Optional  : prefix string (Str)
                suffix      - Optional  : suffix string (Str)
                decimals    - Optional  : positive number of decimals in percent complete (Int)
                length      - Optional  : character length of bar (Int)
                fill        - Optional  : bar fill character (Str)
                printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
            """
            total = len(iterable)
            # Progress Bar Printing Function
            def printProgressBar (iteration):
                percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
                filledLength = int(length * iteration // total)
                bar = fill * filledLength + '-' * (length - filledLength)
                print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
            # Initial Call
            printProgressBar(0)
            # Update Progress Bar
            for i, item in enumerate(iterable):
                yield item
                printProgressBar(i + 1)
            # Print New Line on Complete
            print()

class DB:
    my_db=None
    host = "localhost"
    port  = 3306
    db_Cursor=None
    def Connect(self):
        try:
            self.my_db = mysql.connector.connect(host=self.host,user=self.user,password=self.password,port  = self.port)
            # print(self.my_db)
            self.db_Cursor=self.my_db.cursor()
            data_name="Contact"
            self.db_Cursor.execute("CREATE SCHEMA IF NOT EXISTS {}".format(data_name))
            self.db_Cursor.execute("CREATE TABLE IF NOT EXISTS contact.contact(ID int NOT NULL AUTO_INCREMENT,First_Name varchar(100),Middle_Name varchar(100),Last_Name varchar(100),Nickname varchar(100),Mobile_Number varchar(100),Work_Number varchar(100),Company varchar(100),Birthday varchar(100),Address varchar(100),PRIMARY KEY (ID))")
            return 0
        except:
            return -1
    def Fire(self,Sql,Data):
        self.db_Cursor.execute(Sql, Data)
        self.my_db.commit()
        return self.db_Cursor.rowcount

data =DB()
result = None
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def Log_out():
    clear()
    result = big.figlet_format("LOGING-OUT", font="slant")
    print(result)
    pb=CB()
    # A List of Items
    items = list(range(0, 57))
    # A Nicer, Single-Call Usage
    for item in pb.progressBar(items, prefix = 'Progress:', suffix = 'Complete', length = 50):
        # Do stuff...
        time.sleep(0.1)
    
    clear()
    time.sleep(3)
    result = big.figlet_format("LOG-OFF", font="slant")
    print(result)
    input("Press Any Key...")

def Exit_():
    clear()
    result = big.figlet_format("EXITING", font="slant")
    print(result)
    pb=CB()
    # A List of Items
    items = list(range(0, 57))
    # A Nicer, Single-Call Usage
    for item in pb.progressBar(items, prefix = 'Progress:', suffix = 'Complete', length = 50):
        # Do stuff...
        time.sleep(0.1)
    clear()
    time.sleep(3)
    result = big.figlet_format("Done...", font="slant")
    print(result)
    input("Press Any Key...")
    os._exit(0)

def Start():
    clear()
    while True : 
        try:
            result = big.figlet_format("Contact Book", font="slant")
            print(result)
            print("01.For Connecting Local-Host Database")
            print("02.For Connecting Internet Database")
            x = int(input("Enter any one option :- ")) 
            if x == 1:
                local_Host()
                break
            elif x==2:
                via_Internet()
            else:
                clear()
                result = big.figlet_format("Opp's ! ", font="slant")
                print(result)
                input()
                clear()
        except ValueError:
            clear()
            result = big.figlet_format("INVALID INPUT", font="slant")
            print(result)
            input()
            clear()

def main():
    clear()
    result = big.figlet_format("WELCOME", font="slant")
    print(result)
    print("Press Any Key....")
    input()
    Start()
   

def main_menu():
    while True:
        try:
            clear()
            result = big.figlet_format("Main Menu", font="slant")
            print(result)
            print("01.Show All Contact")
            print("02.Add New Contact")
            print("03.Update Contact")
            print("04.Delete Contact")
            print("05.Search Contact")
            print("06.Log-Out")
            print("07.Log-Out and Exit")
            x = int(input("Enter any one option :- "))
            if x==1:
                pass
            elif x == 2:
                AddScreen()
                break
            elif x==3:
                pass
            elif x == 3:
                pass
            elif x == 4:
                pass
            elif x == 5:
                pass
            elif x == 6:
                Log_out()
                Start()
                break
            elif x == 7:
                Log_out()
                Exit_()
                break    
            else:
                clear()
                result = big.figlet_format("Opp's ! ", font="slant")
                print(result) 
                input()
                clear()         
        except:
            clear()
            result = big.figlet_format("INVALID INPUT", font="slant")
            print(result)
            input()
            clear()



def via_Internet():
    clear()
    result = big.figlet_format("INTERNET DATABASE", font="slant")
    print(result)
    ip=input("Enter Database IP:-")
    port = input("Enter Database Port(Default 3306) :-")
    user = input("Enter Database user Name :-")
    password = input("Enter Database password :-")
    data.host = ip
    data.password=password
    data.user=user
    if len(port.strip()) !=0:
        data.port=port.strip()
    err=data.Connect()
    if err==-1:
        result = big.figlet_format("OOP'S !", font="slant")
        print(result)
        print("Check The User-Name,Password and Port.")
        input()
        clear()
        local_Host()
    elif err==0:
        main_menu()

def local_Host():
    clear()
    result = big.figlet_format("LOCAL DATABASE", font="slant")
    print(result)
    user = input("Enter Database user Name :-")
    password = input("Enter Database password :-")
    port = input("Enter Database Port(Default 3306) :-")
    
    data.password=password
    data.user=user
    if len(port.strip()) !=0:
        data.port=port.strip()
    err=data.Connect()
    if err==-1:
        result = big.figlet_format("OOP'S !", font="slant")
        print(result)
        print("Check The User-Name,Password and Port.")
        input()
        clear()
        local_Host()
    elif err==0:
        main_menu()

def Add(lst):
    clear()
    result = big.figlet_format("Save", font="slant")
    print(result)
    # print(lst)
    Data = tuple(lst)
    # print(data)
    Sql='''INSERT INTO contact.contact (First_Name,Middle_Name,Last_Name,Nickname,Mobile_Number,Work_Number,Company,Birthday,
           Address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    err=data.Fire(Sql,Data)
    if(err==1):
        while True:
            x=input("Do You Want To add More?\nYes\nNo\nEnter The Option : ")
            if x=='y'or x in "yes" or x in "YES" or x=='Y':
                AddScreen()
                break
            elif x=='n'or x in "no" or x in "NO" or x=='N':
                main_menu()
                break
    else:
        del data
        Start()

def AddScreen():
    clear()
    result = big.figlet_format("Add Contact", font="slant")
    print(result)
    time.sleep(0.9)
    F_name=input("Enter First Name :-")
    M_name=input("Enter Middle Name :-")
    L_name=input("Enter Last Name :-")
    N_name=input("Enter Nickname Name :-")
    while True: 
        try:
            Mob_number = int(input('Enter an Mobile: '))
            temp =str(Mob_number) 
            if len(temp)==10:
                break
            else:
                print("Enter 10 digit Valid Mobile Number !")
        except ValueError:
            print('Please only input digits')

    W_Number="Null"   
    while True:
        X=input("Do you want to add a work number (Y,y)-Yes (N,n)-No :- ")
        if X == 'y'or X == 'Y':
            while True: 
                try:
                    W_Number = int(input('Enter an Phone Number: '))
                    temp =str(W_Number) 
                    if len(temp)==10:
                        break
                    else:
                        print("Enter 10 digit Valid Number !")
                except ValueError:
                    print('Please only input digits')
            break
        elif X=='n' or X=='N':
            break
        else:
            print('Select From The Given Option')
    C_name=input("Enter Company Name :-")
    B_Day=input("Enter the Birthday :-")
    Address=input("Enter the Address :-")
    # print("in while")
    
    while True:
        # print("in while")

        temp=[]
        temp.append(F_name)
        temp.append(M_name)
        temp.append(L_name)
        temp.append(N_name)
        temp.append(str(Mob_number))
        temp.append(str(W_Number))
        temp.append(C_name)
        temp.append(B_Day)
        temp.append(Address)
        if len(str(F_name.strip())) == 0:
             F_name=input("Enter First Name :-")
        elif len(str(M_name.strip())) == 0:
            M_name="NULL"
        elif len(str(L_name.strip())) == 0:
            L_name="NULL"
        elif len(str(N_name.strip())) == 0:
            N_name="NULL"
        elif len(str(N_name.strip())) == 0:
            N_name="NULL"
        elif len(str(C_name.strip()))==0:
            C_name="NULL"
        elif len(str(B_Day.strip()))==0:
            B_Day="NULL"
        elif len(str(Address.strip()))==0:
            Address="NULL"
        else:

            x=input("Do You Want To Save ?\nYes\nNo\nEnter The Option : ")
            if x=='y'or x in "yes" or x in "YES" or x=='Y':
                # Add(temp)
                input()
                break
            elif x=='n'or x in "no" or x in "NO" or x=='N':
                print("No")
                input()
                main_menu()
                break
if __name__ == "__main__":
    main()