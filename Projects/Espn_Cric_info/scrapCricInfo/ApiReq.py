import json, urllib.request


def PLAYER_INFORMATION(dataCollection):

    for index in range(len(dataCollection)):
        data = dataCollection[index]
        player = data["Player"] 
        player = player.replace(" ","")
        player = player.replace("  ","")
        player = player.replace("-","")
        player = player.replace("(c)","")
        start = "https://api.fancraze.com/v1/latestSalesInAGroup/"
        Apiurl = start+player+"1"+"?limit=1"
        try:
            output = urllib.request.urlopen(Apiurl).read()
            output = json.loads(output)
            output=output["data"]
            output= output[0]
            output=output["momentId"]
            output=output["momentGroupId"]
            nftClass =output["nftClass"]
            output=output["metaData"]
            team=output["team"]
            playerSkills=output["playerSkills"]
            playerLevel=output["playerLevel"]
            meta = {}
            meta["nftClass"] = nftClass
            meta["team"] = team
            meta["playerSkills"] = playerSkills
            meta["playerLevel"] = playerLevel
            data["meta"] = meta.copy() 
            print(data)
        except Exception as e:
            meta = {}
            meta["nftClass"] = "NA"
            meta["team"] = "NA"
            meta["playerSkills"] = "NA"
            meta["playerLevel"] = "NA"
            data["meta"] = meta.copy() 
            print(e)
        
        
        


