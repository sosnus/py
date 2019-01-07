import urllib.request
from random import randint
import json    
body =  { "SensorId": 27, "Value":(randint(8, 25)), "SensorPassword":"sila"}
req = urllib.request.Request("http://0.0.0.0:7071/api/Function1")
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8') 
req.add_header('Content-Length', len(jsondataasbytes))
response = urllib.request.urlopen(req, jsondataasbytes)
print(response.status)
