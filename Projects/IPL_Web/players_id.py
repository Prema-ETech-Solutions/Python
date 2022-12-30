from scrap import *
from jsonOperations import *
def scrap_Data(listOfIds):
    
   responseData = {}
   for id in listOfIds:
      link = "https://www.cricbuzz.com/profiles/"+str(id)
      response = start_scrap(link)
      responseData[id] = response
    

   jsonCreate("IPL",responseData)