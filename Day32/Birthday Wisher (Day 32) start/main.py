# import smtplib

# my_email = "BrandonHang.Business@gmail.com"
# my_password = ""

# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="brandonhang34@outlook.com",
#     msg="Subject:Hello\n\nThis is the body of my email")
# connection.close()


import datetime as dt
import smtplib
import random


now = dt.datetime.now()
day_of_week = now.weekday()

quotes = []
with open("quotes.txt", "r") as data:
    quotes = (data.readlines())

random_quote = random.choice(quotes)

my_email = "BrandonHang.Business@gmail.com"
my_password = ""

if day_of_week == 6:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="brandonhang34@outlook.com",
        msg=f"Subject:Quote\n\n{random_quote}")
    connection.close()
