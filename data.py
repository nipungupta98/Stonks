from datetime import date, timedelta
import yfinance as yf
import pandas as pd

def get_ticker():
    ticker = input("Name the ticker you want to get the price")
    return ticker

def get_data(ticker, n = 1000):
    today = date.today()
    startd = today - timedelta(days=n)

    ticker_data = yf.Ticker(ticker)
    ticker_data = ticker_data.history(period='1d', start=startd, end=today)

    ticker_pd = pd.DataFrame(ticker_data)
    ticker_pd = ticker_pd.drop(['Dividends', 'Stock Splits'], axis=1)
    return ticker_pd


def print_data(ticker, n = 1000, rev=True):

    today = date.today()
    startd = today - timedelta(days=n)

    ticker_data = yf.Ticker(ticker)
    ticker_data = ticker_data.history(period='1d', start=startd, end=today)

    ticker_pd = pd.DataFrame(ticker_data)
    ticker_pd = ticker_pd.drop(['Dividends', 'Stock Splits'], axis = 1)
    if rev:
        print(ticker_pd[::-1])
    else:
        print(ticker_pd)
