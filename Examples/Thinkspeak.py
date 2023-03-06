import json, urllib.request
from random import *

def Think(val):


    key = "44I2P6SLIFEABHUE"
    url ="https://api.thingspeak.com/update?api_key="+key+"&field1="+str(val)
    try:
        output = urllib.request.urlopen(url).read()
        output = json.loads(output)
        # print(output)
    except:
        print("Error")

if __name__ == "__main__":
    val = 0 
    while(True):
        val = val+1
        Think(randint(1, 100))
        print(val)

