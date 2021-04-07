#!/usr/bin/python3


from urllib.error import HTTPError
from urllib.request import Request
from urllib.request import urlopen
import os
import sys
import time
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from pyfiglet import Figlet
from contextlib import closing



# Selenium libraries

from selenium import webdriver
from selenium.webdriver.common.keys import Keys






URL_PLUSVALIA = 'https://www.plusvalia.com/inmuebles-ordenado-por-variacionporcentual-descendente.html'
URL_REAL_STATE = 'https://ecuadorbienesraices.com/'




def banner():
    f = Figlet(font = 'slant')
    print(f.renderText("Payload present."))



def use_selenium():
    driver = webdriver.Firefox()
    driver.get(URL_PLUSVALIA)
    element = driver.find_element_by_name('div')
    print(element)









def  main():

    time.sleep(0.5)
    banner()        
    print("something")
    stack = []
    try:

        
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/76.0.3809.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

        
        request = Request(url= URL_REAL_STATE, headers=headers)
        with closing(urlopen(request).read()) as f:

            base = BeautifulSoup(f, 'html.parser')
            data_parsed = base.findAll('div', {'class': 'mh-grid__1of3'})

            for x in data_parsed:   
                
                if x.get_text() != '':
                    #print(x.get_text())
                    stack.append(x.get_text().decode('utf-8'))

            pprint(stack)
    except Exception as e:
        print(e)

def sessions():


    req = requests.session()
    req_get = req.get(URL_PLUSVALIA, headers={'User-Agent': 'Mozilla/5.0'})
    print(req_get.status_code)




if __name__ == '__main__':
    main()








