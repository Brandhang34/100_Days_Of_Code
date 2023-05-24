import requests
import os
from datetime import date
from datetime import timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_api_key = os.environ.get("STOCK_AUTH_TOKEN")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key = os.environ.get("NEWS_AUTH_TOKEN")


def getArticles():
	news_params = {
		"from": current_date,
		"to": current_date,
		"q": COMPANY_NAME,
		"apiKey": news_api_key,
	}

	news_response = requests.get(NEWS_ENDPOINT, params=news_params)
	news_response.raise_for_status()
	news_data = news_response.json()
	articles = []
	for i in range(0,3):
		dict = {}
		title = news_data["articles"][i]["title"]
		description = news_data["articles"][i]["description"]
		dict["title"] = title
		dict["description"] = description
		articles.append(dict)
	
	return articles

def sendMessage (list_of_articles, percentage):
	account_sid = 'AC90d0da15a4e51801a75729a6d3e75781'
	auth_token = os.environ.get("AUTH_TOKEN")
	client = Client(account_sid, auth_token)
	
	if percentage >= 0:
		print(type(list_of_articles))
	for article in list_of_articles:
		title=article["title"]
		description=article["description"]
		if percentage > 5:
			message = client.messages.create(
								body=f"\n{STOCK}:🔺{percentage}%\n\nHeadline:{title}\n\nBrief:{description}",
								from_='+18302754848',
								to='+15593009564',
								)
		elif percentage < -5:
			message = client.messages.create(
								body=f"\n{STOCK}:🔻{percentage}%\n\nHeadline:{title}\n\nBrief:{description}",
								from_='+18302754848',
								to='+15593009564',
								)





## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

current_date = str(date.today())
previous_day_date = str(date.today() - timedelta(days=5))
day_before_previous_day_date = str(date.today() - timedelta(days=6))

print(current_date)
print(previous_day_date)

stocks_params={
	"function": "TIME_SERIES_DAILY_ADJUSTED",
	"symbol": STOCK,
	"apikey": stock_api_key,
}

stocks_response = requests.get(STOCK_ENDPOINT, params=stocks_params)
stocks_response.raise_for_status()
stocks_data = stocks_response.json()

#get todays open stock price and yesterdays closing stock price
today_open_stock = float(stocks_data["Time Series (Daily)"][current_date]["1. open"])
yesterday_closing_stock = float(stocks_data["Time Series (Daily)"][previous_day_date]["4. close"])
day_before_yesterday_closing_stock = float(stocks_data["Time Series (Daily)"][day_before_previous_day_date]["4. close"])

price_diff = yesterday_closing_stock - day_before_yesterday_closing_stock

percentage = round((price_diff/yesterday_closing_stock)  * 100, 2)

print("percentage" , percentage)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

#get the current date using datetime
if percentage > 5 or percentage < -5:
	articles = getArticles()
	sendMessage(articles, percentage)
## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

