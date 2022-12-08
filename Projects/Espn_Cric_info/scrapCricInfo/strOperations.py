from changeDate import *

def TeamsOperations(team):
    if(team.find("Under-19s")>-1):
        team = team.replace('Under-19s', '')
    return team
    

def stageOperations(stage):
    temp = stage.lower()
    if temp.find("group")>-1 or temp.find("quarter-final")>-1:
        stage ="Group Stage"
    elif temp.find("semi-final")>-1:
        stage ="Semi - Final"
    return stage

def dateOperations(date):
    if date.find("NA") == -1:
        date = date.split('-')
        date = date[0]
    else:
        date =""
    return date