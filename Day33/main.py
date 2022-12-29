import json
import requests
import smtplib
import time
from datetime import datetime

MY_LAT= 36.737797
MY_LONG= -119.787125

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    longitude = float(response.json()["iss_position"]["longitude"])
    latitude = float(response.json()["iss_position"]["latitude"])

    iss_position = (longitude, latitude)
    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lng": MY_LONG,
        "lat": MY_LAT,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params =parameters)
    response.raise_for_status()
    data=response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(sunrise)

    time_now = datetime.now().hour
    if sunset >= time_now and sunrise <= time_now:
        return True
    
while True:
    time.sleep(60)    
    if is_iss_overhead() == True and is_night()==True:
        my_email = "BrandonHang.Business@gmail.com"
        my_password = "xbcmekeilocmixzi"

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="brandonhang34@outlook.com",
            msg="Look Up\n\nThe ISS is above you in the sky.")
        connection.close()