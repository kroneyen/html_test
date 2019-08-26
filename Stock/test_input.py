# -*- coding: utf-8 -*-

import datetime
import time
from threading import Timer

cho_day_from = None
cho_day_return = None

def check(job) :

    sleep (10)
    if job != None :
       return
    else :
        cho_day_from = datetime.datetime.strftime(datetime.date.today() + datetime.timedelta(days=11),'%Y/%m/%d')  ## booking friday
    if  cho_day_return != None :
        return
    else :
         cho_day_return = datetime.datetime.strftime(datetime.date.today() + datetime.timedelta(days=14),'%Y/%m/%d')  ## booking next monday

cho_day_from = input('Enter choose From date:')

t = threading.Thread(target = check(cho_day_from)).start()
#thread(target = check).start()

cho_day_return = input('Enter choose Ruten date:')








"""
cho_day_from = input('Enter choose From date:')
cho_day_return = input('Enter choose Ruten date:')
##2019/02/02

if cho_day_from == '' :
    cho_day_from = datetime.datetime.strftime(datetime.date.today() + datetime.timedelta(days=11),
                                          '%Y/%m/%d')  ## booking friday
if cho_day_return == '' :
    cho_day_return = datetime.datetime.strftime(datetime.date.today() + datetime.timedelta(days=14),
                                            '%Y/%m/%d')  ## booking next monday

print('f_choose_date:',cho_day_from)
print('r_choose_date:',cho_day_return)
"""
