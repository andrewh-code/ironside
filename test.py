#!/usr/bin/python

import datetime


def make_url(ticker_symbol,start_date, end_date):
    base_url = "http://finance.yahoo.com/d/quotes.csv?s"
    print ticker_symbol
    a = start_date
    b = end_date
    dt_url = '%s&a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&g=d&ignore=.csv'% (ticker_symbol, a.month-1, a.day, a.year, b.month-1, b.day,b.year)
    return base_url + dt_url
    

s = datetime.date(2012,1,1)
e = datetime.date(2013,1,1)
u =  make_url('csco',s,e)
    
print u 

    
    
    

