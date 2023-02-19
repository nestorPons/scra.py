#!usr/bin/python
import mechanicalsoup
import os
from dotenv import load_dotenv
os.system("clear")
load_dotenv()
URL = os.getenv('URL')
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
browser.select_form('form')
browser["identifier"] = USER
browser.submit_selected()
print(browser.url)

if 'additionaldata' in browser.url:
    print('ingresando ADDITIONALDATA........................................')
    browser.select_form('form')
    input_element = browser.page.select_one('input[id="additionaldata"]')
    placeholder_value = input_element["placeholder"]

    if "teléfono" in placeholder_value:
        input_element["value"] = TEL
    elif "Apellido" in placeholder_value:
        input_element["value"] = SURNAME   
    elif "Ciudad" in placeholder_value:
        input_element["value"] = CITY 
    elif "Código" in placeholder_value:
        input_element["value"] = CP 

    with open('../logs/additionaldata.log', 'a+') as f:
        f.write(str(placeholder_value) + '\n')
        print('Archivo guardado correctamente.')

    browser.submit_selected()


print('ingresando password...................................')
print(browser.url)
browser.select_form('form')
browser["password"] = PASS
browser.submit_selected()

if browser.url == "https://my.ionos.es:443/eshop-overview":
    print(browser.url)
    link = browser.page.select_one('a[href="/Shop4Redirect?__lf=eshop-connect-domain"]')
    response = browser.follow_link(link)
   
    print('ingresando administracion........................................')
    print(browser.url)
    with open('../htdocs/admin.html', 'w+') as f:
        f.write(str(browser.page))
        print('Archivo ADMIN guardado correctamente.')
    link = browser.page.select_one('a[href="?ViewAction=UnityMBO-ViewCSVExportImportProduct&amp;ObjectID=14191947"]')
    response = browser.follow_link(link)

browser.launch_browser()
print('Salida --------------------------------------')
print(browser.url)
exit()

browser.select_form('form')
additionaldata = browser.form.selec_one('#additionaldata')

browser.follow_link("a.button-primary")
