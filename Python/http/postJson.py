import urllib.request
import datetime
from random import randint
import json    
import time
_login = 26 #20
_password = "zzzz"   #"eafsef"
temp = 10
for x in range(100):
    print("############################################")
    print(datetime.datetime.now())
    temp += (randint(-20, 20)/10)
    if temp < 5:
        temp = 7 + (randint(0, 50)/10)
    if temp > 30:
        temp = 25 - (randint(0, 50)/10)
    body =  { "SensorId": _login, "Value":temp, "SensorPassword":_password}
    myurl = "https://lorastore20181206101456.azurewebsites.net/api/Measurements"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    print (jsondataasbytes)
    response = urllib.request.urlopen(req, jsondataasbytes)
    print(response.msg, end='  ')
    print(response.status)
    # print(response.read() )
    print("WAIT...")
    time.sleep(2)   
