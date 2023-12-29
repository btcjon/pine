import numpy as np
import pandas as pd
import talib.abstract as ta

# Assuming you have a pandas DataFrame `df` with columns 'open', 'high', 'low', 'close', 'volume'

# Define the functions

def normalize(series, min_val=0, max_val=1):
    return (series - series.min()) / (series.max() - series.min()) * (max_val - min_val) + min_val

def rescale(series, old_min, old_max, new_min, new_max):
    return (series - old_min) / (old_max - old_min) * (new_max - new_min) + new_min

def filter_adx(src, length, adxThreshold, useAdxFilter):
    adx = ta.ADX(src, timeperiod=length)
    return adx > adxThreshold if useAdxFilter else True

def filter_volatility(minLength, maxLength, useVolatilityFilter):
    recentAtr = ta.ATR(df['High'], df['Low'], df['Close'], timeperiod=minLength)
    historicalAtr = ta.ATR(df['High'], df['Low'], df['Close'], timeperiod=maxLength)
    return recentAtr > historicalAtr if useVolatilityFilter else True

def n_rsi(src, n1, n2):
    return rescale(ta.EMA(ta.RSI(src, timeperiod=n1), timeperiod=n2), 0, 100, 0, 1)

def n_cci(src, n1, n2):
    return normalize(ta.EMA(ta.CCI(df['High'], df['Low'], df['Close'], timeperiod=n1), timeperiod=n2))

def n_wt(src, n1=10, n2=11):
    ema1 = ta.EMA(src, timeperiod=n1)
    ema2 = ta.EMA(np.abs(src - ema1), timeperiod=n1)
    ci = (src - ema1) / (0.015 * ema2)
    wt1 = ta.EMA(ci, timeperiod=n2)
    wt2 = ta.SMA(wt1, timeperiod=4)
    return normalize(wt1 - wt2)

def n_adx(highSrc, lowSrc, closeSrc, n1):
    adx = ta.ADX(highSrc, lowSrc, closeSrc, timeperiod=n1)
    return rescale(adx, 0, 100, 0, 1)

# Kernel Functions
def rational_quadratic(_src, _lookback, _relative_weight, start_at_bar):
    _current_weight = 0.
    _cumulative_weight = 0.
    _size = len(_src)
    for i in range(_size + start_at_bar):
        y = _src[i]
        w = np.power(1 + (np.power(i, 2) / ((np.power(_lookback, 2) * 2 * _relative_weight))), -_relative_weight)
        _current_weight += y*w
        _cumulative_weight += w
    yhat = _current_weight / _cumulative_weight
    return yhat

def gaussian(_src, _lookback, start_at_bar):
    _current_weight = 0.
    _cumulative_weight = 0.
    _size = len(_src)
    for i in range(_size + start_at_bar):
        y = _src[i]
        w = np.exp(-np.power(i, 2) / (2 * np.power(_lookback, 2)))
        _current_weight += y*w
        _cumulative_weight += w
    yhat = _current_weight / _cumulative_weight
    return yhat

def periodic(_src, _lookback, _period, start_at_bar):
    _current_weight = 0.
    _cumulative_weight = 0.
    _size = len(_src)
    for i in range(_size + start_at_bar):
        y = _src[i]
        w = np.exp(-2*np.power(np.sin(np.pi * i / _period), 2) / np.power(_lookback, 2))
        _current_weight += y*w
        _cumulative_weight += w
    yhat = _current_weight / _cumulative_weight
    return yhat

def locally_periodic(_src, _lookback, _period, start_at_bar):
    _current_weight = 0.
    _cumulative_weight = 0.
    _size = len(_src)
    for i in range(_size + start_at_bar):
        y = _src[i]
        w = np.exp(-2*np.power(np.sin(np.pi * i / _period), 2) / np.power(_lookback, 2)) * np.exp(-np.power(i, 2) / (2 * np.power(_lookback, 2)))
        _current_weight += y*w
        _cumulative_weight += w
    yhat = _current_weight / _cumulative_weight
    return yhat

# Use the functions

# Assuming df is your DataFrame and 'Close' is your column of interest
df['Normalized_RSI'] = n_rsi(df['Close'], n1=14, n2=14)
df['Normalized_CCI'] = n_cci(df['Close'], n1=14, n2=14)
df['Normalized_ADX'] = n_adx(df['High'], df['Low'], df['Close'], n1=14)

# Assuming you have defined the function `rationalQuadratic` and `gaussian` in your `kernels` module
yhat1 = rational_quadratic(df['close'], h, r, x)
yhat2 = gaussian(df['close'], h-lag, x)
yhat3 = periodic(df['close'], h, p, x)
yhat4 = locally_periodic(df['close'], h, p, x)
   