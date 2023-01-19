
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from changeDate import *
from commentary import *
from strOperations import *
import json

def scrapWeb(dataCollection):
    found = False
    for index in range(len(dataCollection)):
        data = dataCollection[index]
        espnlink = data["espnLink"]

        if "full-scorecard" in espnlink:
            pass
        elif "live-cricket-score" in espnlink:
            espnlink = espnlink.replace("live-cricket-score", "full-scorecard")      
        elif "match-impact-player" in espnlink:
            espnlink = espnlink.replace("match-impact-player", "full-scorecard")      
        elif "match-report" in espnlink:
            espnlink = espnlink.replace("match-report", "full-scorecard")      
        elif "ball-by-ball-commentary" in espnlink:
            espnlink = espnlink.replace("ball-by-ball-commentary", "full-scorecard")      
        elif "match-statistics" in espnlink:
            espnlink = espnlink.replace("match-statistics", "full-scorecard")      
        elif "match-overs-comparison" in espnlink:
            espnlink = espnlink.replace("match-overs-comparison", "full-scorecard")      
        elif "points-table-standings" in espnlink:
            espnlink = espnlink.replace("points-table-standings", "full-scorecard")      
        elif "match-news" in espnlink:
            espnlink = espnlink.replace("match-news", "full-scorecard")      
        elif "match-photo" in espnlink:
            espnlink = espnlink.replace("match-photo", "full-scorecard")      
        else:
            print("Not found!")
            print(espnlink)
        data["espnLink"] = espnlink
        
        content = requests.get(data["espnLink"])
        html_con = content.content
        soup = BeautifulSoup(html_con, "html.parser")
        data["texcept"] = []


        # Scraping The Data From Web:


        # Over
        overs_raw = soup.find_all(
            "span",
            class_="ds-font-regular ds-text-tight-xs",
        )
        over = []
        for el in overs_raw:
            l1 = el.text
            if "Ov" in l1:
               over.append(l1) 
        
        teamsA_Over = "NA"
        teamsB_Over = "NA"
        if (len(over) == 2):
            teamsA_Over = over [0]
            teamsB_Over = over [1]
        else :
            teamsA_Over = "NA"
            teamsB_Over = "NA"
        

        # Teams
        teams = soup.find_all(
            "span",
            class_="ds-text-tight-l ds-font-bold ds-text-ui-typo hover:ds-text-ui-typo-primary ds-block ds-truncate",
        )
        try:
            teamsA = teams[0]
        except Exception as e:
            teamsA = "NA"
            tmp = data["texcept"]
            data["texcept"] =  tmp.append(e)
        
        try:
            teamsB = teams[1]
        except Exception as e:
            teamsB = "NA"
            tmp = data["texcept"]
            data["texcept"] =  tmp.append(e)
        

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

        Players_Table = soup.find_all(
            "div",
            class_="ds-rounded-lg ds-mt-2",
        )
        



        Table_A = Players_Table[0]
        Table_B = Players_Table[1] 
        
        Table_A_Name = BeautifulSoup(str(Table_A), "html.parser")

        Team_A_Name = Table_A_Name.find_all(
            "span",
            class_="ds-text-title-xs ds-font-bold ds-capitalize",
        )
        Table_B_Name = BeautifulSoup(str(Table_B), "html.parser")
        Team_B_Name = Table_B_Name.find_all(
            "span",
            class_="ds-text-title-xs ds-font-bold ds-capitalize",
        )

        Table_B_Name = BeautifulSoup(str(Table_B), "html.parser")
        Table_A_Name = BeautifulSoup(str(Table_A), "html.parser")
        


        Tables_A = BeautifulSoup(str(Table_A), "html.parser")
        Tables_B = BeautifulSoup(str(Table_B), "html.parser")
        
        # Team B Player 
        Tables_A = Tables_A.find_all(
            "div",
            class_="ds-p-0",
        )
        Tables_A = BeautifulSoup(str(Table_A), "html.parser")
        BatterA = Tables_A.find_all(
            "table",
            class_="ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table",
        )
        BowlerB = Tables_A.find_all(
            "table",
            class_="ds-w-full ds-table ds-table-md ds-table-auto",
        )
        BatterA = BeautifulSoup(str(BatterA), "html.parser")
        BatterA = BatterA.find_all(
            "span",
            class_="ds-text-tight-s ds-font-medium ds-text-ui-typo ds-underline ds-decoration-ui-stroke hover:ds-text-ui-typo-primary hover:ds-decoration-ui-stroke-primary ds-block",
        )
        BatterA = BeautifulSoup(str(BatterA), "html.parser")

        BowlerB = BeautifulSoup(str(BowlerB), "html.parser")
        BowlerB = BowlerB.find_all(
            "span",
            class_="ds-text-tight-s ds-font-medium ds-text-ui-typo ds-underline ds-decoration-ui-stroke hover:ds-text-ui-typo-primary hover:ds-decoration-ui-stroke-primary ds-block",
        )
        BowlerB = BeautifulSoup(str(BowlerB), "html.parser")
        


        # Team B Player 

        Tables_B = Tables_B.find_all(
            "div",
            class_="ds-p-0",
        )
        Tables_B = BeautifulSoup(str(Table_B), "html.parser")
        BatterB = Tables_B.find_all(
            "table",
            class_="ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table",
        )

        BowlerA = Tables_B.find_all(
            "table",
            class_="ds-w-full ds-table ds-table-md ds-table-auto",
        )

        BatterB = BeautifulSoup(str(BatterB), "html.parser")
        BatterB = BatterB.find_all(
            "span",
            class_="ds-text-tight-s ds-font-medium ds-text-ui-typo ds-underline ds-decoration-ui-stroke hover:ds-text-ui-typo-primary hover:ds-decoration-ui-stroke-primary ds-block",
        )
        BatterB = BeautifulSoup(str(BatterB), "html.parser")

        BowlerA = BeautifulSoup(str(BowlerA), "html.parser")
        BowlerA = BowlerA.find_all(
            "span",
            class_="ds-text-tight-s ds-font-medium ds-text-ui-typo ds-underline ds-decoration-ui-stroke hover:ds-text-ui-typo-primary hover:ds-decoration-ui-stroke-primary ds-block",
        )
        BowlerA = BeautifulSoup(str(BowlerA), "html.parser")

        # print(Team_A_Name[0].text)
        # print(Team_B_Name[0].text)
        # print()
        # print(BatterA)
        # print(BowlerB)
        # print()
        # print(BatterB)
        # print(BowlerA)
        # print()



        BatterA=BatterA.text
        BowlerB=BowlerB.text
        BatterB=BatterB.text
        BowlerA=BowlerA.text

        # print(BatterA)
        # print(BowlerB)
        # print(BatterB)
        # print(BowlerA)

        BatterA = BatterA.replace("†","")
        BowlerB = BowlerB.replace("†","")
        BatterB = BatterB.replace("†","")
        BowlerA = BowlerA.replace("†","")


        BatterA = BatterA.replace("(c)","")
        BowlerB = BowlerB.replace("(c)","")
        BatterB = BatterB.replace("(c)","")
        BowlerA = BowlerA.replace("(c)","")


        BatterA = BatterA.replace("  ","")
        BowlerB = BowlerB.replace("  ","")
        BatterB = BatterB.replace("  ","")
        BowlerA = BowlerA.replace("  ","")

        BatterA=Space_(BatterA)
        BatterB=Space_(BatterB)
        BowlerA=Space_(BowlerA)
        BowlerB=Space_(BowlerB)

        player_Played= {}
        player_Played ["TeamA"] ={}
        player_Played ["TeamB"] ={}
        TeamA = player_Played ["TeamA"]
        TeamA["Batting"] =BatterA 
        TeamA["Bowling"] =BowlerA 
        TeamB = player_Played ["TeamB"]
        TeamB["Batting"] =BatterB 
        TeamB["Bowling"] =BowlerB 

        actual = soup.find_all(
            "div",
            class_="ds-w-full ds-bg-fill-content-prime ds-overflow-hidden ds-rounded-xl ds-border ds-border-line ds-mb-4",
        )

        actual = BeautifulSoup(str(actual[2]), "html.parser")
        actual = soup.find_all(
            "span",
            class_="ds-text-tight-s ds-font-regular",
        )
        rw = "NA"
        for elem in actual:
            # print(elem.text)
            if 'over' in elem.text:
                rw=elem.text
        
        rw = rw.split("(")
        rw = rw[1]
        rw = rw.replace("-over match)","")
        actual = Check_Num(rw)
        if actual == False:
            actual = "NA"
        

        Potm = soup.find_all(
            "span",
            class_="ds-text-tight-m ds-font-medium ds-text-ui-typo ds-underline ds-decoration-ui-stroke hover:ds-text-ui-typo-primary hover:ds-decoration-ui-stroke-primary ds-block",
        )

        Potm = BeautifulSoup(str(Potm), "html.parser")
        Potm = Potm.text
        Potm=Potm.replace("[","")
        Potm=Potm.replace("]","")
        # print(Potm)

        link ="https://www.fancraze.com/market/nfts?sort=lowestAsk"
        link = link.split("?")
        link =link[0]
        Player = data["Player"]
        Player = Player.lower()
        Player= Player.replace(" ","")
        Player= Player.replace("  ","")
        link =link + "/"+Player+"3"
        # print(link)
        

        
        # Inserting Data in Dictionary
        data["Badges"] = Potm
        data["Players_Team"] = "NA"
        if data["Player"] in BatterA:
            data["Players_Team"] = teamsA.string
        elif data["Player"] in BatterB:
            data["Players_Team"] = teamsB.string
        elif data["Player"] in BowlerA:
            data["Players_Team"] = teamsA.string
        elif data["Player"] in BowlerB:
            data["Players_Team"] = teamsB.string
        else:
            Player = data["Player"]
            status = False
            for item in BatterA:
                if status != True:
                    if item.casefold() == Player.casefold():
                        data["Players_Team"] = teamsA.string
                        status = True
                        break
                else:
                    break
            for item in BatterB:
                if status != True:
                    if item.casefold() == Player.casefold():
                        data["Players_Team"] = teamsB.string
                        status = True
                        break
                else:
                    break
            for item in BowlerA:
                if status != True:
                    if item.casefold() == Player.casefold():
                        data["Players_Team"] = teamsA.string
                        status = True
                        break
                else:
                    break
            for item in BowlerB:
                if status != True:
                    if item.casefold() == Player.casefold():
                        data["Players_Team"] = teamsB.string
                        status = True
                        break
                else:
                    break



        data["teams"] = {"teamA": teamsA.string, "teamB": teamsB.string}
        data["Overs"] = {"teamA_Ov": teamsA_Over, "teamB_Ov": teamsB_Over}
        data["actual"] = actual
        full = full.split(",")
        # print(full)
        # print(len(full))
        if len(full) > 5:
            data["match_no"] = full[0]
            data["stage"] = full[1]
            date =full[3] + full[4]
            date = dateChange(date)
            data["date"] = date
            data["tournament"] = full[5]

        elif len(full) == 4:
            data["match_no"] = "Not Available"
            data["stage"] = "Not Available"
            date =full[1] + full[2]
            date = dateChange(date)
            data["date"] = date
            data["tournament"] = full[3]
        else:
            data["match_no"] = "Not Available"
            data["stage"] = full[0]
            date =full[2] + full[3]
            date = dateChange(date)
            data["date"] = date
            data["tournament"] = full[4]

        data["score"] = {"Score_A": teamA_S, "Score_B": teamB_S}
        data["Played"] = player_Played.copy()
        data["winner"] = winner[0].string
        data["raw"] = full


        # Updating The List With Data
        print(data)
        dataCollection[index] = data.copy()
        data.clear()