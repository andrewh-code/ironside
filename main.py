# include standard python packages/libraries
import os
import sys
import numpy
from datetime import datetime, timedelta, date
from pprint import pprint
import json
import time

# include custom python packages/libraries
#import ystockquote      # custom library to get yahoo stock quotes/prices (https://pypi.python.org/pypi/ystockquote)
#import libraries.yql as yql
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

def convert_dates_to_epoch(in_dict):
    
    #variables
    out_dict = {}
    
    for key in in_dict:
        new_key = TimeDates.convert_to_epoch(key)
        out_dict[new_key] = in_dict[key]

    return out_dict

  
    
def main():

    #variables
    company     = 'BBRY'
    start_date  = '2010-01-04'
    end_date    = '2010-12-30'
    results_dict = {}
    eopch_date = ''
    indicator = TechnicalIndicators(company)
    
    #stock       = ystockquote.get_historical_prices(company, start_date, end_date)
    json_file_out = 'output.json' 
    temp_list = []
    temp_dt = datetime
    
    #print "output results\n", stock_results_dict
    
    check_and_del_previous_json(json_file_out)
    check_and_del_previous_json('output_keyless_array.json')
    
    results_dict = indicator.get_historical_closing(company, start_date, end_date)
    
    results_dict = convert_dates_to_epoch(results_dict)
    
    #temp_list = results_dict.items()
    
    for key, value in results_dict.iteritems():
        temp = [key, float(value)]
        temp_list.append(temp)
        
    
    # output json results to json output file 
    with open('output.json', 'w') as json_file_out:
        json.dump(results_dict, json_file_out, sort_keys=True, indent=4)
    json_file_out.close()
    
    
    # dump to file with an array (keyless, .json file), or list of lists 
    # TO DO: has to be put in order based on key  
    with open('output_keyless_array.json', 'w') as json_file_out2:
        json.dump(temp_list, json_file_out2, sort_keys=True, ensure_ascii=True)
    json_file_out2.close()
    
    #print json.dumps(results_dict, sort_keys=True, indent=4, separators=(',', ': '))
    #print json.dumps(temp_list, ensure_ascii=True)
    
    #print temp_list
    #print subtract_business_days(start_date, 50).strftime("%Y-%m-%d")
    
    print indicator.get_true_range(company, '2016-01-20')
    
    
# run main
if __name__ == "__main__":
    main()