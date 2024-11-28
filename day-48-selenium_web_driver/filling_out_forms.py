from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

web_link = 'https://secure-retreat-92358.herokuapp.com/'

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get(web_link)

first_name = driver.find_element(By.NAME, value='fName')
last_name = driver.find_element(By.NAME, value='lName')
email_address = driver.find_element(By.NAME, value='email')
sign_up = driver.find_element(By.CSS_SELECTOR, value='body > form > button')

first_name.send_keys('Patryk')
last_name.send_keys('Glesman')
email_address.send_keys('pg@gmail.com')
time.sleep(10)
sign_up.send_keys(Keys.ENTER)

# driver.quit()