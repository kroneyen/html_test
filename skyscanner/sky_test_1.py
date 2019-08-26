from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
# import datetime
# from selenium.common.exceptions import NoSuchElementException ## show error msg
# import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
# from bs4 import BeautifulSoup
# import re
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select
import pandas as pd

### airport -- KUL , CEB , PEN ,新加坡樟宜 (SIN) 機場, 雅加達 (JKT) 機場
dep = 'tpet'
dest = 'kul'
oym = '&oym=1811'
iym = '&iym=1811'
sel_dep_day='&selectedoday=23'
sel_dest_day='&selectediday=30'
search_ori = ' TPE'
search_dest = ' KUL'
url = 'https://www.skyscanner.com.tw/'
# url_1 ='https://www.skyscanner.com.tw/transport/flights/tpet/cnx/?adults=2&children=0&adultsv2=2&childrenv2=1&infants=1&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1811&iym=1811&ref=home&selectedoday=01&selectediday=01'
url_1 = 'https://www.skyscanner.com.tw/transport/flights/'
# url_2 ='&ref=home&selectedoday=01&selectediday=01'
url_3 = url_1 + dep + '/' + dest + '?adults=2&children=0&adultsv2=2&childrenv2=1&infants=1&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false' + oym + iym + '&ref=home' + sel_dep_day + sel_dest_day
# url_1 ='https://www.skyscanner.com.tw/transport/flights/tpet/cnx/?adults=2&children=0&adultsv2=2&childrenv2=1&infants=1&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1811&iym=1811&ref=home&selectedoday=01&selectediday=07'
# depart_date=' 2018/9/4'
# return_date=' 2018/9/30
depart_year_month = '2018-11'
class_value = 'Economy'
aduits_num = 2
infrant_num = 1
infrant_age = 1

web = webdriver.Chrome('D:\python_dir\chromedriver')  ## for cron path
# web = webdriver.Chrome('/usr/local/bin/chromedriver') ## for cron path
web.get(url)
time.sleep(random.randrange(1, 5, 1))

## choise trip way
"""
try:
     web.find_elements_by_id('fsc-trip-type-selector-return').click() ##return for radio
     print('select trip way  is success')
except:
      print('select trip way  is failed')

time.sleep(random.randrange(1, 3, 1))
"""
## input fields
## ori & dest

try:
    web.find_element_by_id("origin-fsc-search").clear()
    web.find_element_by_id("origin-fsc-search").send_keys(search_ori)
    time.sleep(random.randrange(5, 10, 1))
    web.find_element_by_id("destination-fsc-search").clear()
    web.find_element_by_id("destination-fsc-search").send_keys(search_dest)
    print('ori-dest search is success :', search_ori, ' -- ', search_dest)
except:
    print('ori-dest search is failed')

time.sleep(random.randrange(1, 5, 1))
## trip date
# web.find_element_by_id("monthselector-3VbbW").send_keys(search_dest)


depart_date_form = WebDriverWait(web, 10).until(
    EC.presence_of_element_located((By.ID, "depart-fsc-datepicker-input")))  ## depart from field
depart_date_form.click()

print('select depart_date_form is success')
time.sleep(random.randrange(2, 5, 1))

### into search page
web.get(url_3)
time.sleep(random.randrange(5, 10, 1))
# soup = BeautifulSoup(web.page_source , "html.parser")
# print(soup.prettify())

try:
    WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "bpk-button-zZ0K5 month-view__trip-summary-cta"))).submit()  ## depart from field
    print('search is sucessed')

except:
       print('search is failed')

time.sleep(random.randrange(10, 30, 1))
web.quit()


