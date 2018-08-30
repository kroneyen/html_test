from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#import datetime
from selenium.common.exceptions import NoSuchElementException ## show error msg
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
from bs4 import BeautifulSoup
import re
from selenium.webdriver.common.action_chains import ActionChains


url = 'https://www.skyscanner.com.tw/'
url_1 ='https://www.skyscanner.com.tw/transport/flights/tpet/cnx/?adults=2&children=0&adultsv2=2&childrenv2=1&infants=1&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1811&iym=1811&ref=home&selectedoday=01&selectediday=01'
# url_1 ='https://www.skyscanner.com.tw/transport/flights/tpet/cnx/?adults=2&children=0&adultsv2=2&childrenv2=1&infants=1&cabinclass=economy&rtn=1&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1811&iym=1811&ref=home&selectedoday=01&selectediday=07'
search_ori=' TPE'
search_dest=' CNX'
#depart_date=' 2018/9/4'
#return_date=' 2018/9/30
depart_year_month='2018-11'
class_value ='Economy'
aduits_num =2
infrant_num =1 
infrant_age =1

web = webdriver.Chrome('D:\python_dir\chromedriver') ## for cron path
#web = webdriver.Chrome('/usr/local/bin/chromedriver') ## for cron path      
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
     web.find_element_by_id("origin-fsc-search").send_keys(search_ori)
     time.sleep(random.randrange(5, 10, 1))
     web.find_element_by_id("destination-fsc-search").send_keys(search_dest)
     print('ori-dest search is success')
except:
      print('ori-dest search is failed')

time.sleep(random.randrange(1, 5, 1))
## trip date
#web.find_element_by_id("monthselector-3VbbW").send_keys(search_dest)


depart_date_form = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.ID, "depart-fsc-datepicker-input")))  ## depart from field
depart_date_form.click()
print('select depart_date_form is success')
time.sleep(random.randrange(2, 5, 1))


### into search page
web.get(url_1)
time.sleep(random.randrange(3, 5, 1))
#soup = BeautifulSoup(web.page_source , "html.parser")
#print(soup.prettify())

time.sleep(random.randrange(5, 10, 1))
i=0
for month_tbody in web.find_elements_by_tag_name('tbody') :
    month_date = month_tbody.find_elements_by_tag_name('button')
    month_prices = month_tbody.find_elements_by_class_name('price')
    if i == 0 :
      print('***********depart_date_view*********** :')
    else :
      print('***********return_date_view*********** :')

    for i in range(len(month_date)) :
        day_price =month_prices[i].get_attribute('innerHTML')
        if len(day_price) > 20 :
            day_price = ' NULL'
        print(month_date[i].get_attribute('aria-label'), '    price:',day_price)




#month_view = web.find_element_by_class_name('clearfix month-view__calendar-area')
#print('month_view',month_view.text)
#soup = BeautifulSoup(web.page_source , "html.parser")
#month_view =soup.find('div',{'class':re.compile('month-view__tabbed-panels')})
#month_view_calendar_area =soup.find('div',{'class':re.compile('clearfix month-view__calendar-area')})
###outbound


"""
month_view_calendar_outbound_calendar = month_view_calendar_area.find('div',{'class':re.compile('month-view-calendar outbound-calendar')})
print('month_view_calendar_outbound_calendar:',)
table_month_calendar = month_view_calendar_outbound_calendar.find('table',{'class':re.compile('bpk-calendar-grid-2GXun month-view-grid--data-loaded')})
for month_tbody in table_month_calendar.findall('tbody') :
  print('month_tbody:' , month_tbody.prettify())
  print('')
"""

###inbound
"""
month_view_calendar_inbound_calendar = month_view_calendar_area.find('div',{'class':re.compile('month-view-calendar inbound-calendar')})
in_table = month_view_calendar_outbound_calendar.find('table',{'class':re.compile('bpk-calendar-grid-2GXun month-view-grid--data-loaded')})
in_tbody = out_table.find('tbody')
print('out_tbody:' ,in_tbody.prettify())
"""
#print('month-view-calendar_outbound-calendar:',month_view_calendar_outbound_calendar.prettify())

#print(table_price)
#for table_body_price in table_price.find_all('tbody'):
#   print('table_body_price',table_body_price)

"""   
try:
     
     ## all select all month
     #Select(web.find_element_by_id("depart-calendar__bpk_calendar_nav_select")).select_by_value(depart_year_month) ## 2018-09
     btn_all_month = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "bpk-horizontal-nav__link-2sBtP fsc-datepicker__tab-11bkT")))  ## 整個月btn
     btn_all_month.click()
     print('btn_all_month is success')
     time.sleep(random.randrange(2, 5, 1))
     btn_month = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='depart-fsc-datepicker-input-popover']/div/div[2]/div/button[3]"))) ##2018-11
     btn_month.click()
     print('btn_month is success')
     #start_month = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.ID, "depart-calendar__bpk_calendar_nav_select")))
     time.sleep(random.randrange(2, 5, 1))

     ddpart = web.find_element_by_id("depart-fsc-datepicker-input")
     print('ddpart:',ddpart.get(class_value))
     time.sleep(random.randrange(2, 5, 1))
     print('depart-fsc-datepicker-input is success')


except:
       print('select depart date is failed')


return_date_form = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.ID, "return-fsc-datepicker-input")))  ## return from field
return_date_form.click()
print('return_date_form is sucess')
time.sleep(random.randrange(2, 5, 1))
try:
    btn_all_month = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "bpk-horizontal-nav__link-2sBtP fsc-datepicker__tab-11bkT")))  ## 整個月btn
    btn_all_month.click()
    print('btn_all_month is sucess')
    time.sleep(random.randrange(2, 5, 1))
    btn_month = WebDriverWait(web, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='return-fsc-datepicker-input-popover']/div/div[2]/div/button[3]")))  ##2018-11
    btn_month.click()
    print('btn_month is sucess')
    time.sleep(random.randrange(2, 5, 1))
    WebDriverWait(web, 10).until(EC.presence_of_element_located((By.ID, "return-fsc-datepicker-input"))).send_keys('2018/11/30')
    print('select return date is success')

except:
       print('select return date is failed')

time.sleep(random.randrange(1, 10, 1))


## trip people num with mouse over  cabin-class-travellers-popover
draw_btn = web.find_element_by_css_selector("CabinClassTravellersSelector__class-travellers-trigger-2Sycq fsc-select-1E9Xu fsc-select-large-above-tablet-3GTSP fsc-select-docked-last-above-tablet-2ovfS") ##button class & pepole
class_level = web.find_element_by_css_selector(".CabinClassTravellersSelector__class-travellers-trigger-2Sycq fsc-select-1E9Xu fsc-select-large-above-tablet-3GTSP fsc-select-docked-last-above-tablet-2ovfS #search-controls-cabin-class-dropdown")  ## input class level 
class_aduit = web.find_element_by_css_selector(".CabinClassTravellersSelector__class-travellers-trigger-2Sycq fsc-select-1E9Xu fsc-select-large-above-tablet-3GTSP fsc-select-docked-last-above-tablet-2ovfS #search-controls-adults-nudger") ##input audits 
class_infrant_1 = web.find_element_by_css_selector(".CabinClassTravellersSelector__class-travellers-trigger-2Sycq fsc-select-1E9Xu fsc-select-large-above-tablet-3GTSP fsc-select-docked-last-above-tablet-2ovfS #child-age-label-0") ## input 1_infrant
class_infrant_1_age = web.find_element_by_css_selector(".CabinClassTravellersSelector__class-travellers-trigger-2Sycq fsc-select-1E9Xu fsc-select-large-above-tablet-3GTSP fsc-select-docked-last-above-tablet-2ovfS #children-age-dropdown-0") ## input 1_infrant_age
click_btn =web.find_element_by_xpath("//*[@id='cabin-class-travellers-popover']/footer/button")


try:
     ActionChains(web).clik(draw_btn).send_keys_to_element(class_level,class_value).send_keys_to_element(class_aduit,aduits_num).send_keys_to_element(class_infrant_1,infrant_num).send_keys_to_element(class_infrant_1_age,infrant_age).click(click_btn).perform() 
     print('search input people field sucessed')

except:
     print('search input people field failed') 


time.sleep(random.randrange(3, 10, 1))     
try:
     web.find_element_by_class_name('bpk-button-2YQI1 bpk-button--large-1Z1P5 SubmitButton-WxCV2').submit()    
     print('search is sucessed')

except:
       print('search is failed')
"""
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


