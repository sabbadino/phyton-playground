import requests
from typing import Any
try:
    response : requests.Response   = requests.get("http://api.open-notify.org/astros.json")
    json: Any = response.json()   
    for person in json["people"]:
        print(person["name"])   
except Exception as e:
    print(e)     
