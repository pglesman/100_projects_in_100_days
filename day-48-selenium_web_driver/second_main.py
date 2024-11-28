# Scrapping from python.org event dates and names

from selenium import webdriver
from selenium.webdriver.common.by import By

PYTHON_WEBPAGE_LINK = 'https://www.python.org/'

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(PYTHON_WEBPAGE_LINK)

event_dict = {}

for i in range(5):
    time_year = (driver.find_element(By.CSS_SELECTOR, value=f'#content > div > section > div.list-widgets.row > '
                                                            f'div.medium-widget.event-widget.last > div > ul > '
                                                            f'li:nth-child({i + 1}) > time > span')
                 .get_attribute('innerText'))
    time_month_day = (driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li['
                                                          f'{i + 1}]/time').text)
    time = time_year + time_month_day
    name = (driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i + 1}]/a')
            .text)
    event_dict[i] = {'time': time, 'name': name}

print(event_dict)

driver.quit()
