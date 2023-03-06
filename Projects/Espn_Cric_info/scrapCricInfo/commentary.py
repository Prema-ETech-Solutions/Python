import json, urllib.request
import math
from bs4 import BeautifulSoup
import time


def commentaryExt(dataCollection):
    print("Commentary Scrape")
    time.sleep(5)
    for index in range(len(dataCollection)):
        commentary_str = "N.A"
        title = "N.A"
        data = dataCollection[index]
        if data["serialId"] == "NA" or data["matchId"] == "NA":
            pass
        else:
            Apiurl = (
                "https://hs-consumer-api.espncricinfo.com/v1/pages/match/comments?lang=en&seriesId="
                + str(data["serialId"])
                + "&matchId="
                + str(data["matchId"])
                + "&inningNumber="
                + str(data["momentInning"])
                + "&commentType=ALL&sortDirection=DESC&fromInningOver="
                + str(math.ceil(data["momentBall"]))
            )
            output = urllib.request.urlopen(Apiurl).read()
            output = json.loads(output)
            print("------>com<------->>>"+str(output))
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            print()
            output = output["comments"]

            for y in range(len(output)):
                apidata = output[y]

                if apidata["oversActual"] == data["momentBall"]:
                    commentary_str = apidata["commentTextItems"]
                    if commentary_str != None:
                        # print(commentary_str)
                        commentary_str = commentary_str[0]
                        commentary_str = BeautifulSoup(
                            commentary_str["html"], "html.parser"
                        ).text
                    elif commentary_str == None and apidata["dismissalText"] != None  :
                        commentary_str = apidata["dismissalText"]
                        commentary_str = commentary_str["long"]
                        
                    Moment_Type=""
                    st = ""
                    if apidata["isFour"] == True:
                        st = "FOUR runs"
                        Moment_Type = "Four"
                    elif apidata["isSix"] == True:
                        st = "SIX runs"

                        Moment_Type = "Six"
                        
                    elif apidata["isWicket"] == True:
                        st = "OUT"
                        Moment_Type = "Wicket"
                        
                    elif apidata["totalRuns"] == 1:
                        st = "1 run"
                        Moment_Type = "Single"
                        
                    elif apidata["totalRuns"] == 2:
                        st = "2 runs"
                        Moment_Type = "Double"
                        
                    elif apidata["totalRuns"] == 3:
                        st = "3 runs"
                        Moment_Type = "Triple"    
                    else:
                        Moment_Type = "NA"
                    title = apidata["title"] + ", " + st
                
                
        data["Moment_Type"] = Moment_Type
        data["commentary"] = {
        "title": title,
        "commentary": commentary_str,
        }


        # print(data)
        # print()
        # print()
        # print()
        time.sleep(0.2)
        # print(data)
        dataCollection[index]=data.copy()
