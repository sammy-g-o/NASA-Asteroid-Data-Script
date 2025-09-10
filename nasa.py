import json
from pathlib import Path
from requests import get

response = get("https://api.nasa.gov/neo/rest/v1/neo/3542519?api_key=kQHNg9ccXn7k7KGWV5JtZyORabwhWlKXeXO8p2lQ")
print("The name of the asteroid: ",response.json()["name"])
print("Is the asteroid potentially dangerous: ",response.json()["is_potentially_hazardous_asteroid"])
print(response.json()["close_approach_data"][0]["orbiting_body"])

response = get("https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=kQHNg9ccXn7k7KGWV5JtZyORabwhWlKXeXO8p2lQ")

data = json.dumps(response.json())
Path("allasteroiddata.json").write_text(data)

asid = 3542519
apikey = "kQHNg9ccXn7k7KGWV5JtZyORabwhWlKXeXO8p2lQ"
response = get(f"https://api.nasa.gov/neo/rest/v1/neo/{asid}?api_key={apikey}")
l = response.json()
print("The name of the asteroid: ",response.json()["name"])
print("Is the asteroid potentially dangerous: ",response.json()["is_potentially_hazardous_asteroid"])
print(response.json()["close_approach_data"][0]["orbiting_body"])
