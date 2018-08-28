from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
#from pyvirtualdisplay import Display #nodisplay on chrome
from selenium.common.exceptions import NoSuchElementException ## show error msg
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
#import send_mail
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.action_chains import ActionChains


url = 'https://www.skyscanner.com.tw/'
search_ori=' TPE'
search_dest=' CNX'
depart_date=' 2018/9/3'
return_date=' 2018/10/30'
class_value ='Economy'
aduits_num =2
infrant_num =1 
infrant_age =1

web = webdriver.Chrome() ## for cron path  
#web = webdriver.Chrome('/usr/local/bin/chromedriver') ## for cron path      
web.get(url)
time.sleep(random.randrange(1, 10, 1))


## choise trip way
try :
     web.find_elements_by_id('fsc-trip-type-selector-return').click() ##return for radio
     print('select trip way  is success')
     
except :      
	    print('select trip way  is failed')

time.sleep(random.randrange(1, 10, 1))
## input fields 
## ori & dest 
try :
     web.find_element_by_id("origin-fsc-search").send_keys(search_ori)
     time.sleep(random.randrange(5, 10, 1))
     web.find_element_by_id("destination-fsc-search").send_keys(search_dest)
     print('ori-dest search is success')
except :      
	      print('ori-dest search is failed')

time.sleep(random.randrange(1, 10, 1))
## trip date
#web.find_element_by_id("monthselector-3VbbW").send_keys(search_dest)

try :
	   #eb.find_element_by_css_selector("#depart-fsc-datepicker-input").clear() 
     #raw_dep = web.find_element_by_css_selector("#depart-fsc-datepicker-input") ##bpk-label-3kiqK form-label-pYNx1
     #dep_month = web.find_element_by_css_selector("bpk-horizontal-nav__link-2sBtP fsc-datepicker__tab-11bkT")
     ##//*[@id="depart-fsc-datepicker-input-modal"]/div/div[2]/div/button[4]
     #draw_dep = web.find_element_by_id("depart-fsc-datepicker-input") ##bpk-label-3kiqK form-label-pYNx1
     #draw_dep_month = web.find_element_by_css_selector(".depart-fsc-datepicker-input #depart-calendar__bpk_calendar_nav_select")
     #draw_dep_month = web.find_element_by_css_selector(".depart-fsc-datepicker-input #")
     web.find_element_by_id("depart-fsc-datepicker-input").send_keys('2018/11/24')
     time.sleep(random.randrange(10, 20, 1))
     web.find_element_by_id("return-fsc-datepicker-input").send_keys('2018/11/30')
     time.sleep(random.randrange(10, 20, 1))
     print('select date is success')
     
except :      
	      print('select date is failed')
 
time.sleep(random.randrange(1, 10, 1))
## trip people num with mouse over  cabin-class-travellers-popover
draw_btn = web.find_element_by_css_selector("CabinClassTravellersSelector__class-travellers-trigger-2Sycq fsc-select-1E9Xu fsc-select-large-above-tablet-3GTSP fsc-select-docked-last-above-tablet-2ovfS") ##button class & pepole
class_level = web.find_element_by_css_selector(".CabinClassTravellersSelector__class-travellers-trigger-2Sycq fsc-select-1E9Xu fsc-select-large-above-tablet-3GTSP fsc-select-docked-last-above-tablet-2ovfS #search-controls-cabin-class-dropdown")  ## input class level 
class_aduit = web.find_element_by_css_selector(".CabinClassTravellersSelector__class-travellers-trigger-2Sycq fsc-select-1E9Xu fsc-select-large-above-tablet-3GTSP fsc-select-docked-last-above-tablet-2ovfS #search-controls-adults-nudger") ##input audits 
class_infrant_1 = web.find_element_by_css_selector(".CabinClassTravellersSelector__class-travellers-trigger-2Sycq fsc-select-1E9Xu fsc-select-large-above-tablet-3GTSP fsc-select-docked-last-above-tablet-2ovfS #child-age-label-0") ## input 1_infrant
class_infrant_1_age = web.find_element_by_css_selector(".CabinClassTravellersSelector__class-travellers-trigger-2Sycq fsc-select-1E9Xu fsc-select-large-above-tablet-3GTSP fsc-select-docked-last-above-tablet-2ovfS #children-age-dropdown-0") ## input 1_infrant_age
click_btn =web.find_element_by_xpath("//*[@id='cabin-class-travellers-popover']/footer/button")


try : 
     ActionChains(web).clik(draw_btn).send_keys_to_element(class_level,class_value).send_keys_to_element(class_aduit,aduits_num).send_keys_to_element(class_infrant_1,infrant_num).send_keys_to_element(class_infrant_1_age,infrant_age).click(click_btn).perform() 
     print('search input people field sucessed')

except :     
     print('search input people field failed') 


time.sleep(random.randrange(3, 10, 1))     
try : 
     web.find_element_by_class_name('bpk-button-2YQI1 bpk-button--large-1Z1P5 SubmitButton-WxCV2').submit()    
     print('search is sucessed')

except : 
	      print('search is failed')

"""
### hidden form 
    loginForm  = web.find_element_by_class_name("mousebox")
    fromname   = web.find_element_by_css_selector(".mousebox  #ls_username")
    frompwd   = web.find_element_by_css_selector(".mousebox #ls_password")
    click_btn =web.find_element_by_xpath("//*[@id='lsform']/div/div/button/em")
    #click_btn =web.find_element_by_xpath("//button[contains(@class, 'pn vm')]")                                                                              
    ### mouse move to element loging
    try :
         ActionChains(web).move_to_element(loginForm).send_keys_to_element(fromname,myusername).send_keys_to_element(frompwd,mypassword).click(click_btn).perform()
         logger = logging.getLogger(myusername)
         logger.info("login botton is success")
         time.sleep(random.randrange(5, 10, 1))

    except :
            logger = logging.getLogger(myusername)
            logger.info("login botton is success")
            break

"""
time.sleep(random.randrange(10, 20, 1))

web.quit()


