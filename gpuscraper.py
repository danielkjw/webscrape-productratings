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

count = 1
for prodlist in flat_plist:
    csv_file = open('productreviews.csv', 'a', encoding='utf-8', newline='\n')
    writer = csv.writer(csv_file)
    writer.writerow(['brand', 'model','GPUSeries', 'gpu', 'Chipset_Manufacturer','Core_Clock','Memory','Memory_Type','Price','Features','title', 'rating','date','time','reviews','username'])
    index = 1
    print("Iteration: ", count)
    print("Current URL: ", prodlist)
    base_url = str(prodlist)
    base_test = r'https://www.newegg.com/asus-geforce-rtx-2080-ti-rog-strix-rtx2080ti-o11g-gaming/p/N82E16814126263?Item=N82E16814126263&quicklink=true'
    # for pr in plists:
    driver.get(base_url)
    time.sleep(2)
    # Click review button to go to the review section
    wait_review = WebDriverWait(driver, 10)
    time.sleep(2)
    try:
        review_button = wait_review.until(EC.presence_of_element_located((By.XPATH,'//div[@class="grpRating"]')))
        review_button.click()
    except:
        try:
            review_button = driver.find_elements_by_xpath('//div[@class="rn-navSections fix"]//li[@id="Community_Tab"]')
            review_button.click()
        except:
            print("no buttons to click")
            continue
    review_wait = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="comments-cell has-side-left is-active"]')))
    try:
        review_num = Select(driver.find_element_by_xpath('//*[@id="reviewPageSize"]'))
        review_num.select_by_value('100')
    except:
        print("no page sizes")
        continue
    try:
        print("Scraping Page number " + str(index))
        index = index + 1
        # Find all the reviews on the page
        time.sleep(2)
        try:
            specbox = driver.find_element_by_xpath('//*[@id="detailSpecContent"]//*[@id="Specs"]/fieldset')
            Price = specbox.find_element_by_xpath('//*[@id="newproductversion"]/span/strong').text
            print("Price",Price)
            #product = driver.find_element_by_xpath('//*h1[@id="grpDescrip_h"]//span[@id="grpDescrip_14-932-208"]').get_attribute('text')
            # model = specbox.find_element_by_xpath('//fieldset//dt[text()="Model"]//dd').text
            # Chipset_Manufacturer = specbox.find_element_by_xpath('//*dt[text()="Chipset Manufacturer"]//dd').text
            # GPUSeries =specbox.find_element_by_xpath('.//*dt[text()="GPU Series"]//dd').text
            # gpu = specbox.find_element_by_xpath('.//*dt[text()="GPU"]//dd').text
        except:
            print('spec data error')
            continue

        wait_review = WebDriverWait(driver, 10)
        reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="Community_Content"]//div[@class="comments"]//div[@class="comments-cell has-side-left is-active"]')))
        for review in reviews:
            # Initialize an empty dictionary for each review
            review_dict = {}
            # driver.execute_script("arguments[0].scrollIntoView(true);", review)
            # Use relative xpath to locate the title, text, username, date, rating.
            # Once you locate the element, you can use 'element.text' to return its string.
            # To get the attribute instead of the text of each element, use 'element.get_attribute()
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
                try:
                    r1 = review.find_element_by_xpath('.//div[@class="comments-content"]/p[1]').text
                    r2 = review.find_element_by_xpath('.//div[@class="comments-content"]/p[2]').text
                    r3 = review.find_element_by_xpath('.//div[@class="comments-content"]/p[3]').text
                    reviews = r1 + r2 + r3
                    print("reviews", reviews)
                except:
                    try:
                        r1 = review.find_element_by_xpath('.//div[@class="comments-content"]//p[1]').text
                        r2 = review.find_element_by_xpath('.//div[@class="comments-content"]//p[2]').text
                        r3 = review.find_element_by_xpath('.//div[@class="comments-content"]//p[3]').text
                        reviews = r1 + ";" + r2 + ";" + r3
                        print("reviews", reviews)
                    except:
                        continue
                
            except:
                print("error in review")
                continue

            # review_dict['brand'] = brand
            # review_dict['model'] = model
            # review_dict['GPUSeries'] = GPUSeries
            # review_dict['gpu'] = gpu 
            review_dict['Price'] = Price
            # review_dict['Features'] = Features
            review_dict['title'] = title
            review_dict['rating'] = rating
            review_dict['date'] = review_date
            review_dict['time'] = review_time
            review_dict['reviews'] = reviews
            review_dict['username'] = username
            # writer.writerow(['title', 'rating','date','time','reviews','username'])
            writer.writerow(review_dict.values())
            print("Writing to csv complete.")
            count +=1    
    except:
        print('error')
        csv_file.close()
        driver.close()
        break