
import csv
import time

def csvCreate(file_Name ,dataCollection):
    with open(file_Name+".csv", "w", newline="") as csvfile:
        fieldnames = [
            "TeamA",
            "TeamB",
            "Match_no",
            "Stage",
            "Date",
            "Tournament",
            "Score_A",
            "Score_B",
            "Commentary_Title",
            "Commentary",
            "Winner",
        ]
        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        thewriter.writeheader()
        for x in range(len(dataCollection)):
            data = dataCollection[x]
            temp = {}
            teams = data["teams"]
            temp["TeamA"] = teams["teamA"]
            temp["TeamB"] = teams["teamB"]
            temp["Match_no"] = data["match_no"]
            temp["Stage"] = data["stage"]
            temp["Date"] = data["date"]
            temp["Tournament"] = data["tournament"]
            score = data["score"]
            temp["Score_A"] = score["Score_A"]
            temp["Score_B"] = score["Score_B"]
            
            
            commentary = data["commentary"]
            temp["Commentary_Title"] = commentary["title"]
            temp["Commentary"] = commentary["commentary"]
               
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
                      
      