import requests
import json
test = {"test": "test1"}
headers = {"content-type": "application/json"}
response = requests.post("http://localhost:5200/test", json.dumps(test), headers=headers)

print(response.text)