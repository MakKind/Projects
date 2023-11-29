import time
import smtplib
import requests
import datetime as dt


def sendmail():

    my_email = "binmainak883@gmail.com"
    password = "lycd grgs atwc blfn"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="binmainak813@gmail.com",
            msg="Subject:ISS Viewing opputtunity!!!\n\nGet out and check the sky for ISS"
        )


now = dt.datetime.now()
ss_url = "https://api.sunrise-sunset.org/json"
iss_now_url = "http://api.open-notify.org/iss-now.json"
MY_LATITUDE = 23.881428
MY_LONGITUDE = 91.267345
parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}
ss_response = requests.get(url=ss_url, params=parameters)
ss_response.raise_for_status()
data = ss_response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

while sunrise > now.hour or now.hour > sunset:
    iss_response = requests.get(url=iss_now_url)
    iss_data = iss_response.json()
    iss_response.raise_for_status()
    latitude = float(iss_data["iss_position"]["latitude"])
    longitude = float(iss_data["iss_position"]["longitude"])
    if MY_LATITUDE+5 <= latitude <= MY_LATITUDE+5 and MY_LONGITUDE+5 <= longitude <= MY_LONGITUDE-5:
        sendmail()
    print("test")
    time.sleep(60)
