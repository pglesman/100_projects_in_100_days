from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

web_link = 'https://orteil.dashnet.org/experiments/cookie/'

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
driver.get(web_link)

cookie = driver.find_element(By.ID, value='cookie')
items_to_buy = ['buyCursor', 'buyGrandma', 'buyFactory', 'buyMine', 'buyShipment', 'buyAlchemy lab', 'buyPortal',
                'buyTime machine']

cursor = driver.find_element(By.CSS_SELECTOR, value=f'#buyCursor b').text.split()[-1]
print(cursor)