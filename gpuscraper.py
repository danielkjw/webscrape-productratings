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
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=7",
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=8",      
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=9"]


#webdriver setup #####

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome("chromedriver.exe",options=options)
# driver.get(base_url)
plists = []

os.chdir('./gpuscraper-project')
with open('productlinks.txt', 'r') as file:
    for i in file:
        string = i + ', '
        plists.append(string)
plists



base_test = r'https://www.newegg.com/asus-geforce-rtx-2080-ti-rog-strix-rtx2080ti-o11g-gaming/p/N82E16814126263?Item=N82E16814126263&quicklink=true'
# for pr in plists:
driver.get(base_test)
time.sleep(2)
# Click review button to go to the review section
wait_review = WebDriverWait(driver, 10)
time.sleep(2)
review_button = wait_review.until(EC.presence_of_element_located((By.XPATH,'//div[@class="grpRating"]')))
review_button.click()
try:
    !driver.find_element_by_xpath('//li[id="Community_Tab"]').isEmpty()


review_wait = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="comments-cell has-side-left is-active"]')))
review_num = Select(driver.find_element_by_xpath('//*[@id="reviewPageSize"]'))
review_num.select_by_value('100')

# review_num = Select(driver.find_element_by_xpath('//*[@id="reviewPageSize"]'))

csv_file = open('productreviews.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
index = 1

try:
    print("Scraping Page number " + str(index))
    index = index + 1
    # Find all the reviews on the page
    time.sleep(2)
    wait_review = WebDriverWait(driver, 10)
    reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="comments-cell has-side-left is-active"]')))
    for review in reviews:
        # Initialize an empty dictionary for each review
        review_dict = {}

        # driver.execute_script("arguments[0].scrollIntoView(true);", review)
        # Use relative xpath to locate the title, text, username, date, rating.
        # Once you locate the element, you can use 'element.text' to return its string.
        # To get the attribute instead of the text of each element, use 'element.get_attribute()
        try:
            username = review.find_element_by_xpath('.//div[@class="comments-name"]').text
            title = review.find_element_by_xpath('.//div[@class="comments-title-content"]').text
            rating = review.get_attribute(('.//div[@class="comments-title"]/i'))
            review_date = review.find_element_by_xpath('.//span[@class="comments-text comments-time comments-time-right"]/').text
            review_time = review.find_element_by_xpath('.//span[@class="comments-text comments-time comments-time-right"]/').text
            try:
                pros = review.find_element_by_xpath('.//div[@class="comments-cell-body"]//div[class="comments-content"]/p[0]').text
                cons = review.find_element_by_xpath('.//div[@class="comments-cell-body"]//div[class="comments-content"]/p[1]').text
                overview = review.find_element_by_xpath('.//div[@class="comments-cell-body"]//div[class="comments-content"]/p[1]').text
            except:
                overview = review.find_element_by_xpath('.//div[@class="comments-cell-body"]//div[class="comments-content"]/p').text
                continue
        except:
            continue
        
        # driver.execute_script("arguments[0].scrollIntoView(true);", review)
       
    
        # username = review.find_element_by_xpath('.//span[@class="padLeft6 NHaasDS55Rg fontSize_12 pad3 noBottomPad padTop2"]').text
        # date_published = review.find_element_by_xpath('.//span[@class="NHaasDS55Rg fontSize_12  pad3 noBottomPad padTop2"]').text
        # rating = review.find_element_by_xpath('.//span[@class="positionAbsolute top0 left0 overflowHidden color_000"]').get_attribute('style')
        # rating = int(re.findall('\d+', rating)[0])/20

        review_dict['name'] = name
        review_dict['title'] = title
        review_dict['rating'] = rating
        review_dict['date'] = review_date
        review_dict['time'] = review_time
        review_dict['pros'] = pros
        review_dict['cons'] = cons
        review_dict['overview'] = overview
        review_dict['username'] = username
        

        writer.writerow(review_dict.values())    
except:
    print('error')
    csv_file.close()
    driver.close()
    # break
        # OPTIONAL PART 1a
        # Attempts to click the "read more" button to expand the text. This needs to be clicked
        # a second time otherwise the button click in the next review will collapse the previous
        # review text (and won't expand the current text).

        # We also need to scroll to the review element first because the button is not in the current view yet.
        


        # writer.writerow(review_dict.values())

# print(PROXY)
# wait_review = WebDriverWait(driver, 10)
# reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,
#                             '//div[@class="row border_grayThree onlyTopBorder noSideMargin"]')))

# wait_review = WebDriverWait(driver, 10)
# reviews_tab = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="Community_Tab"]')))
# reviews_tab.click()
# reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,
# 									'//*[@class="comments"]')))

# while True:
#     try:
#         print("in first try block")
#         try:
#             popup = WebDriverWait(driver, 3).until(driver.find_element_by_css_selector('body > div.newegg-feedback'))
#             popup.find_element_by_class_name("fa fa-close centerPopup-close").click()
#         except:
#             print('error on first try')
#             driver.close()
            
        
#         try:
#             print("price block")
#             price = WebDriverWait(driver, 3).until(driver.find_element_by_xpath('//*[@id="newproductversion"]/span/strong'))
#             print(price)
#         except:
#             continue
#     except:
#         print('last except')
#         break

#     driver.close()
#     break

#         # topics = driver.find_elements_by_xpath('//*[@id="module-tableForumTopics"]/div')
#         try:
#             print("spec block")
#             specs = WebDriverWait(driver, 3).until(driver.find_elements_by_xpath('//*[@id="Specs"]'))
#             soup = BeautifulSoup(specs, "html.parser")
#             print([t.text for t in soup])
#         except Exception as e:
#             continue
#         # ele.send_keys("reddit")
#         # ele.send_keys(Keys.RETURN)
        
#     except Exception as e:
#         print(e)
#         #csv_file.close()
#         driver.close()
#         break

## try:
#     wait_button = WebDriverWait(driver, 10)
#     next_button = wait_button.until(EC.presence_of_element_located((By.CSS_SELECTOR,'reviewPageSize')))
# except:
#     pass

# if(driver.find_elements_by_class_name("pagination--current") != 1):
#     select = Select(driver.find_element_by_xpath('//*[@id="Community_Content"]/div[6]/div/label'))
#     select.select_by_value('100')

#next.click()

# def get_comment_count(driver, url):
#     driver.get(url)
#     class_name = 'content-banner__title'
#     name = driver.find_element_by_class_name(class_name).text
#     e = driver.find_element_by_id('disqus_thread')
#     disqus_iframe = e.find_element_by_tag_name('iframe')
#     iframe_url = disqus_iframe.get_attribute('src')

# driver.get(iframe_url)
# wait = WebDriverWait(driver, 5)
# commentCountPresent = presence_of_element_located(
#     (By.CLASS_NAME, 'comment-count'))
# wait.until(commentCountPresent)
 
# comment_count_span = driver.find_element_by_class_name(
#     'comment-count')
# comment_count = int(comment_count_span.text.split()[0])