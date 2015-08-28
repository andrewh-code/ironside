# include python packages/libraries
import os
import sys
#from yahoo_finance import Share
from pprint import pprint
import json
import time
import ystockquote      # custom library to get yahoo stock quotes/prices (https://pypi.python.org/pypi/ystockquote)
import libraries.ystockquote2
from libraries.yahoo_finance_lib import Share
import libraries.yql

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
    if ((company is None) or (len(str(company)) == 0) or 
        (start_date is None) or (len(str(start_date)) == 0) or 
        (end_date is None) or (len(str(end_date)) == 0)):
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
    if ((company is None) or (len(str(company)) == 0) or 
        (start_date is None) or (len(str(start_date)) == 0) or 
        (end_date is None) or (len(str(end_date)) == 0)):
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
    if ((company is None) or (len(str(company)) == 0) or 
        (start_date is None) or (len(str(start_date)) == 0) or 
        (end_date is None) or (len(str(end_date)) == 0)):
        print "Error: One of the arguments being passed in is empty. Please check the input again."
        sys.exit(1);
    
    # declare variables/objects
    stock_results_dict = {}
    
    historical_info = ystockquote.get_historical_prices(company, start_date, end_date) 
    
    # get the historical openings using date as the key
    for key_date in historical_info:
        stock_results_dict[key_date] = historical_info[key_date]['Adj Close']

    return stock_results_dict

# function over loading if possible (with 2 dates)
def get_50_day_moving_average(company, start_date, end_date): 
    """ Description: Retrieves the 50 day moving average of the stock
        Keyword arguments:
            company     -- company symbole (string)
            start date  -- (string: YYYY-mm-dd) 
            end date    -- (string: YYYY-mm-dd)
        Output: 
             results    -- 
    """
    
    return ystockquote.get_50day_moving_avg(company)



'''
def get_historical_prices(symbol, start_date, end_date):
    """
    Get historical prices for the given ticker symbol.
    Date format is 'YYYY-MM-DD'

    Returns a nested dictionary (dict of dicts).
    outer dict keys are dates ('YYYY-MM-DD')
    """
    params = urlencode({
        's': symbol,
        'a': int(start_date[5:7]) - 1,
        'b': int(start_date[8:10]),
        'c': int(start_date[0:4]),
        'd': int(end_date[5:7]) - 1,
        'e': int(end_date[8:10]),
        'f': int(end_date[0:4]),
        'g': 'd',
        'ignore': '.csv',
    })
    url = 'http://ichart.yahoo.com/table.csv?%s' % params
    req = Request(url)
    resp = urlopen(req)
    content = str(resp.read().decode('utf-8').strip())
    daily_data = content.splitlines()
    hist_dict = dict()
    keys = daily_data[0].split(',')
    for day in daily_data[1:]:
        day_data = day.split(',')
        date = day_data[0]
        hist_dict[date] = \
            {keys[1]: day_data[1],
             keys[2]: day_data[2],
             keys[3]: day_data[3],
             keys[4]: day_data[4],
             keys[5]: day_data[5],
             keys[6]: day_data[6]}
    return hist_dict
'''
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
    
    pprint(get_50_day_moving_average(company, start_date, end_date))
    
    stock = Share('GOOG')
    print stock.get_open()
# run main
if __name__ == "__main__":
    main()