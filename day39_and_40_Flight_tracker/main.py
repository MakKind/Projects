from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from flight_data import FlightData

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

sheet_data = data_manager.prices
your_city = "Paris"  # User Input here
your_city_iatacode = flight_search.iatacode(your_city)
for element in sheet_data:
    if element["iataCode"] == '':
        element["iataCode"] = flight_search.iatacode(element["city"])
        data_manager.update_sheety(element["id"], element["iataCode"])
    try:
        lowest_price = flight_search.get_lowest_price(element["iataCode"], your_city_iatacode)
    except IndexError as e:
        print("No flights found")
        continue
    if element["lowestPrice"] > lowest_price:
        message = flight_data.get_lowest_flight_details(element["iataCode"], your_city_iatacode)
        print(message)
        notification_manager.send_mail(message)
