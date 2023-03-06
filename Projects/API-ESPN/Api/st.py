
from idExtracts import *
from webScrap import scrapWeb
from commentary import *
import os
import time
# from datetime import datetime
from ApiReq import *
from strOperations import *
def start(li):
    dataCollection = []
    data = {}
    count = 0
    for row in li:
        if count != 0:
            link = row[0]
            if link:
                # Checking espncricinfo link
                if "espncricinfo" in link:
                    pass
                else:
                    link = "N A"
            else:
                continue
            momentInning = "NA"
            temp = row[1]
            if temp == "1" or temp == "2":
                momentInning = int(temp)
            else:
                print("Invalid Moment Inning !!" + momentInning)
                continue
            momentBall = "N A"
            try:
                tmp = str(row[2])
                tmp = tmp.split(".")
                if int(tmp[1]) > 0 and int(tmp[1]) < 7:
                    momentBall = float(row[2])
            except:
                print("Invalid Moment Ball !!" + momentBall)
                continue
            Player = "N A"
            try:
                Player = str(row[3])
                Player = Player.replace("(vc)","")
                Player =remove_first_end_spaces(Player)
            except:
                print("Player Name In-valid" + row[3])
                continue
            # print(link)
            # print(momentBall)
            # print(momentInning)
            data["espnLink"] = link
            data["momentBall"] = momentBall
            data["momentInning"] = momentInning
            data["Player"] = Player
            dataCollection.append(data.copy())
        else:
            count = count + 1
    
    if len(dataCollection) > 0:
        idExt(dataCollection)
        PLAYER_INFORMATION(dataCollection)
        scrapWeb(dataCollection)
        commentaryExt(dataCollection)
        
        return {"status":True,"dataCollection":dataCollection}
    else:
        return {"status":False,"dataCollection":[]}