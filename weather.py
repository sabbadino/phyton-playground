import requests
from typing import Any
try:
    response : requests.Response   = requests.get("http://api.open-notify.org/astros.json")
    if response.status_code != 200:
        print(f"Error: {response.status_code} {response.text} ")
        exit()  
    json: Any = response.json()   
    #for person in json["people"]:
     #   print(person["name"])   

# navigating on json / dictionary 
    print(json.get("people")[0].get("name"))

except Exception as e:
    print(f"general error {e}")     
