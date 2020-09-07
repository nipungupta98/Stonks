import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt


class linreg:
    def __init__(self, stock_data, ticker):
        self.stock_data = stock_data
        self.ticker = ticker

    def predict_price(self):
        X = np.array(self.stock_data[["ewm12", "rsi", "stoc", "diff", "ewm26", "Open", "Signal", "Close"]])
        y = np.array(self.stock_data["Close"])

        X = X[15:-1, :]
        y = y[16:]

        X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

        regr = LinearRegression().fit(X_train, y_train)
        y_pred = regr.predict(X_test)

        print("Yesterday's price", y[-1])
        print("Predicted today's price", regr.predict(X[-1:]))
        print("MSE = ", mean_squared_error(y_pred[1:], y_test[:-1]))

