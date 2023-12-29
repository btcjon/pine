import os
import numpy as np
import pandas as pd
import vectorbtpro as vbt
from numba import njit
import requests
from dotenv import load_dotenv
import plotly.graph_objects as go
import talib
import pandas_ta as ta

# Load environment variables from .env file
load_dotenv()

# Get Alpha Vantage API key from environment variables
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

# Define the endpoint URL
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=EURUSD&interval=1min&apikey={api_key}&datatype=json&outputsize=full"

# Check if the CSV file exists
if os.path.exists('data.csv'):
    # Load the DataFrame from the CSV file
    df = pd.read_csv('data.csv', index_col=0, parse_dates=True)
    print("Data loaded from CSV file.")
else:
    # Send a GET request to the Alpha Vantage API
    response = requests.get(url)

    # Convert the response to JSON
    data = response.json()

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data['Time Series (1min)']).T

    # Rename the columns to match the format expected by VectorBT
    df.rename(columns={'1. open': 'open', '2. high': 'high', '3. low': 'low', '4. close': 'close', '5. volume': 'volume'}, inplace=True)

    # Convert the data types to float
    df = df.astype(float)

    # Convert the index to datetime format
    df.index = pd.to_datetime(df.index)

    # Save the DataFrame to a CSV file
    df.to_csv('data.csv')
    print("Data fetched from API and saved to CSV file.")

# User-defined parameters
length = 14  # Pivot Lookback
increment_factor = 100  # Increment factor (assumed in percentage, divide by 100 in calc)
reset_on = 'CHoCH'  # Reset stop on which structure type

# Define numba-compiled function for pivot points and trailing stops logic
@njit
def calculate_trailing_stops(highs, lows, closes, length, increment_factor):
    trailing_stop = np.full(len(closes), np.nan)
    trailing_max = np.copy(closes)
    trailing_min = np.copy(closes)
    for i in range(length, len(closes)):
        is_high = highs[i] == np.max(highs[i-length:i+1])
        is_low = lows[i] == np.min(lows[i-length:i+1])
        if is_high:
            trailing_max[i] = closes[i]
            trailing_stop[i] = trailing_max[i] - increment_factor * (trailing_max[i] - trailing_max[i-1])
        elif is_low:
            trailing_min[i] = closes[i]
            trailing_stop[i] = trailing_min[i] + increment_factor * (trailing_min[i-1] - trailing_min[i])
        # Carry over the last values if no new pivot is found
        trailing_stop[i] = trailing_stop[i-1]
        trailing_max[i] = trailing_max[i-1]
        trailing_min[i] = trailing_min[i-1]
    return trailing_stop

# Compute trailing stops using the 'df' DataFrame
trailing_stop = calculate_trailing_stops(df['high'].values, df['low'].values, df['close'].values, length, increment_factor / 100.0)

# Convert back to DataFrame for plotting with vectorbt
trailing_stop_df = pd.Series(trailing_stop, index=df.index)

# Create signals based on trailing stops and price
long_signals = df['close'] > trailing_stop_df
short_signals = df['close'] < trailing_stop_df

# Backtest the signals using the 'df' DataFrame
portfolio = vbt.Portfolio.from_signals(df['close'], long_signals, short_signals, init_cash=10000)

# Plotting the trailing stops with the candlestick chart and signals using the 'df' DataFrame
# Make sure to use correct case for DataFrame column names
fig = vbt.plot(df.open, df.high, df.low, df.close, df.volume)
trailing_stop_df.vbt.plot(trace_kwargs=dict(name='Trailing Stop'))
long_signals.vbt.signals.plot_as_entry_marks(df['close'], fig=fig)  # Correct method name
short_signals.vbt.signals.plot_as_exit_marks(df['close'], fig=fig)  # Correct method name

# Show and print results
fig.show()
print(portfolio.stats())
