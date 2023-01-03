import requests
import os
from twilio.rest import Client

api_key=os.environ.get("OWM_API_KEY")
OWM_Endpoint="https://api.openweathermap.org/data/3.0/onecall"

weather_params={
	"lat": 36.73,
	"lon": -119.78,
	"exclude": "current,minutely,daily",
	"appid": api_key
}

response=requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data=response.json()

will_rain = False

for i in range(0,12):
	id = weather_data["hourly"][i]["weather"][0]["id"]
	if id < 700:
		will_rain=True

if will_rain:
	account_sid = 'AC90d0da15a4e51801a75729a6d3e75781'
	auth_token = os.environ.get("AUTH_TOKEN") 
	client = Client(account_sid, auth_token)

	message = client.messages \
					.create(
						 body=f"It is going to rain! Bring an umbrella",
						 from_='+18302754848',
						 to='+15593009564'
					 )
