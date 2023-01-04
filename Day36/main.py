import requests
import os
from datetime import date

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_api_key = os.environ.get("STOCK_AUTH_TOKEN")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key = os.environ.get("NEWS_AUTH_TOKEN")


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

current_date = date.today()

stocks_params={
	"function": "TIME_SERIES_DAILY_ADJUSTED",
	"symbol": STOCK,
	"apikey": stock_api_key,
}

stocks_response = requests.get(STOCK_ENDPOINT, params=stocks_params)
stocks_response.raise_for_status()
stocks_data = stocks_response.json()
today_open_stock = stocks_data["Time Series (Daily)"]
print(today_open_stock)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

#get the current date using datetime

news_params={
	"from": current_date,
	"to": current_date,
	"q": COMPANY_NAME,
#	"apiKey": news_api_key,
	"apiKey": "dc5ea2ffd0ff47c9b73e32fc5939e3e9"
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
articles = []
for i in range(0,3):
	articles.append(news_data["articles"][i]["title"])
print (articles)

print (current_date)

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

