# goal

## context
- before you begin, analyze entire script and pay special attention to how variables interact and the 'order flow' from entry to SO, to TP. as well as how levels are calculated and tracked.

- track each "trade round" a trade round starts with either '// long entry' or '// short entry', then poaaible SOs (safety orders), ending with 'take profit' either '// take profit long' or '// take profit short'.
- script runs either short or longs (not both at same time)

## task
- trade round price level stored and starts starts with 'initial_price' or 'initial_S_price'

- We want to track the highest (longs) and lowest (short) possible price reached within new var 'target_bars' user input  (not made yet).
  
- store this in var 'best_tp_deviation' which is highest (longs) lowest (shorts) price reached within the target_bars constraint.
  
- this needs to be expressed in ATRP daily percentage.  See how we caluclate max_pump_atrp and max_drop_atrp_temp to understand.

- if you have any failed attempts, append a note to bottom of 'learnings.txt' with concise not of what you tried and why you think it did not work.  