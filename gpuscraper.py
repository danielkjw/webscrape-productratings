from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import requests
import urllib
from bs4 import BeautifulSoup
import os
import time
import re
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy

base_url_list = ["https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814",
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&Page=2",
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=3,"
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=4",
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=5",
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=6",
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=7",
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=8",      
"https://www.newegg.com/p/pl?N=100007709%20601292088%20601292090%204111%204112%204113%204114%204115%204814&page=9"]


req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list

# proxies[0].get_address()
# proxies[0].country
PROXY = proxies[0].get_address()
webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "proxyType":"MANUAL"
}

wait = WebDriverWait(driver, 10)
element = wait.until(
        at_least_n_elements_found((By.CLASS_NAME, 'my_class'), 3)
)


canada = [] #int is list of Indian proxy
for proxy in proxies:
    if proxy.country == 'Canada':
        canada.append(proxy)





# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
# driver = webdriver.Chrome(options=options)
# # driver.get(base_url)

# # driver.get(base_url)
# # driver = webdriver.Chrome("chromedriver.exe")
# driver.get('https://www.expressvpn.com/what-is-my-ip')

# print(PROXY)


# from selenium.common.exceptions import TimeoutException

# base_url = "https://www.newegg.com/asus-geforce-rtx-2080-ti-rog-strix-rtx2080ti-o11g-gaming/p/N82E16814126263?&quicklink=true"

# curDir = os.getcwd()
# print(curDir)
# # driver = webdriver.Firefox('geckodriver.exe')
# # os.path.join(curDir, "/geckodriver.exe")

# # # driver.execute_script("alert('hello')")
# # driver.save_screenshot("test.png")




# # ,options=options)
# # ele = driver.find_elements_by_xpath('//*[@id="module-tableForumTopics"]/div')
# #driver.get(base_url)
# #$$ element selector
# reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,
#                             '//div[@class="row border_grayThree onlyTopBorder noSideMargin"]')))
                            
# wait_review = WebDriverWait(driver, 10)
# 		wait_review = WebDriverWait(driver, 10)
# 		reviews_tab = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,
# 									'//*[@id="Community_Tab"]')))
# 		reviews_tab.click()
 
# 		reviews = wait_review.until(EC.presence_of_all_elements_located((By.XPATH,
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