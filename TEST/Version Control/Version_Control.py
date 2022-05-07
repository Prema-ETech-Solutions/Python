import os
from re import I
import time
import pyfiglet as sw
def Show(Str,bool=False):
    result = sw.figlet_format(Str, font="digital")
    
    if bool == True :
        clear()
    print(result)

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def Add_Path():

    while True:
        dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        drives = ['%s:' %d for d in dl if os.path.exists('%s:' % d)]
        Show("Drive Letter",True)
        print(f"List Of Drive {drives}")
        letter=input("Enter The Drive Letter: ")
        letter = letter[0]
        letter = letter.upper()
        letter = letter+ ":"
        if letter in drives:
            break
    os.system(f"cd {letter}")
    os.system(letter)
    os.system("dir")

    input()


def Start_Screen():
    Show("Welcome")
    time.sleep(0.9)
    input("Press Any Key.......")
    Add_Path()

if __name__ == "__main__":
    Start_Screen()

