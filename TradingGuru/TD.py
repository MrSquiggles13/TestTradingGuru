import time, requests, re, os
import pandas as pd
import pickle as pkl

apiKey = "AFEIQY5RJQ4ZLDZBPDSDRVNAI5PZHGIL"
accountID = "19715277"

class TD:

    def __init__(self):
        df = pd.read_csv('//Data/tickers.csv')
        self.symbols = df['Symbol'].tolist()

    def get_ticker_price(self, **kwargs):
        url = "https://api.tdameritrade.com/v1/marketdata/{}/pricehistory".format(kwargs.get('symbol'))

        params = {}
        params.update({'apikey': apiKey})

        for arg in kwargs:
            parameter = {arg: kwargs.get(arg)}
            params.update(parameter)

        results = requests.get(url, params=params)
        return results.json()

    def get_all_tickers_data(self):
        dirPath = "/Users/commanderspectre/PycharmProjects/TestTradingGuru/Data/StockOscillationData/"

        for symbol in self.symbols:
            if (symbol + '.csv') not in os.listdir(dirPath):
                f_name = symbol + '.csv'
                data = self.get_ticker_price(symbol=symbol, period='3', periodType='day', frequency='15', frequencyType='minute')
                df = pd.DataFrame(columns=['open', 'high', 'low', 'close', 'volume', 'datetime'])
                try:
                    for dict in data['candles']:
                        df = df.append(dict, ignore_index=True)
                    df.to_csv(dirPath + f_name)
                except:
                    continue
                time.sleep(1)

    def fundamental_screener(self):
        dirPath = "/Users/commanderspectre/PycharmProjects/TestTradingGuru/Data/StockFundamentalData/"
        url = "https://api.tdameritrade.com/v1/instruments"

        start = 0
        end = 100
        files = []
        while start < len(self.symbols):
            tickers = self.symbols[start:end]

            payload = {'apikey': "AFEIQY5RJQ4ZLDZBPDSDRVNAI5PZHGIL",
                       'symbol': tickers,
                       'projection': 'fundamental'}

            results = requests.get(url, params=payload)
            data = results.json()
            f_name = time.asctime() + '.pkl'
            f_name = re.sub("[ :]", "_", f_name)
            files.append(f_name)
            with open(dirPath + f_name, 'wb') as file:
                pkl.dump(data, file)

            start = end
            end += 100
            time.sleep(1)

        data = []

        for file in files:
            with open(dirPath + file, 'rb') as f:
                info = pkl.load(f)
            tickers = list(info)
            points = ['symbol', 'netProfitMarginMRQ', 'peRatio', 'pegRatio', 'high52']
            for ticker in tickers:
                tick = []
                for point in points:
                    tick.append(info[ticker]['fundamental'][point])
                data.append(tick)
            os.remove(dirPath + file)

        points = ['symbol', 'margin', 'PE', 'PEG', 'high52']

        df_results = pd.DataFrame(data, columns=points)

        winners = df_results[
            (df_results['PEG'] < 1) & (df_results['PEG'] > 0) & (df_results['margin'] > 20) & (df_results['PE'] > 10)]

        winners.to_csv("/Users/commanderspectre/PycharmProjects/TestTradingGuru/Data/winners.csv")
