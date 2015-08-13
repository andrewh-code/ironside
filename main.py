# include python packages/libraries
import os
import sys
import ystockquote      # custom library to get yahoo stock quotes/prices (https://pypi.python.org/pypi/ystockquote)
from yahoo_finance import Share
import pprint
import json
import time


def convert_to_epoch(date):
    pattern = '%Y-%m-%d'
    epoch = int(time.mktime(time.strptime(date, pattern)))
    
    return epoch

#def output_to_json_file(dictionary_object):

def check_and_del_previous_json(file_name):
        # delete file
        file_name2 = os.getcwd() + '\\' + file_name
        if (os.remove(file_name2)):
            print "successfully deleted file: ", file_name2
        else:
            print file_name2, "not deleted successfully"


def main():

    #variables
    company     = 'GOOG'
    start_date  = '2015-01-01'
    end_date    = '2015-08-10'
    stock_results_dict = {}
    eopch_date = ''
    stock       = ystockquote.get_historical_prices(company, start_date, end_date)
    json_file_out = 'output.json' 
    
    #print stock.get_open()
    #print stock.get_price()
    #print stock.get_trade_datetime()
    '''
    for keys, values in stock.items():
        print(keys)
        print(values)
    '''     
    for stock_key in stock:
        epoch_date = convert_to_epoch(stock_key)
        #print stock_key, epoch_date
        #print stock[stock_key]['Close']
        
        #for value in stock[key]:
            #print value, ':', stock[key][value]
            #print stock[key]['Close']
        
        # pick values from dictionary and input them into a new dictionary
        stock_results_dict[epoch_date] = stock[stock_key]['Close']   

    #print "output results\n", stock_results_dict
    
    check_and_del_previous_json(json_file_out)
    # output json results to json output file 
    with open('output.json', 'w') as json_file_out:
        json.dump(stock_results_dict, json_file_out)
        
    json_file_out.close()
    
# run main
if __name__ == "__main__":
    main()