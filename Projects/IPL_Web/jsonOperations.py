import json
def jsonCreate(file_Name,dataCollection):
    
    with open(file_Name+".json",'w') as J:
        json.dump(dataCollection,J)
    print(file_Name +".json"+ " Created")