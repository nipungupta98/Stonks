# Stonks
Simple regression based stock predictor using multiple technical indicators. 

1) Pulls relevant stock data till the last trading day for given ticker symbol.
2) Select technical indicators from given list as pandas columns
3) Run regression to get the predicted price.

Employed technical indicators:

1) Moving averages
2) MACD (12, 26)
3) RSI
4) Stochastic

Required libraries:

1) yfinance:

   Installation instructions:
    
   1. Using pip: ```pip install yfinance --upgrade --no-cache-dir```
   2. Using conda: ```conda install -c ranaroussi yfinance```


2) Numpy
3) Pandas

Future scope: Adding more ta indicators, adding LSTM (RNN models), accuracy/loss matrix.

Stay tuned for more...
