# Scrapping from https://en.wikipedia.org/wiki/Main_Page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

web_link = 'https://en.wikipedia.org/wiki/Main_Page'

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get(web_link)

# Find an element and print it text and also click it
articles_nr = driver.find_element(By.CSS_SELECTOR, value='#articlecount > a:nth-child(1)')
print(articles_nr.text)
# articles_nr.click()

# Find a link by text and click it
all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# all_portals.click()

# Finding the search input by name and sending keyboard input to Selenium
search = driver.find_element(By.NAME, value='search')
search.send_keys('Python')
search.send_keys(Keys.ENTER)

# driver.quit()
