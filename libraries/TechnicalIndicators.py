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
        out = {}
        close = 0 
        low = 0 
        high = 0 
        close = 0
         
        
        if (end_date is None):
            end_date = start_date
            
        # retrieve historical info 
        historical_info = stock.get_historical(start_date, end_date)
        
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
                     
            adl += money_flow_volume
            print historical_info[index]['Date'], money_flow_multiplier, money_flow_volume/1000, adl
            out[historical_info[index]['Date']] = adl
            
            index = index - 1
            
        return out
    
    def get_aroon(self, company, current_date, aroon_period, flag = 'High'):
        """Description: Indicator system that determines whether a stock is trending and how 
                        strong the trend is
           Keyword arguments:
               company      -- company symbol (string)
               current_date -- string (YYYY-mm-dd)
               aroon_period -- default aroon period is usually 25 (int)
               flag         -- boolean type either 'High' to calculate the aroon high
                               if not 'High' then automatically calculat ethe aroon low 
        """
        
        # declare variables
        stock = Share(company) 
        start_date = TimeDates.subtract_business_days(current_date, aroon_period)
        
        #convert start_date back to string
        start_date = start_date.strftime('%Y-%m-%d')
        max_high_date = ''
        
        if (flag == 'High'):
            historical_high = self.get_historical_high(company, start_date, current_date)
            max_high_date = max(historical_high, key=historical_high.get)
            days_since_last_high = TimeDates.diff_between_business_dates(max_high_date, current_date)

            aroon_up = ((float(aroon_period) - float(days_since_last_high))/float(aroon_period)) * 100.00
            print "arroon up", aroon_up
            return aroon_up
        else:
            historical_low = self.get_historical_low(company, start_date, current_date)
            least_low_date = low(historical_high, key=historical_low.get)
            days_since_last_low = TimeDates.diff_between_business_dates(least_low_date, current_date)
            
            aroon_down = ((float(aroon_period) - float(days_since_last_low))/float(aroon_period)) * 100.00
            
            return aroon_down
        
        
    def get_aroon_oscillator(self, company, current_date, aroon_period):
        """Description: Take the difference between the aroon high and the aroon low
                        Helps to see which stocks are trending upwards/downwards over a 
                        certain period
            Keyword arguments: 
                company         -- company symbole (string)
                current_date    -- specified date (string YYYY-mm-dd)
                aroon_period    -- period before the specified date (int), default to 25    
        """      
        
        stock = Share(company)
        start_date = TimeDates.subtract_business_days(current_date, aroon_period)
        
        '''
        Aroon Up = 100 x (25 - Days Since 25-day High)/25
            Aroon Down = 100 x (25 - Days Since 25-day Low)/25
            Aroon Oscillator = Aroon-Up  -  Aroon-Down
        '''
        # calculate aroon up 
        historical_high = self.get_historical_high(company, start_date, current_date)
        max_high_date = max(historical_high, key=historical_high.get)
        days_since_last_high = TimeDates.diff_between_business_dates(max_high_date, current_date)
        aroon_up = ((float(aroon_period) - float(days_since_last_high))/float(aroon_period)) * 100.00
        
        # calculate aroon Down
        historical_low = self.get_historical_low(company, start_date, current_date)
        least_low_date = low(historical_high, key=historical_low.get)
        days_since_last_low = TimeDates.diff_between_business_dates(least_low_date, current_date)
        aroon_down = ((float(aroon_period) - float(days_since_last_low))/float(aroon_period)) * 100.00
        
        aroon_oscillator = aroon_up - aroon_down
        
        return aroon_oscillator
        
    def get_average_directional_index():
        return 0
        
    def get_average_true_range(company, start_date, current_date):
        
        number_days = TimeDates.diff_between_business_dates(start_date, curent_date)
        
        while (start_date < current_date):
            sum_true_range += self.get_true_range(company, start_date, current_date)
            start_date += 1
            
            avg_true_range = sum_true_range/number_days
        
        return avg_true_range  
    
    def get_true_range(self, company, date):
        '''
        Description: Wilder started with a concept called True Range (TR), which is defined as the greatest of the following:
                    Method 1: Current High less the current Low
                    Method 2: Current High less the previous Close (absolute value)
                    Method 3: Current Low less the previous Close (absolute value)
                    Absolute values are used to ensure positive numbers. After all, Wilder was interested in measuring the distance between two points, not the direction. 
                    If the current period's high is above the prior period's high and the low is below the prior period's low, then the current period's high-low range will be used as the True Range.
                    
                    When put it in today's date, Yahoo Finance will not return the information needed because it gathers the information at the end of the day. 
                    If put in today's date, have to subtract by one to get the information. 
        Keyword Arguments:
                company     -- company symbol (string)
                start_date  -- initial start date (string YYYY-mm-dd)
                current_date -- end date (string YYYY-mm-dd)
        Output:
                true_range - float
        '''
        start_date = TimeDates.subtract_business_days(date, 1)
        
        stock = Share(company)
        # implement try catch statement in historical info
        # if historical info gives error, that means it's possible that the date given is today's date
        # which means that the stock market might still be going on and you dont' have a final value for 
        # the historical values
        # in such case, subtract one day from today's date so you start from yesterday's final values 
        
        historical_info = stock.get_historical(start_date.strftime('%Y-%m-%d'), date) 
        
        print historical_info
        print historical_info[0]['High']
        print historical_info[0]['Low']
        print historical_info[1]['Close'] 
        current_high = historical_info[0]['High']
        current_low = historical_info[0]['Low']
        previous_close = historical_info[1]['Close'] 
        result1 = result2 = result3 = 0
        true_range = 0
        
        # method 1: Current high less current low
        result1 = abs(float(current_high) - float(current_low))
        
        # method 2: current high less the previous close 
        result2 = abs(float(current_high) - float(previous_close))
        
        # method 3: current low less the previous close
        result3 = abs(float(current_low) - float(previous_close))
        
        true_range = max(result1, result2, result3)
        
        return true_range 
    
        
    def get_average_true_range():
        return 0
 
    def get_bandwidth():
        return 0
        
    def get_volume_weighted_average_price():
        return 0 
    
    def get_volume_by_price():
        return 0 