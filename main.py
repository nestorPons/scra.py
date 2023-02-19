from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
import time
import utils

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
FOLDER_DOWNLOAD=os.getenv('FOLDER_DOWNLOAD')
folder_db=os.getenv('FOLDER_DB')
files = ['Productos.csv', 'tarifa_003461S.csv']

# move_file(FOLDER_DOWNLOAD, FOLDER_DB, ['Productos.csv', 'tarifa_003461S.csv'])

#utils.print_csv(FOLDER_DB, files)
#utils.get_title(FOLDER_DB, files)
utils.get_dialect(folder_db, files)