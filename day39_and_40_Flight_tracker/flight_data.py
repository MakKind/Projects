import requests
import datetime as dt


class FlightData:
    def __init__(self):
        self.kiwi_url = "https://api.tequila.kiwi.com/locations/query"
        self.kiwi_url_search = "https://api.tequila.kiwi.com/v2/search"
        self.kiwi_header = {
            "apikey": "QBpVMVRrLCndSfc2zN7-T5P1hSTcRoEE"
        }

    def get_lowest_flight_details(self, iatacode, your_city_iatacode):
        tommorow = (dt.datetime.now() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        six_months = (dt.datetime.now() + dt.timedelta(days=180)).strftime("%d/%m/%Y")
        kiwi_json = {
            "fly_from": your_city_iatacode,
            "fly_to": iatacode,
            "date_from ": tommorow,
            "date_to ": six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP"
        }
        response = requests.get(url=self.kiwi_url_search, params=kiwi_json, headers=self.kiwi_header)
        response.raise_for_status()
        price = response.json()["data"][0]["price"]
        DCN = response.json()["data"][0]["cityFrom"]
        DAIC = response.json()["data"][0]["flyFrom"]
        ACN = response.json()["data"][0]["cityTo"]
        ACIC = response.json()["data"][0]["cityCodeTo"]
        OD = response.json()["data"][0]["local_departure"].split("T")[0]
        ID = response.json()["data"][0]["route"][-1]["local_departure"].split("T")[0]
        message = f'Price Alert! Only £{price} to fly from {DCN}-{DAIC} to {ACN}-{ACIC}, from {OD} to {ID}'
        return message
