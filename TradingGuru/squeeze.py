import os, time
from TD import TD
import pandas as pd

td = TD()

def oscilations():
    dirPath = "/Users/commanderspectre/PycharmProjects/TestTradingGuru/Data/StockOscillationData/"
    new_df = pd.DataFrame(columns=['Symbol', 'Entry', 'Exit', 'Gains'])
    for filename in os.listdir(dirPath):
        new_row = {}
        symbol = filename.split(".")[0]
        df = pd.read_csv(dirPath + filename)
        if df.empty:
            continue
        high = df['close'].max()
        low = df['close'].min()
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

        entry = fr76
        exit = fr23

        if percentage_gain > 6 and entry < df.iloc[-1]['close'] and exit > df.iloc[-1]['close']:
            print("{} Gain: {}% Entry: {} Exit: {} Close: {}".format(symbol, round(percentage_gain, 2), round(entry, 2), round(exit, 2), round(df.iloc[-1]['close'], 2)))
            new_row['Symbol'] = symbol
            new_row['Entry'] = round(fr76, 2)
            new_row['Exit'] = round(fr23, 2)
            new_row['Gains'] = round(percentage_gain, 2)
            new_df = new_df.append(new_row, ignore_index=True)

    new_df.to_csv("/Users/commanderspectre/PycharmProjects/TestTradingGuru/Data/swings2.csv")

def pump_it():
    dirPathIN = "/Users/commanderspectre/PycharmProjects/TestTradingGuru/Data/StockOscillationData/"
    dirPathOUT = "/Users/commanderspectre/PycharmProjects/TestTradingGuru/Data/StockFundamentalData/"
    for symbol in pd.read_csv("//Data/winners.csv")['symbol']:
        try:
            data = td.get_ticker_price(symbol=symbol, period='1', periodType='day', frequency='1', frequencyType='minute')['candles']
        except:
            continue
        df = pd.DataFrame(data)
        if df.empty:
            continue

        df['20sma'] = df['close'].rolling(window=20).mean()
        df['stddev'] = df['close'].rolling(window=20).std()

        df['lower_band'] = df['20sma'] - (2 * df['stddev'])
        df['upper_band'] = df['20sma'] + (2 * df['stddev'])

        df['TR'] = abs(df['high'] - df['low'])
        df['ATR'] = df['TR'].rolling(window=20).mean()

        df['lower_channel'] = df['20sma'] - (df['ATR'] * 1.5)
        df['upper_channel'] = df['20sma'] + (df['ATR'] * 1.5)

        def in_squeeze(df):
            return df['lower_band'] > df['lower_channel'] and df['upper_band'] < df['upper_channel']

        df['squeeze_on'] = df.apply(in_squeeze, axis=1)

        indexREF = len(df)
        first = int(indexREF * .06)
        second = int((indexREF - first) * .33)
        third = int((indexREF - first) * .66)
        fourth = int(indexREF * .92)


        if not df.iloc[-fourth]['squeeze_on'] and not df.iloc[-third]['squeeze_on'] and df.iloc[-second]['squeeze_on'] and df.iloc[-first]['squeeze_on']:
            print("{} is ready to buy".format(symbol))
            df.to_csv(dirPathOUT + symbol + '.csv')

        time.sleep(1)