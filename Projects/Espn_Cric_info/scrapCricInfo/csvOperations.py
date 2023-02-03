from strOperations import *
import csv
import time


def csvCreate(file_Name, dataCollection):
    with open(file_Name + ".csv", "w", newline="") as csvfile:
        fieldnames = [
            "SR. NO.",
            "Entity PId's",
            "Name",
            "Role",
            "Rarity",
            "Jersey no",
            "Moment Type",
            "Licensor",
            "Player's Team",
            "Moment Inning",
            "Moment Ball/Over",
            "Team A",
            "Team A Score",
            "Overs A",
            "Team B",
            "Team B Score",
            "Overs B",
            "Date",
            "Match Number",
            "Match Stage",
            "Tournament",
            "Badges",
            "Moment Description",
            "Moment Commentary",
            "Opposite player name",
            "slugname",
            "Photos",
            "Pack Name",
            "ESPN Link",
            "Photos Checked",
            "Photos Comments",
            "Player Level",
            "NFT Quality",
            "NFT Class",
            "Verified By",
        ]
        thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
        thewriter.writeheader()
        count = 0
        for x in range(len(dataCollection)):
            data = dataCollection[x]
            # print("------------->",data)
            temp = {}
            Over = data["Overs"]
            meta = data["meta"]
            teams = data["teams"]
            score = data["score"]
            
            
            count=count + 1
            
            Score_A = score["Score_A"]
            if "/" in Score_A:
                pass
            else:
                Score_A = Score_A + "/10"
            


            Score_B = score["Score_B"]
            if "/" in Score_B:
                pass
            else:
                Score_B = Score_B + "/10"
            

            


            num = "".join(filter(lambda i: i.isdigit(), data["match_no"]))
            if num:
                pass
            else:
                num = ""
            

            
            tor = (
                dateOperations(data["date"])
                + " "
                + tournamentOperations(data["tournament"])
            )
            tor = Format_Tor(tor, data["actual"])
            

            Badges = data["Badges"]
            Player = data["Player"]
            Badges = ""
            if Badges.lower() == Player.lower():
                Badges= "POTM"
            

            

            commentary = data["commentary"]
            ball = str(data["momentBall"])
            if commentary["commentary"] == None:
                tmp = ball + ", " + commentary["title"]
            else:
                tmp = (
                    ball
                    + ", "
                    + commentary["title"]
                    + " "
                    + commentary["commentary"].capitalize()
                )
            
            role =meta["playerSkills"]
            role = role.capitalize()



            temp["SR. NO."] = count
            temp["Entity PId's"] = ""
            temp["Name"] = data["Player"]
            temp["Role"] = role
            temp["Rarity"] =""
            temp["Jersey no"] =""
            temp["Moment Type"] =data["Moment_Type"]
            temp["Licensor"] ="ICC"
            temp["Player's Team"] =TeamsOperations(meta["team"])
            temp["Moment Inning"] =data["momentInning"]
            temp["Moment Ball/Over"] =data["momentBall"]
            temp["Team A"] =TeamsOperations(teams["teamA"])
            temp["Team A Score"] = Score_A
            temp["Overs A"] = rmOv(Over["teamA_Ov"])
            temp["Team B"] = TeamsOperations(teams["teamB"])
            temp["Team B Score"] = Score_B
            temp["Overs B"] = rmOv(Over["teamB_Ov"])
            temp["Date"] = data["date"]
            temp["Match Number"] = num
            temp["Match Stage"] = stageOperations(data["stage"])
            temp["Tournament"] = tor
            temp["Badges"] = Badges
            temp["Moment Description"] = ""
            temp["Moment Commentary"] = tmp 
            temp["Opposite player name"] = ""
            temp["slugname"] = ""
            temp["Photos"] = ""
            temp["Pack Name"] = ""
            temp["ESPN Link"] = data["espnLink"]
            temp["Photos Checked"] = ""
            temp["Player Level"] = meta["playerLevel"]
            temp["NFT Quality"] = ""
            temp["NFT Class"] = meta["nftClass"]
            temp["Verified By"] = ""

            thewriter.writerow(temp)
            # temp["Player's Team"] = TeamsOperations(data["Players_Team"])
            # print("======>>>>>>>",temp)
        print(file_Name + ".csv" + " Created")


def csvRead(dataCollection):

    while True:
        try:
            path = input("Enter the Path :")
            # path = "C:\Users\Faze Technologies\Downloads\Flash_.csv"
            with open(path) as file:
                data = {}
                reader = csv.reader(file)
                count = 0
                print("Reading CSV")
                time.sleep(4)
                for row in reader:
                    if count != 0:
                        link = row[0]
                        if link:
                            # Checking espncricinfo link
                            if "espncricinfo" in link:
                                pass
                            else:
                                link = "N A"

                        else:
                            continue

                        momentInning = "NA"
                        temp = row[1]
                        if temp == "1" or temp == "2":
                            momentInning = int(temp)
                        else:
                            print("Invalid Moment Inning !!" + momentInning)
                            continue

                        momentBall = "N A"
                        try:
                            tmp = str(row[2])
                            tmp = tmp.split(".")
                            if int(tmp[1]) > 0 and int(tmp[1]) < 7:
                                momentBall = float(row[2])
                        except:
                            print("Invalid Moment Ball !!" + momentBall)
                            continue
                        Player = "N A"
                        try:

                            Player = str(row[3])
                            Player = Player.replace("(vc)","")
                            Player =remove_first_end_spaces(Player)
                        except:
                            print("Player Name In-valid" + row[3])
                            continue

                        # print(link)
                        # print(momentBall)
                        # print(momentInning)
                        data["espnLink"] = link
                        data["momentBall"] = momentBall
                        data["momentInning"] = momentInning
                        data["Player"] = Player
                        print(data)
                        print()
                        print()
                        print()
                        time.sleep(0.1)
                        dataCollection.append(data.copy())
                    else:
                        count = count + 1
                break

        except Exception as e:
            # print(path)
            print("Invalid Path")
            print(e)
            print()
            print()
            print()
            time.sleep(2)
            continue
