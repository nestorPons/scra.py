#!usr/bin/python
import mechanicalsoup
import os
from dotenv import load_dotenv
os.system("clear")
load_dotenv()
URL = 'http://localhost/htdocs/additionaldata.html'
USER = os.getenv('USER_URL')
PASS = os.getenv('PASS_URL') 
EMAIL= os.getenv('EMAIL') 
TEL = os.getenv('TEL') 
NAME = os.getenv('NAME') 
SURNAME=os.getenv('SURNAME') 
SURNAMES=os.getenv('SURNAMES') 
CITY=os.getenv('CITY') 
DIR=os.getenv('DIR') 
CP=os.getenv('CP') 
COUNTRY=os.getenv('COUNTRY') 

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)

browser.open(URL)
input_element = browser.page.select_one('input[id="additionaldata"]')
placeholder_value = input_element["placeholder"]

if "teléfono" in placeholder_value:
    input_element["value"] = TEL
elif "apellido" in placeholder_value:
    input_element["value"] = SURNAME   
elif "apellido" in placeholder_value:
    input_element["value"] = SURNAME 
elif "ciudad" in placeholder_value:
    input_element["value"] = CITY 
exit(input_element)