#!/usr/bin/python

from yahoo_finance_lib import Share
from TimeDates import TimeDates
import numpy
from datetime import datetime, timedelta, date
from pprint import pprint

class TechnicalIndicators(object):
    
    def __init__(self, company):
        self.company = company
        
    def hello_world(self):
        print self.company
    
    def get_historical_closing(self, company, start_date, end_date):
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
    
    def get_historical_opening(self, company, start_date, end_date):
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
    
    def get_historical_high(self, company, start_date, end_date):
        """ Description: Retrieves the historical high prices of the company
            Keyword arguments:
                company    -- company symbol (string) 
                start date -- (string: YYYY-mm-dd) 
                end date   -- (string: YYYY-mm-dd)
            Output: 
                results    -- dictionary object ['Date': 'high']
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
                    stock_results_dict[record[key_date]] = record['High']
    
        return stock_results_dict
    
    def get_historical_low(self, company, start_date, end_date):
        """ Description: Retrieves the historical low prices of the company
            Keyword arguments:
                company    -- company symbol (string) 
                start date -- (string: YYYY-mm-dd) 
                end date   -- (string: YYYY-mm-dd)
            Output: 
                results    -- dictionary object ['Date': 'low']
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
                    stock_results_dict[record[key_date]] = record['Low']
    
        return stock_results_dict 
    
    def get_historical_volume(self, company, start_date, end_date):
        """ Description: Retrieves the historical volume of the company
            Keyword arguments:
                company    -- company symbol (string) 
                start date -- (string: YYYY-mm-dd) 
                end date   -- (string: YYYY-mm-dd)
            Output: 
                results    -- dictionary object ['Date': 'volume']
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
                    stock_results_dict[record[key_date]] = record['Volume']
    
        return stock_results_dict
    
    def moving_average(self, x, n, type='simple'):
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
    
    def get_historical_adjusted_closing(self, company, start_date, end_date):
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
    
    
    # function over loading if possible (with 2 dates)?
    def get_50_day_moving_average(self, company, start_date, end_date): 
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
        previous_50_days = TimeDates.subtract_business_days(start_date, 50).strftime("%Y-%m-%d")
        
        # get the data set to calculate the 50 day moving average
        stock_results_dict = self.get_historical_adjusted_closing(company, previous_50_days, end_date)
            
        for key in sorted(stock_results_dict):
            stock_results_list.append(float(stock_results_dict[key]))
    
        ma50_list = self.moving_average(stock_results_list, 50, type='simple')
        
        # make sure the length of the dictionary is the same as the 50 day ma ma50_list
        if (len(stock_results_dict) == len(ma50_list)):
            count = 0
    
            for key in sorted(stock_results_dict):
                key = str(key)
                if (datetime.strptime(key, "%Y-%m-%d") >= datetime.strptime(start_date, "%Y-%m-%d")):
                    out[key] = ma50_list[count]
                    print count, key, out[key]
                count = count + 1
        
        return out
        
    def get_200_day_moving_average(self, company, start_date, end_date):
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
        previous_200_days = TimeDates.subtract_business_days(start_date, 200).strftime("%Y-%m-%d")
        
        # get the data set to calculate the 50 day moving average
        stock_results_dict = self.get_historical_adjusted_closing(company, previous_200_days, end_date)
    
        for key in sorted(stock_results_dict):
            stock_results_list.append(float(stock_results_dict[key]))
        
        ma200_list = self.moving_average(stock_results_list, 200, type='simple')
    
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
    
    # use dispatch concept
    def get_accumulation_distribution(self, company, start_date, end_date = None):
        """Description: Volume based indicator designed to measure the cumulative flow of money
                        into and out of a security. 
           Keyword arguments:
                company     -- company symbole (string)
                start date  -- (string: YYYY-mm-dd) 
                end date (optional)   -- (string: YYYY-mm-dd) 
        """
        
        # declare variables
        stock = Share(company)
        money_flow_multiplier = 0
        money_flow_volume = 0 
        adl = 0  
        historical_info = {}
        close = 0 
        low = 0 
        high = 0 
        close = 0 
        
        if (end_date is None):
            end_date = start_date
            
        # retrieve historical info 
        historical_info = stock.get_historical(start_date, end_date)
        
        #pprint (historical_info)
        
        index = len(historical_info) - 1
        
        while (index >= 0):
            low = float(historical_info[index]['Low'])
            high = float(historical_info[index]['High'])
            close = float(historical_info[index]['Close'])
            volume = int(historical_info[index]['Volume']) 
        
            
               
            if (high - low == 0):
                return 0 
            # calculate the accumulation distribution
            money_flow_multiplier = ((close - low) - (high-close))/ (high - low)
            # put in an assert or something 
            money_flow_volume = money_flow_multiplier * volume 
            
            print historical_info[index]['Date'], high, low, close, money_flow_multiplier, money_flow_volume/1000
            
            adl += money_flow_volume
            index = index - 1
            
        return adl
    
    def get_aroon(self):
        return self.symbol 
    
    def get_aroon_oscillator():
        return 0 
        
    def get_volume_weighted_average_price():
        return 0 
    
    def get_volume_by_price():
        return 0 