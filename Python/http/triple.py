import urllib.request
import datetime
from random import randint
import json    
import time
# _login = 26 #20
# _password = "zzzz"   #"eafsef"
# temp = 10
a = [[22, 10, 'zaq', 10], [23, 5, 'xsw', 5], [24, -10, 'cde', -10]]
for x in range(100):
    for y in range(3):
        print("############################################")
        print(datetime.datetime.now())
        a[y][3] += (randint(-20, 20)/10)
        if a[y][3] < 5:
            a[y][3] = 7 + (randint(0, 50)/10)
        if a[y][3] > 30:
            a[y][3] = 25 - (randint(0, 50)/10)
        tempTemp = a[y][3] - a[y][1]
        print(a[y][0], end='  ')
        print(a[y][2], end='  ')
        print(a[y][3]-a[y][1])
        # body =  { "SensorId": _login, "Value":temp, "SensorPassword":_password}
        body =  { "SensorId": a[y][0], "Value": tempTemp, "SensorPassword": a[y][2]}
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
        time.sleep(1)   
