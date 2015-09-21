# include standard python packages/libraries
import os
import sys
import numpy
from datetime import datetime, timedelta, date
from pprint import pprint
import json
import time

# include custom python packages/libraries
import ystockquote      # custom library to get yahoo stock quotes/prices (https://pypi.python.org/pypi/ystockquote)
import libraries.yql as yql
from libraries.yahoo_finance_lib import Share
from libraries.TechnicalIndicators import TechnicalIndicators
from libraries.TimeDates import TimeDates

#def output_to_json_file(dictionary_object):

def check_and_del_previous_json(file_name):
        # delete file
        file_name2 = os.getcwd() + '\\' + file_name
        print file_name2
        
        if (os.path.isfile(file_name2)):
            os.remove(file_name2)
            print "successfully deleted file: ", file_name2
        else:
            print "unable to find file: ", file_name2

def main():

    #variables
    company     = 'BBRY'
    start_date  = '2010-12-10'
    end_date    = '2010-12-15'
    results_dict = {}
    eopch_date = ''
    #stock       = ystockquote.get_historical_prices(company, start_date, end_date)
    json_file_out = 'output.json' 
    temp_list = []
    temp_dt = datetime
    
    #print "output results\n", stock_results_dict
    
    check_and_del_previous_json(json_file_out)
    
    #results_dict = get_historical_adjusted_closing(company, start_date, end_date)
    
    # output json results to json output file 
    with open('output.json', 'w') as json_file_out:
        json.dump(results_dict, json_file_out)
        
    json_file_out.close()
    
    x = TechnicalIndicators(company)
    print (x.get_accumulation_distribution(company, start_date, end_date))
    
    #print temp_list
    
    #print subtract_business_days(start_date, 50).strftime("%Y-%m-%d")
    
# run main
if __name__ == "__main__":
    main()