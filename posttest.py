import requests
import json

url = 'http://localhost:8080/example'
data = {'dollar': 4, 'cents': 34}
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)
print(response)
print(response.text)
print(response.json())
print(type(response))
print(dir(response))