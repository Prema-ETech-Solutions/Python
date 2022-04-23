import os
from pickle import NONE
from re import I
import time
from typing_extensions import Self
from warnings import catch_warnings
from colorama import Cursor
import pyfiglet as big
import mysql.connector
DB = None
class Database:
    db=None
    db_Cursor = None
    def Connect_Db(self,user_,password_,port_=3306,ip="localhost"):
        try:
            self.db = mysql.connector.connect(host=ip,user=user_,password=password_,port=port_)
            self.db_Cursor = self.db.cursor()
            print("DATABASE Connected\n\n")

            time.sleep(0.6)
            return 0
        except:
            return -1
    def Create(self,sql):
        try :
            self.db_Cursor = self.db.cursor()
            self.db_Cursor.execute(sql)
            return 0
        except:
            return -1
    def Insert(self,sql,val):
        try:
            # print("SQL - ",sql)
            # print("Data - ",val)
            # self.db_Cursor = self.db.cursor()
            self.db_Cursor.execute(sql,val)
            self.db.commit()
            return 0
        except:
            return -1
    def Select(self,sql):
        try:
            self.db_Cursor.execute(sql)
            rs=self.db_Cursor.fetchall()
            return rs
        except:
            return None


clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def Show(Str):
    result = big.figlet_format(Str, font="slant")
    clear()
    print(result)

def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
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

def progressBar_():
     # A List of Items
    items = list(range(0, 57))
    # A Nicer, Single-Call Usage
    for item in progressBar(items, prefix = 'Progress:', suffix = 'Complete', length = 50):
        # Do stuff...
        time.sleep(0.1)
def Start_Screen():
    Show("Welcome")
    input("Press any key ....")
    clear()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    progressBar_()
    Connect_Option()

def Connect_Option():
    while True:
        Show("--DATABASE-- "+"configuration".upper())
        option=input("Do you want to connect local database (MYSQL) ? \n Yes \n No\n Enter the option : ")
        if option in "yes" or option in "YES" or option in "Yes" or option in "Y" or option in "y":
            Local_Data()
            break
        elif option in "no" or option in "NO" or option in "No" or option in "N" or option in "n":
            via_Internet()
            break
        else:
            print("Enter For The Given Option !")

def Local_Data():
    while True:
        Show("LOCAL DATABASE")
        user = input("Enter Database user Name : ")
        port = input("Enter Database Port(Default 3306) : ")
        password = input("Enter Database password : ")
        if len(user.strip())==0 or len(password.strip())==0:
            continue
        if len(port.strip())==0:
            port = 3306
        break
    val =DB.Connect_Db(user,password,port_=port)
    data_name="Contact"
    err1=DB.Create("CREATE SCHEMA IF NOT EXISTS {}".format(data_name))
    err =DB.Create("CREATE TABLE IF NOT EXISTS contact.contact(ID int NOT NULL AUTO_INCREMENT,First_Name varchar(100),Middle_Name varchar(100),Last_Name varchar(100),Nickname varchar(100),Mobile_Number varchar(100),Work_Number varchar(100),Company varchar(100),Birthday varchar(100),Address varchar(100),PRIMARY KEY (ID))")
    if val == 0 or err1 == 0 or err == 0:
        
        progressBar_()
        Main_Menu()
    else:
        print("Database error ....")
        input()
        Connect_Option()

def via_Internet():
    
    while True:
       Show(" CONNECT DATABASE")
       host=input("Enter Database IP : ")
       port = input("Enter Database Port(Default 3306) : ")
       user = input("Enter Database user Name : ")
       password = input("Enter Database password : ")
       if len(user.strip())==0 or len(password.strip())==0:
            continue
       if len(port.strip())==0:
           port = 3306
           break
    val =DB.Connect_Db(user,password,port_=port,ip=host)
    data_name="Contact"
    err1=DB.Create("CREATE SCHEMA IF NOT EXISTS {}".format(data_name))
    err =DB.Create("CREATE TABLE IF NOT EXISTS contact.contact(ID int NOT NULL AUTO_INCREMENT,First_Name varchar(100),Middle_Name varchar(100),Last_Name varchar(100),Nickname varchar(100),Mobile_Number varchar(100),Work_Number varchar(100),Company varchar(100),Birthday varchar(100),Address varchar(100),PRIMARY KEY (ID))")
    if val == 0 or err1 == 0 or err == 0:
        progressBar_()
        Main_Menu()
    else:
        print("Database error ....")
        input()
        Connect_Option()

def Main_Menu():
    x=0
    while True:
        Show("Main Menu")
        time.sleep(0.1)
        print("01. Show All Entry")
        time.sleep(0.1)
        print("02. Add Entry")
        time.sleep(0.1)
        print("03. Update Entry")
        time.sleep(0.1)
        print("04. Remove Entry")
        time.sleep(0.1)
        print("05. Search Entry")
        time.sleep(0.1)
        print("06. Log-Out")
        time.sleep(0.1)
        print("07. Exit\n\n\n")
        time.sleep(0.1)
        try:
            x = int(input('Enter From The Option : '))
            if x ==1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7:
                # print(x)
                # input()
                break
            else:
                print("Choose From The Option .")
                input()
        except ValueError:
            print("Invalid Input")
            input()  
    if x == 1 :
        ShowAll()
    elif x == 2 :
        Add_Screen_Logic_Entry()
    elif x == 3 :
        Update_Contact()
    elif x == 4:
        pass
    elif x == 5:
        pass
    elif x == 6:
        Log_Out()
        Connect_Option()
    elif x == 7:
        Exit_()

def Log_Out():
    Show("Log Out")
    time.sleep(0.9)
    progressBar_()
    

def Exit_():
    Log_Out()
    Show("Exiting")
    time.sleep(0.9)
    progressBar_()

def Add_Screen_Logic_Entry():
    Show("Add Contact")
    F_name = input("Enter First Name :- ")
    M_name = input("Enter Middle Name :- ")
    L_name = input("Enter Last Name :- ")
    N_name = input("Enter Nickname :- ")
    while True:
        try:
            Mobile= int(input("Enter Phone Number :- "))
            if len(str(Mobile)) == 10:
                break
            else:
                print("Enter 10 Digit Valid Number")
        except ValueError:
            print("Invalid input")
    Work = "NOT AVAILABLE"
    while True:
        Op = input("Do You Want To Add Work Number? \nYes \nNo\nEnter The Option:")
        if Op in "yes" or Op in "Yes" or Op in "YES" or Op == 'Y' or Op == 'y':
            
            while True:
                try:
                    Work= input("Enter Work Number :- ")
                    if len(str(Work)) == 10:
                        break
                    else:
                        print("Enter 10 Digit Valid Number")
                except ValueError:
                    print("Invalid input")
            break
        elif Op in "no" or Op in "No" or Op in "NO" or Op == 'n' or Op == 'N':
            break
        else:
            print('''Enter 'Yes' OR 'No' ''')
    
    Cmp= input("Enter Company Name :- ")
    B_day= input("Enter Birthday :- ")
    Address =input("Enter Address :- ")
    # Check Data is proper
    while True:
        if len(F_name.strip()) ==0:
            print("You did not enter the First Name !")
            F_name = input("Enter The First Name : ")
        elif len(M_name.strip()) ==0:
            M_name = "NOT AVAILABLE"
        elif len(L_name.strip()) ==0:
            L_name = "NOT AVAILABLE"
        elif len(N_name.strip()) ==0:
            N_name = "NOT AVAILABLE"
        elif len(Cmp.strip()) ==0:
            Cmp = "NOT AVAILABLE"
        elif len(B_day.strip()) ==0:
            B_day = "NOT AVAILABLE"
        elif len(Address.strip()) ==0:
            Address = "NOT AVAILABLE"
        else:
            data=[]
            data.append(F_name)
            data.append(M_name)
            data.append(L_name)
            data.append(N_name)
            data.append(Mobile)
            data.append(Work)
            data.append(Cmp)
            data.append(B_day)
            data.append(Address)
            break

    # Data Saving     
    data_pass = tuple(data)
    sql ="INSERT INTO contact.contact (First_Name, Middle_Name, Last_Name, Nickname, Mobile_Number, Work_Number, Company, Birthday, Address) VALUES (%s, %s,%s,%s, %s,%s,%s, %s,%s);"
    err =DB.Insert(sql,data_pass)
    if err == 0:
        print("Data Saved")
        input()
        Main_Menu()
    else:
        print("The Data Is Not Inserted ")
        input()
        Main_Menu()

def ShowAll():
    Show("Show Contact")   
    count =0
    sql ="SELECT * FROM contact.contact ORDER BY First_Name;"
    rs=DB.Select(sql)
    for x in rs:
        count = count+1
        print()
        print("--------------------------------------------------------------------")
        print("First Name - ",x[1])
        time.sleep(0.1)    
        print("Middle Name - ",x[2])
        time.sleep(0.1)    
        print("Last Name - ",x[3])
        time.sleep(0.1)    
        print("Nickname - ",x[4])
        time.sleep(0.1)    
        print("Mobile Number - ",x[5])
        time.sleep(0.1)    
        print("Work Number - ",x[6])
        time.sleep(0.1)    
        print("Company Name - ",x[7])
        time.sleep(0.1)    
        print("Birth Date - ",x[8])
        time.sleep(0.1)    
        print("Address - ",x[9])
        time.sleep(0.1)    
        print("--------------------------------------------------------------------")
        print()
        time.sleep(0.3)    
    if count == 0:
        print("No Record Found ..... ")
    else:
        print("Total Record Found ",count,".....")
    input()
    Main_Menu()

def Update_Contact():
    Show("Update Contact")
    Old_F_Name = input("Enter The First Name :- ")
    count =0
    sql ="SELECT * FROM contact.contact WHERE First_Name = '{}';".format(Old_F_Name)
    rs=DB.Select(sql)
    for x in rs:
        count = count+1
        print()
        print("Entry No.",count)
        print("--------------------------------------------------------------------")
        print("First Name - ",x[1])
        time.sleep(0.1)    
        print("Middle Name - ",x[2])
        time.sleep(0.1)    
        print("Last Name - ",x[3])
        time.sleep(0.1)    
        print("Nickname - ",x[4])
        time.sleep(0.1)    
        print("Mobile Number - ",x[5])
        time.sleep(0.1)    
        print("Work Number - ",x[6])
        time.sleep(0.1)    
        print("Company Name - ",x[7])
        time.sleep(0.1)    
        print("Birth Date - ",x[8])
        time.sleep(0.1)    
        print("Address - ",x[9])
        time.sleep(0.1)    
        print("--------------------------------------------------------------------")
        print()
        time.sleep(0.3)    
    if count == 0: 
        print("No Record Found ..... ")
        input()
        Main_Menu()
    else:
        print("Total Record Found ",count,".....")
        input()
        while True:
            try:
                print("Enter The Entry Number Range ( 1 - ",count,")")
                Old_Val=int(input(":"))
                if Old_Val >= 1 and Old_Val <= count:
                    break
                else:
                    print("Input is out of range")
            except ValueError:
                print("Invalid Input")
        count =0
        for x in rs:
            count = count+1
            if  count== Old_Val:
                Update_Log(x[0])


def Update_Log(Id):
    F_name = input("Enter First Name :- ")
    M_name = input("Enter Middle Name :- ")
    L_name = input("Enter Last Name :- ")
    N_name = input("Enter Nickname :- ")
    while True:
        try:
            Mobile= int(input("Enter Phone Number :- "))
            if len(str(Mobile)) == 10:
                break
            else:
                print("Enter 10 Digit Valid Number")
        except ValueError:
            print("Invalid input")
    Work = "NOT AVAILABLE"
    while True:
        Op = input("Do You Want To Add Work Number? \nYes \nNo\nEnter The Option:")
        if Op in "yes" or Op in "Yes" or Op in "YES" or Op == 'Y' or Op == 'y':
            
            while True:
                try:
                    Work= input("Enter Work Number :- ")
                    if len(str(Work)) == 10:
                        break
                    else:
                        print("Enter 10 Digit Valid Number")
                except ValueError:
                    print("Invalid input")
            break
        elif Op in "no" or Op in "No" or Op in "NO" or Op == 'n' or Op == 'N':
            break
        else:
            print('''Enter 'Yes' OR 'No' ''')
    
    Cmp= input("Enter Company Name :- ")
    B_day= input("Enter Birthday :- ")
    Address =input("Enter Address :- ")
    # Check Data is proper
    while True:
        if len(F_name.strip()) ==0:
            print("You did not enter the First Name !")
            F_name = input("Enter The First Name : ")
        elif len(M_name.strip()) ==0:
            M_name = "NOT AVAILABLE"
        elif len(L_name.strip()) ==0:
            L_name = "NOT AVAILABLE"
        elif len(N_name.strip()) ==0:
            N_name = "NOT AVAILABLE"
        elif len(Cmp.strip()) ==0:
            Cmp = "NOT AVAILABLE"
        elif len(B_day.strip()) ==0:
            B_day = "NOT AVAILABLE"
        elif len(Address.strip()) ==0:
            Address = "NOT AVAILABLE"
        else:
            data=[]
            data.append(F_name)
            data.append(M_name)
            data.append(L_name)
            data.append(N_name)
            data.append(Mobile)
            data.append(Work)
            data.append(Cmp)
            data.append(B_day)
            data.append(Address)
            break

    # Data Update     
    data.append(Id)
    data_pass = tuple(data)
    sql ="UPDATE contact.contact SET First_Name = %s, Middle_Name = %s, Last_Name = %s, Nickname = %s, Mobile_Number = %s, Work_Number = %s, Company = %s, Birthday = %s, Address = %s WHERE (ID = %s);"
    err =DB.Insert(sql,data_pass)
    if err == 0:
        print("Data Updated")
        input()
        Main_Menu()
    else:
        print("The Data Is Not Updated")
        input()
        Main_Menu()
    







        


if __name__ == "__main__":
    DB=Database()
    Start_Screen()
    # pass