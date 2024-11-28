import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

MY_EMAIL = os.environ['MY_EMAIL']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
YAHOO_EMAIL = 'pglesman@yahoo.com'
TEST_LINK = 'https://appbrewery.github.io/instant_pot/'
AMAZON_LINK = ''

headers = {
    'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/130.0.0.0 Safari/537.36',
}

content = requests.get(TEST_LINK, headers=headers)
soup = BeautifulSoup(content.text, 'html.parser')

price_whole = int(soup.find(class_='a-price-whole').get_text().strip('.'))
price_fraction = int(soup.find(class_='a-price-fraction').get_text())
price = price_whole + price_fraction/100

# Get a user-friendly name of a product
product_name = ' '.join(soup.find(id='productTitle').get_text().split(maxsplit=4)[:4])
# print(f'{name}')

if price < 100:
    message = f'{product_name} is now ${price}!\nLink to a product:\n{TEST_LINK}'

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=YAHOO_EMAIL,
            msg=f'Subject:Amazon Price Alert!\n\n{message}'
        )
    print('Mail with price alert was sent successfully!')
