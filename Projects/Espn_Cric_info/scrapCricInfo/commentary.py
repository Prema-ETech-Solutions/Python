import json, urllib.request
import math
from bs4 import BeautifulSoup


def commentaryExt(dataCollection):
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
                        
                    
                    st = ""
                    if apidata["isFour"] == True:
                        st = "FOUR runs"
                        pass
                    elif apidata["isSix"] == True:
                        st = "SIX runs"
                        pass
                    elif apidata["isWicket"] == True:
                        st = "OUT"
                        pass
                    elif apidata["totalRuns"] == 1:
                        st = "1 run"
                        pass
                    elif apidata["totalRuns"] == 2:
                        st = "2 run"
                        pass
                    elif apidata["totalRuns"] == 3:
                        st = "3 run"
                        pass
                    else:
                        pass
                    title = apidata["title"] + ", " + st
                    break

        data["commentary"] = {
        "title": title,
        "commentary": commentary_str,
        }
        dataCollection[index]=data.copy()
