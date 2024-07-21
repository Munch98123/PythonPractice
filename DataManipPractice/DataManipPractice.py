import requests
import pandas as pd
import yfinance as yf

import matplotlib.pyplot as plt

class StockDataFetcher:
    
    def _init_(self, api_key):
        self.api_key = api_key
        #used for api URL 
        self.base_url = "API URL"

    def fetch_stock_data(symbol, api_key):
        try:
            """
            Example for having an API key using alpha instead of yahoo finance
            endpoint = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
            response = requests.get(endpoint)
            response.raise_for_status()
            data = response.json()['Time Series(Daily)']
            df = pd.DataFrame(data).transpose()
            df.index = pd.to_datetime(df.index)
            df.sort_index(inplace=True)
            """
            stock_data = yf.download(symbol, start='2020-01-01', end='2024-01-01')
            if not stock_data:
                raise ValueError("No data returned from call") 
        
            return stock_data
        except requests.exceptions.RequestException as ex:
            print(f"Error fetching data: {ex}")
            return None
        

symbol = 'AAPL'
stock_fetcher = StockDataFetcher(None)
stock_data = stock_fetcher.fetch_stock_data(symbol, None)

if stock_data is not None:
    print(stock_data.head())

plt.figure(figsize=(10,6))
plt.plot(stock_data.index, stock_data['Close'], label='Close Price', color='b')
plt.title('Stock Close Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()
