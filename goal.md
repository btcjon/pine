# goal

## context
- before you begin, analyze entire script and pay special attention to how variables interact and the 'order flow' from entry to SO, to TP. as well as how levels are calculated and tracked.

- track each "trade round" a trade round starts with either '// long entry' or '// short entry', then poaaible SOs (safety orders), ending with 'take profit' either '// take profit long' or '// take profit short'.
- script runs either short or longs (not both at same time)

## task
We are developing a self-optimizing trading strategy that adjusts its take profit level based on historical trade data. The strategy trades both long and short. For each trade, we track the highest (for long trades) or lowest (for short trades) price within a certain number of bars (target_bars) from the entry. This represents the best possible take profit level for each trade.

We store these optimal take profit levels and calculate their average after a certain number of trades. This average is then used to adjust the take profit level for future trades. Specifically, we set the take profit level to 80% of the average optimal take profit level.

This adjustment is done in a way that the take profit level is expressed in the same terms as the ATRP_daily_factor, which is used to calculate the initial take profit level. This allows us to replace the ATRP_daily_factor with our calculated value (optimized_TP_factor) after a certain number of trades, making the strategy self-optimizing.

1. We're tracking the maximum deviation from the entry price for each trade, both long and short. For long trades, we track the highest price reached within a certain number of bars (target_bars) from the entry. For short trades, we track the lowest price reached within target_bars from the entry. This deviation is stored in dev_since_entry_points.

2. After each trade, we add the deviation to a running total (sum_dev_since_entry).

3. After a certain number of trades, we calculate the average deviation (average_dev_since_entry) and normalize it to be in the same terms as ATRP_daily_factor.

4. We then use this normalized average deviation to adjust the take profit level for future trades.

Our issue is that it is not giving any output.  something wrong in the code.

- if you have any failed attempts, append a note to bottom of 'learnings.txt' with concise not of what you tried and why you think it did not work.  