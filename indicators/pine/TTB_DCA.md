# Automated TradingView Strategy Script

This script enables  backtesting and automating trading alerts for running an automated trading system from tradingview to metatrader 4.

For each pair, we have long and short version activated (our account allows hedging and long/short treated seperately)

We trade relatively small size with 1:500 leverage to reduce risk exposure.

Goal: close as many trades as possible for at least 0.05% price movement (take profit aka TP) without having to use any or all of allotted safety orders.

## Entry Signal

For entry, We use various indicators and signals to filter for trend etc. to increase chances of good entries.

## Safety Orders (SOs)

Safety Orders are activated when the price goes against the initial entry to protect against adverse movements and exit the trade more rapidly as each SO added the TP is adjusted to the average entry.

- **Where the 1st SO activates**: This is typically a set percentage of price movement against entry. 
- **Max number of safety orders**: This defines the maximum number of SOs allowed. Current =4
- **1st SO order activation**: It's based on "Price Deviation To Open Safety Trades (%)", which represents the percent deviation against the original entry. SO orders open every N% of price movement. The price and size are calculated according to settings (step scale, volume scale). Current % = 0.05% 
- **Size of 1st SO**: Defined by "Safe order (lots)". Current 1st SO size is 3000 (same as entry)
- **Size of subsequent SOs**: Calculated by "Safety Order Volume Scale" * "Safety order volume scale". Current Volume scale = "1" (same as previous)
- **Location of additional SOs**: The percentage from the previous SO where the next SO should be placed is calculated using "Safety order step scale" * "Price Deviation To Open Safety Trades (%)". Current Safety order step scale = 2.5

## Deal End

- **Take Profit**: The deal ends when it reaches the "Target Take Profit (%)". (TP) current TP set to 0.07%

**IF deal does not reach TP, we move the position to a different algo called the "bag bot" aka BB that is degined to exit the trade at a break even profit.

Thoughts for improvement

1. Is TP % optimal?
2. Is "Safety order step scale" optimal?
3. Is **Size of subsequent SOs** optimal?