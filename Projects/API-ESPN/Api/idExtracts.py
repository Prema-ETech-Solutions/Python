import time

def idExt(dataCollection):
    print("Serial Id & Match Id")
    time.sleep(4)

    for index in range(len(dataCollection)):
        dic = dataCollection[index]
        
        serialId = dic["espnLink"].split("/")
        serialId = serialId[4].split("-")
        serialId = serialId[-1]

        matchID = dic["espnLink"].split("/")
        matchID = matchID[5].split("-")
        matchID = matchID[-1]

        try:
            int(serialId)            
        except ValueError:
            serialId= "NA"
            
        
        try:
            int(matchID)
        except ValueError:
            matchID= "NA"

        dic["serialId"] = serialId
        dic["matchId"] = matchID
        dataCollection[index] =dic.copy()
