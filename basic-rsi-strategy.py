# Basic RSI strategy
# Single backtest
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
from alpha_vantage.foreignexchange import ForeignExchange
from plotly.subplots import make_subplots

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

open_price = df['open']
close_price = df['close']

vbt.IF.list_indicators("RSI*")

vbt.indicator("talib:RSI")

vbt.RSI

vbt.talib('RSI')

vbt.ta('RSIIndicator')

vbt.pandas_ta('RSI')

vbt.technical('RSI')

vbt.phelp(vbt.RSI.run)

rsi = vbt.RSI.run(open_price)

rsi.rsi

entries = rsi.rsi.vbt.crossed_below(30)

exits = rsi.rsi.vbt.crossed_above(70)

entries = rsi.rsi_crossed_below(30)
exits = rsi.rsi_crossed_above(70)

def plot_rsi(rsi, entries, exits, fig, row, col):
    rsi_plot = rsi.plot()
    rsi_trace = rsi_plot.data[0]
    fig.add_trace(rsi_trace, row=row, col=col)
    entries_plot = entries.vbt.signals.plot_as_entries(rsi.rsi)
    entries_trace = entries_plot.data[0]
    fig.add_trace(entries_trace, row=row, col=col)
    exits_plot = exits.vbt.signals.plot_as_exits(rsi.rsi)
    exits_trace = exits_plot.data[0]
    fig.add_trace(exits_trace, row=row, col=col)
    return fig

clean_entries, clean_exits = entries.vbt.signals.clean(exits)

pf = vbt.Portfolio.from_signals(
    close=close_price,
    entries=clean_entries,
    exits=clean_exits,
    size=100,
    size_type='value',
    init_cash='auto'
)

# Create a subplot grid
fig = make_subplots(rows=4, cols=1)

# Add the first plot to the first subplot
plot_rsi(rsi, entries, exits, fig, 1, 1)

# Add the second plot to the second subplot
plot_rsi(rsi, clean_entries, clean_exits, fig, 2, 1)

# Add the third plot (portfolio value) to the third subplot
pf_plot = pf.plot(settings=dict(bm_returns=False))
pf_trace = pf_plot.data[0]
fig.add_trace(pf_trace, row=3, col=1)

# Add the fourth plot (heatmap) to the fourth subplot
heatmap_plot = comb_stats_df['Expectancy'].vbt.heatmap()
heatmap_trace = heatmap_plot.data[0]
fig.add_trace(heatmap_trace, row=4, col=1)

fig.show()

clean_entries.vbt.signals.total()

clean_exits.vbt.signals.total()

ranges = clean_entries.vbt.signals.between_ranges(other=clean_exits)
ranges.duration.mean(wrap_kwargs=dict(to_timedelta=True))

pf.stats()

# Multiple backtests
# Using for-loop

def test_rsi(window=14, wtype="wilder", lower_th=30, upper_th=70):
    rsi = vbt.RSI.run(open_price, window=window, wtype=wtype)
    entries = rsi.rsi_crossed_below(lower_th)
    exits = rsi.rsi_crossed_above(upper_th)
    pf = vbt.Portfolio.from_signals(
        close=close_price,
        entries=entries,
        exits=exits,
        size=100,
        size_type='value',
        init_cash='auto')
    return pf.stats([
        'total_return',
        'total_trades',
        'win_rate',
        'expectancy'
    ])

test_rsi()

test_rsi(lower_th=20, upper_th=80)

from itertools import product

lower_ths = range(20, 31)
upper_ths = range(70, 81)
th_combs = list(product(lower_ths, upper_ths))

comb_stats = [
    test_rsi(lower_th=lower_th, upper_th=upper_th)
    for lower_th, upper_th in th_combs
]

comb_stats_df = pd.DataFrame(comb_stats)

comb_stats_df.index = pd.MultiIndex.from_tuples(
    th_combs,
    names=['lower_th', 'upper_th'])
comb_stats_df

# Using columns

windows = list(range(8, 21))
wtypes = ["simple", "exp", "wilder"]
lower_ths = list(range(20, 31))
upper_ths = list(range(70, 81))

rsi = vbt.RSI.run(
    open_price,
    window=windows,
    wtype=wtypes,
    param_product=True)

lower_ths_prod, upper_ths_prod = zip(*product(lower_ths, upper_ths))

lower_th_index = vbt.Param(lower_ths_prod, name='lower_th')
entries = rsi.rsi_crossed_below(lower_th_index)

upper_th_index = vbt.Param(upper_ths_prod, name='upper_th')
exits = rsi.rsi_crossed_above(upper_th_index)

pf = vbt.Portfolio.from_signals(
    close=close_price,
    entries=entries,
    exits=exits,
    size=100,
    size_type='value',
    init_cash='auto'
)

stats_df = pf.stats([
    'total_return',
    'total_trades',
    'win_rate',
    'expectancy'
], agg_func=None)

print(pf.getsize())

np.product(pf.wrapper.shape) * 8 / 1024 / 1024

stats_df['Expectancy'].groupby('rsi_window').mean()

stats_df.sort_values(by='Expectancy', ascending=False).head()

pf[(22, 80, 20, "wilder")].plot_value().show()
