import os
import time
import pyfiglet as big
def Show(Str):
    result = big.figlet_format(Str, font="slant")
    clear()
    print(result)
clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

   
    
if __name__ == "__main__":
    Start_Screen()

