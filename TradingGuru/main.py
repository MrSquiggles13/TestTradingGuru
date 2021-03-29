from TD import TD
import paper_trade
import squeeze

td = TD()

#td.get_all_tickers_data()
#td.fundamental_screener()
#squeeze.pump_it()
#squeeze.oscilations()
#paper_trade.set_orders()

#stock = td.get_ticker_price(symbol="AAPL", period='1', periodType='day', frequency='1', frequencyType='minute')['candles'][-1]

# import alpaca_trade_api as alp
# import pandas as pd
# from TD import TD
# import os, time
#
# BASE_URL = "https://paper-api.alpaca.markets"
# API_KEY = "PKP57LLJMPH3OVSEXHQ7"
# API_SECRET = "TO0fS6ElYU5kFCEzmMayWncLHMqR2ph0GpHEqNh3"
#
# td = TD()
# alp = alp.REST(key_id=API_KEY, secret_key=API_SECRET, base_url=BASE_URL, api_version='v2')
#
# alp.submit_order(symbol="AAPL", qty=2, side="buy", type="limit", time_in_force='gtc', limit_price="120.64", order_class='bracket', stop_loss=dict(limit_price='119.50', stop_price='119.50'), take_profit=dict(limit_price='123.5'))


# import pandas as pd
# import time
# from datetime import datetime
#
# start = datetime(2021, 3, 22, 0, 0).timestamp() * 1000
# end = datetime(2021, 3, 23, 12, 0).timestamp() * 1000
#
# entryReached = False
# exitReached = False
# swingComplete = False
#
# swings = pd.read_csv("/Users/commanderspectre/PycharmProjects/TestTradingGuru/Data/old_swings.csv")
#
# compare_df = pd.DataFrame(columns=['Symbol', 'Entry', 'Exit', 'Gains'])
#
# with open('/Users/commanderspectre/PycharmProjects/TestTradingGuru/Data/time_of_swing.txt', 'w') as file:
#
#     for swing in swings.itertuples(index=True, name='Pandas'):
#
#         data = td.get_ticker_price(symbol=swing.Symbol, period='1', periodType='day', frequency='1', frequencyType='minute')['candles']
#         time.sleep(1)
#         entryReached = False
#         exitReached = False
#         swingComplete = False
#         for minute in data:
#             string = ""
#             if minute['low'] <= swing.Entry:
#                 entryReached = True
#                 string = "Entry reached for " + swing.Symbol + " @ " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(minute['datetime']/1000 - 14400))
#                 file.write(string + '\n')
#             if minute['high'] >= swing.Exit:
#                 exitReached = True
#                 string = "Exit reached for " + swing.Symbol + " @ " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(minute['datetime'] / 1000 - 14400))
#                 file.write(string + '\n')
#             if exitReached and entryReached:
#                 swingComplete = True
#
#         if swingComplete:
#             new_row = {}
#             new_row['Symbol'] = swing.Symbol
#             new_row['Entry'] = swing.Entry
#             new_row['Exit'] = swing.Exit
#             new_row['Gains'] = swing.Gains
#             compare_df = compare_df.append(new_row, ignore_index=True)
#
#     file.close()
#
# compare_df.to_csv("/Users/commanderspectre/PycharmProjects/TestTradingGuru/Data/successful_swings.csv")

# data = td.get_ticker_price(symbol='AAPL', period='1', periodType='day', frequency='1', frequencyType='minute')['candles']

import pandas as pd
from datetime import datetime, timedelta

# df = pd.read_csv("/Users/commanderspectre/PycharmProjects/TestTradingGuru/Data/swing_times.csv")
# ########### figure out swing time format #################
#
# holidays_2021 = ['Friday, January 1, 2021',
# 'Monday, January 18, 2021',
# 'Monday, February 15, 2021',
# 'Friday, April 2, 2021',
# 'Monday, May 31, 2021',
# 'Monday, July 5, 2021',
# 'Monday, September 6, 2021',
# 'Thursday, November 25, 2021',
# 'Friday, December 24, 2021']
#
# holidays_2020 = ['01/01/2021',
# '01/01/2020',
# '01/20/2020',
# '02/17/2020',
# '04/10/2020',
# '05/25/2020',
# '07/03/2020',
# '09/07/2020',
# '11/26/2020',
# '12/25/2020']
#
# all_mondays = pd.date_range(start='2020', end='2021', freq='W-MON').strftime('%m/%d/%Y').tolist()
# all_tuesdays = pd.date_range(start='2020', end='2021', freq='W-TUE').strftime('%m/%d/%Y').tolist()
# all_wednesdays = pd.date_range(start='2020', end='2021', freq='W-WED').strftime('%m/%d/%Y').tolist()
# all_thursdays = pd.date_range(start='2020', end='2021', freq='W-THU').strftime('%m/%d/%Y').tolist()
# all_fridays = pd.date_range(start='2020', end='2021', freq='W-FRI').strftime('%m/%d/%Y').tolist()
#
# all_weekdays_in_2020 = all_mondays + all_tuesdays + all_wednesdays + all_thursdays + all_fridays
#
# all_weekdays_in_2020.sort()
#
# open_market_days_2020 = []
#
# for day in all_weekdays_in_2020:
#     if day not in holidays_2020:
#         open_market_days_2020.append(day)
#
# test_market_days = ['12/31/2020', '02/24/2020']
#
#
#
# for day in test_market_days:
#     end = pd.to_datetime(day)
#     start = end - timedelta(days=3)
#     start = str(int(start.timestamp() * 1000))
#     end = str(int(end.timestamp() * 1000))
#     data = td.get_ticker_price(symbol='AAPL', startDate=start, endDate=end, periodType='day', frequency='1',
#                                frequencyType='minute')['candles']
from datetime import datetime
import time

start =  str(int(datetime(2020, 3, 18, 12, 0).timestamp() * 1000))
end = str(int(datetime(2020, 3, 25, 12, 0).timestamp() * 1000))

data = td.get_ticker_price(symbol='AAPL', startDate=start, endDate=end, periodType='day', frequency='1', frequencyType='minute')['candles']


