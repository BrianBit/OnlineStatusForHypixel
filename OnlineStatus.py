import win32api
import win32con
import requests
from bs4 import BeautifulSoup

name = input("PlayerIGN ")
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

while 1<2:
    r = requests.get("https://plancke.io/hypixel/player/stats/"+name,headers=headers)
    page = r.text
    soup = BeautifulSoup(page,"html.parser")
    
    
    if soup.find_all(string = "Offline"):
        status = "Offline"
    elif soup.find_all(string = "Player does not exist!"):
        status = "Player does not exist!"
    else:
        status = "Online"

    if status == "Online":
        win32api.MessageBox(0,name+" is Online right now!","OnlineStatus",win32con.MB_ICONEXCLAMATION)
        break
    
    if status == "Player does not exist!":
        win32api.MessageBox(0,"Player does not exist!","OnlineStatus",win32con.MB_ICONEXCLAMATION)
        break
    
    print(status)
    
