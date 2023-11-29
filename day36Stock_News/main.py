import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

STOCK = "AAPL"
COMPANY_NAME = "Apple"
Change = 0


def check_news(up):
    news_api = "fef58e1bdac94cbe9fef24d7b2d28dfc"
    news_url = "https://newsapi.org/v2/everything"
    parameters_news = {
        "qInTitle": COMPANY_NAME,
        "apiKey": news_api
    }
    news = requests.get(url=news_url, params=parameters_news)
    news.raise_for_status()
    news_data = news.json()["articles"][:3]
    send_mail(news_data, up)


def send_mail(a, up):
    my_email = "binmainak883@gmail.com"
    password = "lycd grgs atwc blfn"
    act_change = abs(round((t_minus_1-t_minus_2)/t_minus_2, 3))
    formatted_news = [f"Headline: {i['title']}. \n Breif: {i['description']}" for i in a]
    for i in formatted_news:
        i = i.encode('utf-8')
        if up:
            arrow = f"Subject:{STOCK}: +{act_change}%\n\n{i}"
        else:
            arrow = f"Subject:{STOCK}: -{act_change}%\n\n{i}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="binmainak813@gmail.com",
                msg=arrow
            )


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_api = "SY6UD3QUA7A6HHM9"
stock_url = "https://www.alphavantage.co/query"
parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api
}

stock = requests.get(url=stock_url, params=parameters_stock)
stock.raise_for_status()
stock_data = stock.json()
time_series = stock_data["Time Series (Daily)"]
dates = [value for (key, value) in time_series.items()]
t_minus_1 = float(dates[0]["4. close"])
t_minus_2 = float(dates[1]["4. close"])
if t_minus_1 >= t_minus_2 * (1 + Change / 100):
    check_news(True)
elif t_minus_1 <= t_minus_2 * (1 - Change / 100):
    check_news(False)
