
import requests
from bs4 import BeautifulSoup
from changeDate import *
from commentary import *

def scrapWeb(dataCollection):
    for index in range(len(dataCollection)):
        data = dataCollection[index]
        content = requests.get(data["espnLink"])
        html_con = content.content
        soup = BeautifulSoup(html_con, "html.parser")
        data["texcept"] = []
        # print(soup)
        # Scraping The Data From Web:
        # Teams
        teams = soup.find_all(
            "span",
            class_="ds-text-tight-l ds-font-bold ds-text-ui-typo hover:ds-text-ui-typo-primary ds-block ds-truncate",
        )
        try:
            teamsA = teams[0]
        except Exception as e:
            teamsA = ""
            tmp = data["texcept"]
            data["texcept"] =  tmp.append(e)
        
        try:
            teamsB = teams[1]
        except Exception as e:
            teamsB = ""
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

        # Inserting Data in Dictionary
        data["teams"] = {"teamA": teamsA.string, "teamB": teamsB.string}

        full = full.split(",")
        print(full)
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

        data["winner"] = winner[0].string
        data["raw"] = full

        # Updating The List With Data
        dataCollection[index] = data.copy()
        data.clear()