from selenium import webdriver
from selenium.webdriver.common.by import By
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
start_time = old_time = time.time()

while True:
    cookie.click()
    if time.time() - old_time > 4:
        old_time = time.time()
        money = int(driver.find_element(By.ID, value='money').text.replace(',', ''))
        max_cost = 0
        index_to_buy = 0
        for i, item in enumerate(items_to_buy):
            item_cost_str = driver.find_element(By.ID, value=f'{item}').text
            item_cost = int(item_cost_str.split("-")[1].split()[0].replace(",", ""))
            if max_cost <= item_cost <= money:
                max_cost = item_cost
                index_to_buy = i
        if max_cost != 0:
            element_id = f'{items_to_buy[index_to_buy]}'
            item_to_click = driver.find_element(By.ID, value=element_id)
            item_to_click.click()

    if time.time() - start_time > 180:
        cookies_per_second = driver.find_element(By.ID, value='cps').text
        print(f'cookies/second {cookies_per_second}')
        break

# driver.quit()
