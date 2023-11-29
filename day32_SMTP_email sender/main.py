# import smtplib
#
# my_email = "binmainak883@gmail.com"
# password = "lycd grgs atwc blfn"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="binmainak813@gmail.com",
#         msg="Subject:Hello\n\nThis is the body"
#     )

# import datetime as dt
# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# now = dt.datetime.now()
# print(now)
# year = now.year
# month = now.month
# day = now.day
# weekday = days_of_week[now.weekday()]
# print(year, month, day, weekday)
# DOB = dt.datetime(day=8, month=8, year=1996)
# print(DOB)
# ----------------------------------MONDAY QUOTE MOTIVATION------------------------------------
# import datetime as dt
# import random
# import smtplib
#
# now = dt.datetime.now()
# days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# my_email = "binmainak883@gmail.com"
# password = "lycd grgs atwc blfn"
# if days_of_week[now.weekday()] == "Thursday":
#     # message = linecache.getline("quotes.txt", random.randint(1, 102)) // This line can be used to get the
#     #                                                                       random line from a piece of text
#     with open("quotes.txt") as file:
#         all_quotes = file.readlines()
#         message = random.choice(all_quotes)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="binmainak813@gmail.com",
#             msg=f"Subject:Monday Motivation\n\n{message}"
#         )
