import requests
import smtplib

MY_LATITUDE = 21.90
MY_LONGITUDE = 77.89
api_key = '358b3c0a4b060108b173b4e6e65318a4'
weather_url = 'https://api.openweathermap.org/data/2.5/forecast'
parameter = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": api_key,
    "cnt": 4,
}

weather = requests.get(url=weather_url, params=parameter)
weather.raise_for_status()
data = weather.json()
will_rain = False
for hour in data["list"]:
    if int(hour["weather"][0]["id"]) < 700:
        will_rain = True
if will_rain:
    my_email = "binmainak883@gmail.com"
    password = "lycd grgs atwc blfn"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="binmainak813@gmail.com",
            msg="Subject:Rain Predictor\n\nIt will rain today. Bring an umbrella"
        )
    print("Mail Sent")


