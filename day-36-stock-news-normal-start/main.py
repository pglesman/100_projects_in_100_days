import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = 'ATVAPBWJHK31MCSN'

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_APIKEY = '9354da1c42e1469883a89a819d920aee'

# Twilio account patryk.glesman86@gmail.com
twilio_account_sid = os.environ["twilio_account_sid"]
twilio_auth_token = os.environ["twilio_auth_token"]
client = Client(twilio_account_sid, twilio_auth_token)

stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': ALPHAVANTAGE_API_KEY,
}

news_parameters = {
    'q': COMPANY_NAME,
    'apiKey': NEWS_APIKEY,
    'sortBy': 'relevancy',
}


def send_message(stock_difference, perc_difference, headline, main_message):
    if stock_difference > 0:
        head = f'{STOCK_NAME}: 🔺{round(100 * perc_difference, 2)}%'
    else:
        head = f'{STOCK_NAME}: 🔻{round(100 * perc_difference, 2)}%'
    body = f'{head}\nHeadline: {headline}\nBrief: {main_message}'
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=body,
        to="whatsapp:+48664993575"
    )
    print(message.status)


def get_perc_diff():
    # STEP 1: Use https://www.alphavantage.co/documentation/#daily
    # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    # Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
    # [new_value for (key, value) in dictionary.items()]
    stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
    stock_data = stock_response.json()
    closing_stock_prices = [value['4. close'] for key, value in stock_data['Time Series (Daily)'].items()]
    yesterday_closing_stock_price = float(closing_stock_prices[0])

    #  Get the day before yesterday's closing stock price
    d_b_yesterday_closing_stock_price = float(closing_stock_prices[1])

    # Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
    # Hint: https://www.w3schools.com/python/ref_func_abs.asp
    price_diff = yesterday_closing_stock_price - d_b_yesterday_closing_stock_price
    abs_price_diff = abs(price_diff)

    # Work out the percentage difference in price between closing price yesterday and closing price the day before
    # yesterday.
    percentage_diff = abs_price_diff / yesterday_closing_stock_price
    # print(percentage_diff)
    return percentage_diff, price_diff


perc_diff, stock_change = get_perc_diff()

# If percentage is greater than 5 then print("Get News").
if perc_diff > 0.02:
    # STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_data = news_response.json()

    # Use Python slice operator to create a list that contains the first 3 articles.
    # Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    news_list = news_data['articles'][:3]

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # Create a new list of the first 3 articles headline and description using list comprehension.
    news_headlines = [dictionary['title'] for dictionary in news_list]
    news_descriptions = [dictionary['description'] for dictionary in news_list]

    # Send each article as a separate message via Twilio.
    for i in range(len(news_headlines)):
        send_message(stock_change, perc_diff, news_headlines[i], news_descriptions[i])

# Optional Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
coronavirus market crash.
"""
