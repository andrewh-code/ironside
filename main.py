# include python packages/libraries
import os
import sys
import ystockquote      # custom library to get yahoo stock quotes/prices (https://pypi.python.org/pypi/ystockquote)
from yahoo_finance import Share
from pprint import pprint
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
        print file_name2
        
        if (os.path.isfile(file_name2)):
            os.remove(file_name2)
            print "successfully deleted file: ", file_name2
        else:
            print "unable to find file: ", file_name2

def get_historical_opening(company, start_date, end_date):
    """ Description: Retrieves the historical opening prices of the company
        Keyword arguments:
            company    -- company symbol (string) 
            start date -- (string: YYYY-mm-dd) 
            end date   -- (string: YYYY-mm-dd)
        Output: 
            results    -- dictionary object ['Date': 'opening']
    """
    # check to see if arguments put in are not empty
    if ((company is None) or (len(str(company)) == 0) or (start_date is None) or (len(str(start_date)) == 0) or (end_date is None) or (len(str(end_date)) == 0)):
        print "Error: One of the arguments being passed in is empty. Please check the input again."
        sys.exit(1);
    
    # declare variables/objects
    stock_results_dict = {}
    
    
    historical_info = ystockquote.get_historical_prices(company, start_date, end_date) 
    
    # get the historical openings using date as the key
    for key_date in historical_info:
        stock_results_dict[key_date] = historical_info[key_date]['Open']

    return stock_results_dict

def get_historical_closing(company, start_date, end_date):
    """ Description: Retrieves the historical closing prices of the company
        Keyword arguments:
            company    -- company symbol (string) 
            start date -- (string: YYYY-mm-dd) 
            end date   -- (string: YYYY-mm-dd)
        Output: 
            results    -- dictionary object ['Date': 'closing']
    """
    # check to see if arguments put in are not empty
    if ((company is None) or (len(str(company)) == 0) or (start_date is None) or (len(str(start_date)) == 0) or (end_date is None) or (len(str(end_date)) == 0)):
        print "Error: One of the arguments being passed in is empty. Please check the input again."
        sys.exit(1);
    
    # declare variables/objects
    stock_results_dict = {}
    
    
    historical_info = ystockquote.get_historical_prices(company, start_date, end_date) 
    
    # get the historical openings using date as the key
    for key_date in historical_info:
        stock_results_dict[key_date] = historical_info[key_date]['Close']

    return stock_results_dict

def get_historical_adjusted_closing(company, start_date, end_date):
    """ Description: Retrieves the historical adjusted closing prices of the company
        Keyword arguments:
            company    -- company symbol (string) 
            start date -- (string: YYYY-mm-dd) 
            end date   -- (string: YYYY-mm-dd)
        Output: 
             results    -- dictionary object ['Date': 'adjusted closing']
    """
    # check to see if arguments put in are not empty
    if ((company is None) or (len(str(company)) == 0) or (start_date is None) or (len(str(start_date)) == 0) or (end_date is None) or (len(str(end_date)) == 0)):
        print "Error: One of the arguments being passed in is empty. Please check the input again."
        sys.exit(1);
    
    # declare variables/objects
    stock_results_dict = {}
    
    
    historical_info = ystockquote.get_historical_prices(company, start_date, end_date) 
    
    # get the historical openings using date as the key
    for key_date in historical_info:
        stock_results_dict[key_date] = historical_info[key_date]['Adj Close']

    return stock_results_dict

def main():

    #variables
    company     = 'GOOG'
    start_date  = '2015-01-01'
    end_date    = '2015-08-10'
    results_dict = {}
    eopch_date = ''
    stock       = ystockquote.get_historical_prices(company, start_date, end_date)
    json_file_out = 'output.json' 
    
    #print "output results\n", stock_results_dict
    
    check_and_del_previous_json(json_file_out)
    
    results_dict = get_historical_adjusted_closing(company, start_date, end_date)
    
    # output json results to json output file 
    with open('output.json', 'w') as json_file_out:
        json.dump(results_dict, json_file_out)
        
    json_file_out.close()
    
    pprint(results_dict)
    
# run main
if __name__ == "__main__":
    main()