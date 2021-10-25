import yfinance as yf
import pandas as pd
import multiprocessing
from joblib import Parallel, delayed


def createMarketDict(ticker, marketData):
    # marketData = dict()
    print(ticker)
    stock = yf.Ticker(f"{ticker}")
    try:
        data = stock.history(period="max")
        if not data.empty:
            marketData[f"{ticker}"] = stock.history(period="max")
    except:
        print("Moving on")



num_cores = multiprocessing.cpu_count()
tickerList = pd.read_csv("tickerList.csv", index_col=False)["Symbol"]
marketData = dict()
Parallel(n_jobs=num_cores)(delayed(createMarketDict)(ticker, marketData) for ticker in tickerList)

