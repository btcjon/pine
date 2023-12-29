import os
import pandas as pd
import requests
from dotenv import load_dotenv
import vectorbtpro as vbt
import plotly.graph_objects as go
import talib
import pandas_ta as ta
import numpy as np
from vectorbtpro.indicators.factory import IndicatorFactory
# Load environment variables from .env file
load_dotenv()

# Fetch the data
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=EURUSD&interval=1min&apikey={api_key}&datatype=json&outputsize=full"

if os.path.exists('data.csv'):
    df = pd.read_csv('data.csv', index_col=0, parse_dates=True)
    print("Data loaded from CSV file.")
else:
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['Time Series (1min)']).T
    df.rename(columns={
        '1. open': 'open', '2. high': 'high', 
        '3. low': 'low', '4. close': 'close', '5. volume': 'volume'}, 
        inplace=True)
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df.to_csv('data.csv')
    print("Data fetched from API and saved to CSV file.")

# Create instances of indicator factories
ema_factory = IndicatorFactory.from_talib('EMA')
rsi_factory = IndicatorFactory.from_talib('RSI')

# Calculate indicators
ema_500 = ema_factory.run(close=df['close'], timeperiod=500)
rsi = rsi_factory.run(close=df['close'], timeperiod=14)

# Define strategy conditions using calculated indicators
entries = (rsi.real <= 20) & (df['close'] > ema_500.real)
exits = (rsi.real >= 80) & (df['close'] < ema_500.real)

# Set up TP and SL percentages
tp_percentage = 0.0007  # TP at 0.07%
sl_percentage = 0.01  # SL at 1%

# Run backtest
portfolio = vbt.Portfolio.from_signals(
    close=df['close'],
    entries=entries,
    exits=exits,
    size=100,  # Use a fixed size for simplicity; adjust as needed
    size_type='value',  # Size represents the value invested in each trade
    tp_stop=tp_percentage,  # Take-profit stop
    sl_stop=sl_percentage,  # Stop-loss stop
    freq='1min'  # 1-minute frequency
)

# Analyze results
print(portfolio.stats())

# Plot results
portfolio.plot().show()