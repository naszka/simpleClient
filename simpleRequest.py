import urllib.parse
import urllib.request
import json

url = 'http://127.0.0.1:8000/'

values = {'list' : [3,2,5,6]}

params= json.dumps(values).encode('utf-8')

req = urllib.request.Request(url, data=params, headers={'content-type': 'application/json'})
response = urllib.request.urlopen(req)
print(response.read().decode('utf8'))
