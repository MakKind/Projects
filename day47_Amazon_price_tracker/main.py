import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

target_price = 8500
item_url = ("https://www.amazon.in/Sleepwell-Mattress-Profiled-Reversible-Layered/dp/B0BRQ75ZJY/ref=sr_1_1?crid"
            "=27BXXUWMGN4Z0&keywords=Sleepwell+Dual+PRO+Profiled+Foam+Reversible+5-inch+Double+Bed+Size%2C+Gentle+and"
            "+Firm%2C+Triple+Layered+Anti+Sag+Foam+Mattress+%28Grey%2C+72x48x5%29&nsdOptOutParam=true&qid=1701586259"
            "&sprefix=%2Caps%2C239&sr=8-1")
response = requests.get(item_url, headers={"User-Agent": "Defined"})
response.raise_for_status()
website_text = response.text
soup = BeautifulSoup(website_text, "lxml")
item_price = soup.find(class_="a-price-whole").getText().strip(".").split(",")
price = int(item_price[0]+item_price[1])
if price < target_price:

    my_email = "binmainak883@gmail.com"
    password = "lycd grgs atwc blfn"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="binmainak813@gmail.com",
            msg=f"Subject:Amazon Price alert\n\nYour item of {price} is below the target price of {target_price}. "
                f"Please buy now at {item_url}"
        )
