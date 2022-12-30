import pymongo as mogo

if __name__ == "__main__":
    client =mogo.MongoClient("mongodb://localhost:27017") 
    print(client)
    db=client['test']
    col = db['sample']
    dic= {'name' : 'Harry', 'marks': 50}
    col.insert_one(dic)