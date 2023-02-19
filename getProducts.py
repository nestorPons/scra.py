#!usr/bin/python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time

os.system("clear")
load_dotenv()
URL = os.getenv('URL_IONOS')
USER = os.getenv('USER_IONOS')
PASS = os.getenv('PASS_IONOS')  
EMAIL= os.getenv('EMAIL') 
TEL = os.getenv('TEL') 
NAME = os.getenv('NAME') 
SURNAME=os.getenv('SURNAME') 
SURNAMES=os.getenv('SURNAMES') 
CITY=os.getenv('CITY') 
DIR=os.getenv('DIR') 
CP=os.getenv('CP') 
COUNTRY=os.getenv('COUNTRY') 

FOLDER_DOWNLOADS=COUNTRY=os.getenv('FOLDER_DOWNLOADS') 
#-----------
browser = webdriver.Firefox()
browser.get(URL)

# Obtener el identificador de las pestañas abiertas
timelimit = 20

username_input =  WebDriverWait(browser, timelimit).until(
EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))
)
username_input.send_keys(USER)

next_button = WebDriverWait(browser, timelimit).until(
EC.presence_of_element_located((By.XPATH, "//button[@id='button--with-loader']"))
)
next_button.click()

input_password =  WebDriverWait(browser, timelimit).until(
EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
)
input_password.send_keys(PASS)

next_button = WebDriverWait(browser, timelimit).until(
EC.presence_of_element_located((By.XPATH, "//button[@id='button--with-loader']"))
)
next_button.click()

next_link = WebDriverWait(browser, timelimit).until(
EC.presence_of_element_located((By.XPATH, "//a[@class='button-primary']"))
)
next_link.click()
EC.presence_of_element_located((By.XPATH, "//a[@class='button-primary']"))
time.sleep(3)

# Cambiar a la pestaña recién abierta
browser.switch_to.window(browser.window_handles[1])

next_link = WebDriverWait(browser, timelimit).until(
EC.presence_of_element_located((By.XPATH, "//li[@class='menu-settings hasChildren']"))
)
next_link.click()

next_link = WebDriverWait(browser, timelimit).until(
EC.presence_of_element_located((By.XPATH, "//a[@href='?ViewAction=UnityMBO-ViewCSVExportImportProduct&ObjectID=14191947']"))
)
next_link.click()

#FIN obtención de productos 
