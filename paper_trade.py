from webull import paper_webull as pw # new module
from webull import webull as wb
import pandas as pd
from datetime import datetime
import os

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
df = pd.read_csv("list.csv", skipinitialspace=True)
pw = pw()
wb = wb()

def limit_buy():
  print("Setting Up Buy Orders...")
  pw.login(username=username, password=password)
  for row in df.itertuples(index=True, name='Pandas'):
        stock = pd.DataFrame(pw.get_bars(stock=row.Symbol, extendTrading=1)).squeeze()
        quantity = int(500/stock.close)
        pw.place_order(stock=row.Symbol, price=row.Entry, action='BUY', orderType='LMT', quant=quantity)
  pw.logout()

def open_market():
    print("Trading Commenced...")
    pw.login(username=username, password=password)
    print(pw.get_account())
    while datetime.now().hour > 4 and datetime.now().hour < 20:
        for row in df.itertuples(index=True, name='Pandas'):
            stock = pd.DataFrame(pw.get_bars(stock=row.Symbol, extendTrading=1)).squeeze()
            if stock.close >= row.Exit or stock.close <= (row.Entry - (row.Entry * .06)):
                for position in pw.get_positions():
                    if row.Symbol in position['ticker']['symbol']:
                        print("Selling Asset...")
                        if stock.close > row.Exit:
                          price = row.Exit
                        else:
                          price = (row.Entry - (row.Entry * .06))
                        pw.place_order(stock=row.Symbol, price=price, action='SELL', orderType='LMT', quant=position['position'])
        pw.refresh_login()
    pw.logout()