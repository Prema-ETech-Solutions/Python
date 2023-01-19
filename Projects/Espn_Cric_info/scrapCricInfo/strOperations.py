from changeDate import *

def TeamsOperations(team):
    team = team.replace('Women', '')
    team = team.replace('Under-19s', '')
    return team
    
def stageOperations(stage):
    temp = stage.lower()
    if temp.find("group")>-1 :
        stage ="Group Stage"
    elif temp.find("semi-final")>-1:
        stage ="Semi Final"
    elif temp.find("quarter-final")>-1:
        stage ="Quarter Final"
    elif temp.find("final")>-1:
        stage ="Final"
    else :
        stage ="Group Stage"

    return stage

def dateOperations(date):
    if date.find("NA") == -1:
        date = date.split('-')
        date = date[0]
    else:
        date =""
    return date

def tournamentOperations(tournament):
    temp = tournament.lower()
    # print(temp)
    if temp.find("icc")==-1 :
        tournament = "ICC "+ tournament
    else:
        pass
    
    return tournament

def remove_first_end_spaces(string0):
    return "".join(string0.rstrip().lstrip())

def Space_(player_list):

    player_list = player_list.replace("[","")
    player_list = player_list.replace("]","")
    player_list =player_list.split(",")
    pl = []
    for x in player_list:
        pl.append(remove_first_end_spaces(x))
    return pl

def rmOv(over):
    over=over.replace("Ov","")
    return over

def Check_Num(val):

    try:
        x =int(val)
        return x
    except ValueError:
        return  False

def Format_Tor(tor,overs):

    tor = tor.replace("Champions Trophy","CT")
    tor = tor.replace("Twenty20", "T20")
    tor = tor.replace("Women's", "W")
    tor = tor.replace("Under-19", "U19")
    tor = tor.replace("  ", " ")
    tor = tor.replace("Cricket World Cup","CWC")
    if tor.find("ICC W") != -1:
        pass
    elif tor.find("ICC World") != -1:
        tor = tor.replace("ICC","ICC Men's")
    else:
        tor = tor.replace("ICC","ICC Men's")
    
    if tor.find("W World Cup") != -1:
        if overs == 50:
            tor = tor.replace("W World Cup","WCWC")

    if tor.find("W T20") != -1:
        tor = tor.replace("W T20","WT20")
    
    if tor.find("World Cup") != -1:
        if overs == 50:
            tor = tor.replace("World Cup","CWC")
        else:
            tor = tor.replace("World Cup","WC")

    if tor.find("W World T20") != -1:
        tor = tor.replace("W World T20","WT20")
        if overs == 50:
            tor = tor.replace("WT20","WT20 CWC")
        else:
            tor = tor.replace("WT20"," WT20 WC")

    if tor.find("World T20") != -1:
        tor = tor.replace("World T20","Men's T20 WC")


    tor = remove_first_end_spaces(tor)

    tor = tor.replace("  "," ")

    return tor

