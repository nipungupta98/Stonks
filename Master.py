import ML_model
import data
import ta

ticker = data.get_ticker()
stock_data = data.get_data(ticker, 4000)
stock_data = ta.analysis(stock_data)

linreg = ML_model.linreg(stock_data, ticker)
linreg.predict_price()


