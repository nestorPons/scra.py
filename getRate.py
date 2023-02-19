import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
os.system("clear")
load_dotenv()

driver = webdriver.Firefox()

URL_RATE = os.getenv('URL_RATE')

driver.get(URL_RATE)


alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()

time.sleep(5)

driver.quit()