import pandas as pd
import vectorbtpro as vbt
import numpy as np
import json
import matplotlib.pyplot as plt

# Load your data into a DataFrame (df) here
# Load the data from the JSON file
with open('data/AUDCHF_2023-10-19_2023-11-18.json', 'r') as f:
    data = json.load(f)

# Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Convert the date column to datetime and set it as the index
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Parameters
output_smoothing = 20
trigger_smoothing = 4
atr_length = 200
multiplier = 6
range_switch = "Body"
use_double = True

# Calculate candle top and bottom
if range_switch != "Body":
    candle_top = df['high']
    candle_bottom = df['low']
else:
    candle_top = df[['open', 'close']].max(axis=1)
    candle_bottom = df[['open', 'close']].min(axis=1)

# Calculate smoothed top and bottom
smooth_top = candle_top.rolling(trigger_smoothing).mean()
smooth_bottom = candle_bottom.rolling(trigger_smoothing).mean()

# Calculate true range and ATR
tr = candle_top - candle_bottom
atr = tr.rolling(atr_length).mean()

# Initialize series
sr_ma = pd.Series(index=df.index)
current_range = pd.Series(index=df.index)
top_range = pd.Series(index=df.index)
bottom_range = pd.Series(index=df.index)

# Calculate SR MA, current range, top range, and bottom range
cross_up = (df['close'] > top_range.shift(1)) & (df['close'].shift(1) <= top_range.shift(2))
cross_down = (df['close'] < bottom_range.shift(1)) & (df['close'].shift(1) >= bottom_range.shift(2))
flag = cross_up | cross_down | current_range.isna()
sr_ma[flag] = df['close'][flag]
sr_ma = sr_ma.ffill()  # forward fill to keep the previous value when the SR MA isn't recalculated
current_range[flag] = atr[flag] * multiplier
top_range[flag] = sr_ma[flag] + current_range[flag]
bottom_range[flag] = sr_ma[flag] - current_range[flag]

# Apply simple filter
if use_double:
    sr_ma = vbt.MA.run(vbt.MA.run(sr_ma, output_smoothing).ma, output_smoothing).ma
    top_range = vbt.MA.run(vbt.MA.run(top_range, output_smoothing).ma, output_smoothing).ma
    bottom_range = vbt.MA.run(vbt.MA.run(bottom_range, output_smoothing).ma, output_smoothing).ma
else:
    sr_ma = vbt.MA.run(sr_ma, output_smoothing).ma
    top_range = vbt.MA.run(top_range, output_smoothing).ma
    bottom_range = vbt.MA.run(bottom_range, output_smoothing).ma

# Define conditions for color changes
plot_neutral = (df['high'] > sr_ma) & (df['low'] < sr_ma)
plot_bullish = df['low'] > sr_ma
plot_bearish = df['high'] < sr_ma

# Create a DataFrame to hold the conditions
conditions = pd.DataFrame({
    'bullish': plot_bullish,
    'bearish': plot_bearish,
    'neutral': plot_neutral
})

# Create a color map for conditions
color_map = {'bullish': 'green', 'bearish': 'red', 'neutral': 'grey'}

# Map the conditions to colors
colors = conditions.idxmax(axis=1).map(color_map)

# Make sr_ma go flat during neutral condition
sr_ma[plot_neutral] = np.nan
sr_ma = sr_ma.ffill()

# Plot a line for each condition
for condition, color in color_map.items():
    mask = conditions[condition]
    plt.plot(df.loc[mask].index, sr_ma[mask], color=color)

plt.show()