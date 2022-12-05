import os

import requests
import math
from bs4 import BeautifulSoup


import json, urllib.request


# import datetime
from datetime import datetime





from changeDate import * 


rawData = []

# Taking User Input Of User :
# Espn-Cric-info
# Ball Number
# Inning Number

# Logic
# 1)Checking Valid link for Espn Link
# 2)Extracting Match-Id & Serial-Id From The Link
# 3)Taking Input Of Over Ball
# 4)Taking Input Of Inning
# 5)Adding All Data in Dictionary
# 6)Copying The Dictionary In List
# 7)Screen Clear
# 8)Checking The 'rawData' len is zero or not


def start():
    while True:
        data = {}

        link = input("Enter Links Espn-Cric-info:")

        # Checking Valid link for Espn Link
        if link:
            # Checking espncricinfo link
            if "espncricinfo" in link:
                pass
            else:
                print("Invalid link !!!")
                continue
        else:
            break

        # Extracting Match-Id & Serial-Id From The Link
        Serialid = link.split("/")
        Serialid = Serialid[4].split("-")
        Serialid = Serialid[-1]

        # Extracting Match-Id & Serial-Id From The Link
        matchID = link.split("/")
        matchID = matchID[5].split("-")
        matchID = matchID[-1]

        # Taking Input Of Over Ball
        valid = False
        while not valid:
            try:
                over_in = float(input("Enter Ball Number (0.1) : "))
                if over_in == 0:
                    over_in = 0.1
                valid = True
            except ValueError:
                print("Please only input digits")

        # Taking Input Of Inning
        valid = False
        while not valid:
            try:
                inningNumber = int(input("Enter Inning Number  (1 or 2): "))
                if inningNumber == 1 or inningNumber == 2:
                    valid = True
                else:
                    print("Enter The 1 OR 2 ")
            except ValueError:
                print("Please only input digits")

        # Adding All Data in Dictionary
        data["link"] = link
        data["serialid"] = Serialid
        data["matchid"] = matchID
        data["over_in"] = over_in
        data["inningNumber"] = inningNumber

        # Copying The Dictionary In List
        rawData.append(data.copy())
        # Screen Clear
        os.system("cls")

    #
    if len(rawData) != 0:
        scrapeWeb()
    else:
        print("NO DATA FOUND !!")


# Scraping The Data From Web Page:
# Reading List 'rawData'
#   Reading List Index Wise To Dictionary Object
#   Logic for Scrap Data
#   Scraping The Data From Web:
#   Scraping Data (Teams,[Match-No , Stage , Location ,Date , Tournament] , Teams Score, Winner)
#   Inserting Data in Dictionary
#   Adding Commentary In Dictionary
#   Updating The List With Data
#   Creating File Name For The CSV And JSON
#   Json File Creating
#   CSV File Creating

def scrapeWeb():
    # Reading 'rawData' List
    for x in range(len(rawData)):
        # Reading List Index Wise To Dictionary Object
        data = rawData[x]

        # Logic for Scrap Data
        content = requests.get(data["link"])
        html_con = content.content
        soup = BeautifulSoup(html_con, "html.parser")

        # Scraping The Data From Web:
        # Teams
        teams = soup.find_all(
            "span",
            class_="ds-text-tight-l ds-font-bold ds-text-ui-typo hover:ds-text-ui-typo-primary ds-block ds-truncate",
        )
        teamsA = teams[0]
        teamsB = teams[1]

        # [Match-No , Stage ,Location ,Date , Tournament]
        f1 = soup.find(
            "div", class_="ds-text-tight-m ds-font-regular ds-text-ui-typo-mid"
        )
        full = ""
        for item in f1.strings:
            full = full + item

        # Teams Score
        teamA_S = ""
        teamB_S = ""
        score = soup.find_all(
            "div",
            class_="ds-text-compact-m ds-text-typo-title ds-text-right ds-whitespace-nowrap",
        )
        score1 = soup.find_all("span", class_="ds-text-compact-s ds-mr-0.5")
        for item in score[0].strings:
            # print(item)
            for item1 in score1[0].strings:
                # print(item1)
                teamA_S = item1
            # full = full + item
            teamA_S = teamA_S + item
        for item in score[1].strings:
            # print(item)
            for item1 in score1[1].strings:
                # print(item1)
                teamB_S = item1
            teamB_S = teamB_S + item

        # Winner
        winner = soup.find_all(
            "p",
            class_="ds-text-tight-m ds-font-regular ds-truncate ds-text-typo-title",
        )

        # Inserting Data in Dictionary
        data["teams"] = {"teamA": teamsA.string, "teamB": teamsB.string}

        full = full.split(",")
        if len(full) > 5:
            data["match_no"] = full[0]
            data["stage"] = full[1]
            date =full[3] + full[4]
            date = dateChange(date)
            data["date"] = date
            data["tournament"] = full[5]

        else:
            data["match_no"] = "Not Available"
            data["stage"] = full[0]
            date =full[2] + full[3]
            date = dateChange(date)
            data["date"] = date
            data["tournament"] = full[4]

        data["score"] = {"Score_A": teamA_S, "Score_B": teamB_S}

        # Adding Commentary In Dictionary
        commentary(data)

        data["winner"] = winner[0].string
        data["raw"] = full

        # Updating The List With Data
        rawData[x] = data.copy()
        data.clear()
    

    # Creating File Name For The CSV And JSON 
    file_Name = ""
    now = datetime.now()
    now = now.strftime("%Y/%m/%d %I:%M:%S")  # 12-hour format.
    file_Name = file_Name +"_"+ now
    file_Name = file_Name.replace(":", "-")
    file_Name = file_Name.replace(" ", "_")
    file_Name = file_Name.replace("/", "-")

    # Json File Creating
    json_Create(file_Name)

    # Csv File Creating
    csv_Create(file_Name)
    






def commentary(data):

    Apiurl = (
        "https://hs-consumer-api.espncricinfo.com/v1/pages/match/comments?lang=en&seriesId="
        + str(data["serialid"])
        + "&matchId="
        + str(data["matchid"])
        + "&inningNumber="
        + str(data["inningNumber"])
        + "&commentType=ALL&sortDirection=DESC&fromInningOver="
        + str(math.ceil(data["over_in"]))
    )


    output = urllib.request.urlopen(Apiurl).read()      
    output = json.loads(output)
    output = output["comments"]


    for y in range(len(output)):
        apidata = output[y]

        if apidata["oversActual"] == data["over_in"]:
            commentary_str = apidata["commentTextItems"]
            commentary_str = commentary_str[0]
            commentary_str = BeautifulSoup(commentary_str["html"], "html.parser").text
            st = ""
            if apidata["isFour"] == True:
                st ="FOUR runs"
                pass 
            elif apidata["isSix"] == True:
                st ="SIX runs"
                pass
            elif apidata["isWicket"] == True:
                st ="OUT"
                pass
            elif apidata["totalRuns"] == 1:
                st ="1 run"
                pass
            elif apidata["totalRuns"] == 2:
                st ="2 run"
                pass
            elif apidata["totalRuns"] == 3:
                st ="3 run"
                pass
            else:
                pass

            

            title = apidata["title"] + ", " + st
            data["commentary"] = {
                "title": title,
                "commentary": commentary_str,
            }
            break


def json_Create(file_Name):
    
    with open(file_Name+".json",'w') as J:
        json.dump(rawData,J)
    print(file_Name +".json"+ " Created")




def csvRead():
    data = {}
    with open("./Booster_Pack.csv") as file:
        reader = csv.reader(file)
        count = 0
        for row in reader:
            if count == 0:
                
                print(row[8])
                print(row[9])
                print(row[28])
            else:
                link =row[28]
                over_in = row[9]
                inningNumber = row[8]
                
                # Extracting Match-Id & Serial-Id From The Link
                Serialid = link.split("/")
                print(Serialid)
                Serialid = Serialid[4].split("-")
                Serialid = Serialid[-1]

                # Extracting Match-Id & Serial-Id From The Link
                matchID = link.split("/")
                matchID = matchID[5].split("-")
                matchID = matchID[-1]

                data["link"] = link
                data["serialid"] = Serialid
                data["matchid"] = matchID
                data["over_in"] = over_in
                data["inningNumber"] = inningNumber
                rawData.append(data.copy())

            #     pass
            count = count +1
    
    if len(rawData) != 0:
        scrapeWeb()
        # pass
    else:
        print("NO DATA FOUND !!")