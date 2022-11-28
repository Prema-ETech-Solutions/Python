import requests
import math
from bs4 import BeautifulSoup
import json, urllib.request
import os
import csv
import datetime
from datetime import datetime
import time


raw = []

# Input Links / all inputs
def Raw_links():

    while True:
        data = {}
        link = input("Enter Links Espn-Cric-info:")

        # Checking input for null
        if link:
            # Checking espncricinfo link
            if "espncricinfo" in link:
                pass
            else:
                print("Invalid link !!!")
                continue
        else:
            break

        # Serial ID
        Serialid = link.split("/")
        Serialid = Serialid[4].split("-")
        Serialid = Serialid[-1]

        # Match ID
        matchID = link.split("/")
        matchID = matchID[5].split("-")
        matchID = matchID[-1]

        # commentary Over
        valid = False
        while not valid:
            try:
                over_in = float(input("Enter Ball Number (0.1) : "))
                if over_in == 0:
                    over_in = 0.1
                valid = True
            except ValueError:
                print("Please only input digits")

        # inningNumber input
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

        # dictionary
        data["link"] = link
        data["serialid"] = Serialid
        data["matchid"] = matchID
        data["over_in"] = over_in
        data["inningNumber"] = inningNumber
        raw.append(data.copy())
        os.system("cls")
    # print(raw)
    Extract()


def commentary(data):

    # Apiurl = 'https://hs-consumer-api.espncricinfo.com/v1/pages/match/comments?lang=en&seriesId=1298134&matchId=1298179&inningNumber=1&commentType=ALL&sortDirection=DESC&fromInningOver=1'
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
    # print(output)
    for y in range(len(output)):
        apidata = output[y]

        if apidata["oversActual"] == data["over_in"]:
            commentary_str = apidata["commentTextItems"]
            commentary_str = commentary_str[0]
            commentary_str = BeautifulSoup(commentary_str["html"], "html.parser").text
            data["commentary"] = {
                "title": apidata["title"],
                "commentary": commentary_str,
            }


def Csv_create():

    file_Name = ""

    now = datetime.now()
    now = now.strftime("%Y/%m/%d %I:%M:%S")  # 12-hour format.
    file_Name = file_Name +"_"+ now + ".csv"
    file_Name = file_Name.replace(":", "-")
    file_Name = file_Name.replace(" ", "_")
    file_Name = file_Name.replace("/", "-")
    with open(file_Name, "w", newline="") as csvfile:
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
        for x in range(len(raw)):
            data = raw[x]
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
            pass


def Extract():
    # print(len(raw))
    if len(raw) != 0:
        for x in range(len(raw)):

            data = raw[x]
            # print(data['link'])
            content = requests.get(data["link"])
            html_con = content.content
            soup = BeautifulSoup(html_con, "html.parser")
            teams = soup.find_all(
                "span",
                class_="ds-text-tight-l ds-font-bold ds-text-ui-typo hover:ds-text-ui-typo-primary ds-block ds-truncate",
            )
            teamsA = teams[0]
            teamsB = teams[1]

            f1 = soup.find(
                "div", class_="ds-text-tight-m ds-font-regular ds-text-ui-typo-mid"
            )
            full = ""
            for item in f1.strings:
                full = full + item

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

            winner = soup.find_all(
                "p",
                class_="ds-text-tight-m ds-font-regular ds-truncate ds-text-typo-title",
            )

            # print()
            # print()
            # print("Team A :" + teamsA.string)
            # print("Team B :" + teamsB.string)
            # data['teamA'] = teamsA.string
            # data['teamB'] = teamsB.string
            data["teams"] = {"teamA": teamsA.string, "teamB": teamsB.string}

            full = full.split(",")
            if len(full) > 5:
                data["match_no"] = full[0]
                data["stage"] = full[1]
                data["date"] = full[3] + full[4]
                data["tournament"] = full[5]
                # full.clear()
                # full.append(match_no)
                # full.append(stage)
                # full.append(date)
                # full.append(tor)
            else:
                data["match_no"] = "Not Available"
                data["stage"] = full[0]
                data["date"] = full[2] + full[3]
                data["tournament"] = full[4]
                # full.clear()
                # full.append(match_no)
                # full.append(stage)
                # full.append(date)
                # full.append(tor)

            # print(data)

            # print("Score")

            # data['score_A'] = teamA_S
            # data['score_B'] =teamB_S
            data["score"] = {"Score_A": teamA_S, "Score_B": teamB_S}

            # print(teamA_S)
            # print(teamB_S)

            # print()
            # print()
            # print(winner[0].string)
            commentary(data)

            data["winner"] = winner[0].string
            data["raw"] = full

            # print(data)

            raw[x] = data.copy()
        # test = raw[0]
        # print(raw)
        Csv_create()

    else:
        print("NO DATA FOUND !!s")


# Start
if __name__ == "__main__":
    Raw_links()
