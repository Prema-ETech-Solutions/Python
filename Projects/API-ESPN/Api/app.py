from flask import Flask , jsonify ,request,send_from_directory
import csv
import codecs
from st import *
from flask_cors import CORS
import time
from datetime import datetime
# from flask_ngrok import run_with_ngrok


app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
# run_with_ngrok(app)
@app.route('/upload/csv', methods=['POST'])
def hello(): 
    flask_file = request.files['file']
    name = request.form['txt']
    name = name.upper() + fileName()
    print(name)
    if not flask_file:
        return send_from_directory('../api', "EER.csv",as_attachment=True)
    
    data = []
    stream = codecs.iterdecode(flask_file.stream, 'utf-8')
    for row in csv.reader(stream, dialect=csv.excel):
        if row:
            # print(roe/)
            data.append(row)
    

    count = 0
    data=start(data)
    if data["status"]== True:
        csvCreate(name,data["dataCollection"])
        return send_from_directory('../data-extraction-service/output', "./"+name+".csv",as_attachment=True)       
    else:
        return send_from_directory('../api', "EER.csv",as_attachment=True)
        
     









def fileName():
    fileName_ = ""
    now = datetime.now()
    now = now.strftime("%Y/%m/%d %I:%M:%S")  # 12-hour format.
    fileName_ = fileName_ + "_" + now
    fileName_ = fileName_.replace(":", "-")
    fileName_ = fileName_.replace(" ", "_")
    fileName_ = fileName_.replace("/", "-")
    return fileName_




def csvCreate(file_Name, dataCollection):
    with open(str("../data-extraction-service/output/"+file_Name + ".csv"), "w", newline="") as csvfile:
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
            if Badges.lower() == Player.lower():
                Badges= "POTM"
            else:
                Badges = ""

            

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













if __name__ == '__main__':

    app.run(debug=True)
