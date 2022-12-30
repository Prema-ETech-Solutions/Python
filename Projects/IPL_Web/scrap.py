import requests
from bs4 import BeautifulSoup

def start_scrap(link):
    elm = {}
    json = {}

    content =requests.get(link)
    html_con = content.content
    # print(type(html_con))
    soup = BeautifulSoup(html_con, "html.parser") 
    div = soup.find_all(
            "table",
            class_="table cb-col-100 cb-plyr-thead",
            )
    p_name =soup.find_all(
            "h1",
            class_="cb-font-40",
            )
    p_name = BeautifulSoup(str(p_name[0]), "html.parser")
    p_name =p_name.text
    content = list(div)
    # print(content[0])
    html_con =str(content[0])
    elm["Batting"] = table_Data(html_con)
    html_con =str(content[1])
    elm["Bowling"]=table_Data(html_con)

    # {
    # print(elm)
    # print(p_name)
    # json[p_name] = elm
    # }
    return elm.copy()
    


def table_Data(html_con):
    heading = []
    data = []
    
    soup =BeautifulSoup(html_con, "html.parser")
    head =soup.find_all("tr",class_="cb-bg-grey cb-font-12")
    head =BeautifulSoup(str(head[0]), "html.parser")
    head =head.find_all("th")
    for at in head:
        if(at.get('title') != None):
            heading.append(at.get('title'))
    
    body = soup.find_all("tbody")
    body =BeautifulSoup(str(body[0]), "html.parser")
    body=body.find_all("tr")
    for val in body:
        l1 = val.text
        l1 = l1.split()
        if(l1[0]== "IPL"):
            data = l1.copy()
    
    heading.insert(0,"Series")
    return Dic(heading,data)
    

def Dic(heading,data):
    json = {}
    # print(heading)
    # print(data)


    if heading[2] == "No of Innings Batted":
        if data:
            json["matches"] = data[1]
            json["innings"] = data[2]
            json["balls"] = 0
            json["overs"] = 0
            json["runs"] = data[4]
            json["wickets"] = 0
            json["bestinning"] = ""
            json["bestmatch"] = ""
            json["econ"] = ""
            json["average"] = data[6]
            json["strike"] = data[8]
            json["wicket4i"] = 0 
            json["wicket5i"] = 0 
            json["wicket10m"] = 0
            json["mattrick"] = 0
            json["expensive_over_runs"] = 0 
        else:
            json["matches"] = 0
            json["innings"] = 0
            json["balls"] = 0
            json["overs"] = 0
            json["runs"] = 0
            json["wickets"] = 0
            json["bestinning"] = ""
            json["bestmatch"] = ""
            json["econ"] = ""
            json["average"] = ""
            json["strike"] = ""
            json["wicket4i"] = 0 
            json["wicket5i"] = 0 
            json["wicket10m"] = 0
            json["mattrick"] = 0
            json["expensive_over_runs"] = 0

          
    elif heading[2] == "No of Innings Bowled":
        if data:
            json["matches"] = data[1]
            json["innings"] = data[2]
            json["balls"] = data[3]
            json["overs"] = 0
            json["runs"] = data[4]
            json["wickets"] = data[5]
            json["bestinning"] = data[6]
            json["bestmatch"] = data[7]
            json["econ"] = data[8]
            json["average"] = data[9]
            json["strike"] = data[10]
            json["wicket4i"] = 0 
            json["wicket5i"] = data[11]
            json["wicket10m"] = data[12]
            json["hattrick"] = 0
            json["expensive_over_runs"] = 0 
        else:
            json["matches"] = 0
            json["innings"] = 0
            json["balls"] = 0
            json["overs"] = 0
            json["runs"] = 0
            json["wickets"] = 0
            json["bestinning"] = ""
            json["bestmatch"] = ""
            json["econ"] = ""
            json["average"] = ""
            json["strike"] = ""
            json["wicket4i"] = 0 
            json["wicket5i"] = 0 
            json["wicket10m"] = 0
            json["mattrick"] = 0
            json["expensive_over_runs"] = 0

    
    # for index, item in enumerate(heading):
        


    #     if data != []:
    #         pass

            # if index == 0:
            #     json[item] = data[index]
            # elif index == 1:
            #     json[item.replace(" ","_")] = data[index]
            # else:
            #     temp = item.replace("No of ","")
            #     temp = temp.replace(" ","_")
            #     json[temp] = data[index]
    # print(json)
    return json.copy()
        
    

        
    

     