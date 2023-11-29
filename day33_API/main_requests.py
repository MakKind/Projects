import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
response.raise_for_status()

data = response.json()
latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])
# print(data["iss_position"])
position = (latitude, longitude)
print(position)


