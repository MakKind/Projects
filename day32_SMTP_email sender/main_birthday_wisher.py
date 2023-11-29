# --------------------- Extra Hard Starting Project ----------------------
#
# - 1. Update the birthdays.csv
#
# - 2. Check if today matches a birthday in the birthdays.csv
#
# - 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
#
# - 4. Send the letter generated in step 3 to that person's email address.
import linecache
import os
import pandas
import smtplib
import datetime as dt
import random


def send_email(name, email):
    my_email = "binmainak883@gmail.com"
    password = "lycd grgs atwc blfn"
    message = get_message(name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday {name}\n\n{message}"
        )


def get_message(name):
    quote = linecache.getline("quotes.txt", random.randint(1, 102))
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", 'r') as file:
        message = file.read()
    message = message.replace("[NAME]", name)
    message = message.replace("Mainak", f"Here is a Quote for you: {quote} \nYours Truly\nMainak")
    return message


now = dt.datetime.now()
month = now.month
day = now.day
birthday = pandas.read_csv("birthdays.csv")
birthday_month_list = birthday["month"].tolist()
birthday_day_list = birthday["day"].tolist()
birthday_name_list = birthday["name"].tolist()
birthday_email_list = birthday["email"].tolist()
for i in range(len(birthday_month_list)):
    if birthday_month_list[i] == month:
        if birthday_day_list[i] == day:
            name = birthday_name_list[i]
            email = birthday_email_list[i]
            send_email(name, email)
