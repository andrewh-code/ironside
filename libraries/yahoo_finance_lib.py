import yql

from datetime import datetime, timedelta
import pytz

__author__ = 'Lukasz Banasiak'
__modified__ = 'Andrew Ho'
__date_modified__ = 'September 12, 2015'
__version__ = '1.1.4_ironside'
__all__ = ['Currency', 'Share']

def edt_to_utc(date, mask='%m/%d/%Y %I:%M%p'):
    """
    Convert EDT (Eastern Daylight Time) to UTC

    :param date: EDT date string e.g. '5/26/2014 4:00pm'
    :param mask: format of input date e.g '%m/%d/%Y %I:%M%'
    :return: UTC date string e.g '2014-03-05 12:23:00 UTC+0000'
    """
    utc = pytz.utc
    eastern = pytz.timezone('US/Eastern')
    date_ = datetime.strptime(date, mask)
    date_eastern = eastern.localize(date_, is_dst=None)
    date_utc = date_eastern.astimezone(utc)
    return date_utc.strftime('%Y-%m-%d %H:%M:%S %Z%z')


def get_date_range(start_day, end_day, step_days=365, mask='%Y-%m-%d'):
    """
    Split date range for a specified number of days.

    Generate tuples with intervals from given range of dates, e.g for `2012-04-25`-`2014-04-29`:

        ('2013-04-29', '2014-04-29')
        ('2012-04-28', '2013-04-28')
        ('2012-04-25', '2012-04-27')

    :param start_day: start date string
    :param end_day: end date string
    :param step_days: step days
    :param mask: format of input date e.g '%Y-%m-%d'
    """

    start = datetime.strptime(start_day, mask)
    end = datetime.strptime(end_day, mask)
    if start > end:
        raise ValueError('Start date "%s" is greater than "%s"' % (start_day, end_day))
    step = timedelta(days=step_days)
    while end - step > start:
        current = end - step
        yield current.strftime(mask), end.strftime(mask)
        end = current - timedelta(days=1)
    else:
        yield start.strftime(mask), end.strftime(mask)


class YQLQueryError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'Query failed with error: "%s".' % repr(self.value)


class YQLResponseMalformedError(Exception):

    def __str__(self):
        return 'Response malformed.'


class Base(object):

    def __init__(self, symbol):
        self.symbol = symbol
        self._table = ''
        self._key = ''

    def _prepare_query(self, table='quotes', key='symbol', **kwargs):
        """
        Simple YQL query bulder

        """
        query = 'select * from yahoo.finance.{table} where {key} = "{symbol}"'.format(
            symbol=self.symbol, table=table, key=key)
        if kwargs:
            for k, v in kwargs.iteritems():
                query += ' and {0}="{1}"'.format(k, v)
        return query

    @staticmethod
    def _is_error_in_results(results):
        """
        Check if key name does not start from `Error*`

        For example when Symbol is not found we can find key:
        `"ErrorIndicationreturnedforsymbolchangedinvalid": "No such ticker symbol. (...)",`
        """
        # check if response is dictionary, skip if it is different e.g. list from `get_historical()`
        if isinstance(results, dict):
            return next((results[i] for i in results.keys() if 'Error' in i), False)

    @staticmethod
    def _change_incorrect_none(results):
        """
        Change N/A values to None

        """
        # check if response is dictionary, skip if it is different e.g. list from `get_historical()`
        if isinstance(results, dict):
            for k, v in results.iteritems():
                if v:
                    if 'N/A' in v:
                        results[k] = None

    def _request(self, query):
        response = yql.YQLQuery().execute(query)
        try:
            results = response['query']['results'].itervalues().next()
        except (KeyError, StopIteration):
            try:
                raise YQLQueryError(response['error']['description'])
            except KeyError:
                raise YQLResponseMalformedError()
        else:
            if self._is_error_in_results(results):
                raise YQLQueryError(self._is_error_in_results(results))
            self._change_incorrect_none(results)
            return results

    def _fetch(self):
        query = self._prepare_query(table=self._table, key=self._key)
        data = self._request(query)
        return data

    def refresh(self):
        """
        Refresh stock data

        """
        self.data_set = self._fetch()


# Phase this out?
class Currency(Base):

    def __init__(self, symbol):
        super(Currency, self).__init__(symbol)
        self._table = 'xchange'
        self._key = 'pair'
        self.refresh()

    def _fetch(self):
        data = super(Currency, self)._fetch()
        if data['Date'] and data['Time']:
            data[u'DateTimeUTC'] = edt_to_utc('{0} {1}'.format(data['Date'], data['Time']))
        return data

    def get_bid(self):
        return self.data_set['Bid']

    def get_ask(self):
        return self.data_set['Ask']

    def get_rate(self):
        return self.data_set['Rate']

    def get_trade_datetime(self):
        return self.data_set['DateTimeUTC']


class Share(Base):

    def __init__(self, symbol):
        super(Share, self).__init__(symbol)
        self._table = 'quotes'
        self._key = 'symbol'
        self.refresh()

    def _fetch(self):
        data = super(Share, self)._fetch()
        if data['LastTradeDate'] and data['LastTradeTime']:
            data[u'LastTradeDateTimeUTC'] = edt_to_utc('{0} {1}'.format(data['LastTradeDate'], data['LastTradeTime']))
        return data

    def get_ask(self):
        return self.data_set['Ask']                         #YQL: a
        
    def get_avg_daily_volume(self):
        return self.data_set['AverageDailyVolume']          #YQL: a2
        
    def get_bid(self):
        return self.data_set['Bid']                         #YQL: b
    
    # returns N/A
    def get_ask_real_time(self):
        return self.data_set['AskRealtime']                 #YQL: b2
    
    # returns N/A
    def get_bid_real_time(self):
        return self.data_set['BidRealtime']                 #YQL: b3
    
    def get_book_value(self):
        return self.data_set['BookValue']                   #YQL: b4
    
    def get_percent_change(self):
        return self.data_set['Change&PercentChange']        #YQL: c

    def get_change(self):
        return self.data_set['Change']                      #YQL: c1

    # returns N/A
    def get_comission(self):
        return self.data_set['Comission']                   #YQL: c3 

    def get_currency(self):
        return self.data_set['Currency']                    #YQL: c4 
    
    # returns N/A
    def get_change_real_time(self):
        return self.data_set['ChangeRealtime']              #YQL: c6 
            
    def get_after_hours_change_real_time(self):
        return self.data_set['AFterHoursChangeRealTime']    #YQL: c8 
    
    # returns N/A
    def get_dividend_share(self):
        return self.data_set['DividendShare']               #YQL: d 
            
    def get_last_trade_date(self):
        return self.data_set['LastTradeDate']               #YQL: d1 
    
    def get_trade_date(self):
        return self.data_set['TradeDate']                   #YQL: d2 
            
    def get_earnings_share(self):
        return self.data_set['EarningsShare']               #YQL: e

    # returns N/A
    def get_(self):
        return self.data_set['ErrorIndicationreturnedforsymbolchangedinvalid']                            #YQL: e1 
            
    def get_eps_estimate_current_year(self):
        return self.data_set['EPSEstimateCurrentYear']      #YQL: e7 
    
    def get_eps_estimate_current_year(self):
        return self.data_set['EPSEstimateNextYear']         #YQL: e8 
    
    def get_eps_estimate_current_year(self):
        return self.data_set['EPSEstimateNextQuater']       #YQL: e9 
    
    def get_days_low(self):
        return self.data_set['DaysLow']                     #YQL: g 
    
    def get_days_high(self):
        return self.data_set['DaysHigh']                    #YQL: h 
    
    def get_year_low(self):
        return self.data_set['YearLow']                     #YQL: j 
        
    def get_year_low(self):
        return self.data_set['YearHigh']                    #YQL: k
    
    # returns N/A
    def get_holdings_gain_percent():
        return self.data_set['HoldingsGainpercent']        #YQL: g1 

    # returns N/A
    def get_annualized_gain():
        return self.data_set['AnnualizedGain']             #YQL: g3 

    # returns N/A
    def get_holdings_gain():
        return self.data_set['HoldingsGain']               #YQL: g4

    # returns N/A
    def get_holdings_gain_percent_real_time():
        return self.data_set['HoldingsGainPercentRealtime']#YQL: g5 

    # returns N/A
    def get_holdings_gain_real_time():
        return self.data_set['HoldingsGainRealtime']       #YQL: g6 

    # returns N/A
    def get_more_info():
        return self.data_set['MoreInfo']                   #YQL: i 

    # returns N/A
    def get_order_book_real_time():
        return self.data_set['OrderBookRealtime']          #YQL: i6 

    def get_market_cap(self):
        return self.data_set['MarketCapitalization']       #YQL: j1
        
    def get_market_cap_real_time():
        return self.data_set['MarketCapRealtime']          #YQL: j3 

    def get_ebitda(self):
        return self.data_set['EBITDA']                     #YQL: j4
        
    def get_change_from_year_low():
        return self.data_set['ChangeFromYearLow']          #YQL: j5 

    def get_percent_change_from_year_low():
        return self.data_set['PercentChangeFromYearLow']   #YQL: j6 

    # returns N/A
    def get_last_trade_real_time_with_time():
        return self.data_set['LastTradeRealtimeWithTime']  #YQL: k1 
    
    # returns N/A
    def get_change_percent_real_time():
        return self.data_set['ChangePercentRealtime']      #YQL: k2 

    def get_change_from_year_high():
        return self.data_set['ChangeFromYearHigh']         #YQL: k4 

    def get_percent_change_from_year_high():
        return self.data_set['PercentchangeFromYearHigh']  #YQL: k5 

    def get_last_trade_with_time():
        return self.data_set['LastTradeWithTime']          #YQL: l 
        
    def get_price(self):
        return self.data_set['LastTradePriceOnly']          #YQL: l1

    def get_high_limit(self):
        return self.data_set['HighLimit']                   #YQL: l2 

    def get_low_limit(self):
        return self.data_set['LowLimit']                    #YQL: l3 
            
    def get_days_range(self):
        return self.data_set['DaysRange']                   #YQL: m 
            
    def get_days_range_real_time(self):
        return self.data_set['DaysRangeRealtime']           #YQL: m2 
         
    def get_50day_moving_avg(self):
        return self.data_set['FiftydayMovingAverage']       #YQL: m3
    
    def get_200day_moving_avg(self):
        return self.data_set['TwoHundreddayMovingAverage']  #YQL: m4
          
    def get_change_from_200_day_moving_avg(self):
        return self.data_set['ChangeFromTwoHundreddayMovingAverage'] #YQL: m5

    def get_percent_change_from_200_day_moving_avg(self):
        return self.data_set['PercentChangeFromTwoHundreddayMovingAverage']      #YQL: m6 
              
    def get_change_from_50_day_moving_avg(self):
        return self.data_set['ChangeFromFiftydayMovingAverage']     #YQL: m7
        
    def get_percent_change_from_50_day_moving_avg(self):
        return self.data_set['PercentChangeFromFiftydayMovingAverage'] #YQL: m8 
       
    def get_company_name(self):
        return self.data_set['Name']                         #YQL: n
    
    # returns N/A
    def get_notes(self):
        return self.data_set['Notes']                        #YQL: n4 
                    
    def get_open(self):
        return self.data_set['Open']                        #YQL: o

    def get_prev_close(self):
        return self.data_set['PreviousClose']               #YQL: p
                    
    def get_price_paid(self):
        return self.data_set['PricePaid']                   #YQL: p1
            
    def get_change_in_percent(self):
        return self.data_set['ChangeinPercent']             #YQL: p2 
            
    def get_price_sales(self):
        return self.data_set['PriceSales']                  #YQL: p5
            
    def get_price_book(self):
        return self.data_set['PriceBook']                   #YQL: p6
            
    def get_ex_dividend_date(self):
        return self.data_set['ExDividendDate']              #YQL: q
           
    def get_PERatio(self):
        return self.data_set['PERatio']                     #YQL: r 
            
    def get_dividend_pay_date(self):
        return self.data_set['DividendPayDate']             #YQL: r1
            
    def get_pe_ratio_real_time(self):
        return self.data_set['PERatioRealtime']             #YQL: r2
            
    def get_peg_ratio(self):
        return self.data_set['PEGRatio']                    #YQL: r5 
            
    def get_price_eps_estimate_current_year(self):
        return self.data_set['PriceEPSEstimateCurrentYear'] #YQL: r6 
            
    def get_price_eps_estimate_next_year(self):
        return self.data_set['PriceEPSEstimateNextYear']    #YQL: r7 
            
    def get_symbol(self):
        return self.data_set['Symbol']                      #YQL: s 
            
    def get_shares_owned(self):
        return self.data_set['SharesOwned']                 #YQL: s1 
    
    def get_short_ratio(self):
        return self.data_set['ShortRatio']                  #YQL: s7
        
    def get_last_trade_time(self):
        return self.data_set['LastTradeTime']               #YQL: t1 
            
    def get_ticker_trend(self):
        return self.data_set['TickerTrend']                 #YQL: t7 
            
    def get_one_year_target_price(self):
        return self.data_set['OneyrTargetPrice']            #YQL: t8
            
    def get_holdings_value(self):
        return self.data_set['HoldingsValue']               #YQL: v1 

    def get_holdinvs_value_real_time(self):
        return self.data_set['HoldingsValuerealtime']       #YQL: v7
    
    def get_year_range(self):
        return self.data_set['YearRange']                   #YQL: w
    
    def get_days_value_change(self):
        return self.data_set['DaysValueChange']             #YQL: w1
            
    def get_days_value_change_real_time(self):
        return self.data_set['DaysValueChangeRealtime']     #YQL: w4
                        
    def get_stock_exchange(self):
        return self.data_set['StockExchange']   #YQL: x
        
    def get_volume(self):
        return self.data_set['Volume']          #YQL: v

    def get_dividend_yield(self):
        return self.data_set['DividendYield']   #YQL: y

    def get_trade_datetime(self):
        return self.data_set['LastTradeDateTimeUTC']
        
    def get_historical(self, start_date, end_date):
        """
        Get Yahoo Finance Stock historical prices

        :param start_date: string date in format '2009-09-11'
        :param end_date: string date in format '2009-09-11'
        :return: list
        """
        hist = []
        for s, e in get_date_range(start_date, end_date):
            try:
                query = self._prepare_query(table='historicaldata', startDate=s, endDate=e)
                result = self._request(query)
                if isinstance(result, dict):
                    result = [result]
                hist.extend(result)
            except AttributeError:
                pass
        return hist

    def get_info(self):
        """
        Get Yahoo Finance Stock Summary Information

        :return: dict
        """
        query = self._prepare_query(table='stocks')
        return self._request(query)
