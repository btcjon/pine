import os
from dotenv import load_dotenv
import pandas as pd
from alpha_vantage.foreignexchange import ForeignExchange
import vectorbtpro as vbt
import matplotlib.pyplot as plt  # Import matplotlib.pyplot
import numpy as np
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Accessing the API key from environment variables
api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

# Check if the API key is retrieved successfully
if not api_key:
    raise ValueError("API key not found. Please check your .env file.")

# Set up client with your API key
client = ForeignExchange(key=api_key)

# Fetch data
data, _ = client.get_currency_exchange_daily('EUR', 'USD', outputsize='full')

# Convert data to DataFrame
df = pd.DataFrame(data).transpose()
df.columns = ['Open', 'High', 'Low', 'Close']

# Convert index to datetime
df.index = pd.to_datetime(df.index)

# Convert data to numeric format
df = df.apply(pd.to_numeric)

# Save data locally
df.to_hdf('my_data.h5', key='data')

# Access the saved data
df = pd.read_hdf('my_data.h5', key='data')

open_price = data.get('Open')
close_price = data.get('Close')


vbt.IF.list_indicators("RSI*")
['vbt:RSI', 'talib:RSI', 'pandas_ta:RSI', 'ta:RSIIndicator', 'technical:RSI']