
import time
import datetime

StartDate = time.strptime("2018/10/28", "%Y/%m/%d")
EndDate = time.strptime("2019/12/31", "%Y/%m/%d")
StartDate = datetime.date(StartDate[0], StartDate[1], StartDate[2])
EndDate = datetime.date(EndDate[0], EndDate[1], EndDate[2])
RangeDate = datetime.timedelta(days=27)
last_date = datetime.timedelta(days=1)
Rangeweek = datetime.timedelta(days=7)

while StartDate + RangeDate <= EndDate:

    print('### Month:',datetime.datetime.strftime(StartDate + RangeDate,"%Y/%m ###"))
    week_start_date =StartDate
    week_end_date = StartDate + RangeDate
    seq=1
    print('Weeks|StartDate|weekday|EndDate|weekday')
    print('--------------|:-----:|-----| ----:|------------------------')
    while week_start_date < week_end_date :
        print(seq,'|',week_start_date,'|','SUN|',week_start_date + Rangeweek - last_date,'|','SAT|')
        week_start_date = week_start_date+Rangeweek
        seq=seq+1
    print('   ')
    print('===============================================================')
    print('   ')
    StartDate = StartDate + RangeDate + last_date

