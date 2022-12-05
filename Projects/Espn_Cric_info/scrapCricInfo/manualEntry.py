from inputVerify import *

def gatherData(dataCollection):
    data = {}
    while True:
        link = input("Enter Links Espn-Cric-info : ")
        if link:
            # Checking espncricinfo link
            if "espncricinfo" in link:
                pass
            else:
                print("Invalid link !!!")
                continue
        else:
            break
        
        while True:
            momentBall=decimalNumber("Enter Moment Ball : ")
            try :
                tmp = str(momentBall)
                tmp = tmp.split('.')
                if int(tmp[1]) >0 and int(tmp[1])<7:
                    break
            except:
                print("Invalid Moment Ball !!"+momentBall)
                 
            

        while True:
            momentInning=wholeNumber("Enter Moment Inning : ")
            if momentInning == 1 or momentInning == 2:
                break
            else:
                print("Invalid Moment Inning !!"+momentInning)   
        

        data["espnLink"] = link
        data["momentBall"] = momentBall
        data["momentInning"] = momentInning
        dataCollection.append(data.copy())
