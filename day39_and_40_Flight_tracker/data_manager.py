import requests


class DataManager:
    def __init__(self):
        self.shetty_url = "https://api.sheety.co/233c09b9cd2e3db5f54c660a1a6311eb/copyOfFlightDeals/prices"
        self.shetty_header = {
            'authorization': 'Bearer Mainak_Secret'
        }

        self.sheety_data = requests.get(url=self.shetty_url, headers=self.shetty_header).json()
        self.prices = self.sheety_data["prices"]

    def update_sheety(self, row_id, iatacode):
        shetty_url = self.shetty_url + "/" + str(row_id)
        shetty_put = {
          "price": {
                  "iataCode": iatacode
          }
        }
        updated_row = requests.put(url=shetty_url, json=shetty_put, headers=self.shetty_header)
        updated_row.raise_for_status()

