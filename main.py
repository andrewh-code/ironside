# include python packages/libraries
import os
import sys
import numpy
from datetime import datetime, timedelta, date
from pprint import pprint
import json
import time
import ystockquote      # custom library to get yahoo stock quotes/prices (https://pypi.python.org/pypi/ystockquote)
import libraries.ystockquote2
from libraries.yahoo_finance_lib import Share
import libraries.yql as yql

def convert_to_epoch(date):
    pattern = '%Y-%m-%d'
    epoch = int(time.mktime(time.strptime(date, pattern)))
    
    return epoch

def check_diff_in_days(start_date, end_date, diff):
    
    # declare variables
    start_date_object = ""
    end_date_object = ""
    
    if (diff.isdigit() == False):
        print "Error: Please input a number as the third parameter"
        return False
        
    # date has to be in the %Y-%m-%d format (because of yahoo query language output)
    start_date_object = datetime.strptime(start_date, '%Y-%m-%d')
    end_date_object = datetime.strptime(end_date, '%Y-%m-%d')
    
    # difference is either 50 days or 200 days (depending on the output)
    if (end_date_object - start_date_object == diff):
        return True
    else:
        return False
 
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
    if ((company is None) or (len(str(company)) == 0) or 
        (start_date is None) or (len(str(start_date)) == 0) or 
        (end_date is None) or (len(str(end_date)) == 0)):
        print "Error: One of the arguments being passed in is empty. Please check the input again."
        sys.exit(1);
    
    # declare variables/objects
    stock = Share(company)
    stock_results_dict = {}
    
    historical_info = stock.get_historical(start_date, end_date) 
    
    # get the historical openings using date as the key
    for record in historical_info:
        for key_date in record:
            if (key_date == 'Date'):
                stock_results_dict[record[key_date]] = record['Open']

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
    if ((company is None) or (len(str(company)) == 0) or 
        (start_date is None) or (len(str(start_date)) == 0) or 
        (end_date is None) or (len(str(end_date)) == 0)):
        print "Error: One of the arguments being passed in is empty. Please check the input again."
        sys.exit(1);
    
    # declare variables/objects
    stock = Share(company)
    stock_results_dict = {}
    
    
    historical_info = stock.get_historical(start_date, end_date) 
    
    # get the historical openings using date as the key
    for record in historical_info:
        for key_date in record:
            if (key_date == 'Date'):
                stock_results_dict[record[key_date]] = record['Close']

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
    if ((company is None) or (len(str(company)) == 0) or 
        (start_date is None) or (len(str(start_date)) == 0) or 
        (end_date is None) or (len(str(end_date)) == 0)):
        print "Error: One of the arguments being passed in is empty. Please check the input again."
        sys.exit(1);
    
    # declare variables/objects
    stock = Share(company)
    stock_results_dict = {}
    
    historical_info = stock.get_historical(start_date, end_date)
    
     # get the historical openings using date as the key
    for record in historical_info:
        for key_date in record:
            if (key_date == 'Date'):
                stock_results_dict[record[key_date]] = record['Adj_Close']

    return stock_results_dict

def moving_average(x, n, type='simple'):
    """ Description: Calculate the moving average"
    """
    
    x = numpy.asarray(x)
    if type=='simple':
        weights = numpy.ones(n)
    else:
        weights = numpy.exp(numpy.linspace(-1., 0., n))

    weights /= weights.sum()

    a =  numpy.convolve(x, weights, mode='full')[:len(x)]
    a[:n] = a[n]
    
    return a

def get_200_day_moving_average(company, start_date, end_date):
    """ Description: Retrieves the 200 day moving average of the stock
        Keyword arguments:
            company     -- company symbole (string)
            start date  -- (string: YYYY-mm-dd) 
            end date    -- (string: YYYY-mm-dd)
        Output: 
             results    -- 
    """
    
    # declare variables
    stock = Share(company)
    stock_results_dict = {}
    stock_results_list = []
    ma200_list = []
    out = {}
    
    # get 50 days before for a base average
    # convert the previous 50 days back to the string format (TO DO: inefficient, change it)
    previous_200_days = subtract_business_days(start_date, 200).strftime("%Y-%m-%d")
    
    # get the data set to calculate the 50 day moving average
    stock_results_dict = get_historical_adjusted_closing(company, previous_200_days, end_date)

    for key in sorted(stock_results_dict):
        stock_results_list.append(float(stock_results_dict[key]))
    
    ma200_list = moving_average(stock_results_list, 200, type='simple')
 
    # make sure the length of the dictionary is the same as the 200 day ma ma50_list
    if (len(stock_results_dict) == len(ma200_list)):
        count = 0

        for key in sorted(stock_results_dict):
            key = str(key)
            if (datetime.strptime(key, "%Y-%m-%d") >= datetime.strptime(start_date, "%Y-%m-%d")):
                out[key] = ma200_list[count]
                print count, key, out[key]
            count = count + 1
    
    return out

# function over loading if possible (with 2 dates)?
def get_50_day_moving_average(company, start_date, end_date): 
    """ Description: Retrieves the 50 day moving average of the stock
        Keyword arguments:
            company     -- company symbole (string)
            start date  -- (string: YYYY-mm-dd) 
            end date    -- (string: YYYY-mm-dd)
        Output: 
             results    -- 
    """
    # declare variables
    stock = Share(company)
    stock_results_dict = {}
    stock_results_list = []
    ma50_list = []
    out = {}
    
    # get 50 days before for a base average
    # convert the previous 50 days back to the string format (TO DO: inefficient, change it)
    previous_50_days = subtract_business_days(start_date, 50).strftime("%Y-%m-%d")
    
    # get the data set to calculate the 50 day moving average
    stock_results_dict = get_historical_adjusted_closing(company, previous_50_days, end_date)
        
    for key in sorted(stock_results_dict):
        stock_results_list.append(float(stock_results_dict[key]))

    ma50_list = moving_average(stock_results_list, 50, type='simple')
    
    # make sure the length of the dictionary is the same as the 50 day ma ma50_list
    if (len(stock_results_dict) == len(ma50_list)):
        count = 0

        for key in sorted(stock_results_dict):
            key = str(key)
            if (datetime.strptime(key, "%Y-%m-%d") >= datetime.strptime(start_date, "%Y-%m-%d")):
                out[key] = ma50_list[count]
                #print count, key, out[key]
            count = count + 1
    
    return out
    
def subtract_business_days(start_date, num_days):
    """ Description: Subtracts number of business days from the start_date (or current date)
        Keyword arguments:
            start_date      -- (string: YYYY-mm-dd (more specifically: %Y-%m-%d))
            num_days        -- int
        Output:
            current_date    -- 
    """
    
    decrement_day = num_days 
    current_date = datetime.strptime(start_date, '%Y-%m-%d') 
    
    #print current_date
    while (decrement_day > 0):
        #print decrement_day, current_date
        current_date = current_date - timedelta(days=1)
        weekday = current_date.weekday()
        
        if (weekday >= 5):  # sunday = 6
            continue

        decrement_day = decrement_day - 1
        
    return current_date

def main():

    #variables
    company     = 'GOOG'
    start_date  = '2015-01-01'
    end_date    = '2015-09-03'
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
    
    
    get_50_day_moving_average(company, start_date, end_date)
    
    print Share('GOOG').get_company_name()
    print Share('GOOG').get_prev_close()
    print Share('GOOG').get_50day_moving_avg()
    print Share('GOOG').get_200day_moving_avg()
    print Share('GOOG').get_change_from_50_day_moving_avg()
    print Share('GOOG').get_change_from_200_day_moving_avg()
    
    #print temp_list
    
    #print subtract_business_days(start_date, 50).strftime("%Y-%m-%d")
    
# run main
if __name__ == "__main__":
    main()