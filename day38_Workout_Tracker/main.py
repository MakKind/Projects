import requests
import datetime as dt

APP_ID = "95c30d94"
APP_KEY = "f469e3186998fa71f9cc419c22695ba3"
DATE = dt.datetime.now().date()
TIME = dt.datetime.now().time()
# EXERCISE = "Ran 1 km and walked 3 min"
EXERCISE = input("EXERCISE: ")

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_parameters = {
    'query': EXERCISE,
}
nutritionix_header = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}
response = requests.post(url=nutritionix_url, json=nutritionix_parameters, headers=nutritionix_header)
response.raise_for_status()
response_dict = response.json()

shetty_url = "https://api.sheety.co/233c09b9cd2e3db5f54c660a1a6311eb/copyOfMyWorkouts/workouts"
shetty_header = {
    'authorization': 'Bearer mainak_secret'
}
for i in response_dict["exercises"]:
    shetty_parameters = {
        "workout": {
            "date": DATE.strftime("%d/%m/%Y"),
            "time": TIME.strftime("%X"),
            "exercise": i["name"],
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
    }
    response_sheety = requests.post(url=shetty_url, json=shetty_parameters, headers=shetty_header)
    print(response_sheety.text)

