import datetime as dt
import smtplib
import pandas as pd
import random
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

birthdays = pd.read_csv('birthdays.csv')
birthday_dict = birthdays.to_dict(orient="records")

# Set a variable of the current date
now = dt.datetime.now()
month = now.month
day = now.day

my_email = "BrandonHang.Business@gmail.com"
my_password = ""

for i in range(0, len(birthday_dict)):
    if birthday_dict[i]["month"] == month and birthday_dict[i]["day"] == day:
        letter_number = random.randint(1, 3)
        birthday_person = birthday_dict[i]["name"]
        birthday_person_email = birthday_dict[i]["email"]

        with open(f"letter_templates/letter_{letter_number}.txt", "r") as letter:
            message = letter.read()
            completed_letter = message.replace("[NAME]", birthday_person)

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person_email,
            msg=f"Subject:Happy Birthday!\n\n{completed_letter}")
        connection.close()

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
