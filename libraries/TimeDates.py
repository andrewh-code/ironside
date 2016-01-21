#/usr/bin/python

from datetime import datetime, timedelta, date
import time 

class TimeDates:
    
    @staticmethod
    def convert_to_epoch(date):
        """ Description: converts the input date into the epoch date equivalent (for highcharts api)
            Keyword arguments:
                date        -- (string: YYYY-mm-dd (more specifically: %Y-%m-%d))
            Output:
                eopch       -- (string: date in epoch UNIX time)
        """
        
        pattern = '%Y-%m-%d'
        epoch = int(time.mktime(time.strptime(date, pattern)))
    
        return epoch

    @staticmethod
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
        
        return current_date.date()   

    @staticmethod
    def check_diff_in_days(start_date, end_date, diff):
        """ Description: Finds the difference between the two inputted dates and checks to see if they are equal to the inputted diff value
            Keyword arguments:
                start_date      -- (string: YYYY-mm-dd (more specifically: %Y-%m-%d))
                end_date        -- (string: YYYY-mm-dd (more specifically: %Y-%m-%d))
                diff            -- (int: supposed difference between the two dates)
            Output:
                true/valse      -- boolean result
        """
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
 
    @staticmethod
    def diff_between_business_dates(date1, date2):
        """ Description: 
        """
        
        # validate date1 and date2
        date1_object = datetime.strptime(date1, '%Y-%m-%d')
        date2_object = datetime.strptime(date2, '%Y-%m-%d')
        
        return (date2_object - date1_object).days

        