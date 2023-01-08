from strOperations import *
import csv
import time

def csvCreate(file_Name ,dataCollection):
    with open(file_Name+".csv", "w", newline="") as csvfile:
        fieldnames = [
            "Link",
            "momentBall",
            "momentInning",
            "TeamA",
            "TeamB",
            "Match_no",
            "Stage",
            "Date",
            "Tournament",
            "Score_A",
            "Score_B",
            "Commentary",
            "Moment Type",
            "Winner",
        ]
        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        thewriter.writeheader()
        for x in range(len(dataCollection)):
            data = dataCollection[x]
            # print(data)
            temp = {}

            temp["Link"] =data["espnLink"]
            temp["momentBall"] =data["momentBall"]
            temp["momentInning"] =data["momentInning"]
            teams = data["teams"]
            temp["TeamA"] = TeamsOperations(teams["teamA"])
            temp["TeamB"] = TeamsOperations(teams["teamB"])
            num = ''.join(filter(lambda i: i.isdigit(), data["match_no"]))
            if num:
                pass
            else:
                num = "NA"
            temp["Match_no"] = num

            temp["Moment Type"] = data["Moment_Type"]


            temp["Stage"] = stageOperations(data["stage"])
            temp["Date"] = data["date"]
            
            temp["Tournament"] = dateOperations(data["date"]) +" "+ tournamentOperations(data["tournament"])
            score = data["score"]
            
            
            Score_A = score["Score_A"]
            if "/" in Score_A:
                pass
            else:
                Score_A = Score_A + "/10"
            temp["Score_A"] = Score_A
            Score_B = score["Score_B"]
            Score_B = Score_B.split(")")
            
            if len(Score_B) ==2:
                Score_B = Score_B[1]
                if "/" in Score_B:
                    pass
                else:
                    Score_B = Score_B + "/10"

            
            temp["Score_B"] = Score_B


            commentary = data["commentary"]
            ball = str(data["momentBall"])
            if commentary["commentary"] == None:
                tmp = ball +", "+ commentary["title"]
                temp["Commentary"] =tmp
            else:  
                tmp = ball +", "+ commentary["title"]+" "+commentary["commentary"].capitalize()
                temp["Commentary"] =tmp
               
            temp["Winner"] = data["winner"]
            # print(temp)
            thewriter.writerow(temp)
        print(file_Name +".csv"+" Created")



def csvRead(dataCollection):
    errLink=[]
    errBall=[]
    errIn=[]
    while True:
        try:
            path = input("Enter the Path :")
            # path = "C:\Users\FCS-LAPTOP\Downloads\Untitled.csv"
            with open(path) as file:
                data ={}
                reader = csv.reader(file)
                count = 0
                for row in reader:
                    if count !=0:
                        link = row[0]
                        if link:
                            # Checking espncricinfo link
                            if "espncricinfo" in link:
                                 pass
                            else:
                                link = "N A"
                   
                        else:
                            continue
                        
                        momentInning="NA"
                        temp=row[1]
                        if temp == '1' or temp == '2':
                            momentInning = int(temp)
                        else:
                            print("Invalid Moment Inning !!"+momentInning)
                        
                        momentBall = "N A"
                        try :
                            tmp = str(row[2])
                            tmp = tmp.split('.')
                            if int(tmp[1]) >0 and int(tmp[1])<7:
                             momentBall = float(row[2])
                        except:
                            print("Invalid Moment Ball !!"+momentBall)
                        
                        # print(link)
                        # print(momentBall)
                        # print(momentInning)
                        data["espnLink"] = link
                        data["momentBall"] = momentBall
                        data["momentInning"] = momentInning
                        dataCollection.append(data.copy())

                    else:
                        count = count +1
                break
                
        except Exception as e :
            # print(path)
            print("Invalid Path")
            print(e)
            time.sleep(2)
            continue
                      



