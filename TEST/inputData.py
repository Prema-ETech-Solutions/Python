import requests

from bs4 import BeautifulSoup


Played={}
content =requests.get("https://www.espncricinfo.com/series/icc-under-19-world-cup-2013-14-700273/australia-under-19s-vs-west-indies-under-19s-2nd-quarter-final-700391/full-scorecard")
html_con = content.content
# print(type(html_con))
soup = BeautifulSoup(html_con, "html.parser") 
# print(soup)
Played_Players = {}


Tables = soup.find_all(
            "div",
            class_="ds-rounded-lg ds-mt-2",
            )
# print(Table[0])
t1 = Tables[0]
t2 = Tables[1]
# print(t1)


t1 = BeautifulSoup(str(t1), "html.parser") 
t1 = t1.find_all(
            "span",
            class_="ds-text-title-xs ds-font-bold ds-capitalize",
            )

t1 = BeautifulSoup(str(t1), "html.parser")
team_a = t1.text

t1 = BeautifulSoup(str(Tables[0]), "html.parser")
# print(t1)
t1 = t1.find_all(
            "div",
            class_="ds-p-0",
            )
print(t1[0])
t1_full = BeautifulSoup(str(t1), "html.parser")

print()







