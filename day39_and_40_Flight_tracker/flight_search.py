import requests
import datetime as dt

class FlightSearch:

    def __init__(self):
        self.kiwi_url = "https://api.tequila.kiwi.com/locations/query"
        self.kiwi_url_search = "https://api.tequila.kiwi.com/v2/search"
        self.kiwi_header = {
            "apikey": "QBpVMVRrLCndSfc2zN7-T5P1hSTcRoEE"
        }

    def iatacode(self, city):
        kiwi_param = {
            "term": city,
        }
        response_kiwi = requests.get(url=self.kiwi_url, params=kiwi_param, headers=self.kiwi_header)
        response_kiwi.raise_for_status()
        response_dict = response_kiwi.json()
        return response_dict["locations"][0]["code"]

    def get_lowest_price(self, iatacode, your_city_iatacode):
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
        return response.json()["data"][0]["price"]
