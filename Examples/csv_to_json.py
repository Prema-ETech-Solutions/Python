import csv
import time
import json


def jsonCreate(dataCollection):
    
    with open("one.json",'w') as J:
        json.dump(dataCollection,J)
    print("Created")




def Csv_read():
    
    while True:
        try:
            path = input("Enter the Path :")
            with open(path) as file:
                head =[]
                reader = csv.reader(file)
                count = 0
                print("Reading CSV")
                time.sleep(4)
                data = []
                # tmp = data["rows"]
                for row in reader:
                    if count != 0:
                        
                        dic ={}
                        for index, item in enumerate(row): 
                            dic[head[index]] = item   
                        # tmp.append(row)
                        data.append(dic.copy())
                        count = count + 1
                    else:
                        head= row
                        count = count + 1
                # print([data.copy()])
                return data.copy()
                # Data_Collection.append(data.copy())
            break
        except Exception as e:
            print("Invalid Path")
            print(e)
            print()
            print()
            print()
            continue




def main():
    jsonCreate(Csv_read())    



if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()
