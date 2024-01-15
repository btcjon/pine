# learnings

### instructions for concise note
- when we make a mistake because we are not trained well on pinescript v5 we should append a note here.

- use this format '- context/language,' 'what you tried,' 'error code,' 'why you think failed'

#### example note

- pinescript v5, tried using if statement within a plot, got syntax error at input, think I needed closing character

## append your learings below with space between each

- Pine Script v5, tried to use highest(high, bar_index - entry_bar_index + 1), got a compilation error, 'Could not find function or function reference 'highest''. The correct usage is ta.highest(high, length), where length is a fixed number of bars to look back. Dynamic lengths, such as bar_index - entry_bar_index + 1, are not supported in Pine Script's ta.highest function.

- Pine Script v4/v5, tried to use plotchar inside a local scope (like inside a function or an if statement), got a compilation error, 'Cannot use 'plotchar' in local scope'. This is because plotchar and other plotting functions in Pine Script can only be used in the global scope. They cannot be used inside local scopes such as if statements, for loops, or user-defined functions. To resolve this, you need to ensure that your plotting function calls are in the global scope of your script.

- Pine Script v4/v5, tried to 'dd_deviation = abs((entry_price - high_since_entry) / entry_price) * 100', error - Could not find function or function reference 'abs', needs to be math.abs

