from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests
import re
from time import sleep

GOOGLE_SHEET_LINK = 'https://forms.gle/td1D5fpxe28pMvq38'
ZILLOW_CLONE_WEBSITE = 'https://appbrewery.github.io/Zillow-Clone/'

# Getting links, prices and addresses from proper website
content = requests.get(ZILLOW_CLONE_WEBSITE)
soup = BeautifulSoup(content.text, 'html.parser')

links_to_property = [i.attrs.get('href') for i in soup.select('div.StyledPropertyCardPhotoBody > a')]
prices_of_property = [re.split(r'[+/]', i.get_text())[0] for i in soup.select('div.StyledPropertyCardDataArea-'
                                                                              'fDSTNn > div > span')]
address_of_property = [i.get_text().strip().replace(' |', ',') for i
                       in soup.select('div.StyledPropertyCardDataWrapper > a > address')]
property_list = [address_of_property, prices_of_property, links_to_property]

# Options for web browser
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GOOGLE_SHEET_LINK)

for i in range(len(links_to_property)):
# for i in range(5):
    answer_inputs = driver.find_elements(By.CSS_SELECTOR, value='div.Xb9hP > input')
    sleep(2)

    for j, answer_input in enumerate(answer_inputs):
        answer_input.send_keys(property_list[j][i])

    send_button = driver.find_element(by=By.CSS_SELECTOR, value="div.lRwqcd > div")
    send_button.click()

    sleep(2)

    new_answer_button = driver.find_element(by=By.CSS_SELECTOR, value=" div.c2gzEf > a")
    new_answer_button.click()

    sleep(2)

    print('Property added to google sheet forms.')

driver.close()
