import yfinance as yf # new module?
import os
import pandas as pd

def weekly_data():
  print("Gathering Weekly Data...")
  file = open("tickers.txt")
  tickers = []
  for line in file:
      tickers.append(line)

  for ticker in tickers:
      tickerstrip = ticker.strip('\n')
      if "^" in tickerstrip or "/" in tickerstrip:
          pass
      else:
          data = yf.download(tickerstrip, start="2021-03-15", end="2021-03-17", interval='15m',)
          data.to_csv("data/{}.csv".format(tickerstrip))

def oscilations():
    print("Filtering Through Algo...")
    number = 1
    new_df = pd.DataFrame(columns=['Symbol', 'Entry', 'Exit', 'Gains'])
    for filename in os.listdir('data'):
        new_row = {}
        symbol = filename.split(".")[0]
        df = pd.read_csv('data/{}'.format(filename))
        if df.empty:
            continue
        high = df['Close'].max()
        low = df['Close'].min()
        mid = (high + low) / 2
        Q1 = (low + mid) / 2
        Q3 = (high + mid) / 2
        A1 = (Q1 + low) / 2
        A2 = (Q3 + high) / 2

        fr23 = (A2 - ((A2 - A1) * 0.236))
        fr38 = (A2 - ((A2 - A1) * 0.382))
        fr50 = (A2 - ((A2 - A1) * 0.500))
        fr61 = (A2 - ((A2 - A1) * 0.618))
        fr76 = (A2 - ((A2 - A1) * 0.764))

        percentage_gain = (fr23 - fr76) / fr76 * 100

        if percentage_gain > 6 and fr76 < df.iloc[-1]['Close'] and fr23 > df.iloc[-1]['Close']:
            print("{} Gain: {}% Entry: {} Exit: {} Close: {} Hits: #{}".format(symbol, round(percentage_gain, 2), round(fr76, 2), round(fr23, 2), round(df.iloc[-1]['Close'], 2), number))
            new_row['Symbol'] = symbol
            new_row['Entry'] = round(fr76, 2)
            new_row['Exit'] = round(fr23, 2)
            new_row['Gains'] = round(percentage_gain, 2)
            new_df = new_df.append(new_row, ignore_index=True)
            number = number + 1

    new_df.to_csv("list.csv")