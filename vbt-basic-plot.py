# this file is to help understand how we get/use data and how we prefer to plot it
import os
import pandas as pd
import requests
from dotenv import load_dotenv
import vectorbtpro as vbt
import plotly.graph_objects as go
import talib
import pandas_ta as ta
import numpy as np

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

# Calculate the SMA
sma = vbt.talib("SMA").run(df['close'], vbt.Default(10))

# Plot the data using Plotly
fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'],
                increasing_line_color= 'cyan', 
                decreasing_line_color= 'gray')])

# Add the SMA to the plot
fig = sma.real.rename("SMA(10)").vbt.plot(trace_kwargs=dict(line_color='red'), fig=fig)


fig.update_layout(
    autosize=True,
    template='plotly_dark',
    width=1800,
    height=1100,
    yaxis=dict(
        title_text="Price",
        titlefont=dict(size=14),
        side="right",
    ),
    paper_bgcolor='rgba(0,0,0,1)',  # This makes the page background black
    plot_bgcolor='rgba(0,0,0,1)'  # This makes the plot background black
)

fig.show()
