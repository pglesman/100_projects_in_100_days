from selenium import webdriver
from selenium.webdriver.common.by import By

TEST_LINK = 'https://appbrewery.github.io/instant_pot/'

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(TEST_LINK)

price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole').text
price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction').text
print(f'{price_dollar}.{price_cents}')

# driver.close()  # close a tab
# driver.quit()  # close a browser
