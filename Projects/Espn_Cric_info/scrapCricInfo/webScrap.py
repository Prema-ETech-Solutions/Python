import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from changeDate import *
from commentary import *
from strOperations import *
import json


def scrapWeb(dataCollection):

    found = False
    # tp = set()
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

        Overs(soup, data)
        Team(soup, data)

        Tor_num(soup, data)
        Team_Score(soup, data)
        Played(soup, data)
        Ov(soup, data)
        Potm_(soup, data)
        Player_team(data)
        
        # Squads(data)

        dataCollection[index] = data.copy()
        data.clear()

def Overs(soup, data):
    overs = soup.find_all(
        "div",
        class_="ds-rounded-lg ds-mt-2",
    )
    temp = []
    for item in overs:
        tmp = BeautifulSoup(str(item), "html.parser")
        tmp = tmp.find_all(
            "span",
            class_="ds-font-regular ds-text-tight-s",
        )
        # print()
        over = tmp[0].text
        over = str(over)
        temp.append(over)

    data["Overs"] = {"teamA_Ov": temp[0], "teamB_Ov": temp[1]}

def Team(soup, data):
    Teams = soup.find_all(
        "span",
        class_="ds-text-tight-l ds-font-bold ds-text-typo hover:ds-text-typo-primary ds-block ds-truncate",
    )
    temp = []
    for item in Teams:
        temp.append(item.text)

    data["teams"] = {"teamA": temp[0], "teamB": temp[1]}
    # print(data)

def Tor_num(soup, data):
    torall = soup.find_all(
        "div",
        class_="ds-text-tight-m ds-font-regular ds-text-typo-mid3",
    )
    full = torall[0].text
    full = full.split(",")
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    data["match_no"] = ""
    for item in full:
        if item.find("Match") != -1 or item.find("Match") != -1:
            data["match_no"] = item
            break
        else:
            # print(full)
            data["match_no"] = ""

    data["stage"] = ""
    for item in full:
        if item.find("Group") != -1:
            data["stage"] = "Group Stage"
            break
        elif item.find("Quarter-Final") != -1:
            data["stage"] = "Quarter-Final"
            break
        elif item.find("Semi Final") != -1 or item.find("Semi-final") != -1 or item.find("Semi-Final") != -1:
            data["stage"] = "Semi-Final"
            break
        elif item.find("Final") != -1:
            data["stage"] = "Final"
            break
        else:
            data["stage"] = ""

    data["date"] = ""
    for index, item in enumerate(full):
        for m in months:
            if item.find(m) != -1:
                date = full[index] + full[index + 1]
                date = dateChange(date)
                data["date"] = str(date)
                break

    data["tournament"] = ""
    if len(full) > 0:
        data["tournament"] = full[-1]

def Team_Score(soup, data):
    Teams_S = soup.find_all(
        "div",
        class_="ds-text-compact-m ds-text-typo ds-text-right ds-whitespace-nowrap",
    )
    Teams_Score = []
    for item in Teams_S:
        score = BeautifulSoup(str(item), "html.parser")
        score = score.find_all(
        "strong",
        )
        for it in score:
            Teams_Score.append(it.text)
    
    # print(Teams_S)
    data["score"] = {"Score_A": Teams_Score[0], "Score_B": Teams_Score[1]}
    # data["score"] = {"Score_A": "10/0", "Score_B": "98/1"}

def Played(soup, data):

    BatterA = []
    BatterB = []
    BowlerA = []
    BowlerB = []

    Players_Tables = soup.find_all(
        "div",
        class_="ds-rounded-lg ds-mt-2",
    )
    T1 = BeautifulSoup(str(Players_Tables[0]), "html.parser")
    T2 = BeautifulSoup(str(Players_Tables[1]), "html.parser")

    T1 = T1.find_all(
        "div",
        class_="ds-p-0",
    )
    T1 = BeautifulSoup(str(T1[0]), "html.parser")
    sub_T1_Bat = T1.find_all(
        "table",
        class_="ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table",
    )
    sub_T1_Ball = T1.find_all(
        "table", class_="ds-w-full ds-table ds-table-md ds-table-auto"
    )

    sub_T1_Bat = BeautifulSoup(str(sub_T1_Bat[0]), "html.parser")
    sub_T1_Bat = sub_T1_Bat.find_all(
        "span",
        class_="ds-text-tight-s ds-font-medium ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block",
    )
    for item in sub_T1_Bat:
        BatterA.append(item.text)

    sub_T1_Ball = BeautifulSoup(str(sub_T1_Ball[0]), "html.parser")
    sub_T1_Ball = sub_T1_Ball.find_all(
        "span",
        class_="ds-text-tight-s ds-font-medium ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block",
    )
    for item in sub_T1_Ball:
        BowlerB.append(item.text)

    T2 = T2.find_all(
        "div",
        class_="ds-p-0",
    )
    T2 = BeautifulSoup(str(T2[0]), "html.parser")
    sub_T2_Bat = T2.find_all(
        "table",
        class_="ds-w-full ds-table ds-table-md ds-table-auto ci-scorecard-table",
    )
    sub_T2_Ball = T2.find_all(
        "table", class_="ds-w-full ds-table ds-table-md ds-table-auto"
    )

    sub_T2_Bat = BeautifulSoup(str(sub_T2_Bat[0]), "html.parser")
    sub_T2_Bat = sub_T2_Bat.find_all(
        "span",
        class_="ds-text-tight-s ds-font-medium ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block",
    )
    for item in sub_T2_Bat:
        BatterB.append(item.text)

    sub_T2_Ball = BeautifulSoup(str(sub_T2_Ball[0]), "html.parser")
    sub_T2_Ball = sub_T2_Ball.find_all(
        "span",
        class_="ds-text-tight-s ds-font-medium ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block",
    )
    for item in sub_T2_Ball:
        BowlerA.append(item.text)

    for index, item in enumerate(BatterA):
        tmp = item
        tmp = remove_first_end_spaces(tmp)
        tmp = tmp.replace("\xa0", "")
        tmp = tmp.replace("(c)", "")
        tmp = tmp.replace("†", "")
        tmp = remove_first_end_spaces(tmp)
        BatterA[index] = tmp

    for index, item in enumerate(BatterB):
        tmp = item
        tmp = remove_first_end_spaces(tmp)
        tmp = tmp.replace("\xa0", "")
        tmp = tmp.replace("(c)", "")
        tmp = tmp.replace("†", "")
        tmp = remove_first_end_spaces(tmp)
        BatterB[index] = tmp

    for index, item in enumerate(BowlerA):
        tmp = item
        tmp = remove_first_end_spaces(tmp)
        tmp = tmp.replace("\xa0", "")
        tmp = tmp.replace("(c)", "")
        tmp = tmp.replace("†", "")
        tmp = remove_first_end_spaces(tmp)
        BowlerA[index] = tmp

    for index, item in enumerate(BowlerB):
        tmp = item
        tmp = remove_first_end_spaces(tmp)
        tmp = tmp.replace("\xa0", "")
        tmp = tmp.replace("(c)", "")
        tmp = tmp.replace("†", "")
        tmp = remove_first_end_spaces(tmp)
        BowlerB[index] = tmp

    player_Played = {}
    player_Played["TeamA"] = {}
    player_Played["TeamB"] = {}
    TeamA = player_Played["TeamA"]
    TeamA["Batting"] = BatterA
    TeamA["Bowling"] = BowlerA
    TeamB = player_Played["TeamB"]
    TeamB["Batting"] = BatterB
    TeamB["Bowling"] = BowlerB

    data["Played"] = player_Played.copy()

def Ov(soup, data):
    actual = soup.find_all(
        "div",
        class_="ds-w-full ds-bg-fill-content-prime ds-overflow-hidden ds-rounded-xl ds-border ds-border-line ds-mb-4",
    )
    actual = BeautifulSoup(str(actual[2]), "html.parser")
    actual = soup.find_all(
        "span",
        class_="ds-text-tight-s ds-font-regular",
    )
    rw = ""
    for item in actual:
        if "over match" in item.text:
            rw = item.text

    rw = rw.split("(")
    rw = rw[1]
    rw = rw.replace("-over match)", "")
    actual = Check_Num(rw)
    if actual == False:
        actual = ""

    data["actual"] = actual
    # print(data)

def Potm_(soup, data):
    print("POTM")
    try:
        Potm = soup.find_all(
            "span",
            class_="ds-text-tight-m ds-font-medium ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block",
        )
        print(Potm)
        Potm = BeautifulSoup(str(Potm[0]), "html.parser")
        Potm = Potm.text
        data["Badges"] = Potm
    except:
        data["Badges"] = ""

def Player_team(data):

    player = data["Player"]
    if player in data["Played"]["TeamA"]["Batting"]:
        data["meta"]["team"] = data["teams"]["teamA"]
    elif player in data["Played"]["TeamA"]["Bowling"]:
        data["meta"]["team"] = data["teams"]["teamA"]
    elif player in data["Played"]["TeamB"]["Batting"]:
        data["meta"]["team"] = data["teams"]["teamB"]
    elif player in data["Played"]["TeamB"]["Bowling"]:
        data["meta"]["team"] = data["teams"]["teamB"]


