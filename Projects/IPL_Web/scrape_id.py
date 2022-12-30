import requests




def scrape_id(pnames):
    json = {}
    for name in pnames:
        temp = []
        # print(name)
        if name == "Mahendra Singh Dhoni":
            temp.append("ms")
            temp.append("Dhoni")
        else:
            temp = name.split(" ")
        url = "https://www.cricbuzz.com/api/search/results?q="+str(temp[0])+"%20"+str(temp[1])
        response = requests.get(url)
        data = response.json()
        data=data["playerList"]
        data =data[0]
        name= name.replace(" ","_")
        json[name]=data["id"]
    return json.copy()
        
        

   