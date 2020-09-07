import numpy as np
import data

stock_data = data.get_data("aapl")

def MACD(ticker_pd):
    ticker_pd['ewm12'] = ticker_pd['Close'].ewm(span=12, adjust = False).mean()
    ticker_pd['ewm26'] = ticker_pd['Close'].ewm(span=26, adjust=False).mean()

    ticker_pd['MACD'] = ticker_pd['ewm12'] - ticker_pd['ewm26']
    ticker_pd['Signal'] = ticker_pd['MACD'].ewm(span=9, adjust=False).mean()
    ticker_pd['diff'] = ticker_pd["MACD"] - ticker_pd["Signal"]

def RSI(ticker_pd, n=14):
    delta = ticker_pd['Close'].diff()
    dUp, dDown = delta.copy(), delta.copy()
    dUp[dUp < 0] = 0
    dDown[dDown > 0] = 0

    RolUp = np.absolute(dUp.rolling(n).mean())
    RolDown = np.absolute(dDown.rolling(n).mean())

    RS = RolUp / RolDown
    ticker_pd['rsi'] = 100.0 - (100.0 / (1.0 + RS))


def stochastic(ticker_pd, n=14):
    ticker_pd["stoc"] = (ticker_pd["Close"] - ticker_pd["Low"].rolling(n).min()) / (
                ticker_pd["High"].rolling(n).max() - ticker_pd["Low"].rolling(n).min()) * 100


def analysis(stock_data):
    MACD(stock_data)
    RSI(stock_data)
    stochastic(stock_data)
    return stock_data

