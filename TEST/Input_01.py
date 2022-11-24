from turtle import title
import requests
from bs4 import BeautifulSoup
url = "https://www.espncricinfo.com/series/england-in-australia-2022-23-1317467/australia-vs-england-2nd-odi-1317490/full-scorecard"
content = requests.get(url)
html_con =content.content
# print(html_con)
soup = BeautifulSoup(html_con,'html.parser')
# print(soup.prettify)

# title =soup.title
# print(title)

# par =soup.find_all('p')
# print(par)

# ancor =soup.find_all('a')
# print(ancor)


# Teams 
# teams = soup.find_all('span', class_= "ds-text-tight-l ds-font-bold ds-text-ui-typo hover:ds-text-ui-typo-primary ds-block ds-truncate")
# print(teams)

# teamsA=teams[0]
# teamsB=teams[1]

# print(teamsA.string)
# print(teamsB.string)


# name = soup.find_all('span', class_= "ds-text-tight-m ds-font-regular ds-text-ui-typo ds-underline ds-decoration-ui-stroke hover:ds-text-ui-typo-primary hover:ds-decoration-ui-stroke-primary ds-block ds-text-ui-typo-mid")
# print(name[0].string)





# f1 =soup.find('div', class_='ds-text-tight-m ds-font-regular ds-text-ui-typo-mid') 
# full = ""
# for item in f1.strings:
#     full = full + item
# print(full)




# teamA_S = ""
# teamB_S = ""
# score = soup.find_all('div', class_= "ds-text-compact-m ds-text-typo-title ds-text-right ds-whitespace-nowrap")
# score1 = soup.find_all('span', class_= "ds-text-compact-s ds-mr-0.5")
# # print(score)
# # print(score1)

# for item in score[0].strings:
#     # print(item)
#     for item1 in score1[0].strings:
#         # print(item1)
#         teamA_S = item1
#     # full = full + item
#     teamA_S =  teamA_S + item

# for item in score[1].strings:
#     # print(item)
#     for item1 in score1[1].strings:
#         # print(item1)
#         teamB_S = item1
#     teamB_S =  teamB_S + item
    
# print(teamA_S)
# print(teamB_S)





# winner = soup.find_all('p', class_= "ds-text-tight-m ds-font-regular ds-truncate ds-text-typo-title")
# print(winner[0].string)
