from turtle import title
import requests
import math
from bs4 import BeautifulSoup
import json,urllib.request

url = "https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2022-23-1298134/england-vs-pakistan-final-1298179/ball-by-ball-commentary"


Serialid = url.split("/")
Serialid=Serialid[4].split("-")
Serialid =Serialid[-1]
# print(Serialid)

matchID = url.split("/")
matchID=matchID[5].split("-")
matchID =matchID[-1]
# print(matchID)

over_in =float(input("Enter over"))

print(type(over_in))


Apiurl = 'https://hs-consumer-api.espncricinfo.com/v1/pages/match/comments?lang=en&seriesId='+str(Serialid)+'&matchId='+str(matchID)+'&inningNumber=1&commentType=ALL&sortDirection=DESC&fromInningOver='+str(math.ceil(over_in))
# Apiurl = "https://hs-consumer-api.espncricinfo.com/v1/pages/match/comments?lang=en&seriesId=1298134&matchId=1298178&inningNumber=1&commentType=ALL&sortDirection=DESC&fromInningOver=1"
# print(Apiurl)
output = urllib.request.urlopen(Apiurl).read()
output = json.loads(output)
# print(type(output))
output =output["comments"]
output =output[1]
print(output["title"])
htm = output["commentTextItems"]
htm =htm[0]
print(htm["html"])








content = requests.get(url)
html_con = content.content
# print(html_con)
soup = BeautifulSoup(html_con, "html.parser")
# print(soup.prettify)

# title =soup.title
# print(title)

# par =soup.find_all('p')
# print(par)

# ancor =soup.find_all('a')
# print(ancor)


# Teams
teams = soup.find_all(
    "span",
    class_="ds-text-tight-l ds-font-bold ds-text-ui-typo hover:ds-text-ui-typo-primary ds-block ds-truncate",
)
# print(teams)

teamsA = teams[0]
teamsB = teams[1]


# name = soup.find_all('span', class_= "ds-text-tight-m ds-font-regular ds-text-ui-typo ds-underline ds-decoration-ui-stroke hover:ds-text-ui-typo-primary hover:ds-decoration-ui-stroke-primary ds-block ds-text-ui-typo-mid")
# print(name[0].string)


f1 = soup.find("div", class_="ds-text-tight-m ds-font-regular ds-text-ui-typo-mid")

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
# print(score)
# print(score1)

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
    "p", class_="ds-text-tight-m ds-font-regular ds-truncate ds-text-typo-title"
)



# print()
# print("Team A :"+teamsA.string)
# print("Team B :"+teamsB.string)


# print()
# full = full.split(",")
# stage = full[0]
# date = full[2] + full[3]
# tor = full[4]
# full.clear()
# full.append(stage)
# full.append(date)
# full.append(tor)
# print(full)


# print("")
# print("Score")
# print(teamA_S)
# print(teamB_S)

# print("")
# print(winner[0].string)
