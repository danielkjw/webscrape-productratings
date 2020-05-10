from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
import re

from selenium.common.exceptions import TimeoutException

base_url = "https://www.newegg.com/gigabyte-radeon-rx-5700-xt-gv-r57xtgaming-oc-8gd/p/N82E16814932208?Item=9SIA4P0BAT9461&quicklink=true"
# driver = webdriver.Chrome("chromedriver.exe")

# # driver.execute_script("alert('hello')")
# driver.save_screenshot("test.png")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome("chromedriver.exe",options=options)
# ele = driver.find_elements_by_xpath('//*[@id="module-tableForumTopics"]/div')
driver.get(base_url)
#$$ element selector
# topics = driver.find_elements_by_xpath('//*[@id="module-tableForumTopics"]/div')
specs = driver.find_elements_by_xpath('//*[@id="Specs"]')

# ele.send_keys("reddit")
# ele.send_keys(Keys.RETURN)
[t.text for t in specs]

//*[@id="Community_Tab"]
# try:
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