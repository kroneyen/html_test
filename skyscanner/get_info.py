# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup

url = 'https://www.skyscanner.com.tw/transport/flights/tpet/kul/181123/181130/?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&ref=home'
web = webdriver.Chrome('D:\python_dir\chromedriver') ## for cron path
web.get(url)

time.sleep(random.randrange(10, 20, 1))

###flight_info

table_asia_from = WebDriverWait(web, 120).until(EC.presence_of_element_located((By.CLASS_NAME, "Ticket__card-2RuB- result card")))
print('**********table_asia_list:*************' )
for table_asia in table_asia_from :
    print('table_asia:',table_asia)
    print(' ----------------')
    print('                 ')


####most_popular_frame airport
"""
table_asia_from = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='most_popular_frame']/div[2]/div/div[1]/table")))
table_asia_list = table_asia_from.find_elements_by_tag_name('a')
i =0
print('**********table_asia_list:*************' )
for table_asia in table_asia_list :
 airport_name = table_asia.get_attribute('innerHTML').split('<span class="label">機場</span>')
 print( airport_name[0])
 i = i +1

"""

time.sleep(random.randrange(1, 5, 1))
web.quit()