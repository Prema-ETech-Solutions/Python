raw = []

# Input Links / all inputs
def Raw_links():

    while(True):
        data = {}
        link = ""
        link = input('Enter Links Espn-Cric-info:')
        
        # Checking input for null
        if link: 
            # Checking espncricinfo link
            if(link.split(".")[1] =="espncricinfo"):
                pass
            else:
                print("Invalid link !!!")
                continue

        else:
            break



        # Serial ID 
        Serialid = link.split("/")
        Serialid=Serialid[4].split("-")
        Serialid =Serialid[-1]

        # Match ID
        matchID = link.split("/")
        matchID=matchID[5].split("-")
        matchID =matchID[-1]


        # commentary Over
        valid =False
        while not valid:
            try:
                over_in =float(input("Enter over"))
                valid = True 
            except ValueError:
                print('Please only input digits')
        
        # inningNumber input
        valid =False
        while not valid:
            try:
                inningNumber =int(input("Enter Inning Number"))
                if(inningNumber == 1):
                    valid = True
                elif(inningNumber == 2):
                    valid = True
                else:
                    print("Enter The 1 OR 2 ")
            except ValueError:
                print('Please only input digits')
        
        # dictionary 
        data['link']=link
        data['serialid']=Serialid
        data['matchid']=matchID
        data['over_in']=over_in
        data['inningNumber']=inningNumber
        raw.append(data.copy())

    print(raw)


    

# Start
if __name__ == "__main__":
    Raw_links()
