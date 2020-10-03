from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

import requests
import urllib
from bs4 import BeautifulSoup
import os
import time
import re
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
import csv
from random import seed
from random import randint
import pandas as pd
import itertools


# Used for other reviews

base_url_list = ["https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814",
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&Page=2",
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=3,"
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=4",
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=5",
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=6",
"https:/`/www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=7",
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=8",      
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=9"]


#webdriver setup #####

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# options.add_argument("--headless")
driver = webdriver.Chrome("chromedriver.exe",options=options)
#driver.get(base_url)
# driver = webdriver.Chrome("chromedriver.exe")

plists = []
print("CWD",os.getcwd())

os.chdir('c:/Users/danie/Python Files/NYCDSA/gpuscraper-project')

with open('productlinks.csv','r') as file:
    line = [str(current_place.rstrip().strip()) for current_place in file.readlines()]
    newlist = [string.strip().split('\n') for string in line if string != ""]
    plists = newlist


chain_object = itertools.chain.from_iterable(plists)
flat_plist = list(chain_object)
index = 1
count = 1

# product_files = open('product_websites22.txt', 'w', encoding='utf-8',newline='\n')
# clist = flat_plist[64:]
clist = flat_plist
# flat_plist
# Use index to keep track of which URL you left off on ####
time.sleep(1)
with open('product_websites.txt','w') as f:
    for prodlist in clist:
        try:
            wait_review = WebDriverWait(driver, 10)
            count = count + 1
            index = index + 1
            print("Scraping Page number " + str(index))
            print("Iteration: ", index)
            print("Current URL: ", prodlist)
            base_url = str(prodlist)
            base_test = r'https://www.newegg.com/asus-geforce-rtx-2080-ti-rog-strix-rtx2080ti-o11g-gaming/p/N82E16814126263?Item=N82E16814126263&quicklink=true'
            # for pr in plists:
            driver.get(base_url)
            time.sleep(2)
            wait_review.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#synopsis > div.grpArticle > div > div.grpRating > a')))
            # html = driver.find_element_by_id("container").get_attribute('outerHTML')
            # print("HTML<", html)
            attrs = BeautifulSoup(driver.page_source, 'html5lib')
            d = attrs.prettify("utf-8")
            f.write(str(d))
            #.prettify("utf-8")
            print(d)
            # product_files.write(attrs)
            time.sleep(1)

    #     # Click review button to go to the review section
            wait_review = WebDriverWait(driver, 10)

        except Exception as e:
            print(e)
            print("error in index area")
            continue
    driver.close()
    f.close()        
    