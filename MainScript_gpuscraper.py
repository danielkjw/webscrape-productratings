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

# req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
# proxies = req_proxy.get_proxy_list() #this will create proxy list

# canada = [] #int is list of Indian proxy
# for proxy in proxies:
#     if proxy.country == 'Canada':
#         canada.append(proxy)


# PROXY = canada[1].get_address()
# webdriver.DesiredCapabilities.CHROME['proxy']={
#     "httpProxy":PROXY,
#     "ftpProxy":PROXY,
#     "sslProxy":PROXY,
#     "proxyType":"MANUAL"
# }


#Subject to change 

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

productweb = open('/product_pages')

chain_object = itertools.chain.from_iterable(plists)
flat_plist = list(chain_object)
# with  open('productreviews1.csv', 'a', encoding='utf-8', newline='\n')
# a if continuing an unfinished job
myFile =  open('productreviews_all.csv', 'w', encoding='utf-8',newline='')
# myFile =  open('productreviews1.csv', 'w', encoding='utf-8',newline='')
writer = csv.writer(myFile, delimiter=',', quotechar='"')
index = 1
count = 1

# clist = flat_plist[64:]
clist = flat_plist
# flat_plist
# Use index to keep track of which URL you left off on ####
for prodlist in clist:
    count = count + 1
    index = index + 1
    print("Scraping Page number " + str(index))
    print("Iteration: ", index)
    print("Current URL: ", prodlist)
    base_url = str(prodlist)
    base_test = r'https://www.newegg.com/asus-geforce-rtx-2080-ti-rog-strix-rtx2080ti-o11g-gaming/p/N82E16814126263?Item=N82E16814126263&quicklink=true'
    # for pr in plists:
    driver.get(base_url)

    
    # .get_text()
    time.sleep(2)
    # Click review button to go to the review section
    wait_review = WebDriverWait(driver, 10)
    time.sleep(2)
    try:
        review_button = wait_review.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#synopsis > div.grpArticle > div > div.grpRating > a')))
        review_button.click()
    except:
        print('review button click error')
        try:
            review_button = driver.find_element_by_css_selector('#Community_Tab > span data-t-e-var78="TAB - Reviews"')
            review_button = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//li[@id="Community_Tab"]')))
            review_button.click()
        except:
            print("no tab review_button to click")
            continue
        continue

    try:
        driver.implicitly_wait(3)
        driver.find_elements_by_xpath('//div[@class="comments-cell has-side-left is-active"]')
        review_wait = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="comments-cell has-side-left is-active"]')))
    except:
        print("no review_wait page")
        continue
    try:
        time.sleep(2)
        review_num = Select(driver.find_element_by_xpath('//*[@id="reviewPageSize"]'))
        review_num.select_by_value('100')
    except:
        print("no page sizes")
        continue

    try:
        # Find all the reviews on the page
        # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'human'))).click()
        Price = driver.find_element_by_xpath('//*[@id="newproductversion"]/span/strong | //*[@id="landingpage-price"]/div/div/ul/li[3]/strong').text
        print("Price",Price)
        time.sleep(2)
        wait_review = WebDriverWait(driver, 10)
        reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="Community_Content"]//div[@class="comments"]//div[@class="comments-cell has-side-left is-active"]')))
        for review in reviews:
            # Initialize an empty dictionary for each review
            review_dict = {}
            try:
                username1 = review.find_element_by_xpath('.//div[@class="comments-name"]//a')
                username = username1.get_attribute('text')
                print('username', username)
                title = review.find_element_by_xpath('.//div[@class="comments-cell-body"]//span[@class="comments-title-content"]').text
                print('title',title)
                print('rating')
                rating = review.find_element_by_xpath('.//div[@class="comments-title"]//i').get_attribute('class')
                print('rating',rating)
                review_date = review.find_element_by_xpath('.//span[@class="comments-text comments-time comments-time-right"]').get_attribute('content')
                print('date',review_date)
                review_time = review.find_element_by_xpath('.//span[@class="comments-text comments-time comments-time-right"]').text
                print('time',review_time)
            except:
                print("error in dictionary or reviews")
                continue 
            try:
                r1 = review.find_element_by_xpath('.//*[@class="comments-cell-body"]//*[@class="comments-cell-body-inner"]//*[@class="comments-cell-body"]//*[@class="comments-content"]').get_attribute('innerText')
                # r2 = review.find_element_by_xpat('.//*[@class="comments-cell-body"]//*[@class="comments-cell-body-inner"]//*[@class="comments-cell-body"]//*[@class="comments-content"]/child::p')
                rev_text = r1

            except:
                print('error r1')
                try:
                    r2 = review.find_elements_by_xpath('.//*[@class="comments-cell-body-inner"]//child::p').text
                    r22 = review.find_elements_by_xpath('.//*[@class="comments-cell-body-inner"]//p/following-sibling::p').text
                    rev_text = r2 + r22
                except:
                    print('error r2')        
                    try:
                        r3 = review.find_elements_by_xpath('.//*[@class="comments-cell-body-inner"]//p').text
                        rev_text = r3
                    except:
                        print('error r3')
                        continue
            
                print("reviews", rev_text)
                prod = base_url.split('/')
                company = prod[3].split('-')[0]
                product = prod[3].replace('-',' ')
                review_dict['id'] = count
                review_dict['Price'] = Price
                print("WRITING PRICE", Price)
                review_dict['Company'] = company
                print("WCompany", company)
                review_dict['Product'] = product
                print("title", title)

                review_dict['title'] = title
                review_dict['rating'] = rating
                review_dict['date'] = review_date
                review_dict['time'] = review_time
                review_dict['reviews'] = rev_text
                review_dict['username'] = username
                writer.writerow((review_dict.values()))
                print("Writing to csv complete.")
                count = count + 1
                # for row in rows:
                #     writr.writerow([row.field1,row.field2,row.field3])
                #     myFile.flush() # whenever you want
                # myFile.close() # when you're done.

    except Exception as e:
        print(e)
        print("error in index area")
        continue

myFile.close()
driver.close()
        
   