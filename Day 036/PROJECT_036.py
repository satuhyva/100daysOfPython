import requests
from secrets import alpha_vantage_api_key, news_org_api_key, twilio_phone_number, twilio_account_sid, \
    twilio_account_token
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={alpha_vantage_api_key}"
stock_response = requests.get(stock_url)
stock_response.raise_for_status()
stock_price_data = stock_response.json()["Time Series (Daily)"]
today = datetime.now()
yesterday = (today - timedelta(1)).strftime('%Y-%m-%d')
day_before = (today - timedelta(2)).strftime('%Y-%m-%d')

yesterday_close = float(stock_price_data[yesterday]["4. close"])
day_before_close = float(stock_price_data[day_before]["4. close"])
difference_percentage = (day_before_close - yesterday_close) / day_before_close * 100
print(
    f"Difference in {STOCK} stock closing price between {yesterday} and {day_before} was {difference_percentage:.1f}%.")
if abs(difference_percentage) >= 5.0:
    print("Difference is more than 5%, so GET NEWS!")
else:
    print("Difference is below 5%, so don't get the news.")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

news_url = ("https://newsapi.org/v2/everything")
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "from": (datetime.now() - timedelta(3)).strftime('%Y-%m-%d'),
    "sortBy": "publishedAt",
    "apiKey": news_org_api_key
}

news_response = requests.get(news_url, news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
latest_3_articles = news_data["articles"][0:3]

emoji = ("🔺", "🔻")[difference_percentage < 0.0]
message_to_phone = f"{COMPANY_NAME} stock price change {emoji} {abs(difference_percentage):.1f}%\n\n"
for article in latest_3_articles:
    message_to_phone += f"{article['title']}:\n{article['description']}\n\n"
print(message_to_phone)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


# Costs a lot!
# client = Client(twilio_account_sid, twilio_account_token)
# message = client.messages.create(
# body=message_to_phone,
# from_=twilio_phone_number,
# to='+358503810631'
# )


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
