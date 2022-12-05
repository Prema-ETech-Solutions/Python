from inputVerify import *
from manualEntry import *
from idExtracts import *
from webScrap import scrapWeb
from commentary import *
import os
from datetime import datetime
from csvOperations import *
from jsonOperations import *


clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")

# Start Function
def start():
    dataCollection = []
    while True:
        print("Enter ")
        print("00)Manual Data Entry")
        print("01)Automation Data Entry")
        print("02)Verify Data Entry")
        print("99)Exit")
        menu_entry = wholeNumber("Enter The Number : ")
        if menu_entry == 00:
            gatherData(dataCollection)
            if len(dataCollection) > 0:
                idExt(dataCollection)
                scrapWeb(dataCollection)
                commentaryExt(dataCollection)
                csvCreate(fileName(),dataCollection)
                jsonCreate(fileName(),dataCollection)
            else:
                # clear()
                print("Invalid Input !!")

        elif menu_entry == 1:
            csvRead(dataCollection)
            if len(dataCollection) > 0:
                idExt(dataCollection)
                scrapWeb(dataCollection)
                commentaryExt(dataCollection)
                csvCreate(fileName(),dataCollection)
                jsonCreate(fileName(),dataCollection)
            else:
                clear()
                print("Invalid Input !!")
        elif menu_entry == 2:
            break
        elif menu_entry == 99:
            break
        else:
            clear()
            print("Invalid Input !!")


def fileName():
    fileName_ = ""
    now = datetime.now()
    now = now.strftime("%Y/%m/%d %I:%M:%S")  # 12-hour format.
    fileName_ = fileName_ + "_" + now
    fileName_ = fileName_.replace(":", "-")
    fileName_ = fileName_.replace(" ", "_")
    fileName_ = fileName_.replace("/", "-")
    return fileName_
