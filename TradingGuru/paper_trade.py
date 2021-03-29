import alpaca_trade_api as alp
import pandas as pd
from TD import TD
import os, time

BASE_URL = "https://paper-api.alpaca.markets"
API_KEY = "PKP57LLJMPH3OVSEXHQ7"
API_SECRET = "TO0fS6ElYU5kFCEzmMayWncLHMqR2ph0GpHEqNh3"

td = TD()
alp = alp.REST(key_id=API_KEY, secret_key=API_SECRET, base_url=BASE_URL, api_version='v2')

def set_orders():
    df = pd.read_csv("//Data/swings.csv")

    for row in df.itertuples(index=True, name='Pandas'):
        try:
            stock = \
            td.get_ticker_price(symbol=row.Symbol, period='1', periodType='day', frequency='1', frequencyType='minute')[
                'candles'][-1]
            quantity = int(300 / stock['close'])
            alp.submit_order(symbol=row.Symbol, qty=quantity, side='buy', type='limit', order_class='bracket', limit_price=str(row.Entry), stop_loss=dict(stop_price=str(row.Entry - row.Entry * .06), limit_price=str(row.Entry - row.Entry * .06)), take_profit=dict(limit_price=str(row.Exit)), time_in_force='gtc')
            time.sleep(1)
        except:
            continue