import requests
import re
import base64
import json

address = "http://10.33.102.2:12001"
session = requests.Session()
response = session.get(address)
gakure = set()

for i in range(150):
    cookie = re.split('\.', session.cookies.get_dict()['session'])[0]
    try:
        pad = len(cookie) % 4
        cookie += "=" * pad
        decodedBytes = base64.urlsafe_b64decode(cookie)
    except:
        continue
    decodedStr = str(decodedBytes, "utf-8")
    jsStr = json.loads(decodedStr)['task']
    gakure.add(jsStr)
    response = session.get(address, params={"answer": jsStr})
print(response.text)
print(gakure)
