import requests
z = {'number': 12524, 'type': 'issue', 'action': 'show'}
# adr = "http://bugs.python.org"
adr = "https://lorastore20181206101456.azurewebsites.net/api/Measurements"
r = requests.post(adr, data=z)
print(r.status_code, r.reason)