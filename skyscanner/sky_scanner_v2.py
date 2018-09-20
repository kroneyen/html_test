
from selenium import webdriver
import time
#import datetime
#from selenium.common.exceptions import NoSuchElementException ## show error msg
#import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
#from bs4 import BeautifulSoup
#import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
#import pandas as pd

url = 'https://www.skyscanner.com.tw'
#url = 'https://www.skyscanner.net/'
search_ori = ' TPE'
search_dest = ' CNX'
sel_depart_calendar_month = '2018-11'
sel_return_calendar_month = '2018-11'
sel_depart_day = '23'
sel_return_day = '29'

web = webdriver.Chrome('D:\python_dir\chromedriver') ## for cron path
web.get(url)
time.sleep(random.randrange(1, 5, 1))


try:
     #web.find_element_by_id("origin-fsc-search").clear()
     #origin_fsc_search_from = web.find_element_by_id("origin-fsc-search")
     origin_fsc_search = web.find_element_by_id("origin-fsc-search")
     #.send_keys(search_ori)
     ActionChains(web).move_to_element(origin_fsc_search).click(origin_fsc_search).send_keys_to_element(origin_fsc_search,search_ori).perform()
     time.sleep(random.randrange(5, 10, 1))

     #destination_fsc_search_from = web.find_element_by_id("destination-fsc-search")
     destination_fsc_search = web.find_element_by_id("destination-fsc-search")
     ActionChains(web).move_to_element(destination_fsc_search).click(destination_fsc_search).send_keys_to_element(destination_fsc_search,search_dest).perform()
     time.sleep(random.randrange(5, 10, 1))
     #web.find_element_by_id("destination-fsc-search").clear()
     #web.find_element_by_id("destination-fsc-search").send_keys(search_dest)
     print('ori-dest search is success :' ,search_ori , ' -- ' , search_dest)
except:
      print('ori-dest search is failed')

time.sleep(random.randrange(1, 5, 1))



depart_date_form = web.find_element_by_id("depart-fsc-datepicker-input")  ## depart from field
#depart_date_form.click()
ActionChains(web).move_to_element(depart_date_form).click(depart_date_form).perform()
time.sleep(random.randrange(3, 5, 1))
## select month
#depart_mon_from = web.find_element_by_id("depart-calendar__bpk_calendar_nav_select"),select_by_value(sel_depart_calendar_month)
Select(web.find_element_by_id("depart-calendar__bpk_calendar_nav_select")).select_by_value(sel_depart_calendar_month) ## 2018_12
time.sleep(random.randrange(3, 5, 1))

### select day
try :
     sel_depart_calendar_day = "//*[@id='depart-fsc-datepicker-input-popover']/div/div[2]/div/table/tbody/tr/td/button[@class='bpk-calendar-date-1Mg7I']/span[contains(text() ," + sel_depart_day + ")]"

     depart_from_btn_lists = web.find_elements_by_xpath(sel_depart_calendar_day)
     if len(depart_from_btn_lists) > 1 :
        depart_from_btn_lists[1].click()
     else :
        depart_from_btn_lists[0].click()

     print('choice depart successes!!')
except :
     print("choice depart failed ")
     web.quit()

time.sleep(random.randrange(3, 5, 1))
####return return_date_form

return_date_form = web.find_element_by_id("return-fsc-datepicker-input")  ## depart from field
ActionChains(web).move_to_element(return_date_form).click(return_date_form).perform()
#return_date_form.click()
time.sleep(random.randrange(3, 5, 1))

Select(web.find_element_by_id("return-calendar__bpk_calendar_nav_select")).select_by_value(sel_return_calendar_month) ## 2018_11
time.sleep(random.randrange(3, 5, 1))

try :
     sel_return_calendar_day = "//*[@id='return-fsc-datepicker-input-popover']/div/div[2]/div/table/tbody/tr/td/button[@class='bpk-calendar-date-1Mg7I']/span[contains(text() ," + sel_return_day + ")]"
     return_from_btn_list = web.find_elements_by_xpath(sel_return_calendar_day)  ## 2018/11/29
     if len(return_from_btn_list) > 1:
        return_from_btn_list[1].click()
     else:
        return_from_btn_list[0].click()

     print('choice return  successes!!')
except :
     print('choice return failed ')
     web.quit()

##### research btn

time.sleep(random.randrange(10, 15, 1))
try :
     WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='flights-search-controls-root']/div/div/form/div[3]/button"))).click()
     print('research is success')
except :
      print('research is  failed !!1')
      web.quit()

time.sleep(random.randrange(100, 120, 1))
### web filter

try :

     filter_btn = web.find_element_by_xpath("//*[@id='filter-controls']/div[2]/dl[1]/dd/ol") ## one_stop
     filter_btn.find_elements_by_xpath("//li[@data-id='one_stop']/label/input").click()
     time.sleep(random.randrange(3, 5, 1))
     filter_btn.find_elements_by_xpath("//li[@data-id='two_plus_stops']/label/input").click()

     print("filter is successes")
except :
     print("filter is failed !!!")
     time.sleep(random.randrange(3, 5, 1))
     #web.quit()



#time.sleep(random.randrange(120, 180, 1))
#web.quit()




