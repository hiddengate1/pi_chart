from datetime import datetime
import re
import csv
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

URL = 'https://sanpinetwork.com/'

options = uc.ChromeOptions()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
driver = uc.Chrome(options=options)
driver.implicitly_wait(10.0)
driver.get(url=URL)
driver.get_screenshot_as_file("screenshot.png")
buyPrice = driver.find_element(by=By.XPATH, value='//*[@id="container"]/section[1]/div[1]/ul/li[1]/strong').text
sellPrice = driver.find_element(by=By.XPATH, value='//*[@id="container"]/section[1]/div[1]/ul/li[2]/strong').text
data = []
utc_datetime = datetime.utcnow()
intTime = utc_datetime.timestamp()
data.append(intTime)
data.append(re.sub(r'[^0-9]', '', buyPrice))
data.append(re.sub(r'[^0-9]', '', sellPrice))
with open('price2.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(data)
