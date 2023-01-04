from datetime import datetime
import re
import csv
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display

URL = 'https://sanpinetwork.com/'

display = Display(visible=0, size=(800, 600))
display.start()

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
chrome_options = uc.ChromeOptions()
driver = uc.Chrome(service=chrome_service, options=chrome_options)
driver.get(url=URL)
buyPrice = WebDriverWait(driver=driver, timeout=20.0).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/section[1]/div[1]/ul/li[1]/strong'))).text
sellPrice = WebDriverWait(driver=driver, timeout=20.0).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/section[1]/div[1]/ul/li[2]/strong'))).text
data = []
utc_datetime = datetime.utcnow()
intTime = utc_datetime.timestamp()
data.append(intTime)
data.append(re.sub(r'[^0-9]', '', buyPrice))
data.append(re.sub(r'[^0-9]', '', sellPrice))
with open('price.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(data)
