import urllib.parse
import urllib.request
import json
import codecs

url = 'http://localhost:8000/maradek'

data =json.loads(codecs.open("maradek/data2.json", "r", 'utf-8-sig').read())

params= json.dumps(data).encode('utf-8')

req = urllib.request.Request(url, data=params, headers={'content-type': 'application/json'})
response = urllib.request.urlopen(req)
print(response.read().decode('utf8'))
