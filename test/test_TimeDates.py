#/usr/bin/python
import time
from datetime import datetime, timedelta, date
import sys
sys.path.append('C:\Users\I849467\Documents\GitHub\ironside\libraries')
from TimeDates import TimeDates


#test subtract_business_days method 

list_dates = ['2016-01-01',
              '2016-01-02',
              '2016-01-03',
              '2016-01-04',
              '2016-01-05',
              '2016-01-06',
              '2016-01-07',
              '2016-01-08',
              '2016-01-09',
              '2016-01-10']

for today in list_dates:
    yesterday = TimeDates.subtract_business_days(today, 1)
    print yesterday