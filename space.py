import requests
response : requests.Response   = requests.get("http://api.open-notify.org/astros.json")
json : str = response.json()   
print(json)   
