import requests
import json
from random import randint
body =  { "SensorId": 30, "Value":11, "SensorPassword":"aaa"}
# x =  '{ "SensorId":"27", "Value":23, "SensorPassword":"sila"}'
dane = json.loads(body)
print(dane)
adr = "https://lorastore20181206101456.azurewebsites.net/api/Measurements"
r = requests.post("https://lorastore20181206101456.azurewebsites.net/api/Measurements", data=dane)
print(r.status_code, r.reason)
print(r.text)


# x =  '{ "name":"John", "age":30, "city":"New York"}'
# dane = "{ 'SensorId': 1, 'Value': 24, 'SensorPassword': 'temp1a'}"
# temp = 10 + (randint(0, 200)/10)