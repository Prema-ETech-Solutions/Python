import csv
import time

def Csv_read():
    
    while True:
        try:
            path = input("Enter the Path :")
            with open(path) as file:
                data = {}
                reader = csv.reader(file)
                count = 0
                print("Reading CSV")
                time.sleep(4)
                data["rows"]= []
                tmp = data["rows"]
                for row in reader:
                    if count != 0:
                        tmp.append(row)
                        count = count + 1
                    else:
                        data["header"] = row
                        count = count + 1
                # print([data.copy()])
                return [data.copy()]
                # Data_Collection.append(data.copy())
            break
        except Exception as e:
            print("Invalid Path")
            print(e)
            print()
            print()
            print()
            continue
            
def Split(Data_Collection , chunks):

    data = Data_Collection[0]
    head = data["header"]
    data = data["rows"]
    # print(data)
    temp = []
    dic = {}
    for item in data: 
        tmp = item
        for index1, item1 in enumerate(tmp):
            dic[head[index1]] = item1
        temp.append(dic.copy()) 

    data = [temp[x:x+chunks] for x in range(0, len(temp), chunks)]    
    for index, item in enumerate(data):
        tmp = item
        with open(str(index)+ ".csv", "w", newline="") as csvfile:
            thewriter = csv.DictWriter(csvfile, fieldnames=head)
            thewriter.writeheader()
            for item1 in tmp:
                thewriter.writerow(item1)
    
    print("Done")

def chunks():
    while True: 
        try:
            x = int(input('Enter an chunks size: '))
            return x
        except ValueError:
            print('Please only input digits')


            


def main():
    Split(Csv_read(),chunks())
    



if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()

