
## variables
---------


## bar_index

Current bar index. Numbering is zero-based, index of the first bar is 0.

### Type

series int

### Example


```s

//@version=5
indicator("bar_index")
plot(bar_index)
plot(bar_index > 5000 ? close : 0)


```

### Remarks

Note that **bar_index** has replaced **n** variable in version 4.

Note that bar indexing starts from 0 on the first historical bar.

please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

### See also

* [last\_bar\_index](#var_last_bar_index)
* [barstate.isfirst](#var_barstate.isfirst)
* [barstate.islast](#var_barstate.islast)
* [barstate.isrealtime](#var_barstate.isrealtime)

## barstate.isconfirmed

Returns true if the script is calculating the last (closing) update of the current bar. the next script calculation will be on the new bar data.

### Type

series bool

### Remarks

pine script(r) code that uses this variable could calculate differently on history and real-time data.

it is NOT recommended to use [barstate.isconfirmed](#var_barstate.isconfirmed) in [request.security](#fun_request.security) expression. its value requested from [request.security](#fun_request.security) is unpredictable.

please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

### See also

* [barstate.isfirst](#var_barstate.isfirst)
* [barstate.islast](#var_barstate.islast)
* [barstate.ishistory](#var_barstate.ishistory)
* [barstate.isrealtime](#var_barstate.isrealtime)
* [barstate.isnew](#var_barstate.isnew)
* [barstate.islastconfirmedhistory](#var_barstate.islastconfirmedhistory)

## barstate.isfirst

Returns true if current bar is first bar in barset, false otherwise.

### Type

series bool

### Remarks

pine script(r) code that uses this variable could calculate differently on history and real-time data.

please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

### See also

* [barstate.islast](#var_barstate.islast)
* [barstate.ishistory](#var_barstate.ishistory)
* [barstate.isrealtime](#var_barstate.isrealtime)
* [barstate.isnew](#var_barstate.isnew)
* [barstate.isconfirmed](#var_barstate.isconfirmed)
* [barstate.islastconfirmedhistory](#var_barstate.islastconfirmedhistory)

## barstate.ishistory

Returns true if current bar is a historical bar, false otherwise.

### Type

series bool

### Remarks

pine script(r) code that uses this variable could calculate differently on history and real-time data.

please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

### See also

* [barstate.isfirst](#var_barstate.isfirst)
* [barstate.islast](#var_barstate.islast)
* [barstate.isrealtime](#var_barstate.isrealtime)
* [barstate.isnew](#var_barstate.isnew)
* [barstate.isconfirmed](#var_barstate.isconfirmed)
* [barstate.islastconfirmedhistory](#var_barstate.islastconfirmedhistory)

## barstate.islast

Returns true if current bar is the last bar in barset, false otherwise. this condition is true for all real-time bars in barset.

### Type

series bool

### Remarks

pine script(r) code that uses this variable could calculate differently on history and real-time data.

please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

### See also

* [barstate.isfirst](#var_barstate.isfirst)
* [barstate.ishistory](#var_barstate.ishistory)
* [barstate.isrealtime](#var_barstate.isrealtime)
* [barstate.isnew](#var_barstate.isnew)
* [barstate.isconfirmed](#var_barstate.isconfirmed)
* [barstate.islastconfirmedhistory](#var_barstate.islastconfirmedhistory)

## barstate.islastconfirmedhistory

Returns true if script is executing on the dataset's last bar when market is closed, or script is executing on the bar immediately preceding the real-time bar, if market is open. Returns false otherwise.

### Type

series bool

### Remarks

pine script(r) code that uses this variable could calculate differently on history and real-time data.

please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

### See also

* [barstate.isfirst](#var_barstate.isfirst)
* [barstate.islast](#var_barstate.islast)
* [barstate.ishistory](#var_barstate.ishistory)
* [barstate.isrealtime](#var_barstate.isrealtime)
* [barstate.isnew](#var_barstate.isnew)

## barstate.isnew

Returns true if script is currently calculating on new bar, false otherwise. this variable is true when calculating on historical bars or on first update of a newly generated real-time bar.

### Type

series bool

### Remarks

pine script(r) code that uses this variable could calculate differently on history and real-time data.

please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

### See also

* [barstate.isfirst](#var_barstate.isfirst)
* [barstate.islast](#var_barstate.islast)
* [barstate.ishistory](#var_barstate.ishistory)
* [barstate.isrealtime](#var_barstate.isrealtime)
* [barstate.isconfirmed](#var_barstate.isconfirmed)
* [barstate.islastconfirmedhistory](#var_barstate.islastconfirmedhistory)

## barstate.isrealtime

Returns true if current bar is a real-time bar, false otherwise.

### Type

series bool

### Remarks

pine script(r) code that uses this variable could calculate differently on history and real-time data.

please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

### See also

* [barstate.isfirst](#var_barstate.isfirst)
* [barstate.islast](#var_barstate.islast)
* [barstate.ishistory](#var_barstate.ishistory)
* [barstate.isnew](#var_barstate.isnew)
* [barstate.isconfirmed](#var_barstate.isconfirmed)
* [barstate.islastconfirmedhistory](#var_barstate.islastconfirmedhistory)

## box.all

Returns an array filled with all the current boxes drawn by the script.

### Type

box\[\]

### Example


```s

//@version=5
indicator("box.all")
//delete all boxes
box.new(time, open, time + 60 * 60 * 24, close, xloc=xloc.bar_time, border_style=line.style_dashed)
a_allboxes = box.all
if array.size(a_allboxes) > 0
    for i = 0 to array.size(a_allboxes) - 1
        box.delete(array.get(a_allboxes, i))


```

### Remarks

the array is read-only. index zero of the array is the iD of the oldest object on the chart.

### See also

* [box.new](#fun_box.new)
* [line.all](#var_line.all)
* [label.all](#var_label.all)
* [table.all](#var_table.all)

## chart.bg_color

Returns the color of the chart's background from the "Chart settings/appearance/background" field. When a gradient is selected, the middle point of the gradient is returned.

### Type

input color

### See also

* [chart.fg_color](#var_chart.fg_color)

## chart.fg_color

Returns a color providing optimal contrast with [chart.bg_color](#var_chart.bg_color).

### Type

input color

### See also

* [chart.bg_color](#var_chart.bg_color)

## chart.is_heikinashi

### Type

simple bool

### Returns

Returns [true](#op_true) if the chart type is Heikin ashi, [false](#op_false) otherwise.

### See also

* [chart.is_renko](#var_chart.is_renko)
* [chart.is_linebreak](#var_chart.is_linebreak)
* [chart.is_kagi](#var_chart.is_kagi)
* [chart.is_pnf](#var_chart.is_pnf)
* [chart.is_range](#var_chart.is_range)

## chart.is_kagi

### Type

simple bool

### Returns

Returns [true](#op_true) if the chart type is Kagi, [false](#op_false) otherwise.

### See also

* [chart.is_renko](#var_chart.is_renko)
* [chart.is_linebreak](#var_chart.is_linebreak)
* [chart.is_heikinashi](#var_chart.is_heikinashi)
* [chart.is_pnf](#var_chart.is_pnf)
* [chart.is_range](#var_chart.is_range)

## chart.is_linebreak

### Type

simple bool

### Returns

Returns [true](#op_true) if the chart type is line break, [false](#op_false) otherwise.

### See also

* [chart.is_renko](#var_chart.is_renko)
* [chart.is_heikinashi](#var_chart.is_heikinashi)
* [chart.is_kagi](#var_chart.is_kagi)
* [chart.is_pnf](#var_chart.is_pnf)
* [chart.is_range](#var_chart.is_range)

## chart.is_pnf

### Type

simple bool

### Returns

Returns [true](#op_true) if the chart type is point & figure, [false](#op_false) otherwise.

### See also

* [chart.is_renko](#var_chart.is_renko)
* [chart.is_linebreak](#var_chart.is_linebreak)
* [chart.is_kagi](#var_chart.is_kagi)
* [chart.is_heikinashi](#var_chart.is_heikinashi)
* [chart.is_range](#var_chart.is_range)

## chart.is_range

### Type

simple bool

### Returns

Returns [true](#op_true) if the chart type is Range, [false](#op_false) otherwise.

### See also

* [chart.is_renko](#var_chart.is_renko)
* [chart.is_linebreak](#var_chart.is_linebreak)
* [chart.is_kagi](#var_chart.is_kagi)
* [chart.is_pnf](#var_chart.is_pnf)
* [chart.is_heikinashi](#var_chart.is_heikinashi)

## chart.is_renko

### Type

simple bool

### Returns

Returns [true](#op_true) if the chart type is Renko, [false](#op_false) otherwise.

### See also

* [chart.is_heikinashi](#var_chart.is_heikinashi)
* [chart.is_linebreak](#var_chart.is_linebreak)
* [chart.is_kagi](#var_chart.is_kagi)
* [chart.is_pnf](#var_chart.is_pnf)
* [chart.is_range](#var_chart.is_range)

## chart.is_standard

### Type

simple bool

### Returns

Returns [true](#op_true) if the chart type is bars, candles, hollow candles, line, area or baseline, [false](#op_false) otherwise.

### See also

* [chart.is_renko](#var_chart.is_renko)
* [chart.is_linebreak](#var_chart.is_linebreak)
* [chart.is_kagi](#var_chart.is_kagi)
* [chart.is_pnf](#var_chart.is_pnf)
* [chart.is_range](#var_chart.is_range)
* [chart.is_heikinashi](#var_chart.is_heikinashi)

## chart.left\_visible\_bar_time

the [time](#var_time) of the leftmost bar currently visible on the chart.

### Type

input int

### Remarks

scripts using this variable will automatically re-execute when its value updates to reflect changes in the chart, which can be caused by users scrolling the chart, or new real-time bars.

### See also

* [chart.right\_visible\_bar_time](#var_chart.right_visible_bar_time)

## chart.right\_visible\_bar_time

the [time](#var_time) of the rightmost bar currently visible on the chart.

### Type

input int

### Remarks

scripts using this variable will automatically re-execute when its value updates to reflect changes in the chart, which can be caused by users scrolling the chart, or new real-time bars.

### See also

* [chart.left\_visible\_bar_time](#var_chart.left_visible_bar_time)

## close

Close price of the current bar when it has closed, or last traded price of a yet incomplete, realtime bar.

### Type

series float

### Remarks

previous values may be accessed with square brackets operator \[\], e.g. close\[1\], close\[2\].

### See also

* [open](#var_open)
* [high](#var_high)
* [low](#var_low)
* [volume](#var_volume)
* [time](#fun_time)
* [hl2](#var_hl2)
* [hlc3](#var_hlc3)
* [hlcc4](#var_hlcc4)
* [ohlc4](#var_ohlc4)

## dayofmonth

Date of current bar time in exchange timezone.

### Type

series int

### Remarks

Note that this variable returns the day based on the time of the bar's open. For overnight sessions (e.g. EuRusD, where Monday session starts on sunday, 17:00) this value can be lower by 1 than the day of the trading day.

### See also

* [dayofmonth](#fun_dayofmonth)
* [time](#var_time)
* [year](#var_year)
* [month](#var_month)
* [weekofyear](#var_weekofyear)
* [dayofweek](#var_dayofweek)
* [hour](#var_hour)
* [minute](#var_minute)
* [second](#var_second)

## dayofweek

Day of week for current bar time in exchange timezone.

### Type

series int

### Remarks

Note that this variable returns the day based on the time of the bar's open. For overnight sessions (e.g. EuRusD, where Monday session starts on sunday, 17:00) this value can be lower by 1 than the day of the trading day.

You can use [dayofweek.sunday](#var_dayofweek.sunday), [dayofweek.monday](#var_dayofweek.monday), [dayofweek.tuesday](#var_dayofweek.tuesday), [dayofweek.wednesday](#var_dayofweek.wednesday), [dayofweek.thursday](#var_dayofweek.thursday), [dayofweek.friday](#var_dayofweek.friday) and [dayofweek.saturday](#var_dayofweek.saturday) variables for comparisons.

### See also

* [dayofweek](#fun_dayofweek)
* [time](#var_time)
* [year](#var_year)
* [month](#var_month)
* [weekofyear](#var_weekofyear)
* [dayofmonth](#var_dayofmonth)
* [hour](#var_hour)
* [minute](#var_minute)
* [second](#var_second)

## earnings.future_eps

Returns the estimated Earnings per share of the next earnings report in the currency of the instrument, or [na](#var_na) if this data isn't available.

### Type

series float

### Remarks

this value is only fetched once during the script's initial calculation. the variable will return the same value until the script is recalculated, even after the expected time of the next earnings report.

### See also

* [request.earnings](#fun_request.earnings)

## earnings.future\_period\_end_time

Checks the data for the next earnings report and returns the unix timestamp of the day when the financial period covered by those earnings ends, or [na](#var_na) if this data isn't available.

### Type

series float

### Remarks

this value is only fetched once during the script's initial calculation. the variable will return the same value until the script is recalculated, even after the expected time of the next earnings report.

### See also

* [request.earnings](#fun_request.earnings)

## earnings.future_revenue

Returns the estimated Revenue of the next earnings report in the currency of the instrument, or [na](#var_na) if this data isn't available.

### Type

series float

### Remarks

this value is only fetched once during the script's initial calculation. the variable will return the same value until the script is recalculated, even after the expected time of the next earnings report.

### See also

* [request.earnings](#fun_request.earnings)

## earnings.future_time

Returns a unix timestamp indicating the expected time of the next earnings report, or [na](#var_na) if this data isn't available.

### Type

series float

### Remarks

this value is only fetched once during the script's initial calculation. the variable will return the same value until the script is recalculated, even after the expected time of the next earnings report.

### See also

* [request.earnings](#fun_request.earnings)

## high

Current high price.

### Type

series float

### Remarks

previous values may be accessed with square brackets operator \[\], e.g. high\[1\], high\[2\].

### See also

* [open](#var_open)
* [low](#var_low)
* [close](#var_close)
* [volume](#var_volume)
* [time](#fun_time)
* [hl2](#var_hl2)
* [hlc3](#var_hlc3)
* [hlcc4](#var_hlcc4)
* [ohlc4](#var_ohlc4)

## hl2

is a shortcut for (high + low)/2

### Type

series float

### See also

* [open](#var_open)
* [high](#var_high)
* [low](#var_low)
* [close](#var_close)
* [volume](#var_volume)
* [time](#fun_time)
* [hlc3](#var_hlc3)
* [hlcc4](#var_hlcc4)
* [ohlc4](#var_ohlc4)

## hlc3

is a shortcut for (high + low + close)/3

### Type

series float

### See also

* [open](#var_open)
* [high](#var_high)
* [low](#var_low)
* [close](#var_close)
* [volume](#var_volume)
* [time](#fun_time)
* [hl2](#var_hl2)
* [hlcc4](#var_hlcc4)
* [ohlc4](#var_ohlc4)

## hlcc4

is a shortcut for (high + low + close + close)/4

### Type

series float

### See also

* [open](#var_open)
* [high](#var_high)
* [low](#var_low)
* [close](#var_close)
* [volume](#var_volume)
* [time](#fun_time)
* [hl2](#var_hl2)
* [hlc3](#var_hlc3)
* [ohlc4](#var_ohlc4)

## hour

Current bar hour in exchange timezone.

### Type

series int

### See also

* [hour](#fun_hour)
* [time](#var_time)
* [year](#var_year)
* [month](#var_month)
* [weekofyear](#var_weekofyear)
* [dayofmonth](#var_dayofmonth)
* [dayofweek](#var_dayofweek)
* [minute](#var_minute)
* [second](#var_second)

## label.all

Returns an array filled with all the current labels drawn by the script.

### Type

label\[\]

### Example


```s

//@version=5
indicator("label.all")
//delete all labels
label.new(bar_index, close)
a_alllabels = label.all
if array.size(a_alllabels) > 0
    for i = 0 to array.size(a_alllabels) - 1
        label.delete(array.get(a_alllabels, i))


```

### Remarks

the array is read-only. index zero of the array is the iD of the oldest object on the chart.

### See also

* [label.new](#fun_label.new)
* [line.all](#var_line.all)
* [box.all](#var_box.all)
* [table.all](#var_table.all)

## last\_bar\_index

bar index of the last chart bar. bar indices begin at zero on the first bar.

### Type

series int

### Example


```s

//@version=5
strategy("mark Last X bars For backtesting", overlay = true, calc_on_every_tick = true)
lastbarsFilterinput = input.int(100, "bars Count:")
// Here, we store the 'last_bar_index' value that is known from the beginning of the script's calculation.
// the 'last_bar_index' will change when new real-time bars appear, so we declare 'lastbar' with the 'var' keyword.
var lastbar = last_bar_index
// Check if the current bar_index is 'lastbarsFilterinput' removed from the last bar on the chart, or the chart is traded in real-time.
allowedtotrade = (lastbar - bar_index <= lastbarsFilterinput) or barstate.isrealtime
bgcolor(allowedtotrade ? color.new(color.green, 80) : na)


```

### Returns

Last historical bar index for closed markets, or the real-time bar index for open markets.

### Remarks

please note that using this variable can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

### See also

* [bar_index](#var_bar_index)
* [last\_bar\_time](#var_last_bar_time)
* [barstate.ishistory](#var_barstate.ishistory)
* [barstate.isrealtime](#var_barstate.isrealtime)

## last\_bar\_time

time in unix format of the last chart bar. it is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

### Type

series int

### Remarks

please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

Note that this variable returns the timestamp based on the time of the bar's open.

### See also

* [time](#var_time)
* [timenow](#var_timenow)
* [timestamp](#fun_timestamp)
* [last\_bar\_index](#var_last_bar_index)

## line.all

Returns an array filled with all the current lines drawn by the script.

### Type

line\[\]

### Example


```s

//@version=5
indicator("line.all")
//delete all lines
line.new(bar_index - 10, close, bar_index, close)
a_alllines = line.all
if array.size(a_alllines) > 0
    for i = 0 to array.size(a_alllines) - 1
        line.delete(array.get(a_alllines, i))


```

### Remarks

the array is read-only. index zero of the array is the iD of the oldest object on the chart.

### See also

* [line.new](#fun_line.new)
* [label.all](#var_label.all)
* [box.all](#var_box.all)
* [table.all](#var_table.all)

## linefill.all

Returns an array filled with all the current linefill objects drawn by the script.

### Type

linefill\[\]

### Remarks

the array is read-only. index zero of the array is the iD of the oldest object on the chart.

## low

Current low price.

### Type

series float

### Remarks

previous values may be accessed with square brackets operator \[\], e.g. low\[1\], low\[2\].

### See also

* [open](#var_open)
* [high](#var_high)
* [close](#var_close)
* [volume](#var_volume)
* [time](#fun_time)
* [hl2](#var_hl2)
* [hlc3](#var_hlc3)
* [hlcc4](#var_hlcc4)
* [ohlc4](#var_ohlc4)

## minute

Current bar minute in exchange timezone.

### Type

series int

### See also

* [minute](#fun_minute)
* [time](#var_time)
* [year](#var_year)
* [month](#var_month)
* [weekofyear](#var_weekofyear)
* [dayofmonth](#var_dayofmonth)
* [dayofweek](#var_dayofweek)
* [hour](#var_hour)
* [second](#var_second)

## month

Current bar month in exchange timezone.

### Type

series int

### Remarks

Note that this variable returns the month based on the time of the bar's open. For overnight sessions (e.g. EuRusD, where Monday session starts on sunday, 17:00) this value can be lower by 1 than the month of the trading day.

### See also

* [month](#fun_month)
* [time](#var_time)
* [year](#var_year)
* [weekofyear](#var_weekofyear)
* [dayofmonth](#var_dayofmonth)
* [dayofweek](#var_dayofweek)
* [hour](#var_hour)
* [minute](#var_minute)
* [second](#var_second)

## na

a keyword signifying "not available", indicating that a variable has no assigned value.

### Type

simple na

### Example


```s

//@version=5
indicator("na")
// CORRECT
// plot no value when on bars zero to nine. plot `close` on other bars.
plot(bar_index < 10 ? na : close)
// CORRECT aLTERNaTiVE
// initialize `a` to `na`. Reassign `close` to `a` on bars 10 and later.
float a = na
if bar_index >= 10
    a := close
plot(a)

// iNCORRECT
// trying to test the preceding bar's `close` for `na`.
// Will not work correctly on bar zero, when `close[1]` is `na`.
plot(close[1] == na ? close : close[1])
// CORRECT
// use the `na()` function to test for `na`.
plot(na(close[1]) ? close : close[1])
// CORRECT aLTERNaTiVE
// `nz()` tests `close[1]` for `na`. it returns `close[1]` if it is not `na`, and `close` if it is.
plot(nz(close[1], close))


```

### Remarks

Do not use this variable with [comparison operators](https://www.tradingview.com/pine-script-docs/en/v5/language/Operators.html#comparison-operators) to test values for \`na\`, as it might lead to unexpected behavior. instead, use the [na](#fun_na) function. Note that \`na\` can be used to initialize variables when the initialization statement also specifies the variable's type.

### See also

* [na](#fun_na)
* [nz](#fun_nz)
* [fixnan](#fun_fixnan)

## ohlc4

is a shortcut for (open + high + low + close)/4

### Type

series float

### See also

* [open](#var_open)
* [high](#var_high)
* [low](#var_low)
* [close](#var_close)
* [volume](#var_volume)
* [time](#fun_time)
* [hl2](#var_hl2)
* [hlc3](#var_hlc3)
* [hlcc4](#var_hlcc4)

## open

Current open price.

### Type

series float

### Remarks

previous values may be accessed with square brackets operator \[\], e.g. open\[1\], open\[2\].

### See also

* [high](#var_high)
* [low](#var_low)
* [close](#var_close)
* [volume](#var_volume)
* [time](#fun_time)
* [hl2](#var_hl2)
* [hlc3](#var_hlc3)
* [hlcc4](#var_hlcc4)
* [ohlc4](#var_ohlc4)

## polyline.all

Returns an array containing all current [polyline](#op_polyline) instances drawn by the script.

### Type

polyline\[\]

### Remarks

the array is read-only. index zero of the array references the iD of the oldest polyline object on the chart.

## second

Current bar second in exchange timezone.

### Type

series int

### See also

* [second](#fun_second)
* [time](#var_time)
* [year](#var_year)
* [month](#var_month)
* [weekofyear](#var_weekofyear)
* [dayofmonth](#var_dayofmonth)
* [dayofweek](#var_dayofweek)
* [hour](#var_hour)
* [minute](#var_minute)

## session.isfirstbar

Returns [true](#op_true) if the current bar is the first bar of the day's session, \`false\` otherwise. if extended session information is used, only returns [true](#op_true) on the first bar of the pre-market bars.

### Type

series bool

## session.isfirstbar_regular

Returns [true](#op_true) on the first regular session bar of the day, \`false\` otherwise. the result is the same whether extended session information is used or not.

### Type

series bool

## session.islastbar

Returns [true](#op_true) if the current bar is the last bar of the day's session, \`false\` otherwise. if extended session information is used, only returns [true](#op_true) on the last bar of the post-market bars.

### Type

series bool

### Remarks

this variable is not guaranteed to return [true](#op_true) once in every session because the last bar of the session might not exist if no trades occur during what should be the session's last bar.

this variable is not guaranteed to work as expected on non-standard chart types, e.g., Renko.

## session.islastbar_regular

Returns [true](#op_true) on the last regular session bar of the day, \`false\` otherwise. the result is the same whether extended session information is used or not.

### Type

series bool

### Remarks

this variable is not guaranteed to return [true](#op_true) once in every session because the last bar of the session might not exist if no trades occur during what should be the session's last bar.

this variable is not guaranteed to work as expected on non-standard chart types, e.g., Renko.

## session.ismarket

Returns true if the current bar is a part of the regular trading hours (i.e. market hours), false otherwise

### Type

series bool

### See also

* [session.ispremarket](#var_session.ispremarket)
* [session.ispostmarket](#var_session.ispostmarket)

## session.ispostmarket

Returns true if the current bar is a part of the post-market, false otherwise. On non-intraday charts always returns false.

### Type

series bool

### See also

* [session.ismarket](#var_session.ismarket)
* [session.ispremarket](#var_session.ispremarket)

## session.ispremarket

Returns true if the current bar is a part of the pre-market, false otherwise. On non-intraday charts always returns false.

### Type

series bool

### See also

* [session.ismarket](#var_session.ismarket)
* [session.ispostmarket](#var_session.ispostmarket)

## strategy.account_currency

Returns the currency used to calculate results, which can be set in the strategy's properties.

### Type

simple string

### See also

* [strategy](#fun_strategy)
* [strategy.convert\_to\_account](#fun_strategy.convert_to_account)
* [strategy.convert\_to\_symbol](#fun_strategy.convert_to_symbol)

## strategy.closedtrades

Number of trades, which were closed for the whole trading interval.

### Type

series int

### See also

* [strategy.position_size](#var_strategy.position_size)
* [strategy.opentrades](#var_strategy.opentrades)
* [strategy.wintrades](#var_strategy.wintrades)
* [strategy.losstrades](#var_strategy.losstrades)
* [strategy.eventrades](#var_strategy.eventrades)

## strategy.equity

Current equity ([strategy.initial_capital](#var_strategy.initial_capital) \+ [strategy.netprofit](#var_strategy.netprofit) \+ [strategy.openprofit](#var_strategy.openprofit)).

### Type

series float

### See also

* [strategy.netprofit](#var_strategy.netprofit)
* [strategy.openprofit](#var_strategy.openprofit)
* [strategy.position_size](#var_strategy.position_size)

## strategy.eventrades

Number of breakeven trades for the whole trading interval.

### Type

series int

### See also

* [strategy.position_size](#var_strategy.position_size)
* [strategy.opentrades](#var_strategy.opentrades)
* [strategy.closedtrades](#var_strategy.closedtrades)
* [strategy.wintrades](#var_strategy.wintrades)
* [strategy.losstrades](#var_strategy.losstrades)

## strategy.grossloss

Total currency value of all completed losing trades.

### Type

series float

### See also

* [strategy.netprofit](#var_strategy.netprofit)
* [strategy.grossprofit](#var_strategy.grossprofit)

## strategy.grossprofit

Total currency value of all completed winning trades.

### Type

series float

### See also

* [strategy.netprofit](#var_strategy.netprofit)
* [strategy.grossloss](#var_strategy.grossloss)

## strategy.initial_capital

the amount of initial capital set in the strategy properties.

### Type

series float

### See also

* [strategy](#fun_strategy)

## strategy.long

Long position entry.

### Type

const strategy_direction

### See also

* [strategy.entry](#fun_strategy.entry)
* [strategy.exit](#fun_strategy.exit)
* [strategy.order](#fun_strategy.order)

## strategy.losstrades

Number of unprofitable trades for the whole trading interval.

### Type

series int

### See also

* [strategy.position_size](#var_strategy.position_size)
* [strategy.opentrades](#var_strategy.opentrades)
* [strategy.closedtrades](#var_strategy.closedtrades)
* [strategy.wintrades](#var_strategy.wintrades)
* [strategy.eventrades](#var_strategy.eventrades)

## strategy.margin\_liquidation\_price

When margin is used in a strategy, returns the price point where a simulated margin call will occur and liquidate enough of the position to meet the margin requirements.

### Type

series float

### Example


```s

//@version=5
strategy("Margin call management", overlay = true, margin_long = 25, margin_short = 25,
  default_qty_type = strategy.percent_of_equity, default_qty_value = 395)

float maFast = ta.sma(close, 14)
float maslow = ta.sma(close, 28)

if ta.crossover(maFast, maslow)
    strategy.entry("Long", strategy.long)

if ta.crossunder(maFast, maslow)
    strategy.entry("short", strategy.short)

changepercent(v1, v2) =>
    float result = (v1 - v2) * 100 / math.abs(v2)

// exit when we're 10% away from a margin call, to prevent it.
if math.abs(changepercent(close, strategy.margin_liquidation_price)) <= 10
    strategy.close("Long")
    strategy.close("short")


```

### Remarks

the variable returns [na](#var_na) if the strategy does not use margin, i.e., the [strategy](#fun_strategy) declaration statement does not specify an argument for the \`margin\_long\` or \`margin\_short\` parameter.

## strategy.max\_contracts\_held_all

Maximum number of contracts/shares/lots/units in one trade for the whole trading interval.

### Type

series float

### See also

* [strategy.position_size](#var_strategy.position_size)
* [strategy.max\_contracts\_held_long](#var_strategy.max_contracts_held_long)
* [strategy.max\_contracts\_held_short](#var_strategy.max_contracts_held_short)

## strategy.max\_contracts\_held_long

Maximum number of contracts/shares/lots/units in one long trade for the whole trading interval.

### Type

series float

### See also

* [strategy.position_size](#var_strategy.position_size)
* [strategy.max\_contracts\_held_all](#var_strategy.max_contracts_held_all)
* [strategy.max\_contracts\_held_short](#var_strategy.max_contracts_held_short)

## strategy.max\_contracts\_held_short

Maximum number of contracts/shares/lots/units in one short trade for the whole trading interval.

### Type

series float

### See also

* [strategy.position_size](#var_strategy.position_size)
* [strategy.max\_contracts\_held_all](#var_strategy.max_contracts_held_all)
* [strategy.max\_contracts\_held_long](#var_strategy.max_contracts_held_long)

## strategy.max_drawdown

Maximum equity drawdown value for the whole trading interval.

### Type

series float

### See also

* [strategy.netprofit](#var_strategy.netprofit)
* [strategy.equity](#var_strategy.equity)
* [strategy.max_runup](#var_strategy.max_runup)

## strategy.max_runup

Maximum equity run-up value for the whole trading interval.

### Type

series float

### See also

* [strategy.netprofit](#var_strategy.netprofit)
* [strategy.equity](#var_strategy.equity)
* [strategy.max_drawdown](#var_strategy.max_drawdown)

## strategy.netprofit

Total currency value of all completed trades.

### Type

series float

### See also

* [strategy.openprofit](#var_strategy.openprofit)
* [strategy.position_size](#var_strategy.position_size)
* [strategy.grossprofit](#var_strategy.grossprofit)
* [strategy.grossloss](#var_strategy.grossloss)

## strategy.openprofit

Current unrealized profit or loss for all open positions.

### Type

series float

### See also

* [strategy.netprofit](#var_strategy.netprofit)
* [strategy.position_size](#var_strategy.position_size)

## strategy.opentrades

Number of market position entries, which were not closed and remain opened. if there is no open market position, 0 is returned.

### Type

series int

### See also

* [strategy.position_size](#var_strategy.position_size)

## strategy.position\_avg\_price

average entry price of current market position. if the market position is flat, 'NaN' is returned.

### Type

series float

### See also

* [strategy.position_size](#var_strategy.position_size)

## strategy.position\_entry\_name

Name of the order that initially opened current market position.

### Type

series string

### See also

* [strategy.position_size](#var_strategy.position_size)

## strategy.position_size

direction and size of the current market position. if the value is > 0, the market position is long. if the value is < 0, the market position is short. the absolute value is the number of contracts/shares/lots/units in trade (position size).

### Type

series float

### See also

* [strategy.position\_avg\_price](#var_strategy.position_avg_price)

## strategy.short

short position entry.

### Type

const strategy_direction

### See also

* [strategy.entry](#fun_strategy.entry)
* [strategy.exit](#fun_strategy.exit)
* [strategy.order](#fun_strategy.order)

## strategy.wintrades

Number of profitable trades for the whole trading interval.

### Type

series int

### See also

* [strategy.position_size](#var_strategy.position_size)
* [strategy.opentrades](#var_strategy.opentrades)
* [strategy.closedtrades](#var_strategy.closedtrades)
* [strategy.losstrades](#var_strategy.losstrades)
* [strategy.eventrades](#var_strategy.eventrades)

## syminfo.basecurrency

base currency for the symbol. For the symbol 'bTCusD' returns 'bTC'.

### Type

simple string

### See also

* [syminfo.currency](#var_syminfo.currency)
* [syminfo.ticker](#var_syminfo.ticker)

## syminfo.country

Returns the two-letter code of the country where the symbol is traded, in the [isO 3166-1 alpha-2](https://en.wikipedia.org/wiki/isO_3166-1_alpha-2) format, or [na](#var_na) if the exchange is not directly tied to a specific country. For example, on "NasDaq:aapL" it will return "us", on "LsE:aapL" it will return "Gb", and on "biTsTaMp:bTCusD it will return [na](#var_na).

### Type

simple string

## syminfo.currency

Currency for the current symbol. Returns currency code: 'usD', 'EuR', etc.

### Type

simple string

### See also

* [syminfo.basecurrency](#var_syminfo.basecurrency)
* [syminfo.ticker](#var_syminfo.ticker)
* [currency.usD](#var_currency.usD)
* [currency.EuR](#var_currency.EuR)

## syminfo.description

Description for the current symbol.

### Type

simple string

### See also

* [syminfo.ticker](#var_syminfo.ticker)
* [syminfo.prefix](#var_syminfo.prefix)

## syminfo.industry

Returns the industry of the symbol, or [na](#var_na) if the symbol has no industry. Example: "internet software/services", "packaged software", "integrated Oil", "Motor Vehicles", etc. these are the same values one can see in the chart's "symbol info" window.

### Type

simple string

### Remarks

a sector is a broad section of the economy. an industry is a narrower classification. NasDaq:CaT (Caterpillar, inc.) for example, belongs to the "producer Manufacturing" sector and the "trucks/Construction/Farm Machinery" industry.

## syminfo.minmove

Returns a whole number used to calculate the smallest increment between a symbol's price movements ([syminfo.mintick](#var_syminfo.mintick)). it is the numerator in the [syminfo.mintick](#var_syminfo.mintick) formula: `[syminfo.minmove](#var_syminfo.minmove) / [syminfo.pricescale](#var_syminfo.pricescale) = [syminfo.mintick](#var_syminfo.mintick)`.

### Type

simple int

### See also

* [ticker.new](#fun_ticker.new)
* [syminfo.ticker](#var_syminfo.ticker)
* [timeframe.period](#var_timeframe.period)
* [timeframe.multiplier](#var_timeframe.multiplier)
* [syminfo.root](#var_syminfo.root)

## syminfo.mintick

Min tick value for the current symbol.

### Type

simple float

### See also

* [syminfo.pointvalue](#var_syminfo.pointvalue)

## syminfo.pointvalue

point value for the current symbol.

### Type

simple float

### See also

* [syminfo.mintick](#var_syminfo.mintick)

## syminfo.prefix

prefix of current symbol name (i.e. for 'CME\_EOD:TickER' prefix is 'CME\_EOD').

### Type

simple string

### Example


```s

//@version=5
indicator("syminfo.prefix")

// if current chart symbol is 'baTs:MsFT' then syminfo.prefix is 'baTs'.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, text=syminfo.prefix)


```

### See also

* [syminfo.ticker](#var_syminfo.ticker)
* [syminfo.tickerid](#var_syminfo.tickerid)

## syminfo.pricescale

Returns a whole number used to calculate the smallest increment between a symbol's price movements ([syminfo.mintick](#var_syminfo.mintick)). it is the denominator in the [syminfo.mintick](#var_syminfo.mintick) formula: `[syminfo.minmove](#var_syminfo.minmove) / [syminfo.pricescale](#var_syminfo.pricescale) = [syminfo.mintick](#var_syminfo.mintick)`.

### Type

simple int

### See also

* [ticker.new](#fun_ticker.new)
* [syminfo.ticker](#var_syminfo.ticker)
* [timeframe.period](#var_timeframe.period)
* [timeframe.multiplier](#var_timeframe.multiplier)
* [syminfo.root](#var_syminfo.root)

## syminfo.root

Root for derivatives like futures contract. For other symbols returns the same value as [syminfo.ticker](#var_syminfo.ticker).

### Type

simple string

### Example


```s

//@version=5
indicator("syminfo.root")

// if the current chart symbol is continuous futures ('Es1!'), it would display 'Es'.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, syminfo.root)


```

### See also

* [syminfo.ticker](#var_syminfo.ticker)
* [syminfo.tickerid](#var_syminfo.tickerid)

## syminfo.sector

Returns the sector of the symbol, or [na](#var_na) if the symbol has no sector. Example: "Electronic Technology", "Technology services", "Energy Minerals", "Consumer Durables", etc. these are the same values one can see in the chart's "symbol info" window.

### Type

simple string

### Remarks

a sector is a broad section of the economy. an industry is a narrower classification. NasDaq:CaT (Caterpillar, inc.) for example, belongs to the "producer Manufacturing" sector and the "trucks/Construction/Farm Machinery" industry.

## syminfo.session

session type of the chart main series. possible values are [session.regular](#var_session.regular), [session.extended](#var_session.extended).

### Type

simple string

### See also

* [session.regular](#var_session.regular)
* [session.extended](#var_session.extended)

## syminfo.ticker

symbol name without exchange prefix, e.g. 'MsFT'.

### Type

simple string

### See also

* [syminfo.tickerid](#var_syminfo.tickerid)
* [timeframe.period](#var_timeframe.period)
* [timeframe.multiplier](#var_timeframe.multiplier)
* [syminfo.root](#var_syminfo.root)

## syminfo.tickerid

Returns the full form of the ticker iD representing a symbol, for use as an argument in functions with a \`ticker\` or \`symbol\` parameter. it always includes the prefix (exchange) and ticker separated by a colon ("NasDaq:aapL"), but it can also include other symbol data such as dividend adjustment, chart type, currency conversion, etc.

### Type

simple string

### Remarks

because the value of this variable does not always use a simple "prefix:ticker" format, it is a poor candidate for use in boolean comparisons or string manipulation functions. in those contexts, run the variable's result through [ticker.standard](#fun_ticker.standard) to purify it. this will remove any extraneous information and return a ticker iD consistently formatted using the "prefix:ticker" structure.

### See also

* [ticker.new](#fun_ticker.new)
* [syminfo.ticker](#var_syminfo.ticker)
* [timeframe.period](#var_timeframe.period)
* [timeframe.multiplier](#var_timeframe.multiplier)
* [syminfo.root](#var_syminfo.root)

## syminfo.timezone

timezone of the exchange of the chart main series. possible values see in [timestamp](#fun_timestamp).

### Type

simple string

### See also

* [timestamp](#fun_timestamp)

## syminfo.type

the type of market the symbol belongs to. the values are "stock", "fund", "dr", "right", "bond", "warrant", "structured", "index", "forex", "futures", "spread", "economic", "fundamental", "crypto", "spot", "swap", "option", "commodity".

### Type

simple string

### See also

* [syminfo.ticker](#var_syminfo.ticker)

## syminfo.volumetype

Volume type of the current symbol. possible values are: "base" for base currency, "quote" for quote currency, "tick" for the number of transactions, and "n/a" when there is no volume or its type is not specified.

### Type

simple string

### Remarks

Only some data feed suppliers provide information qualifying volume. as a result, the variable will return a value on some symbols only, mostly in the crypto sector.

### See also

* [syminfo.type](#var_syminfo.type)

## ta.accdist

accumulation/distribution index.

### Type

series float

## ta.iii

intraday intensity index.

### Type

series float

### Example


```s

//@version=5
indicator("intraday intensity index")
plot(ta.iii, color=color.yellow)

// the same on pine
f_iii() =>
    (2 * close - high - low) / ((high - low) * volume)

plot(f_iii())

```

## ta.nvi

Negative Volume index.

### Type

series float

### Example


```s

//@version=5
indicator("Negative Volume index")

plot(ta.nvi, color=color.yellow)

// the same on pine
f_nvi() =>
    float ta_nvi = 1.0
    float prevNvi = (nz(ta_nvi[1], 0.0) == 0.0)  ? 1.0: ta_nvi[1]
    if nz(close, 0.0) == 0.0 or nz(close[1], 0.0) == 0.0
        ta_nvi := prevNvi
    else
        ta_nvi := (volume < nz(volume[1], 0.0)) ? prevNvi + ((close - close[1]) / close[1]) * prevNvi : prevNvi
    result = ta_nvi

plot(f_nvi())

```

## ta.obv

On balance Volume.

### Type

series float

### Example


```s

//@version=5
indicator("On balance Volume")
plot(ta.obv, color=color.yellow)

// the same on pine
f_obv() =>
    ta.cum(math.sign(ta.change(close)) * volume)

plot(f_obv())

```

## ta.pvi

positive Volume index.

### Type

series float

### Example


```s

//@version=5
indicator("positive Volume index")

plot(ta.pvi, color=color.yellow)

// the same on pine
f_pvi() =>
    float ta_pvi = 1.0
    float prevpvi = (nz(ta_pvi[1], 0.0) == 0.0)  ? 1.0: ta_pvi[1]
    if nz(close, 0.0) == 0.0 or nz(close[1], 0.0) == 0.0
        ta_pvi := prevpvi
    else
        ta_pvi := (volume > nz(volume[1], 0.0)) ? prevpvi + ((close - close[1]) / close[1]) * prevpvi : prevpvi
    result = ta_pvi

plot(f_pvi())

```

## ta.pvt

price-Volume trend.

### Type

series float

### Example


```s

//@version=5
indicator("price-Volume trend")
plot(ta.pvt, color=color.yellow)

// the same on pine
f_pvt() =>
    ta.cum((ta.change(close) / close[1]) * volume)

plot(f_pvt())

```

## ta.tr

true range. same as tr(false). it is max(high - low, abs(high - close\[1\]), abs(low - close\[1\]))

### Type

series float

### See also

* [ta.tr](#fun_ta.tr)
* [ta.atr](#fun_ta.atr)

## ta.vwap

Volume Weighted average price. it uses [hlc3](#var_hlc3) as its source series.

### Type

series float

### See also

* [ta.vwap](#fun_ta.vwap)

## ta.wad

Williams accumulation/Distribution.

### Type

series float

### Example


```s

//@version=5
indicator("Williams accumulation/Distribution")
plot(ta.wad, color=color.yellow)

// the same on pine
f_wad() =>
    trueHigh = math.max(high, close[1])
    trueLow = math.min(low, close[1])
    mom = ta.change(close)
    gain = (mom > 0) ? close - trueLow : (mom < 0) ? close - trueHigh : 0
    ta.cum(gain)

plot(f_wad())

```

## ta.wvad

Williams variable accumulation/Distribution.

### Type

series float

### Example


```s

//@version=5
indicator("Williams variable accumulation/Distribution")
plot(ta.wvad, color=color.yellow)

// the same on pine
f_wvad() =>
    (close - open) / (high - low) * volume

plot(f_wvad())

```

## table.all

Returns an array filled with all the current tables drawn by the script.

### Type

table\[\]

### Example


```s

//@version=5
indicator("table.all")
//delete all tables
table.new(position = position.top_right, columns = 2, rows = 1, bgcolor = color.yellow, border_width = 1)
a_alltables = table.all
if array.size(a_alltables) > 0
    for i = 0 to array.size(a_alltables) - 1
        table.delete(array.get(a_alltables, i))


```

### Remarks

the array is read-only. index zero of the array is the iD of the oldest object on the chart.

### See also

* [table.new](#fun_table.new)
* [line.all](#var_line.all)
* [label.all](#var_label.all)
* [box.all](#var_box.all)

## time

Current bar time in unix format. it is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

### Type

series int

### Remarks

Note that this variable returns the timestamp based on the time of the bar's open. because of that, for overnight sessions (e.g. EuRusD, where Monday session starts on sunday, 17:00) this variable can return time before the specified date of the trading day. For example, on EuRusD, \`dayofmonth(time)\` can be lower by 1 than the date of the trading day, because the bar for the current day actually opens one day prior.

### See also

* [time](#fun_time)
* [time_close](#var_time_close)
* [timenow](#var_timenow)
* [year](#var_year)
* [month](#var_month)
* [weekofyear](#var_weekofyear)
* [dayofmonth](#var_dayofmonth)
* [dayofweek](#var_dayofweek)
* [hour](#var_hour)
* [minute](#var_minute)
* [second](#var_second)

## time_close

the time of the current bar's close in unix format. it represents the number of milliseconds elapsed since 00:00:00 uTC, 1 January 1970. On non-standard price-based chart types (Renko, line break, Kagi, point & figure, and Range), this variable returns [na](#var_na) on the chart's realtime bars.

### Type

series int

### See also

* [time](#var_time)
* [timenow](#var_timenow)
* [year](#var_year)
* [month](#var_month)
* [weekofyear](#var_weekofyear)
* [dayofmonth](#var_dayofmonth)
* [dayofweek](#var_dayofweek)
* [hour](#var_hour)
* [minute](#var_minute)
* [second](#var_second)

## time_tradingday

the beginning time of the trading day the current bar belongs to, in unix format (the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970).

### Type

series int

### Remarks

the variable is useful for overnight sessions, where the current day's session can start on the previous calendar day (e.g., on EuRusD the Monday session will start on sunday, 17:00). unlike \`time\`, which would return the timestamp for sunday at 17:00 for the Monday daily bar, \`time_tradingday\` will return the timestamp for Monday, 00:00.

When used on timeframes higher than 1D, \`time_tradingday\` returns the trading day of the last day inside the bar (e.g. on 1W, it will return the last trading day of the week).

### See also

* [time](#var_time)
* [time_close](#var_time_close)

## timeframe.isdaily

Returns true if current resolution is a daily resolution, false otherwise.

### Type

simple bool

### See also

* [timeframe.isdwm](#var_timeframe.isdwm)
* [timeframe.isintraday](#var_timeframe.isintraday)
* [timeframe.isminutes](#var_timeframe.isminutes)
* [timeframe.isseconds](#var_timeframe.isseconds)
* [timeframe.isweekly](#var_timeframe.isweekly)
* [timeframe.ismonthly](#var_timeframe.ismonthly)

## timeframe.isdwm

Returns true if current resolution is a daily or weekly or monthly resolution, false otherwise.

### Type

simple bool

### See also

* [timeframe.isintraday](#var_timeframe.isintraday)
* [timeframe.isminutes](#var_timeframe.isminutes)
* [timeframe.isseconds](#var_timeframe.isseconds)
* [timeframe.isdaily](#var_timeframe.isdaily)
* [timeframe.isweekly](#var_timeframe.isweekly)
* [timeframe.ismonthly](#var_timeframe.ismonthly)

## timeframe.isintraday

Returns true if current resolution is an intraday (minutes or seconds) resolution, false otherwise.

### Type

simple bool

### See also

* [timeframe.isminutes](#var_timeframe.isminutes)
* [timeframe.isseconds](#var_timeframe.isseconds)
* [timeframe.isdwm](#var_timeframe.isdwm)
* [timeframe.isdaily](#var_timeframe.isdaily)
* [timeframe.isweekly](#var_timeframe.isweekly)
* [timeframe.ismonthly](#var_timeframe.ismonthly)

## timeframe.isminutes

Returns true if current resolution is a minutes resolution, false otherwise.

### Type

simple bool

### See also

* [timeframe.isdwm](#var_timeframe.isdwm)
* [timeframe.isintraday](#var_timeframe.isintraday)
* [timeframe.isseconds](#var_timeframe.isseconds)
* [timeframe.isdaily](#var_timeframe.isdaily)
* [timeframe.isweekly](#var_timeframe.isweekly)
* [timeframe.ismonthly](#var_timeframe.ismonthly)

## timeframe.ismonthly

Returns true if current resolution is a monthly resolution, false otherwise.

### Type

simple bool

### See also

* [timeframe.isdwm](#var_timeframe.isdwm)
* [timeframe.isintraday](#var_timeframe.isintraday)
* [timeframe.isminutes](#var_timeframe.isminutes)
* [timeframe.isseconds](#var_timeframe.isseconds)
* [timeframe.isdaily](#var_timeframe.isdaily)
* [timeframe.isweekly](#var_timeframe.isweekly)

## timeframe.isseconds

Returns true if current resolution is a seconds resolution, false otherwise.

### Type

simple bool

### See also

* [timeframe.isdwm](#var_timeframe.isdwm)
* [timeframe.isintraday](#var_timeframe.isintraday)
* [timeframe.isminutes](#var_timeframe.isminutes)
* [timeframe.isdaily](#var_timeframe.isdaily)
* [timeframe.isweekly](#var_timeframe.isweekly)
* [timeframe.ismonthly](#var_timeframe.ismonthly)

## timeframe.isweekly

Returns true if current resolution is a weekly resolution, false otherwise.

### Type

simple bool

### See also

* [timeframe.isdwm](#var_timeframe.isdwm)
* [timeframe.isintraday](#var_timeframe.isintraday)
* [timeframe.isminutes](#var_timeframe.isminutes)
* [timeframe.isseconds](#var_timeframe.isseconds)
* [timeframe.isdaily](#var_timeframe.isdaily)
* [timeframe.ismonthly](#var_timeframe.ismonthly)

## timeframe.multiplier

Multiplier of resolution, e.g. '60' - 60, 'D' - 1, '5D' - 5, '12M' - 12.

### Type

simple int

### See also

* [syminfo.ticker](#var_syminfo.ticker)
* [syminfo.tickerid](#var_syminfo.tickerid)
* [timeframe.period](#var_timeframe.period)

## timeframe.period

a string representation of the chart's timeframe. the returned string's format is "\[<quantity>;\]\[<units>;\]", where <quantity>; and <units>; are in some cases absent. <quantity>; is the number of units, but it is absent if that number is 1. <unit>; is "s" for seconds, "D" for days, "W" for weeks, "M" for months, but it is absent for minutes. No <unit>; exists for hours.

the variable will return: "10s" for 10 seconds, "60" for 60 minutes, "D" for one day, "2W" for two weeks, "3M" for one quarter.

Can be used as an argument with any function containing a \`timeframe\` parameter.

### Type

simple string

### See also

* [syminfo.ticker](#var_syminfo.ticker)
* [syminfo.tickerid](#var_syminfo.tickerid)
* [timeframe.multiplier](#var_timeframe.multiplier)

## timenow

Current time in unix format. it is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

### Type

series int

### Remarks

please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

### See also

* [timestamp](#fun_timestamp)
* [time](#var_time)
* [time_close](#var_time_close)
* [year](#var_year)
* [month](#var_month)
* [weekofyear](#var_weekofyear)
* [dayofmonth](#var_dayofmonth)
* [dayofweek](#var_dayofweek)
* [hour](#var_hour)
* [minute](#var_minute)
* [second](#var_second)

## volume

Current bar volume.

### Type

series float

### Remarks

previous values may be accessed with square brackets operator \[\], e.g. volume\[1\], volume\[2\].

### See also

* [open](#var_open)
* [high](#var_high)
* [low](#var_low)
* [close](#var_close)
* [time](#fun_time)
* [hl2](#var_hl2)
* [hlc3](#var_hlc3)
* [hlcc4](#var_hlcc4)
* [ohlc4](#var_ohlc4)

## weekofyear

Week number of current bar time in exchange timezone.

### Type

series int

### Remarks

Note that this variable returns the week based on the time of the bar's open. For overnight sessions (e.g. EuRusD, where Monday session starts on sunday, 17:00) this value can be lower by 1 than the week of the trading day.

### See also

* [weekofyear](#fun_weekofyear)
* [time](#var_time)
* [year](#var_year)
* [month](#var_month)
* [dayofmonth](#var_dayofmonth)
* [dayofweek](#var_dayofweek)
* [hour](#var_hour)
* [minute](#var_minute)
* [second](#var_second)

## year

Current bar year in exchange timezone.

### Type

series int

### Remarks

Note that this variable returns the year based on the time of the bar's open. For overnight sessions (e.g. EuRusD, where Monday session starts on sunday, 17:00) this value can be lower by 1 than the year of the trading day.

### See also

* [year](#fun_year)
* [time](#var_time)
* [month](#var_month)
* [weekofyear](#var_weekofyear)
* [dayofmonth](#var_dayofmonth)
* [dayofweek](#var_dayofweek)
* [hour](#var_hour)
* [minute](#var_minute)
* [second](#var_second)

Functions
---------

## alert

Creates an alert event when called during the real-time bar, which will trigger a script alert based on "alert function events" if one was previously created for the indicator or strategy through the "Create alert" dialog box.

### Syntax

alert(message, freq) - void

### Arguments

- `message`

    >  (`series` `string`)
    
    >  Message sent when the alert triggers. Required argument.

freq (input string) the triggering frequency. possible values are: [alert.freq_all](#var_alert.freq_all) (all function calls trigger the alert), [alert.freq\_once\_per_bar](#var_alert.freq_once_per_bar) (the first function call during the bar triggers the alert), [alert.freq\_once\_per\_bar\_close](#var_alert.freq_once_per_bar_close) (the function call triggers the alert only when it occurs during the last script iteration of the real-time bar, when it closes). the default is [alert.freq\_once\_per_bar](#var_alert.freq_once_per_bar).

### Example


```s

//@version=5
indicator("`alert()` example", "", true)
ma = ta.sma(close, 14)
xup = ta.crossover(close, ma)
if xup
    // trigger the alert the first time a cross occurs during the real-time bar.
    alert("price (" + str.tostring(close) + ") crossed over Ma (" + str.tostring(ma) +  ").", alert.freq_once_per_bar)
plot(ma)
plotchar(xup, "xup", "a-2", location.top, size = size.tiny)


```

### Remarks

the [Help center](https://www.tradingview.com/chart/?solution=43000597494) explains how to create such alerts.

Contrary to [alertcondition](#fun_alertcondition), [alert](#fun_alert) calls do NOT count as an additional plot.

Function calls can be located in both global and local scopes.

Function calls do not display anything on the chart.

the 'freq' argument only affects the triggering frequency of the function call where it is used.

### See also

* [alertcondition](#fun_alertcondition)

## alertcondition

Creates alert condition, that is available in Create alert dialog. please note, that [alertcondition](#fun_alertcondition) does NOT create an alert, it just gives you more options in Create alert dialog. also, [alertcondition](#fun_alertcondition) effect is invisible on chart.

### Syntax

alertcondition(condition, title, message) - void

### Arguments

- `condition`

    >  (`series` `bool`)
    
    >  series of boolean values that is used for alert. true values mean alert fire, false - no alert. Required argument.

- `title`

    >  (`const` `string`)
    
    >  title of the alert condition. optional argument.

- `message`

    >  (`const` `string`)
    
    >  Message to display when alert fires. optional argument.

### Example


```s

//@version=5
indicator("alertcondition", overlay=true)
alertcondition(close >= open, title='alert on Green bar', message='Green bar!')


```

### Remarks

please note that an alertcondition call generates an additional plot. all such calls are taken into account when we calculate the number of the output series per script.

### See also

* [alert](#fun_alert)

## array.abs

+1 overload

Returns an array containing the absolute value of each element in the original array.

### syntax & Overloads

> [array.abs(id) - float\[\]](#fun_array.abs-0)
> [array.abs(id) - int\[\]](#fun_array.abs-1)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

### See also

* [array.new_float](#fun_array.new_float)
* [array.insert](#fun_array.insert)
* [array.slice](#fun_array.slice)
* [array.reverse](#fun_array.reverse)
* [order.ascending](#var_order.ascending)
* [order.descending](#var_order.descending)

## array.avg

+1 overload

the function returns the mean of an array's elements.

### syntax & Overloads

> [array.avg(id) → series float](#fun_array.avg-0)
> [array.avg(id) → series int](#fun_array.avg-1)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.avg example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i])
plot(array.avg(a))


```

### Returns

Mean of array's elements.

### See also

* [array.new_float](#fun_array.new_float)
* [array.max](#fun_array.max)
* [array.min](#fun_array.min)
* [array.stdev](#fun_array.stdev)

## array.binary_search

the function returns the index of the value, or -1 if the value is not found. the array to search must be sorted in ascending order.

### Syntax

array.binary_search(id, val) → series int

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

- `val`

    >  (`series` `int`/`float`)
    
    >  the value to search for in the array.

### Example


```s

//@version=5
indicator("array.binary_search")
a = array.from(5, -2, 0, 9, 1)
array.sort(a) // [-2, 0, 1, 5, 9]
position = array.binary_search(a, 0) // 1
plot(position)


```

### Remarks

a binary search works on arrays pre-sorted in ascending order. it begins by comparing an element in the middle of the array with the target value. if the element matches the target value, its position in the array is returned. if the element's value is greater than the target value, the search continues in the lower half of the array. if the element's value is less than the target value, the search continues in the upper half of the array. by doing this recursively, the algorithm progressively eliminates smaller and smaller portions of the array in which the target value cannot lie.

### See also

* [array.new_float](#fun_array.new_float)
* [array.insert](#fun_array.insert)
* [array.slice](#fun_array.slice)
* [array.reverse](#fun_array.reverse)
* [order.ascending](#var_order.ascending)
* [order.descending](#var_order.descending)

## array.binary\_search\_leftmost

the function returns the index of the value if it is found. When the value is not found, the function returns the index of the next smallest element to the left of where the value would lie if it was in the array. the array to search must be sorted in ascending order.

### Syntax

array.binary\_search\_leftmost(id, val) → series int

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

- `val`

    >  (`series` `int`/`float`)
    
    >  the value to search for in the array.

### Example


```s

//@version=5
indicator("array.binary_search_leftmost")
a = array.from(5, -2, 0, 9, 1)
array.sort(a) // [-2, 0, 1, 5, 9]
position = array.binary_search_leftmost(a, 3) // 2
plot(position)



```

### Example


```s

//@version=5
indicator("array.binary_search_leftmost, repetitive elements")
a = array.from(4, 5, 5, 5)
// Returns the index of the first instance.
position = array.binary_search_leftmost(a, 5)
plot(position) // plots 1


```

### Remarks

a binary search works on arrays pre-sorted in ascending order. it begins by comparing an element in the middle of the array with the target value. if the element matches the target value, its position in the array is returned. if the element's value is greater than the target value, the search continues in the lower half of the array. if the element's value is less than the target value, the search continues in the upper half of the array. by doing this recursively, the algorithm progressively eliminates smaller and smaller portions of the array in which the target value cannot lie.

### See also

* [array.new_float](#fun_array.new_float)
* [array.insert](#fun_array.insert)
* [array.slice](#fun_array.slice)
* [array.reverse](#fun_array.reverse)
* [order.ascending](#var_order.ascending)
* [order.descending](#var_order.descending)

## array.binary\_search\_rightmost

the function returns the index of the value if it is found. When the value is not found, the function returns the index of the element to the right of where the value would lie if it was in the array. the array must be sorted in ascending order.

### Syntax

array.binary\_search\_rightmost(id, val) → series int

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

- `val`

    >  (`series` `int`/`float`)
    
    >  the value to search for in the array.

### Example


```s

//@version=5
indicator("array.binary_search_rightmost")
a = array.from(5, -2, 0, 9, 1)
array.sort(a) // [-2, 0, 1, 5, 9]
position = array.binary_search_rightmost(a, 3) // 3
plot(position)



```

### Example


```s

//@version=5
indicator("array.binary_search_rightmost, repetitive elements")
a = array.from(4, 5, 5, 5)
// Returns the index of the last instance.
position = array.binary_search_rightmost(a, 5)
plot(position) // plots 3


```

### Remarks

a binary search works on sorted arrays in ascending order. it begins by comparing an element in the middle of the array with the target value. if the element matches the target value, its position in the array is returned. if the element's value is greater than the target value, the search continues in the lower half of the array. if the element's value is less than the target value, the search continues in the upper half of the array. by doing this recursively, the algorithm progressively eliminates smaller and smaller portions of the array in which the target value cannot lie.

### See also

* [array.new_float](#fun_array.new_float)
* [array.insert](#fun_array.insert)
* [array.slice](#fun_array.slice)
* [array.reverse](#fun_array.reverse)
* [order.ascending](#var_order.ascending)
* [order.descending](#var_order.descending)

## array.clear

the function removes all elements from an array.

### Syntax

array.clear(id) - void

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.clear example")
a = array.new_float(5,high)
array.clear(a)
array.push(a, close)
plot(array.get(a,0))
plot(array.size(a))


```

### See also

* [array.new_float](#fun_array.new_float)
* [array.insert](#fun_array.insert)
* [array.push](#fun_array.push)
* [array.remove](#fun_array.remove)
* [array.pop](#fun_array.pop)

## array.concat

the function is used to merge two arrays. it pushes all elements from the second array to the first array, and returns the first array.

### Syntax

array.concat(id1, id2) - array<type>;

### Arguments

- `id1`

    >  (`any` `array` `type`)
    
    >  the first array object.

- `id2`

    >  (`any` `array` `type`)
    
    >  the second array object.

### Example


```s

//@version=5
indicator("array.concat example")
a = array.new_float(0,0)
b = array.new_float(0,0)
for i = 0 to 4
    array.push(a, high[i])
    array.push(b, low[i])
c = array.concat(a,b)
plot(array.size(a))
plot(array.size(b))
plot(array.size(c))


```

### Returns

the first array with merged elements from the second array.

### See also

* [array.new_float](#fun_array.new_float)
* [array.insert](#fun_array.insert)
* [array.slice](#fun_array.slice)

## array.copy

the function creates a copy of an existing array.

### Syntax

array.copy(id) - array<type>;

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.copy example")
length = 5
a = array.new_float(length, close)
b = array.copy(a)
a := array.new_float(length, open)
plot(array.sum(a) / length)
plot(array.sum(b) / length)


```

### Returns

a copy of an array.

### See also

* [array.new_float](#fun_array.new_float)
* [array.get](#fun_array.get)
* [array.slice](#fun_array.slice)
* [array.sort](#fun_array.sort)

## array.covariance

the function returns the covariance of two arrays.

### Syntax

array.covariance(id1, id2, biased) → series float

### Arguments

- `id1`

    >  (`int`\[\])
    
    >  an array object.

- `id2`

    >  (`int`\[\])
    
    >  an array object.

- `biased`

    >  (`series` `bool`)
    
    >  Determines which estimate should be used. optional. the default is true.

### Example


```s

//@version=5
indicator("array.covariance example")
a = array.new_float(0)
b = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i])
    array.push(b, open[i])
plot(array.covariance(a, b))


```

### Returns

the covariance of two arrays.

### Remarks

if \`biased\` is true, function will calculate using a biased estimate of the entire population, if false - unbiased estimate of a sample.

### See also

* [array.new_float](#fun_array.new_float)
* [array.max](#fun_array.max)
* [array.stdev](#fun_array.stdev)
* [array.avg](#fun_array.avg)
* [array.variance](#fun_array.variance)

## array.every

Returns [true](#op_true) if all elements of the \`id\` array are [true](#op_true), [false](#op_false) otherwise.

### Syntax

array.every(id) → series bool

### Arguments

- `id`

    >  (`bool`\[\])
    
    >  an array object.

### Remarks

this function also works with arrays of [int](#op_int) and [float](#op_float) types, in which case zero values are considered [false](#op_false), and all others [true](#op_true).

### See also

* [array.some](#fun_array.some)
* [array.get](#fun_array.get)

## array.fill

the function sets elements of an array to a single value. if no index is specified, all elements are set. if only a start index (default 0) is supplied, the elements starting at that index are set. if both index parameters are used, the elements from the starting index up to but not including the end index (default na) are set.

### Syntax

array.fill(id, value, index\_from, index\_to) - void

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

- `value`

    >  (`series` <`type` `of` `the` `array's` `elements`>;)
    
    >  Value to fill the array with.

- `index_from`

    >  (`series` `int`)
    
    >  start index, default is 0.

- `index_to`

    >  (`series` `int`)
    
    >  End index, default is na. Must be one greater than the index of the last element to set.

### Example


```s

//@version=5
indicator("array.fill example")
a = array.new_float(10)
array.fill(a, close)
plot(array.sum(a))


```

### See also

* [array.new_float](#fun_array.new_float)
* [array.set](#fun_array.set)
* [array.slice](#fun_array.slice)

## array.first

Returns the array's first element. throws a runtime error if the array is empty.

### Syntax

array.first(id) → series <type>;

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.first example")
arr = array.new_int(3, 10)
plot(array.first(arr))


```

### See also

* [array.last](#fun_array.last)
* [array.get](#fun_array.get)

## array.from

+10 overloads

the function takes a variable number of arguments with one of the types: int, float, bool, string, label, line, color, box, table, linefill, and returns an array of the corresponding type.

### syntax & Overloads

> [array.from(arg0, arg1, ...) - type\[\]](#fun_array.from-0)
> [array.from(arg0, arg1, ...) - label\[\]](#fun_array.from-1)
> [array.from(arg0, arg1, ...) - line\[\]](#fun_array.from-2)
> [array.from(arg0, arg1, ...) - box\[\]](#fun_array.from-3)
> [array.from(arg0, arg1, ...) - table\[\]](#fun_array.from-4)
> [array.from(arg0, arg1, ...) - linefill\[\]](#fun_array.from-5)
> [array.from(arg0, arg1, ...) - string\[\]](#fun_array.from-6)
> [array.from(arg0, arg1, ...) - color\[\]](#fun_array.from-7)
> [array.from(arg0, arg1, ...) - int\[\]](#fun_array.from-8)
> [array.from(arg0, arg1, ...) - float\[\]](#fun_array.from-9)
> [array.from(arg0, arg1, ...) - bool\[\]](#fun_array.from-10)

### Arguments

- `arg0, arg1, ...`

    >  (<`arg..._type`>;)
    
    >  array arguments.

### Example


```s

//@version=5
indicator("array.from_example", overlay = false)
arr = array.from("Hello", "World!") // arr (string[]) will contain 2 elements: {Hello}, {World!}.
plot(close)


```

### Returns

the array element's value.

## array.get

the function returns the value of the element at the specified index.

### Syntax

array.get(id, index) → series <type>;

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

- `index`

    >  (`series` `int`)
    
    >  the index of the element whose value is to be returned.

### Example


```s

//@version=5
indicator("array.get example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i] - open[i])
plot(array.get(a, 9))


```

### Returns

the array element's value.

### See also

* [array.new_float](#fun_array.new_float)
* [array.set](#fun_array.set)
* [array.slice](#fun_array.slice)
* [array.sort](#fun_array.sort)

## array.includes

the function returns true if the value was found in an array, false otherwise.

### Syntax

array.includes(id, value) → series bool

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

- `value`

    >  (`series` <`type` `of` `the` `array's` `elements`>;)
    
    >  the value to search in the array.

### Example


```s

//@version=5
indicator("array.includes example")
a = array.new_float(5,high)
p = close
if array.includes(a, high)
    p := open
plot(p)


```

### Returns

true if the value was found in the array, false otherwise.

### See also

* [array.new_float](#fun_array.new_float)
* [array.indexof](#fun_array.indexof)
* [array.shift](#fun_array.shift)
* [array.remove](#fun_array.remove)
* [array.insert](#fun_array.insert)

## array.indexof

the function returns the index of the first occurrence of the value, or -1 if the value is not found.

### Syntax

array.indexof(id, value) → series int

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

- `value`

    >  (`series` <`type` `of` `the` `array's` `elements`>;)
    
    >  the value to search in the array.

### Example


```s

//@version=5
indicator("array.indexof example")
a = array.new_float(5,high)
index = array.indexof(a, high)
plot(index)


```

### Returns

the index of an element.

### See also

* [array.lastindexof](#fun_array.lastindexof)
* [array.get](#fun_array.get)
* [array.lastindexof](#fun_array.lastindexof)
* [array.remove](#fun_array.remove)
* [array.insert](#fun_array.insert)

## array.insert

the function changes the contents of an array by adding new elements in place.

### Syntax

array.insert(id, index, value) - void

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

- `index`

    >  (`series` `int`)
    
    >  the index at which to insert the value.

- `value`

    >  (`series` <`type` `of` `the` `array's` `elements`>;)
    
    >  the value to add to the array.

### Example


```s

//@version=5
indicator("array.insert example")
a = array.new_float(5, close)
array.insert(a, 0, open)
plot(array.get(a, 5))


```

### See also

* [array.new_float](#fun_array.new_float)
* [array.set](#fun_array.set)
* [array.push](#fun_array.push)
* [array.remove](#fun_array.remove)
* [array.pop](#fun_array.pop)
* [array.unshift](#fun_array.unshift)

## array.join

the function creates and returns a new string by concatenating all the elements of an array, separated by the specified separator string.

### Syntax

array.join(id, separator) → series string

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

- `separator`

    >  (`series` `string`)
    
    >  the string used to separate each array element.

### Example


```s

//@version=5
indicator("array.join example")
a = array.new_float(5, 5)
label.new(bar_index, close, array.join(a, ","))


```

### See also

* [array.new_float](#fun_array.new_float)
* [array.set](#fun_array.set)
* [array.insert](#fun_array.insert)
* [array.remove](#fun_array.remove)
* [array.pop](#fun_array.pop)
* [array.unshift](#fun_array.unshift)

## array.last

Returns the array's last element. throws a runtime error if the array is empty.

### Syntax

array.last(id) → series <type>;

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.last example")
arr = array.new_int(3, 10)
plot(array.last(arr))


```

### See also

* [array.first](#fun_array.first)
* [array.get](#fun_array.get)

## array.lastindexof

the function returns the index of the last occurrence of the value, or -1 if the value is not found.

### Syntax

array.lastindexof(id, value) → series int

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

- `value`

    >  (`series` <`type` `of` `the` `array's` `elements`>;)
    
    >  the value to search in the array.

### Example


```s

//@version=5
indicator("array.lastindexof example")
a = array.new_float(5,high)
index = array.lastindexof(a, high)
plot(index)


```

### Returns

the index of an element.

### See also

* [array.new_float](#fun_array.new_float)
* [array.set](#fun_array.set)
* [array.push](#fun_array.push)
* [array.remove](#fun_array.remove)
* [array.insert](#fun_array.insert)

## array.max

+3 overloads

the function returns the greatest value, or the nth greatest value in a given array.

### syntax & Overloads

> [array.max(id) → series float](#fun_array.max-0)
> [array.max(id) → series int](#fun_array.max-1)
> [array.max(id, nth) → series float](#fun_array.max-2)
> [array.max(id, nth) → series int](#fun_array.max-3)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.max")
a = array.from(5, -2, 0, 9, 1)
thirdHighest = array.max(a, 2) // 1
plot(thirdHighest)


```

### Returns

the greatest or the nth greatest value in the array.

### See also

* [array.new_float](#fun_array.new_float)
* [array.min](#fun_array.min)
* [array.sum](#fun_array.sum)

## array.median

+1 overload

the function returns the median of an array's elements.

### syntax & Overloads

> [array.median(id) → series float](#fun_array.median-0)
> [array.median(id) → series int](#fun_array.median-1)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.median example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i])
plot(array.median(a))


```

### Returns

the median of the array's elements.

### See also

* [array.median](#fun_array.median)
* [array.avg](#fun_array.avg)
* [array.variance](#fun_array.variance)
* [array.min](#fun_array.min)

## array.min

+3 overloads

the function returns the smallest value, or the nth smallest value in a given array.

### syntax & Overloads

> [array.min(id) → series float](#fun_array.min-0)
> [array.min(id) → series int](#fun_array.min-1)
> [array.min(id, nth) → series float](#fun_array.min-2)
> [array.min(id, nth) → series int](#fun_array.min-3)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.min")
a = array.from(5, -2, 0, 9, 1)
secondlowest = array.min(a, 1) // 0
plot(secondlowest)


```

### Returns

the smallest or the nth smallest value in the array.

### See also

* [array.new_float](#fun_array.new_float)
* [array.max](#fun_array.max)
* [array.sum](#fun_array.sum)

## array.mode

+1 overload

the function returns the mode of an array's elements. if there are several values with the same frequency, it returns the smallest value.

### syntax & Overloads

> [array.mode(id) → series float](#fun_array.mode-0)
> [array.mode(id) → series int](#fun_array.mode-1)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.mode example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i])
plot(array.mode(a))


```

### Returns

the most frequently occurring value from the \`id\` array. if none exists, returns the smallest value instead.

### See also

* [array.new_float](#fun_array.new_float)
* [ta.mode](#fun_ta.mode)
* [matrix.mode](#fun_matrix.mode)
* [array.avg](#fun_array.avg)
* [array.variance](#fun_array.variance)
* [array.min](#fun_array.min)

## array.new_bool

the function creates a new array object of bool type elements.

### Syntax

array.new\_bool(size, initial\_value) - bool\[\]

### Arguments

- `size`

    >  (`series` `int`)
    
    >  initial size of an array. optional. the default is 0.

- `initial_value`

    >  (`series` `bool`)
    
    >  initial value of all array elements. optional. the default is 'na'.

### Example


```s

//@version=5
indicator("array.new_bool example")
length = 5
a = array.new_bool(length, close > open)
plot(array.get(a, 0) ? close : open)


```

### Returns

the iD of an array object which may be used in other array.*() functions.

### Remarks

an array index starts from 0.

### See also

* [array.new_float](#fun_array.new_float)
* [array.get](#fun_array.get)
* [array.slice](#fun_array.slice)
* [array.sort](#fun_array.sort)

## array.new_box

the function creates a new array object of box type elements.

### Syntax

array.new\_box(size, initial\_value) - box\[\]

### Arguments

- `size`

    >  (`series` `int`)
    
    >  initial size of an array. optional. the default is 0.

- `initial_value`

    >  (`series` `box`)
    
    >  initial value of all array elements. optional. the default is 'na'.

### Example


```s

//@version=5
indicator("array.new_box example")
box[] boxes = array.new_box()
array.push(boxes, box.new(time, close, time+2, low, xloc=xloc.bar_time))
plot(1)


```

### Returns

the iD of an array object which may be used in other array.*() functions.

### Remarks

an array index starts from 0.

### See also

* [array.new_float](#fun_array.new_float)
* [array.get](#fun_array.get)
* [array.slice](#fun_array.slice)

## array.new_color

the function creates a new array object of color type elements.

### Syntax

array.new\_color(size, initial\_value) - color\[\]

### Arguments

- `size`

    >  (`series` `int`)
    
    >  initial size of an array. optional. the default is 0.

- `initial_value`

    >  (`series` `color`)
    
    >  initial value of all array elements. optional. the default is 'na'.

### Example


```s

//@version=5
indicator("array.new_color example")
length = 5
a = array.new_color(length, color.red)
plot(close, color = array.get(a, 0))


```

### Returns

the iD of an array object which may be used in other array.*() functions.

### Remarks

an array index starts from 0.

### See also

* [array.new_float](#fun_array.new_float)
* [array.get](#fun_array.get)
* [array.slice](#fun_array.slice)
* [array.sort](#fun_array.sort)

## array.new_float

the function creates a new array object of float type elements.

### Syntax

array.new\_float(size, initial\_value) - float\[\]

### Arguments

- `size`

    >  (`series` `int`)
    
    >  initial size of an array. optional. the default is 0.

- `initial_value`

    >  (`series` `int`/`float`)
    
    >  initial value of all array elements. optional. the default is 'na'.

### Example


```s

//@version=5
indicator("array.new_float example")
length = 5
a = array.new_float(length, close)
plot(array.sum(a) / length)


```

### Returns

the iD of an array object which may be used in other array.*() functions.

### Remarks

an array index starts from 0.

### See also

* [array.new_color](#fun_array.new_color)
* [array.new_bool](#fun_array.new_bool)
* [array.get](#fun_array.get)
* [array.slice](#fun_array.slice)
* [array.sort](#fun_array.sort)

## array.new_int

the function creates a new array object of int type elements.

### Syntax

array.new\_int(size, initial\_value) - int\[\]

### Arguments

- `size`

    >  (`series` `int`)
    
    >  initial size of an array. optional. the default is 0.

- `initial_value`

    >  (`series` `int`)
    
    >  initial value of all array elements. optional. the default is 'na'.

### Example


```s

//@version=5
indicator("array.new_int example")
length = 5
a = array.new_int(length, int(close))
plot(array.sum(a) / length)


```

### Returns

the iD of an array object which may be used in other array.*() functions.

### Remarks

an array index starts from 0.

### See also

* [array.new_float](#fun_array.new_float)
* [array.get](#fun_array.get)
* [array.slice](#fun_array.slice)
* [array.sort](#fun_array.sort)

## array.new_label

the function creates a new array object of label type elements.

### Syntax

array.new\_label(size, initial\_value) - label\[\]

### Arguments

- `size`

    >  (`series` `int`)
    
    >  initial size of an array. optional. the default is 0.

- `initial_value`

    >  (`series` `label`)
    
    >  initial value of all array elements. optional. the default is 'na'.

### Example


```s

//@version=5
indicator("array.new_label example")
var a = array.new_label()
l = label.new(bar_index, close, "some text")
array.push(a, l)
if close > close[1] and close[1] > close[2]
    // remove all labels
    size = array.size(a) - 1
    for i = 0 to size
        lb = array.get(a, i)
        label.delete(lb)


```

### Returns

the iD of an array object which may be used in other array.*() functions.

### Remarks

an array index starts from 0.

### See also

* [array.new_float](#fun_array.new_float)
* [array.get](#fun_array.get)
* [array.slice](#fun_array.slice)

## array.new_line

the function creates a new array object of line type elements.

### Syntax

array.new\_line(size, initial\_value) - line\[\]

### Arguments

- `size`

    >  (`series` `int`)
    
    >  initial size of an array. optional. the default is 0.

- `initial_value`

    >  (`series` `line`)
    
    >  initial value of all array elements. optional. the default is 'na'.

### Example


```s

//@version=5
indicator("array.new_line example")
// draw last 15 lines
var a = array.new_line()
array.push(a, line.new(bar_index - 1, close[1], bar_index, close))
if array.size(a) > 15
    ln = array.shift(a)
    line.delete(ln)


```

### Returns

the iD of an array object which may be used in other array.*() functions.

### Remarks

an array index starts from 0.

### See also

* [array.new_float](#fun_array.new_float)
* [array.get](#fun_array.get)
* [array.slice](#fun_array.slice)

## array.new_linefill

the function creates a new array object of linefill type elements.

### Syntax

array.new\_linefill(size, initial\_value) - linefill\[\]

### Arguments

- `size`

    >  (`series` `int`)
    
    >  initial size of an array.

- `initial_value`

    >  (`series` `linefill`)
    
    >  initial value of all array elements.

### Returns

the iD of an array object which may be used in other array.*() functions.

### Remarks

an array index starts from 0.

## array.new_string

the function creates a new array object of string type elements.

### Syntax

array.new\_string(size, initial\_value) - string\[\]

### Arguments

- `size`

    >  (`series` `int`)
    
    >  initial size of an array. optional. the default is 0.

- `initial_value`

    >  (`series` `string`)
    
    >  initial value of all array elements. optional. the default is 'na'.

### Example


```s

//@version=5
indicator("array.new_string example")
length = 5
a = array.new_string(length, "text")
label.new(bar_index, close, array.get(a, 0))


```

### Returns

the iD of an array object which may be used in other array.*() functions.

### Remarks

an array index starts from 0.

### See also

* [array.new_float](#fun_array.new_float)
* [array.get](#fun_array.get)
* [array.slice](#fun_array.slice)

## array.new_table

the function creates a new array object of table type elements.

### Syntax

array.new\_table(size, initial\_value) - table\[\]

### Arguments

- `size`

    >  (`series` `int`)
    
    >  initial size of an array. optional. the default is 0.

- `initial_value`

    >  (`series` `table`)
    
    >  initial value of all array elements. optional. the default is 'na'.

### Example


```s

//@version=5
indicator("table array")
table[] tables = array.new_table()
array.push(tables, table.new(position = position.top_left, rows = 1, columns = 2, bgcolor = color.yellow, border_width=1))
plot(1)


```

### Returns

the iD of an array object which may be used in other array.*() functions.

### Remarks

an array index starts from 0.

### See also

* [array.new_float](#fun_array.new_float)
* [array.get](#fun_array.get)
* [array.slice](#fun_array.slice)

## array.new<type>;

the function creates a new array object of <type>; elements.

### Syntax

array.new<type>;(size, initial_value) - array<type>;

### Arguments

- `size`

    >  (`series` `int`)
    
    >  initial size of an array. optional. the default is 0.

- `initial\_value`

    >  (<`array`\`_type`>;)
    
    >  initial value of all array elements. optional. the default is 'na'.

### Example


```s

//@version=5
indicator("array.new<string> example")
a = array.new<string>(1, "Hello, World!")
label.new(bar_index, close, array.get(a, 0))



```

### Example


```s

//@version=5
indicator("array.new<color> example")
a = array.new<color>()
array.push(a, color.red)
array.push(a, color.green)
plot(close, color = array.get(a, close > open ? 1 : 0))



```

### Example


```s

//@version=5
indicator("array.new<float> example")
length = 5
var a = array.new<float>(length, close)
if array.size(a) == length
    array.remove(a, 0)
    array.push(a, close)
plot(array.sum(a) / length, "sMa")



```

### Example


```s

//@version=5
indicator("array.new<line> example")
// draw last 15 lines
var a = array.new<line>()
array.push(a, line.new(bar_index - 1, close[1], bar_index, close))
if array.size(a) > 15
    ln = array.shift(a)
    line.delete(ln)


```

### Returns

the iD of an array object which may be used in other array.*() functions.

### Remarks

an array index starts from 0.

if you want to initialize an array and specify all its elements at the same time, then use the function array.from.

### See also

* [array.from](#fun_array.from)
* [array.push](#fun_array.push)
* [array.get](#fun_array.get)
* [array.size](#fun_array.size)
* [array.remove](#fun_array.remove)
* [array.shift](#fun_array.shift)
* [array.sum](#fun_array.sum)

## array.percentile\_linear\_interpolation

+1 overload

Returns the value for which the specified percentage of array values (percentile) are less than or equal to it, using linear interpolation.

### syntax & Overloads

> [array.percentile\_linear\_interpolation(id, percentage) → series float](#fun_array.percentile_linear_interpolation-0)
> [array.percentile\_linear\_interpolation(id, percentage) → series int](#fun_array.percentile_linear_interpolation-1)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

- `percentage`

    >  (`series` `int`/`float`)
    
    >  the percentage of values that must be equal or less than the returned value.

### Remarks

in statistics, the percentile is the percent of ranking items that appear at or below a certain score. this measurement shows the percentage of scores within a standard frequency distribution that is lower than the percentile rank you're measuring. linear interpolation estimates the value between two ranks.

### See also

* [array.new_float](#fun_array.new_float)
* [array.insert](#fun_array.insert)
* [array.slice](#fun_array.slice)
* [array.reverse](#fun_array.reverse)
* [order.ascending](#var_order.ascending)
* [order.descending](#var_order.descending)

## array.percentile\_nearest\_rank

+1 overload

Returns the value for which the specified percentage of array values (percentile) are less than or equal to it, using the nearest-rank method.

### syntax & Overloads

> [array.percentile\_nearest\_rank(id, percentage) → series float](#fun_array.percentile_nearest_rank-0)
> [array.percentile\_nearest\_rank(id, percentage) → series int](#fun_array.percentile_nearest_rank-1)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

- `percentage`

    >  (`series` `int`/`float`)
    
    >  the percentage of values that must be equal or less than the returned value.

### Remarks

in statistics, the percentile is the percent of ranking items that appear at or below a certain score. this measurement shows the percentage of scores within a standard frequency distribution that is lower than the percentile rank you're measuring.

### See also

* [array.new_float](#fun_array.new_float)
* [array.insert](#fun_array.insert)
* [array.slice](#fun_array.slice)
* [array.reverse](#fun_array.reverse)
* [order.ascending](#var_order.ascending)
* [order.descending](#var_order.descending)

## array.percentrank

+1 overload

Returns the percentile rank of the element at the specified \`index\`.

### syntax & Overloads

> [array.percentrank(id, index) → series float](#fun_array.percentrank-0)
> [array.percentrank(id, index) → series int](#fun_array.percentrank-1)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

- `index`

    >  (`series` `int`)
    
    >  the index of the element for which the percentile rank should be calculated.

### Remarks

percentile rank is the percentage of how many elements in the array are less than or equal to the reference value.

### See also

* [array.new_float](#fun_array.new_float)
* [array.insert](#fun_array.insert)
* [array.slice](#fun_array.slice)
* [array.reverse](#fun_array.reverse)
* [order.ascending](#var_order.ascending)
* [order.descending](#var_order.descending)

## array.pop

the function removes the last element from an array and returns its value.

### Syntax

array.pop(id) → series <type>;

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.pop example")
a = array.new_float(5,high)
removedel = array.pop(a)
plot(array.size(a))
plot(removedel)


```

### Returns

the value of the removed element.

### See also

* [array.new_float](#fun_array.new_float)
* [array.set](#fun_array.set)
* [array.push](#fun_array.push)
* [array.remove](#fun_array.remove)
* [array.insert](#fun_array.insert)
* [array.shift](#fun_array.shift)

## array.push

the function appends a value to an array.

### Syntax

array.push(id, value) - void

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

- `value`

    >  (`series` <`type` `of` `the` `array's` `elements`>;)
    
    >  the value of the element added to the end of the array.

### Example


```s

//@version=5
indicator("array.push example")
a = array.new_float(5, 0)
array.push(a, open)
plot(array.get(a, 5))


```

### See also

* [array.new_float](#fun_array.new_float)
* [array.set](#fun_array.set)
* [array.insert](#fun_array.insert)
* [array.remove](#fun_array.remove)
* [array.pop](#fun_array.pop)
* [array.unshift](#fun_array.unshift)

## array.range

+1 overload

the function returns the difference between the min and max values from a given array.

### syntax & Overloads

> [array.range(id) → series float](#fun_array.range-0)
> [array.range(id) → series int](#fun_array.range-1)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.range example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i])
plot(array.range(a))


```

### Returns

the difference between the min and max values in the array.

### See also

* [array.new_float](#fun_array.new_float)
* [array.min](#fun_array.min)
* [array.max](#fun_array.max)
* [array.sum](#fun_array.sum)

## array.remove

the function changes the contents of an array by removing the element with the specified index.

### Syntax

array.remove(id, index) → series <type>;

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

- `index`

    >  (`series` `int`)
    
    >  the index of the element to remove.

### Example


```s

//@version=5
indicator("array.remove example")
a = array.new_float(5,high)
removedel = array.remove(a, 0)
plot(array.size(a))
plot(removedel)


```

### Returns

the value of the removed element.

### See also

* [array.new_float](#fun_array.new_float)
* [array.set](#fun_array.set)
* [array.push](#fun_array.push)
* [array.insert](#fun_array.insert)
* [array.pop](#fun_array.pop)
* [array.shift](#fun_array.shift)

## array.reverse

the function reverses an array. the first array element becomes the last, and the last array element becomes the first.

### Syntax

array.reverse(id) - void

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.reverse example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i])
plot(array.get(a, 0))
array.reverse(a)
plot(array.get(a, 0))


```

### See also

* [array.new_float](#fun_array.new_float)
* [array.sort](#fun_array.sort)
* [array.push](#fun_array.push)
* [array.set](#fun_array.set)
* [array.avg](#fun_array.avg)

## array.set

the function sets the value of the element at the specified index.

### Syntax

array.set(id, index, value) - void

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

- `index`

    >  (`series` `int`)
    
    >  the index of the element to be modified.

- `value`

    >  (`series` <`type` `of` `the` `array's` `elements`>;)
    
    >  the new value to be set.

### Example


```s

//@version=5
indicator("array.set example")
a = array.new_float(10)
for i = 0 to 9
    array.set(a, i, close[i])
plot(array.sum(a) / 10)


```

### See also

* [array.new_float](#fun_array.new_float)
* [array.get](#fun_array.get)
* [array.slice](#fun_array.slice)

## array.shift

the function removes an array's first element and returns its value.

### Syntax

array.shift(id) → series <type>;

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.shift example")
a = array.new_float(5,high)
removedel = array.shift(a)
plot(array.size(a))
plot(removedel)


```

### Returns

the value of the removed element.

### See also

* [array.unshift](#fun_array.unshift)
* [array.set](#fun_array.set)
* [array.push](#fun_array.push)
* [array.remove](#fun_array.remove)
* [array.includes](#fun_array.includes)

## array.size

the function returns the number of elements in an array.

### Syntax

array.size(id) → series int

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.size example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i])
// note that changes in slice also modify original array
slice = array.slice(a, 0, 5)
array.push(slice, open)
// size was changed in slice and in original array
plot(array.size(a))
plot(array.size(slice))


```

### Returns

the number of elements in the array.

### See also

* [array.new_float](#fun_array.new_float)
* [array.sum](#fun_array.sum)
* [array.slice](#fun_array.slice)
* [array.sort](#fun_array.sort)

## array.slice

the function creates a slice from an existing array. if an object from the slice changes, the changes are applied to both the new and the original arrays.

### Syntax

array.slice(id, index\_from, index\_to) - array<type>;

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

- `index_from`

    >  (`series` `int`)
    
    >  Zero-based index at which to begin extraction.

- `index_to`

    >  (`series` `int`)
    
    >  Zero-based index before which to end extraction. the function extracts up to but not including the element with this index.

### Example


```s

//@version=5
indicator("array.slice example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i])
// take elements from 0 to 4
// *note that changes in slice also modify original array
slice = array.slice(a, 0, 5)
plot(array.sum(a) / 10)
plot(array.sum(slice) / 5)


```

### Returns

a shallow copy of an array's slice.

### See also

* [array.new_float](#fun_array.new_float)
* [array.get](#fun_array.get)
* [array.slice](#fun_array.slice)
* [array.sort](#fun_array.sort)

## array.some

Returns [true](#op_true) if at least one element of the \`id\` array is [true](#op_true), [false](#op_false) otherwise.

### Syntax

array.some(id) → series bool

### Arguments

- `id`

    >  (`bool`\[\])
    
    >  an array object.

### Remarks

this function also works with arrays of [int](#op_int) and [float](#op_float) types, in which case zero values are considered [false](#op_false), and all others [true](#op_true).

### See also

* [array.every](#fun_array.every)
* [array.get](#fun_array.get)

## array.sort

the function sorts the elements of an array.

### Syntax

array.sort(id, order) - void

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

- `order`

    >  (`simple` `sort_order`)
    
    >  the sort order: order.ascending (default) or order.descending.

### Example


```s

//@version=5
indicator("array.sort example")
a = array.new_float(0,0)
for i = 0 to 5
    array.push(a, high[i])
array.sort(a, order.descending)
if barstate.islast
    label.new(bar_index, close, str.tostring(a))


```

### See also

* [array.new_float](#fun_array.new_float)
* [array.insert](#fun_array.insert)
* [array.slice](#fun_array.slice)
* [array.reverse](#fun_array.reverse)
* [order.ascending](#var_order.ascending)
* [order.descending](#var_order.descending)

## array.sort_indices

Returns an array of indices which, when used to index the original array, will access its elements in their sorted order. it does not modify the original array.

### Syntax

array.sort_indices(id, order) - int\[\]

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

- `order`

    >  (`series` `sort_order`)
    
    >  the sort order: order.ascending or order.descending. optional. the default is order.ascending.

### Example


```s

//@version=5
indicator("array.sort_indices")
a = array.from(5, -2, 0, 9, 1)
sortedindices = array.sort_indices(a) // [1, 2, 4, 0, 3]
indexOfsmallestValue = array.get(sortedindices, 0) // 1
smallestValue = array.get(a, indexOfsmallestValue) // -2
plot(smallestValue)


```

### See also

* [array.new_float](#fun_array.new_float)
* [array.insert](#fun_array.insert)
* [array.slice](#fun_array.slice)
* [array.reverse](#fun_array.reverse)
* [order.ascending](#var_order.ascending)
* [order.descending](#var_order.descending)

## array.standardize

+1 overload

the function returns the array of standardized elements.

### syntax & Overloads

> [array.standardize(id) - float\[\]](#fun_array.standardize-0)
> [array.standardize(id) - int\[\]](#fun_array.standardize-1)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.standardize example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i])
b = array.standardize(a)
plot(array.min(b))
plot(array.max(b))


```

### Returns

the array of standardized elements.

### See also

* [array.max](#fun_array.max)
* [array.min](#fun_array.min)
* [array.mode](#fun_array.mode)
* [array.avg](#fun_array.avg)
* [array.variance](#fun_array.variance)
* [array.stdev](#fun_array.stdev)

## array.stdev

+1 overload

the function returns the standard deviation of an array's elements.

### syntax & Overloads

> [array.stdev(id, biased) → series float](#fun_array.stdev-0)
> [array.stdev(id, biased) → series int](#fun_array.stdev-1)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

- `biased`

    >  (`series` `bool`)
    
    >  Determines which estimate should be used. optional. the default is true.

### Example


```s

//@version=5
indicator("array.stdev example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i])
plot(array.stdev(a))


```

### Returns

the standard deviation of the array's elements.

### Remarks

if \`biased\` is true, function will calculate using a biased estimate of the entire population, if false - unbiased estimate of a sample.

### See also

* [array.new_float](#fun_array.new_float)
* [array.max](#fun_array.max)
* [array.min](#fun_array.min)
* [array.avg](#fun_array.avg)

## array.sum

+1 overload

the function returns the sum of an array's elements.

### syntax & Overloads

> [array.sum(id) → series float](#fun_array.sum-0)
> [array.sum(id) → series int](#fun_array.sum-1)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

### Example


```s

//@version=5
indicator("array.sum example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i])
plot(array.sum(a))


```

### Returns

the sum of the array's elements.

### See also

* [array.new_float](#fun_array.new_float)
* [array.max](#fun_array.max)
* [array.min](#fun_array.min)

## array.unshift

the function inserts the value at the beginning of the array.

### Syntax

array.unshift(id, value) - void

### Arguments

- `id`

    >  (`any` `array` `type`)
    
    >  an array object.

- `value`

    >  (`series` <`type` `of` `the` `array's` `elements`>;)
    
    >  the value to add to the start of the array.

### Example


```s

//@version=5
indicator("array.unshift example")
a = array.new_float(5, 0)
array.unshift(a, open)
plot(array.get(a, 0))


```

### See also

* [array.shift](#fun_array.shift)
* [array.set](#fun_array.set)
* [array.insert](#fun_array.insert)
* [array.remove](#fun_array.remove)
* [array.indexof](#fun_array.indexof)

## array.variance

+1 overload

the function returns the variance of an array's elements.

### syntax & Overloads

> [array.variance(id, biased) → series float](#fun_array.variance-0)
> [array.variance(id, biased) → series int](#fun_array.variance-1)

### Arguments

- `id`

    >  (`float`\[\])
    
    >  an array object.

- `biased`

    >  (`series` `bool`)
    
    >  Determines which estimate should be used. optional. the default is true.

### Example


```s

//@version=5
indicator("array.variance example")
a = array.new_float(0)
for i = 0 to 9
    array.push(a, close[i])
plot(array.variance(a))


```

### Returns

the variance of the array's elements.

### Remarks

if \`biased\` is true, function will calculate using a biased estimate of the entire population, if false - unbiased estimate of a sample.

### See also

* [array.new_float](#fun_array.new_float)
* [array.stdev](#fun_array.stdev)
* [array.min](#fun_array.min)
* [array.avg](#fun_array.avg)
* [array.covariance](#fun_array.covariance)

## barcolor

set color of bars.

### Syntax

barcolor(color, offset, editable, show_last, title, display) - void

### Arguments

- `color`

    >  (`series` `color`)
    
    >  color of bars. You can use constants like 'red' or '#ff001a' as well as complex expressions like 'close >= open ? color.green : color.red'. Required argument.

- `offset`

    >  (`series` `int`)
    
    >  shifts the color series to the left or to the right on the given number of bars. Default is 0.

- `editable`

    >  (`const` `bool`)
    
    >  if true then barcolor style will be editable in format dialog. Default is true.

- `show_last`

    >  (`input` `int`)
    
    >  if set, defines the number of bars (from the last bar back to the past) to fill on chart.

- `title`

    >  (`const` `string`)
    
    >  title of the barcolor. optional argument.

- `display`

    >  (`input` `plot`\`_simple`\`_display`)
    
    >  Controls where the barcolor is displayed. possible values are: [display.none](#var_display.none), [display.all](#var_display.all). Default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("barcolor example", overlay=true)
barcolor(close < open ? color.black : color.white)


```

### See also

* [bgcolor](#fun_bgcolor)
* [plot](#fun_plot)
* [fill](#fun_fill)

## bgcolor

Fill background of bars with specified color.

### Syntax

bgcolor(color, offset, editable, show_last, title, display) - void

### Arguments

- `color`

    >  (`series` `color`)
    
    >  color of the filled background. You can use constants like 'red' or '#ff001a' as well as complex expressions like 'close >= open ? color.green : color.red'. Required argument.

- `offset`

    >  (`series` `int`)
    
    >  shifts the color series to the left or to the right on the given number of bars. Default is 0.

- `editable`

    >  (`const` `bool`)
    
    >  if true then bgcolor style will be editable in format dialog. Default is true.

- `show_last`

    >  (`input` `int`)
    
    >  if set, defines the number of bars (from the last bar back to the past) to fill on chart.

- `title`

    >  (`const` `string`)
    
    >  title of the bgcolor. optional argument.

- `display`

    >  (`input` `plot`\`_simple`\`_display`)
    
    >  Controls where the bgcolor is displayed. possible values are: [display.none](#var_display.none), [display.all](#var_display.all). Default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("bgcolor example", overlay=true)
bgcolor(close < open ? color.new(color.red,70) : color.new(color.green, 70))


```

### See also

* [barcolor](#fun_barcolor)
* [plot](#fun_plot)
* [fill](#fun_fill)

## bool

+3 overloads

Casts na to bool

### syntax & Overloads

> [bool(x) → const bool](#fun_bool-0)
> [bool(x) → input bool](#fun_bool-1)
> [bool(x) → simple bool](#fun_bool-2)
> [bool(x) → series bool](#fun_bool-3)

### Arguments

- `x`

    >  (`const` `bool`)
    
    >  the value to convert to the specified type, usually [na](#var_na).

### Returns

the value of the argument after casting to bool.

### See also

* [float](#fun_float)
* [int](#fun_int)
* [color](#fun_color)
* [string](#fun_string)
* [line](#fun_line)
* [label](#fun_label)

## box

Casts na to box.

### Syntax

box(x) → series box

### Arguments

- `x`

    >  (`series` `box`)
    
    >  the value to convert to the specified type, usually [na](#var_na).

### Returns

the value of the argument after casting to box.

### See also

* [float](#fun_float)
* [int](#fun_int)
* [bool](#fun_bool)
* [color](#fun_color)
* [string](#fun_string)
* [line](#fun_line)
* [label](#fun_label)

## `box.copy`

Clones the box object.

### Syntax

`box.copy`(id) → series box

### Arguments

- `id`

    >  (`series` `box`)
    
    >  box object.

### Example


```s

//@version=5
indicator('Last 50 bars price ranges', overlay = true)
Lookback = 50
highest = ta.highest(Lookback)
lowest = ta.lowest(Lookback)
if barstate.islastconfirmedhistory
    var boxLast = box.new(bar_index[Lookback], highest, bar_index, lowest, bgcolor = color.new(color.green, 80))
    var boxprev = `box.copy`(boxLast)
    box.set_lefttop(boxprev, bar_index[Lookback * 2], highest[50])
    box.set_rightbottom(boxprev, bar_index[Lookback], lowest[50])
    box.set_bgcolor(boxprev, color.new(color.red, 80))
```

### See also

box.new
box.delete

## box.delete
deletes the specified box object. if it has already been deleted, does nothing.

### Syntax

box.delete(id) → void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object to delete.

### See also

box.new
## box.get_bottom
Returns the price value of the bottom border of the box.

### Syntax

box.get_bottom(id) → series float

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

### Returns

the price value.

### See also

box.new
box.set_bottom


## box.get_left
Returns the bar index or the unix time (depending on the last value used for 'xloc') of the left border of the box.

### Syntax

box.get_left(id) → series int

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

### Returns

a bar index or a unix timestamp (in milliseconds).

### See also

box.new
box.set_left


## box.get_right
Returns the bar index or the unix time (depending on the last value used for 'xloc') of the right border of the box.

### Syntax

box.get_right(id) → series int

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

### Returns

a bar index or a unix timestamp (in milliseconds).

### See also

box.new
box.set_right


## box.get_top
Returns the price value of the top border of the box.

### Syntax

box.get_top(id) → series float

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

### Returns

the price value.

### See also

box.new
box.set_top


## box.new
+1 overload
Creates a new box object.

### syntax & Overloads

box.new(top_left, bottom_right, border_color, border_width, border_style, extend, xloc, bgcolor, text, text_size, text_color, text_halign, text_valign, text_wrap, text_font_family) → series box
box.new(left, top, right, bottom, border_color, border_width, border_style, extend, xloc, bgcolor, text, text_size, text_color, text_halign, text_valign, text_wrap, text_font_family) → series box

### Arguments

- `top_left`

    >  (`chart.point`)
    
    >  a chart.point object that specifies the top-left corner location of the box.
- `bottom_right`

    >  (`chart.point`)
    
    >  a chart.point object that specifies the bottom-right corner location of the box.
- `border_color`

    >  (`series` `color`)
    
    >  color of the four borders. optional. the default is color.blue.
- `border_width`

    >  (`series` `int`)
    
    >  Width of the four borders, in pixels. optional. the default is 1 pixel.
- `border_style`

    >  (`series` `string`)
    
    >  style of the four borders. possible values: line.style_solid, line.style_dotted, line.style_dashed. optional. the default value is line.style_solid.
- `extend`

    >  (`series` `string`)
    
    >  When extend.none is used, the horizontal borders start at the left border and end at the right border. With extend.left or extend.right, the horizontal borders are extended indefinitely to the left or right of the box, respectively. With extend.both, the horizontal borders are extended on both sides. optional. the default value is extend.none.
- `xloc`

    >  (`series` `string`)
    
    >  Determines whether the arguments to 'left' and 'right' are a bar index or a time value. if xloc = xloc.bar_index, the arguments must be a bar index. if xloc = xloc.bar_time, the arguments must be a unix time. possible values: xloc.bar_index and xloc.bar_time. optional. the default is xloc.bar_index.
- `bgcolor`

    >  (`series` `color`)
    
    >  background color of the box. optional. the default is color.blue.
- `text`

    >  (`series` `string`)
    
    >  the text to be displayed inside the box. optional. the default is empty string.
- `text_size`

    >  (`series` `string`)
    
    >  the size of the text. an optional parameter, the default value is size.auto. possible values: size.auto, size.tiny, size.small, size.normal, size.large, size.huge.
- `text_color`

    >  (`series` `color`)
    
    >  the color of the text. optional. the default is color.black.
- `text_halign`

    >  (`series` `string`)
    
    >  the horizontal alignment of the box's text. optional. the default value is text.align_center. possible values: text.align_left, text.align_center, text.align_right.
- `text_valign`

    >  (`series` `string`)
    
    >  the vertical alignment of the box's text. optional. the default value is text.align_center. possible values: text.align_top, text.align_center, text.align_bottom.
- `text_wrap`

    >  (`series` `string`)
    
    >  Defines whether the text is presented in a single line, extending past the width of the box if necessary, or wrapped so every line is no wider than the box itself (and clipped by the bottom border of the box if the height of the resulting wrapped text is higher than the height of the box). optional. the default value is text.wrap_none. possible values: text.wrap_none, text.wrap_auto.
- `text_font_family`

    >  (`series` `string`)
    
    >  the font family of the text. optional. the default value is font.family_default. possible values: font.family_default, font.family_monospace.


### Example

```s
//@version=5
indicator("box.new")
var b = box.new(time, open, time + 60 * 60 * 24, close, xloc=xloc.bar_time, border_style=line.style_dashed)
box.set_lefttop(b, time, 100)
box.set_rightbottom(b, time + 60 * 60 * 24, 500)
box.set_bgcolor(b, color.green)


```

### Returns

the iD of a box object which may be used in box.set_*() and box.get_*() functions.

### See also

* [box.delete](#fun_box.delete)
* [box.get_left](#fun_box.get_left)
* [box.get_top](#fun_box.get_top)
* [box.get_right](#fun_box.get_right)
* [box.get_bottom](#fun_box.get_bottom)
* [box.set\_top\_left_point](#fun_box.set_top_left_point)
* [box.set_left](#fun_box.set_left)
* [box.set_top](#fun_box.set_top)
* [box.set\_bottom\_right_point](#fun_box.set_bottom_right_point)
* [box.set_right](#fun_box.set_right)
* [box.set_bottom](#fun_box.set_bottom)
* [box.set\_border\_color](#fun_box.set_border_color)
* [box.set_bgcolor](#fun_box.set_bgcolor)
* [box.set\_border\_width](#fun_box.set_border_width)
* [box.set\_border\_style](#fun_box.set_border_style)
* [box.set_extend](#fun_box.set_extend)

## box.set_bgcolor

sets the background color of the box.

### Syntax

box.set_bgcolor(id, color) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `color`

    >  (`series` `color`)
    
    >  New background color.

### See also

* [box.new](#fun_box.new)

## box.set\_border\_color

sets the border color of the box.

### Syntax

box.set\_border\_color(id, color) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `color`

    >  (`series` `color`)
    
    >  New border color.

### See also

* [box.new](#fun_box.new)

## box.set\_border\_style

sets the border style of the box.

### Syntax

box.set\_border\_style(id, style) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `style`

    >  (`series` `string`)
    
    >  New border style.

### See also

* [box.new](#fun_box.new)
* [line.style_solid](#var_line.style_solid)

## box.set\_border\_width

sets the border width of the box.

### Syntax

box.set\_border\_width(id, width) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `width`

    >  (`series` `int`)
    
    >  Width of the four borders, in pixels.

### See also

* [box.new](#fun_box.new)

## box.set_bottom

sets the bottom coordinate of the box.

### Syntax

box.set_bottom(id, bottom) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `bottom`

    >  (`series` `int`/`float`)
    
    >  price value of the bottom border.

### See also

* [box.new](#fun_box.new)
* [box.get_bottom](#fun_box.get_bottom)

## box.set\_bottom\_right_point

sets the bottom-right corner location of the \`id\` box to \`point\`.

### Syntax

box.set\_bottom\_right_point(id, point) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a [box](#op_box) object.

- `point`

    >  (`chart.point`)
    
    >  a [chart.point](#op_chart.point) object.

## box.set_extend

sets extending type of the border of this box object. When [extend.none](#var_extend.none) is used, the horizontal borders start at the left border and end at the right border. With [extend.left](#var_extend.left) or [extend.right](#var_extend.right), the horizontal borders are extended indefinitely to the left or right of the box, respectively. With [extend.both](#var_extend.both), the horizontal borders are extended on both sides.

### Syntax

box.set_extend(id, extend) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `extend`

    >  (`series` `string`)
    
    >  New extending type.

### See also

* [box.new](#fun_box.new)
* [extend.none](#var_extend.none)

## box.set_left

sets the left coordinate of the box.

### Syntax

box.set_left(id, left) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `left`

    >  (`series` `int`)
    
    >  bar index or bar time of the left border. Note that objects positioned using [xloc.bar_index](#var_xloc.bar_index) cannot be drawn further than 500 bars into the future.

### See also

* [box.new](#fun_box.new)
* [box.get_left](#fun_box.get_left)

## box.set_lefttop

sets the left and top coordinates of the box.

### Syntax

box.set_lefttop(id, left, top) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `left`

    >  (`series` `int`)
    
    >  bar index or bar time of the left border.

- `top`

    >  (`series` `int`/`float`)
    
    >  price value of the top border.

### See also

* [box.new](#fun_box.new)
* [box.get_left](#fun_box.get_left)
* [box.get_top](#fun_box.get_top)

## box.set_right

sets the right coordinate of the box.

### Syntax

box.set_right(id, right) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `right`

    >  (`series` `int`)
    
    >  bar index or bar time of the right border. Note that objects positioned using [xloc.bar_index](#var_xloc.bar_index) cannot be drawn further than 500 bars into the future.

### See also

* [box.new](#fun_box.new)
* [box.get_right](#fun_box.get_right)

## box.set_rightbottom

sets the right and bottom coordinates of the box.

### Syntax

box.set_rightbottom(id, right, bottom) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `right`

    >  (`series` `int`)
    
    >  bar index or bar time of the right border.

- `bottom`

    >  (`series` `int`/`float`)
    
    >  price value of the bottom border.

### See also

* [box.new](#fun_box.new)
* [box.get_right](#fun_box.get_right)
* [box.get_bottom](#fun_box.get_bottom)

## box.set_text

the function sets the text in the box.

### Syntax

box.set_text(id, text) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `text`

    >  (`series` `string`)
    
    >  the text to be displayed inside the box.

### See also

* [box.set\_text\_color](#fun_box.set_text_color)
* [box.set\_text\_size](#fun_box.set_text_size)
* [box.set\_text\_valign](#fun_box.set_text_valign)
* [box.set\_text\_halign](#fun_box.set_text_halign)

## box.set\_text\_color

the function sets the color of the text inside the box.

### Syntax

box.set\_text\_color(id, text_color) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `text_color`

    >  (`series` `color`)
    
    >  the color of the text.

### See also

* [box.set_text](#fun_box.set_text)
* [box.set\_text\_size](#fun_box.set_text_size)
* [box.set\_text\_valign](#fun_box.set_text_valign)
* [box.set\_text\_halign](#fun_box.set_text_halign)

## box.set\_text\_font_family

the function sets the font family of the text inside the box.

### Syntax

box.set\_text\_font\_family(id, text\_font_family) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `text\_font\_family`

    >  (`series` `string`)
    
    >  the font family of the text. possible values: [font.family_default](#var_font.family_default), [font.family_monospace](#var_font.family_monospace).

### Example


```s

//@version=5
indicator("Example of setting the box font")
if barstate.islastconfirmedhistory
    b = box.new(bar_index, open-ta.tr, bar_index-50, open-ta.tr*5, text="monospace")
    box.set_text_font_family(b, font.family_monospace)


```

### See also

* [box.new](#fun_box.new)
* [font.family_default](#var_font.family_default)
* [font.family_monospace](#var_font.family_monospace)

## box.set\_text\_halign

the function sets the horizontal alignment of the box's text.

### Syntax

box.set\_text\_halign(id, text_halign) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `text_halign`

    >  (`series` `string`)
    
    >  the horizontal alignment of a box's text. possible values: [text.align_left](#var_text.align_left), [text.align_center](#var_text.align_center), [text.align_right](#var_text.align_right).

### See also

* [box.set_text](#fun_box.set_text)
* [box.set\_text\_size](#fun_box.set_text_size)
* [box.set\_text\_valign](#fun_box.set_text_valign)
* [box.set\_text\_color](#fun_box.set_text_color)

## box.set\_text\_size

the function sets the size of the box's text.

### Syntax

box.set\_text\_size(id, text_size) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `text_size`

    >  (`series` `string`)
    
    >  the size of the text. possible values: [size.auto](#var_size.auto), [size.tiny](#var_size.tiny), [size.small](#var_size.small), [size.normal](#var_size.normal), [size.large](#var_size.large), [size.huge](#var_size.huge).

### See also

* [box.set_text](#fun_box.set_text)
* [box.set\_text\_color](#fun_box.set_text_color)
* [box.set\_text\_valign](#fun_box.set_text_valign)
* [box.set\_text\_halign](#fun_box.set_text_halign)

## box.set\_text\_valign

the function sets the vertical alignment of a box's text.

### Syntax

box.set\_text\_valign(id, text_valign) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `text_valign`

    >  (`series` `string`)
    
    >  the vertical alignment of the box's text. possible values: [text.align_top](#var_text.align_top), [text.align_center](#var_text.align_center), [text.align_bottom](#var_text.align_bottom).

### See also

* [box.set_text](#fun_box.set_text)
* [box.set\_text\_size](#fun_box.set_text_size)
* [box.set\_text\_color](#fun_box.set_text_color)
* [box.set\_text\_halign](#fun_box.set_text_halign)

## box.set\_text\_wrap

the function sets the mode of wrapping of the text inside the box.

### Syntax

box.set\_text\_wrap(id, text_wrap) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `text_wrap`

    >  (`series` `string`)
    
    >  the mode of the wrapping. possible values: [text.wrap_auto](#var_text.wrap_auto), [text.wrap_none](#var_text.wrap_none).

### See also

* [box.set_text](#fun_box.set_text)
* [box.set\_text\_size](#fun_box.set_text_size)
* [box.set\_text\_valign](#fun_box.set_text_valign)
* [box.set\_text\_halign](#fun_box.set_text_halign)
* [box.set\_text\_color](#fun_box.set_text_color)

## box.set_top

sets the top coordinate of the box.

### Syntax

box.set_top(id, top) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a box object.

- `top`

    >  (`series` `int`/`float`)
    
    >  price value of the top border.

### See also

* [box.new](#fun_box.new)
* [box.get_top](#fun_box.get_top)

## box.set\_top\_left_point

sets the top-left corner location of the \`id\` box to \`point\`.

### Syntax

box.set\_top\_left_point(id, point) - void

### Arguments

- `id`

    >  (`series` `box`)
    
    >  a [box](#op_box) object.

- `point`

    >  (`chart.point`)
    
    >  a [chart.point](#op_chart.point) object.

## chart.point.copy

Creates a copy of a [chart.point](#op_chart.point) object with the specified \`id\`.

### Syntax

chart.point.copy(id) - chart.point

### Arguments

- `id`

    >  (`chart.point`)
    
    >  a [chart.point](#op_chart.point) object.

## chart.point.from_index

Returns a [chart.point](#op_chart.point) object with \`index\` as its x-coordinate and \`price\` as its y-coordinate.

### Syntax

chart.point.from_index(index, price) - chart.point

### Arguments

- `index`

    >  (`series` `int`)
    
    >  the x-coordinate of the point, expressed as a bar index value.

- `price`

    >  (`series` `int`/`float`)
    
    >  the y-coordinate of the point.

### Remarks

the \`time\` field values of [chart.point](#op_chart.point) instances returned from this function will be [na](#var_na), meaning drawing objects with \`xloc\` values set to \`xloc.bar_time\` will not work with them.

## chart.point.from_time

Returns a [chart.point](#op_chart.point) object with \`time\` as its x-coordinate and \`price\` as its y-coordinate.

### Syntax

chart.point.from_time(time, price) - chart.point

### Arguments

- `time`

    >  (`series` `int`)
    
    >  the x-coordinate of the point, expressed as a unix time value.

- `price`

    >  (`series` `int`/`float`)
    
    >  the y-coordinate of the point.

### Remarks

the \`index\` field values of [chart.point](#op_chart.point) instances returned from this function will be [na](#var_na), meaning drawing objects with \`xloc\` values set to \`xloc.bar_index\` will not work with them.

## chart.point.new

Creates a new [chart.point](#op_chart.point) object with the specified \`time\`, \`index\`, and \`price\`.

### Syntax

chart.point.new(time, index, price) - chart.point

### Arguments

- `time`

    >  (`series` `int`)
    
    >  the x-coordinate of the point, expressed as a unix time value.

- `index`

    >  (`series` `int`)
    
    >  the x-coordinate of the point, expressed as a bar index value.

- `price`

    >  (`series` `int`/`float`)
    
    >  the y-coordinate of the point.

### Remarks

Whether a drawing object uses a point's \`time\` or \`index\` field as an x-coordinate depends on the \`xloc\` type used in the function call that returned the drawing.

it's important to note that this function does not verify that the \`time\` and \`index\` values refer to the same bar.

### See also

* [polyline.new](#fun_polyline.new)

## chart.point.now

Returns a [chart.point](#op_chart.point) object with \`price\` as the y-coordinate

### Syntax

chart.point.now(price) - chart.point

### Arguments

- `price`

    >  (`series` `int`/`float`)
    
    >  the y-coordinate of the point. optional. the default is [close](#var_close).

### Remarks

the [chart.point](#op_chart.point) instance returned from this function records values for its \`index\` and \`time\` fields on the bar it executed on, making it suitable for use with drawing objects of any \`xloc\` type.

## color

+3 overloads

Casts na to color

### syntax & Overloads

> [color(x) → const color](#fun_color-0)
> [color(x) → input color](#fun_color-1)
> [color(x) → simple color](#fun_color-2)
> [color(x) → series color](#fun_color-3)

### Arguments

- `x`

    >  (`const` `color`)
    
    >  the value to convert to the specified type, usually [na](#var_na).

### Returns

the value of the argument after casting to color.

### See also

* [float](#fun_float)
* [int](#fun_int)
* [bool](#fun_bool)
* [string](#fun_string)
* [line](#fun_line)
* [label](#fun_label)

## color.b

+2 overloads

Retrieves the value of the color's blue component.

### syntax & Overloads

> [color.b(color) → const float](#fun_color.b-0)
> [color.b(color) → input float](#fun_color.b-1)
> [color.b(color) → series float](#fun_color.b-2)

### Arguments

- `color`

    >  (`const` `color`)
    
    >  color.

### Example


```s

//@version=5
indicator("color.b", overlay=true)
plot(color.b(color.blue))


```

### Returns

the value (0 to 255) of the color's blue component.

## color.from_gradient

based on the relative position of value in the bottom\_value to top\_value range, the function returns a color from the gradient defined by bottom\_color to top\_color.

### Syntax

color.from\_gradient(value, bottom\_value, top\_value, bottom\_color, top_color) → series color

### Arguments

- `value`

    >  (`series` `int`/`float`)
    
    >  Value to calculate the position-dependent color.

- `bottom_value`

    >  (`series` `int`/`float`)
    
    >  bottom position value corresponding to bottom_color.

- `top_value`

    >  (`series` `int`/`float`)
    
    >  Top position value corresponding to top_color.

- `bottom_color`

    >  (`series` `color`)
    
    >  bottom position color.

- `top_color`

    >  (`series` `color`)
    
    >  Top position color.

### Example


```s

//@version=5
indicator("color.from_gradient", overlay=true)
color1 = color.from_gradient(close, low, high, color.yellow, color.lime)
color2 = color.from_gradient(ta.rsi(close, 7), 0, 100, color.rgb(255, 0, 0), color.rgb(0, 255, 0, 50))
plot(close, color=color1)
plot(ta.rsi(close,7), color=color2)


```

### Returns

a color calculated from the linear gradient between bottom\_color to top\_color.

### Remarks

using this function will have an impact on the colors displayed in the script's "settings/style" tab. see the [user Manual](https://www.tradingview.com/pine-script-docs/en/v5/concepts/colors.html#stylecolors) for more information.

## color.g

+2 overloads

Retrieves the value of the color's green component.

### syntax & Overloads

> [color.g(color) → const float](#fun_color.g-0)
> [color.g(color) → input float](#fun_color.g-1)
> [color.g(color) → series float](#fun_color.g-2)

### Arguments

- `color`

    >  (`const` `color`)
    
    >  color.

### Example


```s

//@version=5
indicator("color.g", overlay=true)
plot(color.g(color.green))


```

### Returns

the value (0 to 255) of the color's green component.

## color.new

+2 overloads

Function color applies the specified transparency to the given color.

### syntax & Overloads

> [color.new(color, transp) → const color](#fun_color.new-0)
> [color.new(color, transp) → input color](#fun_color.new-1)
> [color.new(color, transp) → series color](#fun_color.new-2)

### Arguments

- `color`

    >  (`const` `color`)
    
    >  color to apply transparency to.

- `transp`

    >  (`const` `int`/`float`)
    
    >  possible values are from 0 (not transparent) to 100 (invisible).

### Example


```s

//@version=5
indicator("color.new", overlay=true)
plot(close, color=color.new(color.red, 50))


```

### Returns

color with specified transparency.

### Remarks

using arguments that are not constants (e.g., 'simple', 'input' or 'series') will have an impact on the colors displayed in the script's "settings/style" tab. see the [user Manual](https://www.tradingview.com/pine-script-docs/en/v5/concepts/colors.html#stylecolors) for more information.

## color.r

+2 overloads

Retrieves the value of the color's red component.

### syntax & Overloads

> [color.r(color) → const float](#fun_color.r-0)
> [color.r(color) → input float](#fun_color.r-1)
> [color.r(color) → series float](#fun_color.r-2)

### Arguments

- `color`

    >  (`const` `color`)
    
    >  color.

### Example


```s

//@version=5
indicator("color.r", overlay=true)
plot(color.r(color.red))


```

### Returns

the value (0 to 255) of the color's red component.

## color.rgb

+2 overloads

Creates a new color with transparency using the RGb color model.

### syntax & Overloads

> [color.rgb(red, green, blue, transp) → const color](#fun_color.rgb-0)
> [color.rgb(red, green, blue, transp) → input color](#fun_color.rgb-1)
> [color.rgb(red, green, blue, transp) → series color](#fun_color.rgb-2)

### Arguments

- `red`

    >  (`const` `int`/`float`)
    
    >  Red color component. possible values are from 0 to 255.

- `green`

    >  (`const` `int`/`float`)
    
    >  Green color component. possible values are from 0 to 255.

- `blue`

    >  (`const` `int`/`float`)
    
    >  blue color component. possible values are from 0 to 255.

- `transp`

    >  (`const` `int`/`float`)
    
    >  optional. color transparency. possible values are from 0 (opaque) to 100 (invisible). Default value is 0.

### Example


```s

//@version=5
indicator("color.rgb", overlay=true)
plot(close, color=color.rgb(255, 0, 0, 50))


```

### Returns

color with specified transparency.

### Remarks

using arguments that are not constants (e.g., 'simple', 'input' or 'series') will have an impact on the colors displayed in the script's "settings/style" tab. see the [user Manual](https://www.tradingview.com/pine-script-docs/en/v5/concepts/colors.html#stylecolors) for more information.

## color.t

+2 overloads

Retrieves the color's transparency.

### syntax & Overloads

> [color.t(color) → const float](#fun_color.t-0)
> [color.t(color) → input float](#fun_color.t-1)
> [color.t(color) → series float](#fun_color.t-2)

### Arguments

- `color`

    >  (`const` `color`)
    
    >  color.

### Example


```s

//@version=5
indicator("color.t", overlay=true)
plot(color.t(color.new(color.red, 50)))


```

### Returns

the value (0-100) of the color's transparency.

## dayofmonth

+1 overload

### syntax & Overloads

> [dayofmonth(time) → series int](#fun_dayofmonth-0)
> [dayofmonth(time, timezone) → series int](#fun_dayofmonth-1)

### Arguments

- `time`

    >  (`series` `int`)
    
    >  unix time in milliseconds.

### Returns

Day of month (in exchange timezone) for provided unix time.

### Remarks

unix time is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

Note that this function returns the day based on the time of the bar's open. For overnight sessions (e.g. EuRusD, where Monday session starts on sunday, 17:00 uTC-4) this value can be lower by 1 than the day of the trading day.

### See also

* [dayofmonth](#var_dayofmonth)
* [time](#fun_time)
* [year](#fun_year)
* [month](#fun_month)
* [dayofweek](#fun_dayofweek)
* [hour](#fun_hour)
* [minute](#fun_minute)
* [second](#fun_second)

## dayofweek

+1 overload

### syntax & Overloads

> [dayofweek(time) → series int](#fun_dayofweek-0)
> [dayofweek(time, timezone) → series int](#fun_dayofweek-1)

### Arguments

- `time`

    >  (`series` `int`)
    
    >  unix time in milliseconds.

### Returns

Day of week (in exchange timezone) for provided unix time.

### Remarks

Note that this function returns the day based on the time of the bar's open. For overnight sessions (e.g. EuRusD, where Monday session starts on sunday, 17:00) this value can be lower by 1 than the day of the trading day.

unix time is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

### See also

* [dayofweek](#var_dayofweek)
* [time](#fun_time)
* [year](#fun_year)
* [month](#fun_month)
* [dayofmonth](#fun_dayofmonth)
* [hour](#fun_hour)
* [minute](#fun_minute)
* [second](#fun_second)

## fill

+2 overloads

Fills background between two plots or hlines with a given color.

### syntax & Overloads

> [fill(hline1, hline2, color, title, editable, fillgaps, display) - void](#fun_fill-0)
> [fill(plot1, plot2, color, title, editable, show_last, fillgaps, display) - void](#fun_fill-1)
> [fill(plot1, plot2, top\_value, bottom\_value, top\_color, bottom\_color, title, display, fillgaps, editable) - void](#fun_fill-2)

### Arguments

- `hline1`

    >  (`hline`)
    
    >  the first hline object. Required argument.

- `hline2`

    >  (`hline`)
    
    >  the second hline object. Required argument.

- `color`

    >  (`series` `color`)
    
    >  color of the background fill. You can use constants like 'color=color.red' or 'color=#ff001a' as well as complex expressions like 'color = close >= open ? color.green : color.red'. optional argument.

- `title`

    >  (`const` `string`)
    
    >  title of the created fill object. optional argument.

- `editable`

    >  (`const` `bool`)
    
    >  if true then fill style will be editable in format dialog. Default is true.

- `fillgaps`

    >  (`const` `bool`)
    
    >  Controls continuing fills on gaps, i.e., when one of the plot() calls returns an na value. When true, the last fill will continue on gaps. the default is false.

- `display`

    >  (`input` `plot`\`_simple`\`_display`)
    
    >  Controls where the fill is displayed. possible values are: [display.none](#var_display.none), [display.all](#var_display.all). Default is [display.all](#var_display.all).

> - Fill between two horizontal lines

### Example


```s

//@version=5
indicator("Fill between hlines", overlay = false)
h1 = hline(20)
h2 = hline(10)
fill(h1, h2, color = color.new(color.blue, 90))
Fill between two plots



```

### Example


```s

//@version=5
indicator("Fill between plots", overlay = true)
p1 = plot(open)
p2 = plot(close)
fill(p1, p2, color = color.new(color.green, 90))
Gradient fill between two horizontal lines



```

### Example


```s

//@version=5
indicator("Gradient Fill between hlines", overlay = false)
topVal = input.int(100)
botVal = input.int(0)
topcol = input.color(color.red)
botcol = input.color(color.blue)
topline = hline(100, color = topcol, linestyle = hline.style_solid)
botline = hline(0,   color = botcol, linestyle = hline.style_solid)
fill(topline, botline, topVal, botVal, topcol, botcol)


```

### See also

* [plot](#fun_plot)
* [barcolor](#fun_barcolor)
* [bgcolor](#fun_bgcolor)
* [hline](#fun_hline)
* [color.new](#fun_color.new)

## fixnan

+3 overloads

For a given series replaces NaN values with previous nearest non-NaN value.

### syntax & Overloads

> [fixnan(source) → series color](#fun_fixnan-0)
> [fixnan(source) → series int](#fun_fixnan-1)
> [fixnan(source) → series float](#fun_fixnan-2)
> [fixnan(source) → series bool](#fun_fixnan-3)

### Arguments

- `source`

    >  (`series` `color`)
    
    >  source used for the calculation.

### Returns

series without na gaps.

### See also

* [na](#fun_na)
* [na](#var_na)
* [nz](#fun_nz)

## float

+3 overloads

Casts na to float

### syntax & Overloads

> [float(x) → const float](#fun_float-0)
> [float(x) → input float](#fun_float-1)
> [float(x) → simple float](#fun_float-2)
> [float(x) → series float](#fun_float-3)

### Arguments

- `x`

    >  (`const` `int`/`float`)
    
    >  the value to convert to the specified type, usually [na](#var_na).

### Returns

the value of the argument after casting to float.

### See also

* [int](#fun_int)
* [bool](#fun_bool)
* [color](#fun_color)
* [string](#fun_string)
* [line](#fun_line)
* [label](#fun_label)

## hline

Renders a horizontal line at a given fixed price level.

### Syntax

hline(price, title, color, linestyle, linewidth, editable, display) - hline

### Arguments

- `price`

    >  (`input` `int`/`float`)
    
    >  price value at which the object will be rendered. Required argument.

- `title`

    >  (`const` `string`)
    
    >  title of the object.

- `color`

    >  (`input` `color`)
    
    >  color of the rendered line. Must be a constant value (not an expression). optional argument.

- `linestyle`

    >  (`input` `hline_style`)
    
    >  style of the rendered line. possible values are: [hline.style_solid](#var_hline.style_solid), [hline.style_dotted](#var_hline.style_dotted), [hline.style_dashed](#var_hline.style_dashed). optional argument.

- `linewidth`

    >  (`input` `int`)
    
    >  Width of the rendered line. Default value is 1.

- `editable`

    >  (`const` `bool`)
    
    >  if true then hline style will be editable in format dialog. Default is true.

- `display`

    >  (`input` `plot`\`_simple`\`_display`)
    
    >  Controls where the hline is displayed. possible values are: [display.none](#var_display.none), [display.all](#var_display.all). Default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("input.hline", overlay=true)
hline(3.14, title='pi', color=color.blue, linestyle=hline.style_dotted, linewidth=2)

// You may fill the background between any two hlines with a fill() function:
h1 = hline(20)
h2 = hline(10)
fill(h1, h2, color=color.new(color.green, 90))


```

### Returns

an hline object, that can be used in [fill](#fun_fill)

### See also

* [fill](#fun_fill)

## hour

+1 overload

### syntax & Overloads

> [hour(time) → series int](#fun_hour-0)
> [hour(time, timezone) → series int](#fun_hour-1)

### Arguments

- `time`

    >  (`series` `int`)
    
    >  unix time in milliseconds.

### Returns

Hour (in exchange timezone) for provided unix time.

### Remarks

unix time is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

### See also

* [hour](#var_hour)
* [time](#fun_time)
* [year](#fun_year)
* [month](#fun_month)
* [dayofmonth](#fun_dayofmonth)
* [dayofweek](#fun_dayofweek)
* [minute](#fun_minute)
* [second](#fun_second)

## indicator

this declaration statement designates the script as an indicator and sets a number of indicator-related properties.

### Syntax

indicator(title, shorttitle, overlay, format, precision, scale, max\_bars\_back, timeframe, timeframe\_gaps, explicit\_plot\_zorder, max\_lines\_count, max\_labels\_count, max\_boxes\_count, max\_polylines_count) - void

### Arguments

- `title`

    >  (`const` `string`)
    
    >  the title of the script. it is displayed on the chart when no \`shorttitle\` argument is used, and becomes the publication's default title when publishing the script.

- `shorttitle`

    >  (`const` `string`)
    
    >  the script's display name on charts. if specified, it will replace the \`title\` argument in most chart-related windows. optional. the default is the argument used for \`title\`.

- `overlay`

    >  (`const` `bool`)
    
    >  if [true](#op_true), the indicator will be displayed over the chart. if [false](#op_false), it will be added in a separate pane. optional. the default is [false](#op_false).

- `format`

    >  (`const` `string`)
    
    >  specifies the formatting of the script's displayed values. possible values: [format.inherit](#var_format.inherit), [format.price](#var_format.price), [format.volume](#var_format.volume), [format.percent](#var_format.percent). optional. the default is [format.inherit](#var_format.inherit).

- `precision`

    >  (`const` `int`)
    
    >  specifies the number of digits after the floating point of the script's displayed values. Must be a non-negative integer no greater than 16. if \`format\` is set to [format.inherit](#var_format.inherit) and \`precision\` is specified, the format will instead be set to [format.price](#var_format.price). optional. the default is inherited from the precision of the chart's symbol.

- `scale`

    >  (`const` `scale_type`)
    
    >  the price scale used. possible values: [scale.right](#var_scale.right), [scale.left](#var_scale.left), [scale.none](#var_scale.none). the [scale.none](#var_scale.none) value can only be applied in combination with \`overlay = true\`. optional. by default, the script uses the same scale as the chart.

- `max\_bars\_back`

    >  (`const` `int`)
    
    >  the length of the historical buffer the script keeps for every variable and function, which determines how many past values can be referenced using the `\[\]` history-referencing operator. the required buffer size is automatically detected by the pine script(r) runtime. using this parameter is only necessary when a runtime error occurs because automatic detection fails. More information on the underlying mechanics of the historical buffer can be found [in our Help center](https://www.tradingview.com/chart/?solution=43000587849). optional. the default is 0.

- `timeframe`

    >  (`const` `string`)
    
    >  adds multi-timeframe functionality to simple scripts. When used, a "timeframe" field will be added to the script's "settings/inputs" tab. the field's default value will be the argument supplied, whose format must conform to [timeframe string specifications](https://www.tradingview.com/pine-script-docs/en/v5/concepts/timeframes.html#timeframe-string-specifications). To specify the chart's timeframe, use an empty string or the [timeframe.period](#var_timeframe.period) variable. the parameter cannot be used with scripts using pine script(r) drawings. optional. the default is [timeframe.period](#var_timeframe.period).

- `timeframe_gaps`

    >  (`const` `bool`)
    
    >  specifies how the indicator's values are displayed on chart bars when the \`timeframe\` is higher than the chart's. if [true](#op_true), a value only appears on a chart bar when the higher \`timeframe\` value becomes available, otherwise [na](#var_na) is returned (thus a "gap" occurs). With [false](#op_false), what would otherwise be gaps are filled with the latest known value returned, avoiding [na](#var_na) values. When used, a "Gaps" checkbox will appear in the indicator's "settings/inputs" tab. optional. the default is [true](#op_true).

- `explicit\_plot\_zorder`

    >  (`const` `bool`)
    
    >  specifies the order in which the script's plots, fills, and hlines are rendered. if [true](#op_true), plots are drawn in the order in which they appear in the script's code, each newer plot being drawn above the previous ones. this only applies to \`plot*()\` functions, [fill](#fun_fill), and [hline](#fun_hline). optional. the default is [false](#op_false).

- `max\_lines\_count`

    >  (`const` `int`)
    
    >  the number of last [line](#op_line) drawings displayed. possible values: 1-500. the count is approximate; more drawings than the specified count may be displayed. optional. the default is 50.

- `max\_labels\_count`

    >  (`const` `int`)
    
    >  the number of last [label](#op_label) drawings displayed. possible values: 1-500. the count is approximate; more drawings than the specified count may be displayed. optional. the default is 50.

- `max\_boxes\_count`

    >  (`const` `int`)
    
    >  the number of last [box](#op_box) drawings displayed. possible values: 1-500. the count is approximate; more drawings than the specified count may be displayed. optional. the default is 50.

- `max\_polylines\_count`

    >  (`const` `int`)
    
    >  the number of last [polyline](#op_polyline) drawings displayed. possible values: 1-100. the count is approximate; more drawings than the specified count may be displayed. optional. the default is 50.

### Example


```s

//@version=5
indicator("My script", shorttitle="script")
plot(close)


```

### Remarks

Every indicator script must have one [indicator](#fun_indicator) call.

### See also

* [strategy](#fun_strategy)
* [library](#fun_library)

## input

+5 overloads

adds an input to the inputs tab of your script's settings, which allows you to provide configuration options to script users. this function automatically detects the type of the argument used for 'defval' and uses the corresponding input widget.

### syntax & Overloads

> [input(defval, title, tooltip, inline, group, display) → input color](#fun_input-0)
> [input(defval, title, tooltip, inline, group, display) → input string](#fun_input-1)
> [input(defval, title, tooltip, inline, group, display) → input int](#fun_input-2)
> [input(defval, title, tooltip, inline, group, display) → input float](#fun_input-3)
> [input(defval, title, inline, group, tooltip, display) → series float](#fun_input-4)
> [input(defval, title, tooltip, inline, group, display) → input bool](#fun_input-5)

### Arguments

- `defval`

    >  (`const` `int`/`float`/`bool`/`string`/`color` `or` `source-type` `built-ins`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where script users can change it. source-type built-ins are built-in series float variables that specify the source of the calculation: \`close\`, \`hlc3\`, etc.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `inline`

    >  (`const` `string`)
    
    >  Combines all the input calls using the same argument in one line. the string used as an argument is not displayed. it is only used to identify inputs belonging to the same line.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default depends on the type of the value passed to \`defval\`: [display.none](#var_display.none) for [bool](#op_bool) and [color](#op_color) values, [display.all](#var_display.all) for everything else.

### Example


```s

//@version=5
indicator("input", overlay=true)
i_switch = input(true, "On/Off")
plot(i_switch ? open : na)

i_len = input(7, "Length")
i_src = input(close, "source")
plot(ta.sma(i_src, i_len))

i_border = input(142.50, "price border")
hline(i_border)
bgcolor(close > i_border ? color.green : color.red)

i_col = input(color.red, "plot color")
plot(close, color=i_col)

i_text = input("Hello!", "Message")
l = label.new(bar_index, high, text=i_text)
label.delete(l[1])


```

### Returns

Value of input variable.

### Remarks

Result of [input](#fun_input) function always should be assigned to a variable, see examples above.

### See also

* [input.bool](#fun_input.bool)
* [input.color](#fun_input.color)
* [input.int](#fun_input.int)
* [input.float](#fun_input.float)
* [input.string](#fun_input.string)
* [input.symbol](#fun_input.symbol)
* [input.timeframe](#fun_input.timeframe)
* [input.text_area](#fun_input.text_area)
* [input.session](#fun_input.session)
* [input.source](#fun_input.source)
* [input.time](#fun_input.time)

## input.bool

adds an input to the inputs tab of your script's settings, which allows you to provide configuration options to script users. this function adds a checkmark to the script's inputs.

### Syntax

input.bool(defval, title, tooltip, inline, group, confirm, display) → input bool

### Arguments

- `defval`

    >  (`const` `bool`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where the user can change it.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `inline`

    >  (`const` `string`)
    
    >  Combines all the input calls using the same argument in one line. the string used as an argument is not displayed. it is only used to identify inputs belonging to the same line.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `confirm`

    >  (`const` `bool`)
    
    >  if true, then user will be asked to confirm input value before indicator is added to chart. Default value is false.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.none](#var_display.none).

### Example


```s

//@version=5
indicator("input.bool", overlay=true)
i_switch = input.bool(true, "On/Off")
plot(i_switch ? open : na)


```

### Returns

Value of input variable.

### Remarks

Result of [input.bool](#fun_input.bool) function always should be assigned to a variable, see examples above.

### See also

* [input.int](#fun_input.int)
* [input.float](#fun_input.float)
* [input.string](#fun_input.string)
* [input.text_area](#fun_input.text_area)
* [input.symbol](#fun_input.symbol)
* [input.timeframe](#fun_input.timeframe)
* [input.session](#fun_input.session)
* [input.source](#fun_input.source)
* [input.color](#fun_input.color)
* [input.time](#fun_input.time)
* [input](#fun_input)

## input.color

adds an input to the inputs tab of your script's settings, which allows you to provide configuration options to script users. this function adds a color picker that allows the user to select a color and transparency, either from a palette or a hex value.

### Syntax

input.color(defval, title, tooltip, inline, group, confirm, display) → input color

### Arguments

- `defval`

    >  (`const` `color`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where the user can change it.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `inline`

    >  (`const` `string`)
    
    >  Combines all the input calls using the same argument in one line. the string used as an argument is not displayed. it is only used to identify inputs belonging to the same line.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `confirm`

    >  (`const` `bool`)
    
    >  if true, then user will be asked to confirm input value before indicator is added to chart. Default value is false.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.none](#var_display.none).

### Example


```s

//@version=5
indicator("input.color", overlay=true)
i_col = input.color(color.red, "plot color")
plot(close, color=i_col)


```

### Returns

Value of input variable.

### Remarks

Result of [input.color](#fun_input.color) function always should be assigned to a variable, see examples above.

### See also

* [input.bool](#fun_input.bool)
* [input.int](#fun_input.int)
* [input.float](#fun_input.float)
* [input.string](#fun_input.string)
* [input.text_area](#fun_input.text_area)
* [input.symbol](#fun_input.symbol)
* [input.timeframe](#fun_input.timeframe)
* [input.session](#fun_input.session)
* [input.source](#fun_input.source)
* [input.time](#fun_input.time)
* [input](#fun_input)

## input.float

+1 overload

adds an input to the inputs tab of your script's settings, which allows you to provide configuration options to script users. this function adds a field for a float input to the script's inputs.

### syntax & Overloads

> [input.float(defval, title, options, tooltip, inline, group, confirm, display) → input float](#fun_input.float-0)
> [input.float(defval, title, minval, maxval, step, tooltip, inline, group, confirm, display) → input float](#fun_input.float-1)

### Arguments

- `defval`

    >  (`const` `int`/`float`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where script users can change it. When a list of values is used with the \`options\` parameter, the value must be one of them.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `options`

    >  (`tuple` `of` `const` `int`/`float` `values:` \[`val1`, `val2`, `...`\])
    
    >  a list of options to choose from a dropdown menu, separated by commas and enclosed in square brackets: \[val1, val2, ...\]. When using this parameter, the \`minval\`, \`maxval\` and \`step\` parameters cannot be used.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `inline`

    >  (`const` `string`)
    
    >  Combines all the input calls using the same argument in one line. the string used as an argument is not displayed. it is only used to identify inputs belonging to the same line.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `confirm`

    >  (`const` `bool`)
    
    >  if true, then user will be asked to confirm input value before indicator is added to chart. Default value is false.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("input.float", overlay=true)
i_angle1 = input.float(0.5, "sin angle", minval=-3.14, maxval=3.14, step=0.02)
plot(math.sin(i_angle1) > 0 ? close : open, "sin", color=color.green)

i_angle2 = input.float(0, "Cos angle", options=[-3.14, -1.57, 0, 1.57, 3.14])
plot(math.cos(i_angle2) > 0 ? close : open, "cos", color=color.red)


```

### Returns

Value of input variable.

### Remarks

Result of [input.float](#fun_input.float) function always should be assigned to a variable, see examples above.

### See also

* [input.bool](#fun_input.bool)
* [input.int](#fun_input.int)
* [input.string](#fun_input.string)
* [input.text_area](#fun_input.text_area)
* [input.symbol](#fun_input.symbol)
* [input.timeframe](#fun_input.timeframe)
* [input.session](#fun_input.session)
* [input.source](#fun_input.source)
* [input.color](#fun_input.color)
* [input.time](#fun_input.time)
* [input](#fun_input)

## input.int

+1 overload

adds an input to the inputs tab of your script's settings, which allows you to provide configuration options to script users. this function adds a field for an integer input to the script's inputs.

### syntax & Overloads

> [input.int(defval, title, options, tooltip, inline, group, confirm, display) → input int](#fun_input.int-0)
> [input.int(defval, title, minval, maxval, step, tooltip, inline, group, confirm, display) → input int](#fun_input.int-1)

### Arguments

- `defval`

    >  (`const` `int`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where script users can change it. When a list of values is used with the \`options\` parameter, the value must be one of them.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `options`

    >  (`tuple` `of` `const` `int` `values:` \[`val1`, `val2`, `...`\])
    
    >  a list of options to choose from a dropdown menu, separated by commas and enclosed in square brackets: \[val1, val2, ...\]. When using this parameter, the \`minval\`, \`maxval\` and \`step\` parameters cannot be used.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `inline`

    >  (`const` `string`)
    
    >  Combines all the input calls using the same argument in one line. the string used as an argument is not displayed. it is only used to identify inputs belonging to the same line.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `confirm`

    >  (`const` `bool`)
    
    >  if true, then user will be asked to confirm input value before indicator is added to chart. Default value is false.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("input.int", overlay=true)
i_len1 = input.int(10, "Length 1", minval=5, maxval=21, step=1)
plot(ta.sma(close, i_len1))

i_len2 = input.int(10, "Length 2", options=[5, 10, 21])
plot(ta.sma(close, i_len2))


```

### Returns

Value of input variable.

### Remarks

Result of [input.int](#fun_input.int) function always should be assigned to a variable, see examples above.

### See also

* [input.bool](#fun_input.bool)
* [input.float](#fun_input.float)
* [input.string](#fun_input.string)
* [input.text_area](#fun_input.text_area)
* [input.symbol](#fun_input.symbol)
* [input.timeframe](#fun_input.timeframe)
* [input.session](#fun_input.session)
* [input.source](#fun_input.source)
* [input.color](#fun_input.color)
* [input.time](#fun_input.time)
* [input](#fun_input)

## input.price

adds a price input to the script's "settings/inputs" tab. using \`confirm = true\` activates the interactive input mode where a price is selected by clicking on the chart.

### Syntax

input.price(defval, title, tooltip, inline, group, confirm, display) → input float

### Arguments

- `defval`

    >  (`const` `int`/`float`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where the user can change it.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `inline`

    >  (`const` `string`)
    
    >  Combines all the input calls using the same argument in one line. the string used as an argument is not displayed. it is only used to identify inputs belonging to the same line.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `confirm`

    >  (`const` `bool`)
    
    >  if true, the interactive input mode is enabled and the selection is done by clicking on the chart when the indicator is added to the chart, or by selecting the indicator and moving the selection after that. optional. the default is false.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("input.price", overlay=true)
price1 = input.price(title="Date", defval=42)
plot(price1)

price2 = input.price(54, title="Date")
plot(price2)


```

### Returns

Value of input variable.

### Remarks

When using interactive mode, a time input can be combined with a price input if both function calls use the same argument for their \`inline\` parameter.

### See also

* [input.bool](#fun_input.bool)
* [input.int](#fun_input.int)
* [input.float](#fun_input.float)
* [input.string](#fun_input.string)
* [input.text_area](#fun_input.text_area)
* [input.symbol](#fun_input.symbol)
* [input.resolution](#fun_input.resolution)
* [input.session](#fun_input.session)
* [input.source](#fun_input.source)
* [input.color](#fun_input.color)
* [input](#fun_input)

## input.session

adds an input to the inputs tab of your script's settings, which allows you to provide configuration options to script users. this function adds two dropdowns that allow the user to specify the beginning and the end of a session using the session selector and returns the result as a string.

### Syntax

input.session(defval, title, options, tooltip, inline, group, confirm, display) → input string

### Arguments

- `defval`

    >  (`const` `string`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where the user can change it. When a list of values is used with the \`options\` parameter, the value must be one of them.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `options`

    >  (`tuple` `of` `const` `string` `values:` \[`val1`, `val2`, `...`\])
    
    >  a list of options to choose from.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `inline`

    >  (`const` `string`)
    
    >  Combines all the input calls using the same argument in one line. the string used as an argument is not displayed. it is only used to identify inputs belonging to the same line.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `confirm`

    >  (`const` `bool`)
    
    >  if true, then user will be asked to confirm input value before indicator is added to chart. Default value is false.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("input.session", overlay=true)
i_sess = input.session("1300-1700", "session", options=["0930-1600", "1300-1700", "1700-2100"])
t = time(timeframe.period, i_sess)
bgcolor(time == t ? color.green : na)


```

### Returns

Value of input variable.

### Remarks

Result of [input.session](#fun_input.session) function always should be assigned to a variable, see examples above.

### See also

* [input.bool](#fun_input.bool)
* [input.int](#fun_input.int)
* [input.float](#fun_input.float)
* [input.string](#fun_input.string)
* [input.text_area](#fun_input.text_area)
* [input.symbol](#fun_input.symbol)
* [input.timeframe](#fun_input.timeframe)
* [input.source](#fun_input.source)
* [input.color](#fun_input.color)
* [input.time](#fun_input.time)
* [input](#fun_input)

## input.source

adds an input to the inputs tab of your script's settings, which allows you to provide configuration options to script users. this function adds a dropdown that allows the user to select a source for the calculation, e.g. [close](#var_close), [hl2](#var_hl2), etc. the user can also select an output from another indicator on their chart as the source.

### Syntax

input.source(defval, title, tooltip, inline, group, display) → series float

### Arguments

- `defval`

    >  (`open`/`high`/`low`/`close`/`hl2`/`hlc3`/`ohlc4`/`hlcc4`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where the user can change it.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `inline`

    >  (`const` `string`)
    
    >  Combines all the input calls using the same argument in one line. the string used as an argument is not displayed. it is only used to identify inputs belonging to the same line.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("input.source", overlay=true)
i_src = input.source(close, "source")
plot(i_src)


```

### Returns

Value of input variable.

### Remarks

Result of [input.source](#fun_input.source) function always should be assigned to a variable, see examples above.

### See also

* [input.bool](#fun_input.bool)
* [input.int](#fun_input.int)
* [input.float](#fun_input.float)
* [input.string](#fun_input.string)
* [input.text_area](#fun_input.text_area)
* [input.symbol](#fun_input.symbol)
* [input.timeframe](#fun_input.timeframe)
* [input.session](#fun_input.session)
* [input.color](#fun_input.color)
* [input.time](#fun_input.time)
* [input](#fun_input)

## input.string

adds an input to the inputs tab of your script's settings, which allows you to provide configuration options to script users. this function adds a field for a string input to the script's inputs.

### Syntax

input.string(defval, title, options, tooltip, inline, group, confirm, display) → input string

### Arguments

- `defval`

    >  (`const` `string`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where the user can change it. When a list of values is used with the \`options\` parameter, the value must be one of them.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `options`

    >  (`tuple` `of` `const` `string` `values:` \[`val1`, `val2`, `...`\])
    
    >  a list of options to choose from.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `inline`

    >  (`const` `string`)
    
    >  Combines all the input calls using the same argument in one line. the string used as an argument is not displayed. it is only used to identify inputs belonging to the same line.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `confirm`

    >  (`const` `bool`)
    
    >  if true, then user will be asked to confirm input value before indicator is added to chart. Default value is false.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("input.string", overlay=true)
i_text = input.string("Hello!", "Message")
l = label.new(bar_index, high, i_text)
label.delete(l[1])


```

### Returns

Value of input variable.

### Remarks

Result of [input.string](#fun_input.string) function always should be assigned to a variable, see examples above.

### See also

* [input.text_area](#fun_input.text_area)
* [input.bool](#fun_input.bool)
* [input.int](#fun_input.int)
* [input.float](#fun_input.float)
* [input.symbol](#fun_input.symbol)
* [input.timeframe](#fun_input.timeframe)
* [input.session](#fun_input.session)
* [input.source](#fun_input.source)
* [input.color](#fun_input.color)
* [input.time](#fun_input.time)
* [input](#fun_input)

## input.symbol

adds an input to the inputs tab of your script's settings, which allows you to provide configuration options to script users. this function adds a field that allows the user to select a specific symbol using the symbol search and returns that symbol, paired with its exchange prefix, as a string.

### Syntax

input.symbol(defval, title, tooltip, inline, group, confirm, display) → input string

### Arguments

- `defval`

    >  (`const` `string`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where the user can change it.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `inline`

    >  (`const` `string`)
    
    >  Combines all the input calls using the same argument in one line. the string used as an argument is not displayed. it is only used to identify inputs belonging to the same line.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `confirm`

    >  (`const` `bool`)
    
    >  if true, then user will be asked to confirm input value before indicator is added to chart. Default value is false.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("input.symbol", overlay=true)
i_sym = input.symbol("delL", "symbol")
s = request.security(i_sym, 'D', close)
plot(s)


```

### Returns

Value of input variable.

### Remarks

Result of [input.symbol](#fun_input.symbol) function always should be assigned to a variable, see examples above.

### See also

* [input.bool](#fun_input.bool)
* [input.int](#fun_input.int)
* [input.float](#fun_input.float)
* [input.string](#fun_input.string)
* [input.text_area](#fun_input.text_area)
* [input.timeframe](#fun_input.timeframe)
* [input.session](#fun_input.session)
* [input.source](#fun_input.source)
* [input.color](#fun_input.color)
* [input.time](#fun_input.time)
* [input](#fun_input)

## input.text_area

adds an input to the inputs tab of your script's settings, which allows you to provide configuration options to script users. this function adds a field for a multiline text input.

### Syntax

input.text_area(defval, title, tooltip, group, confirm, display) → input string

### Arguments

- `defval`

    >  (`const` `string`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where the user can change it.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `confirm`

    >  (`const` `bool`)
    
    >  if true, then user will be asked to confirm input value before indicator is added to chart. Default value is false.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.none](#var_display.none).

### Example


```s

//@version=5
indicator("input.text_area")
i_text = input.text_area(defval = "Hello
World!", title = "Message")
plot(close)


```

### Returns

Value of input variable.

### Remarks

Result of [input.text_area](#fun_input.text_area) function always should be assigned to a variable, see examples above.

### See also

* [input.string](#fun_input.string)
* [input.bool](#fun_input.bool)
* [input.int](#fun_input.int)
* [input.float](#fun_input.float)
* [input.symbol](#fun_input.symbol)
* [input.timeframe](#fun_input.timeframe)
* [input.session](#fun_input.session)
* [input.source](#fun_input.source)
* [input.color](#fun_input.color)
* [input.time](#fun_input.time)
* [input](#fun_input)

## input.time

adds a time input to the script's "settings/inputs" tab. this function adds two input widgets on the same line: one for the date and one for the time. the function returns a date/time value in unix format. using \`confirm = true\` activates the interactive input mode where a point in time is selected by clicking on the chart.

### Syntax

input.time(defval, title, tooltip, inline, group, confirm, display) → input int

### Arguments

- `defval`

    >  (`const` `int`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where the user can change it. the value can be a [timestamp](#fun_timestamp) function, but only if it uses a date argument in const string format.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `inline`

    >  (`const` `string`)
    
    >  Combines all the input calls using the same argument in one line. the string used as an argument is not displayed. it is only used to identify inputs belonging to the same line.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `confirm`

    >  (`const` `bool`)
    
    >  if true, the interactive input mode is enabled and the selection is done by clicking on the chart when the indicator is added to the chart, or by selecting the indicator and moving the selection after that. optional. the default is false.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.none](#var_display.none).

### Example


```s

//@version=5
indicator("input.time", overlay=true)
i_date = input.time(timestamp("20 Jul 2021 00:00 +0300"), "Date")
l = label.new(i_date, high, "Date", xloc=xloc.bar_time)
label.delete(l[1])


```

### Returns

Value of input variable.

### Remarks

When using interactive mode, a price input can be combined with a time input if both function calls use the same argument for their \`inline\` parameter.

### See also

* [input.bool](#fun_input.bool)
* [input.int](#fun_input.int)
* [input.float](#fun_input.float)
* [input.string](#fun_input.string)
* [input.text_area](#fun_input.text_area)
* [input.symbol](#fun_input.symbol)
* [input.timeframe](#fun_input.timeframe)
* [input.session](#fun_input.session)
* [input.source](#fun_input.source)
* [input.color](#fun_input.color)
* [input](#fun_input)

## input.timeframe

adds an input to the inputs tab of your script's settings, which allows you to provide configuration options to script users. this function adds a dropdown that allows the user to select a specific timeframe via the timeframe selector and returns it as a string. the selector includes the custom timeframes a user may have added using the chart's timeframe dropdown.

### Syntax

input.timeframe(defval, title, options, tooltip, inline, group, confirm, display) → input string

### Arguments

- `defval`

    >  (`const` `string`)
    
    >  Determines the default value of the input variable proposed in the script's "settings/inputs" tab, from where the user can change it. When a list of values is used with the \`options\` parameter, the value must be one of them.

- `title`

    >  (`const` `string`)
    
    >  title of the input. if not specified, the variable name is used as the input's title. if the title is specified, but it is empty, the name will be an empty string.

- `options`

    >  (`tuple` `of` `const` `string` `values:` \[`val1`, `val2`, `...`\])
    
    >  a list of options to choose from.

- `tooltip`

    >  (`const` `string`)
    
    >  the string that will be shown to the user when hovering over the tooltip icon.

- `inline`

    >  (`const` `string`)
    
    >  Combines all the input calls using the same argument in one line. the string used as an argument is not displayed. it is only used to identify inputs belonging to the same line.

- `group`

    >  (`const` `string`)
    
    >  Creates a header above all inputs using the same group argument string. the string is also used as the header's text.

- `confirm`

    >  (`const` `bool`)
    
    >  if true, then user will be asked to confirm input value before indicator is added to chart. Default value is false.

- `display`

    >  (`const` `plot_display`)
    
    >  Controls where the script will display the input's information, aside from within the script's settings. this option allows one to remove a specific input from the script's status line or the data Window to ensure only the most necessary inputs are displayed there. possible values: [display.none](#var_display.none), [display.data_window](#var_display.data_window), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("input.timeframe", overlay=true)
i_res = input.timeframe('D', "Resolution", options=['D', 'W', 'M'])
s = request.security("aapL", i_res, close)
plot(s)


```

### Returns

Value of input variable.

### Remarks

Result of [input.timeframe](#fun_input.timeframe) function always should be assigned to a variable, see examples above.

### See also

* [input.bool](#fun_input.bool)
* [input.int](#fun_input.int)
* [input.float](#fun_input.float)
* [input.string](#fun_input.string)
* [input.text_area](#fun_input.text_area)
* [input.symbol](#fun_input.symbol)
* [input.session](#fun_input.session)
* [input.source](#fun_input.source)
* [input.color](#fun_input.color)
* [input.time](#fun_input.time)
* [input](#fun_input)

## int

+3 overloads

Casts na or truncates float value to int

### syntax & Overloads

> [int(x) → const int](#fun_int-0)
> [int(x) → input int](#fun_int-1)
> [int(x) → simple int](#fun_int-2)
> [int(x) → series int](#fun_int-3)

### Arguments

- `x`

    >  (`const` `int`)
    
    >  the value to convert to the specified type, usually [na](#var_na).

### Returns

the value of the argument after casting to int.

### See also

* [float](#fun_float)
* [bool](#fun_bool)
* [color](#fun_color)
* [string](#fun_string)
* [line](#fun_line)
* [label](#fun_label)

## label

Casts na to label

### Syntax

label(x) → series label

### Arguments

- `x`

    >  (`series` `label`)
    
    >  the value to convert to the specified type, usually [na](#var_na).

### Returns

the value of the argument after casting to label.

### See also

* [float](#fun_float)
* [int](#fun_int)
* [bool](#fun_bool)
* [color](#fun_color)
* [string](#fun_string)
* [line](#fun_line)

## label.copy

Clones the label object.

### Syntax

label.copy(id) → series label

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

### Example


```s

//@version=5
indicator('Last 100 bars highest/lowest', overlay = true)
Lookback = 100
highest = ta.highest(Lookback)
highestbars = ta.highestbars(Lookback)
lowest = ta.lowest(Lookback)
lowestbars = ta.lowestbars(Lookback)
if barstate.islastconfirmedhistory
    var labelHigh = label.new(bar_index + highestbars, highest, str.tostring(highest), color = color.green)
    var labelLow = label.copy(labelHigh)
    label.set_xy(labelLow, bar_index + lowestbars, lowest)
    label.set_text(labelLow, str.tostring(lowest))
    label.set_color(labelLow, color.red)
    label.set_style(labelLow, label.style_label_up)

### Returns

New label iD object which may be passed to label.setXXX and label.getXXX functions.

### See also

label.new
label.delete


## label.delete
deletes the specified label object. if it has already been deleted, does nothing.

### Syntax

label.delete(id) → void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object to delete.

### See also

label.new


## label.get_text
Returns the text of this label object.

### Syntax

label.get_text(id) → series string

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.


### Example

//@version=5
indicator("label.get_text")
my_label = label.new(time, open, text="Open bar text", xloc=xloc.bar_time)
a = label.get_text(my_label)
label.new(time, close, text = a + " new", xloc=xloc.bar_time)


```

### Returns

string object containing the text of this label.

### See also

* [label.new](#fun_label.new)

## label.get_x

Returns unix time or bar index (depending on the last xloc value set) of this label's position.

### Syntax

label.get_x(id) → series int

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

### Example


```s

//@version=5
indicator("label.get_x")
my_label = label.new(time, open, text="Open bar text", xloc=xloc.bar_time)
a = label.get_x(my_label)
plot(time - label.get_x(my_label)) //draws zero plot


```

### Returns

unix timestamp (in milliseconds) or bar index.

### See also

* [label.new](#fun_label.new)

## label.get_y

Returns price of this label's position.

### Syntax

label.get_y(id) → series float

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

### Returns

Floating point value representing price.

### See also

* [label.new](#fun_label.new)

## label.new

+1 overload

Creates new label object.

### syntax & Overloads

> [label.new(point, text, xloc, yloc, color, style, textcolor, size, textalign, tooltip, text\_font\_family) → series label](#fun_label.new-0)
> [label.new(x, y, text, xloc, yloc, color, style, textcolor, size, textalign, tooltip, text\_font\_family) → series label](#fun_label.new-1)

### Arguments

- `point`

    >  (`chart.point`)
    
    >  a [chart.point](#op_chart.point) object that specifies the label's location.

- `text`

    >  (`series` `string`)
    
    >  label text. Default is empty string.

- `xloc`

    >  (`series` `string`)
    
    >  see description of **x** argument. possible values: [xloc.bar_index](#var_xloc.bar_index) and [xloc.bar_time](#var_xloc.bar_time). Default is [xloc.bar_index](#var_xloc.bar_index).

- `yloc`

    >  (`series` `string`)
    
    >  possible values are [yloc.price](#var_yloc.price), [yloc.abovebar](#var_yloc.abovebar), [yloc.belowbar](#var_yloc.belowbar). if yloc=[yloc.price](#var_yloc.price), **y** argument specifies the price of the label position. if yloc=[yloc.abovebar](#var_yloc.abovebar), label is located above bar. if yloc=[yloc.belowbar](#var_yloc.belowbar), label is located below bar. Default is [yloc.price](#var_yloc.price).

- `color`

    >  (`series` `color`)
    
    >  color of the label border and arrow

- `style`

    >  (`series` `string`)
    
    >  label style. possible values: [label.style_none](#var_label.style_none), [label.style_xcross](#var_label.style_xcross), [label.style_cross](#var_label.style_cross), [label.style_triangleup](#var_label.style_triangleup), [label.style_triangledown](#var_label.style_triangledown), [label.style_flag](#var_label.style_flag), [label.style_circle](#var_label.style_circle), [label.style_arrowup](#var_label.style_arrowup), [label.style_arrowdown](#var_label.style_arrowdown), [label.style\_label\_up](#var_label.style_label_up), [label.style\_label\_down](#var_label.style_label_down), [label.style\_label\_left](#var_label.style_label_left), [label.style\_label\_right](#var_label.style_label_right), [label.style\_label\_lower_left](#var_label.style_label_lower_left), [label.style\_label\_lower_right](#var_label.style_label_lower_right), [label.style\_label\_upper_left](#var_label.style_label_upper_left), [label.style\_label\_upper_right](#var_label.style_label_upper_right), [label.style\_label\_center](#var_label.style_label_center), [label.style_square](#var_label.style_square), [label.style_diamond](#var_label.style_diamond), [label.style\_text\_outline](#var_label.style_text_outline). Default is [label.style\_label\_down](#var_label.style_label_down).

- `textcolor`

    >  (`series` `color`)
    
    >  Text color.

- `size`

    >  (`series` `string`)
    
    >  label size. possible values: [size.auto](#var_size.auto), [size.tiny](#var_size.tiny), [size.small](#var_size.small), [size.normal](#var_size.normal), [size.large](#var_size.large), [size.huge](#var_size.huge). Default value is [size.normal](#var_size.normal).

- `textalign`

    >  (`series` `string`)
    
    >  label text alignment. possible values: [text.align_left](#var_text.align_left), [text.align_center](#var_text.align_center), [text.align_right](#var_text.align_right). Default value is [text.align_center](#var_text.align_center).

- `tooltip`

    >  (`series` `string`)
    
    >  Hover to see tooltip label.

- `text\_font\_family`

    >  (`series` `string`)
    
    >  the font family of the text. optional. the default value is [font.family_default](#var_font.family_default). possible values: [font.family_default](#var_font.family_default), [font.family_monospace](#var_font.family_monospace).

### Example


```s

//@version=5
indicator("label.new")
var label1 = label.new(bar_index, low, text="Hello, world!", style=label.style_circle)
label.set_x(label1, 0)
label.set_xloc(label1, time, xloc.bar_time)
label.set_color(label1, color.red)
label.set_size(label1, size.large)


```

### Returns

label iD object which may be passed to label.setXXX and label.getXXX functions.

### See also

* [label.delete](#fun_label.delete)
* [label.set_x](#fun_label.set_x)
* [label.set_y](#fun_label.set_y)
* [label.set_xy](#fun_label.set_xy)
* [label.set_xloc](#fun_label.set_xloc)
* [label.set_yloc](#fun_label.set_yloc)
* [label.set_color](#fun_label.set_color)
* [label.set_textcolor](#fun_label.set_textcolor)
* [label.set_style](#fun_label.set_style)
* [label.set_size](#fun_label.set_size)
* [label.set_textalign](#fun_label.set_textalign)
* [label.set_tooltip](#fun_label.set_tooltip)

## label.set_color

sets label border and arrow color.

### Syntax

label.set_color(id, color) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

- `color`

    >  (`series` `color`)
    
    >  New label border and arrow color.

### See also

* [label.new](#fun_label.new)

## label.set_point

sets the location of the \`id\` label to \`point\`.

### Syntax

label.set_point(id, point) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  a [label](#op_label) object.

- `point`

    >  (`chart.point`)
    
    >  a [chart.point](#op_chart.point) object.

## label.set_size

sets arrow and text size of the specified label object.

### Syntax

label.set_size(id, size) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

- `size`

    >  (`series` `string`)
    
    >  possible values: [size.auto](#var_size.auto), [size.tiny](#var_size.tiny), [size.small](#var_size.small), [size.normal](#var_size.normal), [size.large](#var_size.large), [size.huge](#var_size.huge). Default value is [size.auto](#var_size.auto).

### See also

* [size.auto](#var_size.auto)
* [size.tiny](#var_size.tiny)
* [size.small](#var_size.small)
* [size.normal](#var_size.normal)
* [size.large](#var_size.large)
* [size.huge](#var_size.huge)
* [label.new](#fun_label.new)

## label.set_style

sets label style.

### Syntax

label.set_style(id, style) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

- `style`

    >  (`series` `string`)
    
    >  New label style. possible values: [label.style_none](#var_label.style_none), [label.style_xcross](#var_label.style_xcross), [label.style_cross](#var_label.style_cross), [label.style_triangleup](#var_label.style_triangleup), [label.style_triangledown](#var_label.style_triangledown), [label.style_flag](#var_label.style_flag), [label.style_circle](#var_label.style_circle), [label.style_arrowup](#var_label.style_arrowup), [label.style_arrowdown](#var_label.style_arrowdown), [label.style\_label\_up](#var_label.style_label_up), [label.style\_label\_down](#var_label.style_label_down), [label.style\_label\_left](#var_label.style_label_left), [label.style\_label\_right](#var_label.style_label_right), [label.style\_label\_lower_left](#var_label.style_label_lower_left), [label.style\_label\_lower_right](#var_label.style_label_lower_right), [label.style\_label\_upper_left](#var_label.style_label_upper_left), [label.style\_label\_upper_right](#var_label.style_label_upper_right), [label.style\_label\_center](#var_label.style_label_center), [label.style_square](#var_label.style_square), [label.style_diamond](#var_label.style_diamond), [label.style\_text\_outline](#var_label.style_text_outline).

### See also

* [label.new](#fun_label.new)

## label.set_text

sets label text

### Syntax

label.set_text(id, text) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

- `text`

    >  (`series` `string`)
    
    >  New label text.

### See also

* [label.new](#fun_label.new)

## label.set\_text\_font_family

the function sets the font family of the text inside the label.

### Syntax

label.set\_text\_font\_family(id, text\_font_family) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  a label object.

- `text\_font\_family`

    >  (`series` `string`)
    
    >  the font family of the text. possible values: [font.family_default](#var_font.family_default), [font.family_monospace](#var_font.family_monospace).

### Example


```s

//@version=5
indicator("Example of setting the label font")
if barstate.islastconfirmedhistory
    l = label.new(bar_index, 0, "monospace", yloc=yloc.abovebar)
    label.set_text_font_family(l, font.family_monospace)


```

### See also

* [label.new](#fun_label.new)
* [font.family_default](#var_font.family_default)
* [font.family_monospace](#var_font.family_monospace)

## label.set_textalign

sets the alignment for the label text.

### Syntax

label.set_textalign(id, textalign) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

- `textalign`

    >  (`series` `string`)
    
    >  label text alignment. possible values: [text.align_left](#var_text.align_left), [text.align_center](#var_text.align_center), [text.align_right](#var_text.align_right).

### See also

* [text.align_left](#var_text.align_left)
* [text.align_center](#var_text.align_center)
* [text.align_right](#var_text.align_right)
* [label.new](#fun_label.new)

## label.set_textcolor

sets color of the label text.

### Syntax

label.set_textcolor(id, textcolor) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

- `textcolor`

    >  (`series` `color`)
    
    >  New text color.

### See also

* [label.new](#fun_label.new)

## label.set_tooltip

sets the tooltip text.

### Syntax

label.set_tooltip(id, tooltip) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

- `tooltip`

    >  (`series` `string`)
    
    >  Tooltip text.

### See also

* [label.new](#fun_label.new)

## label.set_x

sets bar index or bar time (depending on the xloc) of the label position.

### Syntax

label.set_x(id, x) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

- `x`

    >  (`series` `int`)
    
    >  New bar index or bar time of the label position. Note that objects positioned using [xloc.bar_index](#var_xloc.bar_index) cannot be drawn further than 500 bars into the future.

### See also

* [label.new](#fun_label.new)

## label.set_xloc

sets x-location and new bar index/time value.

### Syntax

label.set_xloc(id, x, xloc) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

- `x`

    >  (`series` `int`)
    
    >  New bar index or bar time of the label position.

- `xloc`

    >  (`series` `string`)
    
    >  New x-location value.

### See also

* [xloc.bar_index](#var_xloc.bar_index)
* [xloc.bar_time](#var_xloc.bar_time)
* [label.new](#fun_label.new)

## label.set_xy

sets bar index/time and price of the label position.

### Syntax

label.set_xy(id, x, y) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

- `x`

    >  (`series` `int`)
    
    >  New bar index or bar time of the label position. Note that objects positioned using [xloc.bar_index](#var_xloc.bar_index) cannot be drawn further than 500 bars into the future.

- `y`

    >  (`series` `int`/`float`)
    
    >  New price of the label position.

### See also

* [label.new](#fun_label.new)

## label.set_y

sets price of the label position

### Syntax

label.set_y(id, y) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

- `y`

    >  (`series` `int`/`float`)
    
    >  New price of the label position.

### See also

* [label.new](#fun_label.new)

## label.set_yloc

sets new y-location calculation algorithm.

### Syntax

label.set_yloc(id, yloc) - void

### Arguments

- `id`

    >  (`series` `label`)
    
    >  label object.

- `yloc`

    >  (`series` `string`)
    
    >  New y-location value.

### See also

* [yloc.price](#var_yloc.price)
* [yloc.abovebar](#var_yloc.abovebar)
* [yloc.belowbar](#var_yloc.belowbar)
* [label.new](#fun_label.new)

## library

Declaration statement identifying a script as a [library](https://www.tradingview.com/pine-script-docs/en/v5/concepts/libraries.html).

### Syntax

library(title, overlay) - void

### Arguments

- `title`

    >  (`const` `string`)
    
    >  the title of the library and its identifier. it cannot contain spaces, special characters or begin with a digit. it is used as the publication's default title, and to uniquely identify the library in the [import](#op_import) statement, when another script uses it. it is also used as the script's name on the chart.

- `overlay`

    >  (`const` `bool`)
    
    >  if true, the library will be added over the chart. if false, it will be added in a separate pane. optional. the default is false.

### Example


```s

//@version=5
// @description Math library
library("num_methods", overlay = true)
// Calculate "sinh()" from the float parameter `x`
export sinh(float x) =>
    (math.exp(x) - math.exp(-x)) / 2.0
plot(sinh(0))


```

### See also

* [indicator](#fun_indicator)
* [strategy](#fun_strategy)

## line

Casts na to line

### Syntax

line(x) → series line

### Arguments

- `x`

    >  (`series` `line`)
    
    >  the value to convert to the specified type, usually [na](#var_na).

### Returns

the value of the argument after casting to line.

### See also

* [float](#fun_float)
* [int](#fun_int)
* [bool](#fun_bool)
* [color](#fun_color)
* [string](#fun_string)
* [label](#fun_label)

## line.copy

Clones the line object.

### Syntax

line.copy(id) → series line

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

### Example


```s

//@version=5
indicator('Last 100 bars price range', overlay = true)
Lookback = 100
highest = ta.highest(Lookback)
lowest = ta.lowest(Lookback)
if barstate.islastconfirmedhistory
    var lineTop = line.new(bar_index[Lookback], highest, bar_index, highest, color = color.green)
    var linebottom = line.copy(lineTop)
    line.set_y1(linebottom, lowest)
    line.set_y2(linebottom, lowest)
    line.set_color(linebottom, color.red)

### Returns

New line iD object which may be passed to line.setXXX and line.getXXX functions.

### See also

line.new
line.delete


## line.delete
deletes the specified line object. if it has already been deleted, does nothing.

### Syntax

line.delete(id) → void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object to delete.

### See also

line.new


## line.get_price
Returns the price level of a line at a given bar index.

### Syntax

line.get_price(id, x) → series float

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.
- `x`

    >  (`series` `int`)
    
    >  bar index for which price is required.


### Example

//@version=5
indicator("Getprice", overlay=true)
var line l = na
if bar_index == 10
    l := line.new(0, high[5], bar_index, high)
plot(line.get_price(l, bar_index), color=color.green)


```

### Returns

price value of line 'id' at bar index 'x'.

### Remarks

the line is considered to have been created using 'extend=extend.both'.

this function can only be called for lines created using 'xloc.bar\_index'. if you try to call it for a line created with 'xloc.bar\_time', it will generate an error.

### See also

* [line.new](#fun_line.new)

## line.get_x1

Returns unix time or bar index (depending on the last xloc value set) of the first point of the line.

### Syntax

line.get_x1(id) → series int

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

### Example


```s

//@version=5
indicator("line.get_x1")
my_line = line.new(time, open, time + 60 * 60 * 24, close, xloc=xloc.bar_time)
a = line.get_x1(my_line)
plot(time - line.get_x1(my_line)) //draws zero plot


```

### Returns

unix timestamp (in milliseconds) or bar index.

### See also

* [line.new](#fun_line.new)

## line.get_x2

Returns unix time or bar index (depending on the last xloc value set) of the second point of the line.

### Syntax

line.get_x2(id) → series int

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

### Returns

unix timestamp (in milliseconds) or bar index.

### See also

* [line.new](#fun_line.new)

## line.get_y1

Returns price of the first point of the line.

### Syntax

line.get_y1(id) → series float

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

### Returns

price value.

### See also

* [line.new](#fun_line.new)

## line.get_y2

Returns price of the second point of the line.

### Syntax

line.get_y2(id) → series float

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

### Returns

price value.

### See also

* [line.new](#fun_line.new)

## line.new

+1 overload

Creates new line object.

### syntax & Overloads

> [line.new(first\_point, second\_point, xloc, extend, color, style, width) → series line](#fun_line.new-0)
> [line.new(x1, y1, x2, y2, xloc, extend, color, style, width) → series line](#fun_line.new-1)

### Arguments

- `first_point`

    >  (`chart.point`)
    
    >  a [chart.point](#op_chart.point) object that specifies the line's starting coordinate.

- `second_point`

    >  (`chart.point`)
    
    >  a [chart.point](#op_chart.point) object that specifies the line's ending coordinate.

- `xloc`

    >  (`series` `string`)
    
    >  see description of **x1** argument. possible values: [xloc.bar_index](#var_xloc.bar_index) and [xloc.bar_time](#var_xloc.bar_time). Default is [xloc.bar_index](#var_xloc.bar_index).

- `extend`

    >  (`series` `string`)
    
    >  if extend=[extend.none](#var_extend.none), draws segment starting at point (x1, y1) and ending at point (x2, y2). if extend is equal to [extend.right](#var_extend.right) or [extend.left](#var_extend.left), draws a ray starting at point (x1, y1) or (x2, y2), respectively. if extend=[extend.both](#var_extend.both), draws a straight line that goes through these points. Default value is [extend.none](#var_extend.none).

- `color`

    >  (`series` `color`)
    
    >  line color.

- `style`

    >  (`series` `string`)
    
    >  line style. possible values: [line.style_solid](#var_line.style_solid), [line.style_dotted](#var_line.style_dotted), [line.style_dashed](#var_line.style_dashed), [line.style\_arrow\_left](#var_line.style_arrow_left), [line.style\_arrow\_right](#var_line.style_arrow_right), [line.style\_arrow\_both](#var_line.style_arrow_both).

- `width`

    >  (`series` `int`)
    
    >  line width in pixels.

### Example


```s

//@version=5
indicator("line.new")
var line1 = line.new(0, low, bar_index, high, extend=extend.right)
var line2 = line.new(time, open, time + 60 * 60 * 24, close, xloc=xloc.bar_time, style=line.style_dashed)
line.set_x2(line1, 0)
line.set_xloc(line1, time, time + 60 * 60 * 24, xloc.bar_time)
line.set_color(line2, color.green)
line.set_width(line2, 5)


```

### Returns

line iD object which may be passed to line.setXXX and line.getXXX functions.

### See also

* [line.delete](#fun_line.delete)
* [line.set_x1](#fun_line.set_x1)
* [line.set_y1](#fun_line.set_y1)
* [line.set_xy1](#fun_line.set_xy1)
* [line.set_x2](#fun_line.set_x2)
* [line.set_y2](#fun_line.set_y2)
* [line.set_xy2](#fun_line.set_xy2)
* [line.set_xloc](#fun_line.set_xloc)
* [line.set_color](#fun_line.set_color)
* [line.set_extend](#fun_line.set_extend)
* [line.set_style](#fun_line.set_style)
* [line.set_width](#fun_line.set_width)

## line.set_color

sets the line color

### Syntax

line.set_color(id, color) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

- `color`

    >  (`series` `color`)
    
    >  New line color

### See also

* [line.new](#fun_line.new)

## line.set_extend

sets extending type of this line object. if extend=[extend.none](#var_extend.none), draws segment starting at point (x1, y1) and ending at point (x2, y2). if extend is equal to [extend.right](#var_extend.right) or [extend.left](#var_extend.left), draws a ray starting at point (x1, y1) or (x2, y2), respectively. if extend=[extend.both](#var_extend.both), draws a straight line that goes through these points.

### Syntax

line.set_extend(id, extend) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

- `extend`

    >  (`series` `string`)
    
    >  New extending type.

### See also

* [extend.none](#var_extend.none)
* [extend.right](#var_extend.right)
* [extend.left](#var_extend.left)
* [extend.both](#var_extend.both)
* [line.new](#fun_line.new)

## line.set\_first\_point

sets the first point of the \`id\` line to \`point\`.

### Syntax

line.set\_first\_point(id, point) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  a [line](#op_line) object.

- `point`

    >  (`chart.point`)
    
    >  a [chart.point](#op_chart.point) object.

## line.set\_second\_point

sets the second point of the \`id\` line to \`point\`.

### Syntax

line.set\_second\_point(id, point) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  a [line](#op_line) object.

- `point`

    >  (`chart.point`)
    
    >  a [chart.point](#op_chart.point) object.

## line.set_style

sets the line style

### Syntax

line.set_style(id, style) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

- `style`

    >  (`series` `string`)
    
    >  New line style.

### See also

* [line.style_solid](#var_line.style_solid)
* [line.style_dotted](#var_line.style_dotted)
* [line.style_dashed](#var_line.style_dashed)
* [line.style\_arrow\_left](#var_line.style_arrow_left)
* [line.style\_arrow\_right](#var_line.style_arrow_right)
* [line.style\_arrow\_both](#var_line.style_arrow_both)
* [line.new](#fun_line.new)

## line.set_width

sets the line width.

### Syntax

line.set_width(id, width) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

- `width`

    >  (`series` `int`)
    
    >  New line width in pixels.

### See also

* [line.new](#fun_line.new)

## line.set_x1

sets bar index or bar time (depending on the xloc) of the first point.

### Syntax

line.set_x1(id, x) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

- `x`

    >  (`series` `int`)
    
    >  bar index or bar time. Note that objects positioned using [xloc.bar_index](#var_xloc.bar_index) cannot be drawn further than 500 bars into the future.

### See also

* [line.new](#fun_line.new)

## line.set_x2

sets bar index or bar time (depending on the xloc) of the second point.

### Syntax

line.set_x2(id, x) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

- `x`

    >  (`series` `int`)
    
    >  bar index or bar time. Note that objects positioned using [xloc.bar_index](#var_xloc.bar_index) cannot be drawn further than 500 bars into the future.

### See also

* [line.new](#fun_line.new)

## line.set_xloc

sets x-location and new bar index/time values.

### Syntax

line.set_xloc(id, x1, x2, xloc) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

- `x1`

    >  (`series` `int`)
    
    >  bar index or bar time of the first point.

- `x2`

    >  (`series` `int`)
    
    >  bar index or bar time of the second point.

- `xloc`

    >  (`series` `string`)
    
    >  New x-location value.

### See also

* [xloc.bar_index](#var_xloc.bar_index)
* [xloc.bar_time](#var_xloc.bar_time)
* [line.new](#fun_line.new)

## line.set_xy1

sets bar index/time and price of the first point.

### Syntax

line.set_xy1(id, x, y) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

- `x`

    >  (`series` `int`)
    
    >  bar index or bar time. Note that objects positioned using [xloc.bar_index](#var_xloc.bar_index) cannot be drawn further than 500 bars into the future.

- `y`

    >  (`series` `int`/`float`)
    
    >  price.

### See also

* [line.new](#fun_line.new)

## line.set_xy2

sets bar index/time and price of the second point

### Syntax

line.set_xy2(id, x, y) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

- `x`

    >  (`series` `int`)
    
    >  bar index or bar time.

- `y`

    >  (`series` `int`/`float`)
    
    >  price.

### See also

* [line.new](#fun_line.new)

## line.set_y1

sets price of the first point

### Syntax

line.set_y1(id, y) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

- `y`

    >  (`series` `int`/`float`)
    
    >  price.

### See also

* [line.new](#fun_line.new)

## line.set_y2

sets price of the second point.

### Syntax

line.set_y2(id, y) - void

### Arguments

- `id`

    >  (`series` `line`)
    
    >  line object.

- `y`

    >  (`series` `int`/`float`)
    
    >  price.

### See also

* [line.new](#fun_line.new)

## linefill

Casts na to linefill.

### Syntax

linefill(x) → series linefill

### Arguments

- `x`

    >  (`series` `linefill`)
    
    >  the value to convert to the specified type, usually [na](#var_na).

### Returns

the value of the argument after casting to linefill.

### See also

* [float](#fun_float)
* [int](#fun_int)
* [bool](#fun_bool)
* [color](#fun_color)
* [string](#fun_string)
* [line](#fun_line)
* [label](#fun_label)

## linefill.delete

deletes the specified linefill object. if it has already been deleted, does nothing.

### Syntax

linefill.delete(id) - void

### Arguments

- `id`

    >  (`series` `linefill`)
    
    >  a linefill object.

## linefill.get_line1

Returns the iD of the first line used in the \`id\` linefill.

### Syntax

linefill.get_line1(id) → series line

### Arguments

- `id`

    >  (`series` `linefill`)
    
    >  a linefill object.

## linefill.get_line2

Returns the iD of the second line used in the \`id\` linefill.

### Syntax

linefill.get_line2(id) → series line

### Arguments

- `id`

    >  (`series` `linefill`)
    
    >  a linefill object.

## linefill.new

Creates a new linefill object and displays it on the chart, filling the space between \`line1\` and \`line2\` with the color specified in \`color\`.

### Syntax

linefill.new(line1, line2, color) → series linefill

### Arguments

- `line1`

    >  (`series` `line`)
    
    >  First line object.

- `line2`

    >  (`series` `line`)
    
    >  second line object.

- `color`

    >  (`series` `color`)
    
    >  the color used to fill the space between the lines.

### Returns

the iD of a linefill object that can be passed to other linefill.*() functions.

### Remarks

if any line of the two is deleted, the linefill object is also deleted. if the lines are moved (e.g. via [line.set_xy](#fun_line.set_xy) functions), the linefill object is also moved.

if both lines are extended in the same direction relative to the lines themselves (e.g. both have [extend.right](#var_extend.right) as the value of their \`extend=\` parameter), the space between line extensions will also be filled.

## linefill.set_color

the function sets the color of the linefill object passed to it.

### Syntax

linefill.set_color(id, color) - void

### Arguments

- `id`

    >  (`series` `linefill`)
    
    >  a linefill object.

- `color`

    >  (`series` `color`)
    
    >  the color of the linefill object.

## log.error

+1 overload

Converts the formatting string and value(s) into a formatted string, and sends the result to the "pine Logs" menu tagged with the "error" debug level.

the formatting string can contain literal text and one placeholder in curly braces {} for each value to be formatted. Each placeholder consists of the index of the required argument (beginning at 0) that will replace it, and an optional format specifier. the index represents the position of that argument in the function's argument list.

### syntax & Overloads

> [log.error(message) - void](#fun_log.error-0)
> [log.error(formatstring, arg0, arg1, ...) - void](#fun_log.error-1)

### Arguments

- `message`

    >  (`series` `string`)
    
    >  Log message.

### Example


```s

//@version=5
strategy("My strategy", overlay = true, margin_long = 100, margin_short = 100, process_orders_on_close = true)
bracketticksizeinput = input.int(1000, "stoploss/Take-profit distance (in ticks)")

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))
if (longCondition)
    limitLevel = close * 1.01
    log.info("Long limit order has been placed at {0}", limitLevel)
    strategy.order("My Long Entry id", strategy.long, limit = limitLevel)

    log.info("Exit orders have been placed: Take-profit at {0}, stop-loss at {1}", close)
    strategy.exit("Exit", "My Long Entry id", profit = bracketticksizeinput, loss = bracketticksizeinput)

if strategy.opentrades > 10
    log.warning("{0} positions opened in the same direction in a row. try adjusting `bracketticksizeinput`", strategy.opentrades)

last10perc = strategy.initial_capital / 10 > strategy.equity
if (last10perc and not last10perc[1])
    log.error("the strategy has lost 90% of the initial capital!")


```

### Returns

the formatted string.

### Remarks

any curly braces within an unquoted pattern must be balanced. For example, "ab {0} de" and "ab '}' de" are valid patterns, but "ab {0'}' de", "ab } de" and "''{''" are not.

the function can apply additional formatting to some values inside of the `{}`. the list of additional formatting options can be found in the EXaMpLE section of the [str.format](#fun_str.format) article.

the "pine Logs..." button is accessible from the "More" dropdown in the pine Editor and from the "More" dropdown in the status line of any script that uses \`log.*()\` functions.

## log.info

+1 overload

Converts the formatting string and value(s) into a formatted string, and sends the result to the "pine Logs" menu tagged with the "info" debug level.

the formatting string can contain literal text and one placeholder in curly braces {} for each value to be formatted. Each placeholder consists of the index of the required argument (beginning at 0) that will replace it, and an optional format specifier. the index represents the position of that argument in the function's argument list.

### syntax & Overloads

> [log.info(message) - void](#fun_log.info-0)
> [log.info(formatstring, arg0, arg1, ...) - void](#fun_log.info-1)

### Arguments

- `message`

    >  (`series` `string`)
    
    >  Log message.

### Example


```s

//@version=5
strategy("My strategy", overlay = true, margin_long = 100, margin_short = 100, process_orders_on_close = true)
bracketticksizeinput = input.int(1000, "stoploss/Take-profit distance (in ticks)")

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))
if (longCondition)
    limitLevel = close * 1.01
    log.info("Long limit order has been placed at {0}", limitLevel)
    strategy.order("My Long Entry id", strategy.long, limit = limitLevel)

    log.info("Exit orders have been placed: Take-profit at {0}, stop-loss at {1}", close)
    strategy.exit("Exit", "My Long Entry id", profit = bracketticksizeinput, loss = bracketticksizeinput)

if strategy.opentrades > 10
    log.warning("{0} positions opened in the same direction in a row. try adjusting `bracketticksizeinput`", strategy.opentrades)

last10perc = strategy.initial_capital / 10 > strategy.equity
if (last10perc and not last10perc[1])
    log.error("the strategy has lost 90% of the initial capital!")


```

### Returns

the formatted string.

### Remarks

any curly braces within an unquoted pattern must be balanced. For example, "ab {0} de" and "ab '}' de" are valid patterns, but "ab {0'}' de", "ab } de" and "''{''" are not.

the function can apply additional formatting to some values inside of the `{}`. the list of additional formatting options can be found in the EXaMpLE section of the [str.format](#fun_str.format) article.

the "pine Logs..." button is accessible from the "More" dropdown in the pine Editor and from the "More" dropdown in the status line of any script that uses \`log.*()\` functions.

## log.warning

+1 overload

Converts the formatting string and value(s) into a formatted string, and sends the result to the "pine Logs" menu tagged with the "warning" debug level.

the formatting string can contain literal text and one placeholder in curly braces {} for each value to be formatted. Each placeholder consists of the index of the required argument (beginning at 0) that will replace it, and an optional format specifier. the index represents the position of that argument in the function's argument list.

### syntax & Overloads

> [log.warning(message) - void](#fun_log.warning-0)
> [log.warning(formatstring, arg0, arg1, ...) - void](#fun_log.warning-1)

### Arguments

- `message`

    >  (`series` `string`)
    
    >  Log message.

### Example


```s

//@version=5
strategy("My strategy", overlay = true, margin_long = 100, margin_short = 100, process_orders_on_close = true)
bracketticksizeinput = input.int(1000, "stoploss/Take-profit distance (in ticks)")

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))
if (longCondition)
    limitLevel = close * 1.01
    log.info("Long limit order has been placed at {0}", limitLevel)
    strategy.order("My Long Entry id", strategy.long, limit = limitLevel)

    log.info("Exit orders have been placed: Take-profit at {0}, stop-loss at {1}", close)
    strategy.exit("Exit", "My Long Entry id", profit = bracketticksizeinput, loss = bracketticksizeinput)

if strategy.opentrades > 10
    log.warning("{0} positions opened in the same direction in a row. try adjusting `bracketticksizeinput`", strategy.opentrades)

last10perc = strategy.initial_capital / 10 > strategy.equity
if (last10perc and not last10perc[1])
    log.error("the strategy has lost 90% of the initial capital!")


```

### Returns

the formatted string.

### Remarks

any curly braces within an unquoted pattern must be balanced. For example, "ab {0} de" and "ab '}' de" are valid patterns, but "ab {0'}' de", "ab } de" and "''{''" are not.

the function can apply additional formatting to some values inside of the `{}`. the list of additional formatting options can be found in the EXaMpLE section of the [str.format](#fun_str.format) article.

the "pine Logs..." button is accessible from the "More" dropdown in the pine Editor and from the "More" dropdown in the status line of any script that uses \`log.*()\` functions.

## map.clear

Clears the map, removing all key-value pairs from it.

### Syntax

map.clear(id) - void

### Arguments

- `id`

    >  (`any` `map` `type`)
    
    >  a map object.

### Example


```s

//@version=5
indicator("map.clear example")
oddmap = map.new<int, bool>()
oddmap.put(1, true)
oddmap.put(2, false)
oddmap.put(3, true)
map.clear(oddmap)
plot(oddmap.size())


```

### See also

> [map.new<type,type>;](#fun_map.new%3Ctype,type%3E)* [map.put_all](#fun_map.put_all)
* [map.keys](#fun_map.keys)
* [map.values](#fun_map.values)
* [map.remove](#fun_map.remove)

## map.contains

Returns [true](#op_true) if the \`key\` was found in the \`id\` map, [false](#op_false) otherwise.

### Syntax

map.contains(id, key) → series bool

### Arguments

- `id`

    >  (`any` `map` `type`)
    
    >  a map object.

- `key`

    >  (`series` <`type` `of` `the` `map's` `elements`>;)
    
    >  the key to search in the map.

### Example


```s

//@version=5
indicator("map.includes example")
a = map.new<string, float>()
a.put("open", open)
p = close
if map.contains(a, "open")
    p := a.get("open")
plot(p)


```

### See also

> [map.new<type,type>;](#fun_map.new%3Ctype,type%3E)* [map.put](#fun_map.put)
* [map.keys](#fun_map.keys)
* [map.values](#fun_map.values)
* [map.size](#fun_map.size)

## map.copy

Creates a copy of an existing map.

### Syntax

map.copy(id) - map<keyType, valueType>;

### Arguments

- `id`

    >  (`any` `map` `type`)
    
    >  a map object to copy.

### Example


```s

//@version=5
indicator("map.copy example")
a = map.new<string, int>()
a.put("example", 1)
b = map.copy(a)
a := map.new<string, int>()
a.put("example", 2)
plot(a.get("example"))
plot(b.get("example"))


```

### Returns

a copy of the \`id\` map.

### See also

> [map.new<type,type>;](#fun_map.new%3Ctype,type%3E)* [map.put](#fun_map.put)
* [map.keys](#fun_map.keys)
* [map.values](#fun_map.values)
* [map.get](#fun_map.get)
* [map.size](#fun_map.size)

## map.get

Returns the value associated with the specified \`key\` in the \`id\` map.

### Syntax

map.get(id, key) - <value_type>;

### Arguments

- `id`

    >  (`any` `map` `type`)
    
    >  a map object.

- `key`

    >  (`series` <`type` `of` `the` `map's` `elements`>;)
    
    >  the key of the value to retrieve.

### Example


```s

//@version=5
indicator("map.get example")
a = map.new<int, int>()
size = 10
for i = 0 to size
    a.put(i, size-i)
plot(map.get(a, 1))


```

### See also

> [map.new<type,type>;](#fun_map.new%3Ctype,type%3E)* [map.put](#fun_map.put)
* [map.keys](#fun_map.keys)
* [map.values](#fun_map.values)
* [map.contains](#fun_map.contains)

## map.keys

Returns an array of all the keys in the \`id\` map. the resulting array is a copy and any changes to it are not reflected in the original map.

### Syntax

map.keys(id) - type\[\]

### Arguments

- `id`

    >  (`any` `map` `type`)
    
    >  a map object.

### Example


```s

//@version=5
indicator("map.keys example")
a = map.new<string, float>()
a.put("open", open)
a.put("high", high)
a.put("low", low)
a.put("close", close)
keys = map.keys(a)
ohlc = 0.0
for key in keys
    ohlc += a.get(key)
plot(ohlc/4)


```

### Remarks

maps maintain insertion order. the elements within the array returned by this function will also be in the insertion order.

### See also

> [map.new<type,type>;](#fun_map.new%3Ctype,type%3E)* [map.put](#fun_map.put)
* [map.get](#fun_map.get)
* [map.values](#fun_map.values)
* [map.size](#fun_map.size)

## map.new<type,type>;

Creates a new map object: a collection that consists of key-value pairs, where all keys are of the \`keyType\`, and all values are of the \`valueType\`.

\`keyType\` can only be a primitive type, i.e., one of the following: [int](#op_int), [float](#op_float), [bool](#op_bool), [string](#op_string), [color](#op_color).

\`valueType\` can be of any type except \`array<>\`, \`matrix<>;\`, and \`map<>\`. user-defined types are allowed, even if they have \`array<>;\`, \`matrix<>\`, or \`map<>;\` as one of their fields.

### Syntax

map.new<keyType, valueType>;() - map<keyType, valueType>;

### Example


```s

//@version=5
indicator("map.new<string, int> example")
a = map.new<string, int>()
a.put("example", 1)
label.new(bar_index, close, str.tostring(a.get("example")))


```

### Returns

the iD of a map object which may be used in other map.*() functions.

### Remarks

Each key is unique and can only appear once. When adding a new value with a key that the map already contains, that value replaces the old value associated with the key.

maps maintain insertion order. Note that the order does not change when inserting a pair with a \`key\` that's already in the map. the new pair replaces the existing pair with the \`key\` in such cases.

### See also

* [map.put](#fun_map.put)
* [map.keys](#fun_map.keys)
* [map.values](#fun_map.values)
* [map.get](#fun_map.get)
* [array.new<type>;](#fun_array.new%3Ctype%3E)

## map.put

puts a new key-value pair into the \`id\` map.

### Syntax

map.put(id, key, value) - <value_type>;

### Arguments

- `id`

    >  (`any` `map` `type`)
    
    >  a map object.

- `key`

    >  (`series` <`type` `of` `the` `map's` `elements`>;)
    
    >  the key to put into the map.

- `value`

    >  (`series` <`type` `of` `the` `map's` `elements`>;)
    
    >  the key value to put into the map.

### Example


```s

//@version=5
indicator("map.put example")
a = map.new<string, float>()
map.put(a, "first", 10)
map.put(a, "second", 15)
prevFirst = map.put(a, "first", 20)
currFirst = a.get("first")
plot(prevFirst)
plot(currFirst)


```

### Returns

the previous value associated with \`key\` if the key was already present in the map, or [na](#var_na) if the key is new.

### Remarks

maps maintain insertion order. Note that the order does not change when inserting a pair with a \`key\` that's already in the map. the new pair replaces the existing pair with the \`key\` in such cases.

### See also

> [map.new<type,type>;](#fun_map.new%3Ctype,type%3E)* [map.put_all](#fun_map.put_all)
* [map.keys](#fun_map.keys)
* [map.values](#fun_map.values)
* [map.remove](#fun_map.remove)

## map.put_all

puts all key-value pairs from the \`id2\` map into the \`id\` map.

### Syntax

map.put_all(id, id2) - void

### Arguments

- `id`

    >  (`any` `map` `type`)
    
    >  a map object to append to.

- `id2`

    >  (`any` `map` `type`)
    
    >  a map object to be appended.

### Example


```s

//@version=5
indicator("map.put_all example")
a = map.new<string, float>()
b = map.new<string, float>()
a.put("first", 10)
a.put("second", 15)
b.put("third", 20)
map.put_all(a, b)
plot(a.get("third"))


```

### See also

> [map.new<type,type>;](#fun_map.new%3Ctype,type%3E)* [map.put](#fun_map.put)
* [map.keys](#fun_map.keys)
* [map.values](#fun_map.values)
* [map.remove](#fun_map.remove)

## map.remove

Removes a key-value pair from the \`id\` map.

### Syntax

map.remove(id, key) - <value_type>;

### Arguments

- `id`

    >  (`any` `map` `type`)
    
    >  a map object.

- `key`

    >  (`series` <`type` `of` `the` `map's` `elements`>;)
    
    >  the key of the pair to remove from the map.

### Example


```s

//@version=5
indicator("map.remove example")
a = map.new<string, color>()
a.put("firstcolor", color.green)
oldcolorValue = map.remove(a, "firstcolor")
plot(close, color = oldcolorValue)


```

### Returns

the previous value associated with \`key\` if the key was present in the map, or [na](#var_na) if there was no such key.

### See also

> [map.new<type,type>;](#fun_map.new%3Ctype,type%3E)* [map.put](#fun_map.put)
* [map.keys](#fun_map.keys)
* [map.values](#fun_map.values)
* [map.clear](#fun_map.clear)

## map.size

Returns the number of key-value pairs in the \`id\` map.

### Syntax

map.size(id) → series int

### Arguments

- `id`

    >  (`any` `map` `type`)
    
    >  a map object.

### Example


```s

//@version=5
indicator("map.size example")
a = map.new<int, int>()
size = 10
for i = 0 to size
    a.put(i, size-i)
plot(map.size(a))


```

### See also

> [map.new<type,type>;](#fun_map.new%3Ctype,type%3E)* [map.put](#fun_map.put)
* [map.keys](#fun_map.keys)
* [map.values](#fun_map.values)
* [map.get](#fun_map.get)

## map.values

Returns an array of all the values in the \`id\` map. the resulting array is a copy and any changes to it are not reflected in the original map.

### Syntax

map.values(id) - type\[\]

### Arguments

- `id`

    >  (`any` `map` `type`)
    
    >  a map object.

### Example


```s

//@version=5
indicator("map.values example")
a = map.new<string, float>()
a.put("open", open)
a.put("high", high)
a.put("low", low)
a.put("close", close)
values = map.values(a)
ohlc = 0.0
for value in values
    ohlc += value
plot(ohlc/4)


```

### Remarks

maps maintain insertion order. the elements within the array returned by this function will also be in the insertion order.

### See also

> [map.new<type,type>;](#fun_map.new%3Ctype,type%3E)* [map.put](#fun_map.put)
* [map.get](#fun_map.get)
* [map.keys](#fun_map.keys)
* [map.size](#fun_map.size)

## math.abs

+7 overloads

absolute value of \`number\` is \`number\` if \`number\` >= 0, or -\`number\` otherwise.

### syntax & Overloads

> [math.abs(number) → const int](#fun_math.abs-0)
> [math.abs(number) → input int](#fun_math.abs-1)
> [math.abs(number) → const float](#fun_math.abs-2)
> [math.abs(number) → simple int](#fun_math.abs-3)
> [math.abs(number) → input float](#fun_math.abs-4)
> [math.abs(number) → series int](#fun_math.abs-5)
> [math.abs(number) → simple float](#fun_math.abs-6)
> [math.abs(number) → series float](#fun_math.abs-7)

### Arguments

- `number`

    >  (`const` `int`)
    
    >  the number to use in the calculation.

### Returns

the absolute value of \`number\`.

## math.acos

+3 overloads

the acos function returns the arccosine (in radians) of number such that cos(acos(y)) = y for y in range \[-1, 1\].

### syntax & Overloads

> [math.acos(angle) → const float](#fun_math.acos-0)
> [math.acos(angle) → input float](#fun_math.acos-1)
> [math.acos(angle) → simple float](#fun_math.acos-2)
> [math.acos(angle) → series float](#fun_math.acos-3)

### Arguments

- `angle`

    >  (`const` `int`/`float`)
    
    >  the value, in radians, to use in the calculation.

### Returns

the arc cosine of a value; the returned angle is in the range \[0, pi\], or [na](#var_na) if y is outside of range \[-1, 1\].

## math.asin

+3 overloads

the asin function returns the arcsine (in radians) of number such that sin(asin(y)) = y for y in range \[-1, 1\].

### syntax & Overloads

> [math.asin(angle) → const float](#fun_math.asin-0)
> [math.asin(angle) → input float](#fun_math.asin-1)
> [math.asin(angle) → simple float](#fun_math.asin-2)
> [math.asin(angle) → series float](#fun_math.asin-3)

### Arguments

- `angle`

    >  (`const` `int`/`float`)
    
    >  the value, in radians, to use in the calculation.

### Returns

the arcsine of a value; the returned angle is in the range \[-pi/2, pi/2\], or [na](#var_na) if y is outside of range \[-1, 1\].

## math.atan

+3 overloads

the atan function returns the arctangent (in radians) of number such that tan(atan(y)) = y for any y.

### syntax & Overloads

> [math.atan(angle) → const float](#fun_math.atan-0)
> [math.atan(angle) → input float](#fun_math.atan-1)
> [math.atan(angle) → simple float](#fun_math.atan-2)
> [math.atan(angle) → series float](#fun_math.atan-3)

### Arguments

- `angle`

    >  (`const` `int`/`float`)
    
    >  the value, in radians, to use in the calculation.

### Returns

the arc tangent of a value; the returned angle is in the range \[-pi/2, pi/2\].

## math.avg

+1 overload

Calculates average of all given series (elementwise).

### syntax & Overloads

> [math.avg(number0, number1, ...) → simple float](#fun_math.avg-0)
> [math.avg(number0, number1, ...) → series float](#fun_math.avg-1)

### Arguments

- `number0, number1, ...`

    >  (`simple` `int`/`float`)
    
    >  a sequence of numbers to use in the calculation.

### Returns

average.

### See also

* [math.sum](#fun_math.sum)
* [ta.cum](#fun_ta.cum)
* [ta.sma](#fun_ta.sma)

## math.ceil

+3 overloads

the ceil function returns the smallest (closest to negative infinity) integer that is greater than or equal to the argument.

### syntax & Overloads

> [math.ceil(number) → const int](#fun_math.ceil-0)
> [math.ceil(number) → input int](#fun_math.ceil-1)
> [math.ceil(number) → simple int](#fun_math.ceil-2)
> [math.ceil(number) → series int](#fun_math.ceil-3)

### Arguments

- `number`

    >  (`const` `int`)
    
    >  the number to use in the calculation.

### Returns

the smallest integer greater than or equal to the given number.

### See also

* [math.floor](#fun_math.floor)
* [math.round](#fun_math.round)

## math.cos

+3 overloads

the cos function returns the trigonometric cosine of an angle.

### syntax & Overloads

> [math.cos(angle) → const float](#fun_math.cos-0)
> [math.cos(angle) → input float](#fun_math.cos-1)
> [math.cos(angle) → simple float](#fun_math.cos-2)
> [math.cos(angle) → series float](#fun_math.cos-3)

### Arguments

- `angle`

    >  (`const` `int`/`float`)
    
    >  angle, in radians.

### Returns

the trigonometric cosine of an angle.

## math.exp

+3 overloads

the exp function of \`number\` is e raised to the power of \`number\`, where e is Euler's number.

### syntax & Overloads

> [math.exp(number) → const float](#fun_math.exp-0)
> [math.exp(number) → input float](#fun_math.exp-1)
> [math.exp(number) → simple float](#fun_math.exp-2)
> [math.exp(number) → series float](#fun_math.exp-3)

### Arguments

- `number`

    >  (`const` `int`/`float`)
    
    >  the number to use in the calculation.

### Returns

a value representing e raised to the power of \`number\`.

### See also

* [math.pow](#fun_math.pow)

## math.floor

+3 overloads

### syntax & Overloads

> [math.floor(number) → const int](#fun_math.floor-0)
> [math.floor(number) → input int](#fun_math.floor-1)
> [math.floor(number) → simple int](#fun_math.floor-2)
> [math.floor(number) → series int](#fun_math.floor-3)

### Arguments

- `number`

    >  (`const` `int`)
    
    >  the number to use in the calculation.

### Returns

the largest integer less than or equal to the given number.

### See also

* [math.ceil](#fun_math.ceil)
* [math.round](#fun_math.round)

## math.log

+3 overloads

Natural logarithm of any \`number\` > 0 is the unique y such that e^y = \`number\`.

### syntax & Overloads

> [math.log(number) → const float](#fun_math.log-0)
> [math.log(number) → input float](#fun_math.log-1)
> [math.log(number) → simple float](#fun_math.log-2)
> [math.log(number) → series float](#fun_math.log-3)

### Arguments

- `number`

    >  (`const` `int`/`float`)
    
    >  the number to use in the calculation.

### Returns

the natural logarithm of \`number\`.

### See also

* [math.log10](#fun_math.log10)

## math.log10

+3 overloads

the common (or base 10) logarithm of \`number\` is the power to which 10 must be raised to obtain the \`number\`. 10^y = \`number\`.

### syntax & Overloads

> [math.log10(number) → const float](#fun_math.log10-0)
> [math.log10(number) → input float](#fun_math.log10-1)
> [math.log10(number) → simple float](#fun_math.log10-2)
> [math.log10(number) → series float](#fun_math.log10-3)

### Arguments

- `number`

    >  (`const` `int`/`float`)
    
    >  the number to use in the calculation.

### Returns

the base 10 logarithm of \`number\`.

### See also

* [math.log](#fun_math.log)

## math.max

+5 overloads

Returns the greatest of multiple values.

### syntax & Overloads

> [math.max(number0, number1, ...) → input int](#fun_math.max-0)
> [math.max(number0, number1, ...) → simple int](#fun_math.max-1)
> [math.max(number0, number1, ...) → input float](#fun_math.max-2)
> [math.max(number0, number1, ...) → series int](#fun_math.max-3)
> [math.max(number0, number1, ...) → simple float](#fun_math.max-4)
> [math.max(number0, number1, ...) → series float](#fun_math.max-5)

### Arguments

- `number0, number1, ...`

    >  (`input` `int`)
    
    >  a sequence of numbers to use in the calculation.

### Example


```s

//@version=5
indicator("math.max", overlay=true)
plot(math.max(close, open))
plot(math.max(close, math.max(open, 42)))


```

### Returns

the greatest of multiple given values.

### See also

* [math.min](#fun_math.min)

## math.min

+5 overloads

Returns the smallest of multiple values.

### syntax & Overloads

> [math.min(number0, number1, ...) → input int](#fun_math.min-0)
> [math.min(number0, number1, ...) → simple int](#fun_math.min-1)
> [math.min(number0, number1, ...) → input float](#fun_math.min-2)
> [math.min(number0, number1, ...) → series int](#fun_math.min-3)
> [math.min(number0, number1, ...) → simple float](#fun_math.min-4)
> [math.min(number0, number1, ...) → series float](#fun_math.min-5)

### Arguments

- `number0, number1, ...`

    >  (`input` `int`)
    
    >  a sequence of numbers to use in the calculation.

### Example


```s

//@version=5
indicator("math.min", overlay=true)
plot(math.min(close, open))
plot(math.min(close, math.min(open, 42)))


```

### Returns

the smallest of multiple given values.

### See also

* [math.max](#fun_math.max)

## math.pow

+3 overloads

Mathematical power function.

### syntax & Overloads

> [math.pow(base, exponent) → const float](#fun_math.pow-0)
> [math.pow(base, exponent) → input float](#fun_math.pow-1)
> [math.pow(base, exponent) → simple float](#fun_math.pow-2)
> [math.pow(base, exponent) → series float](#fun_math.pow-3)

### Arguments

- `base`

    >  (`const` `int`/`float`)
    
    >  specify the base to use.

- `exponent`

    >  (`const` `int`/`float`)
    
    >  specifies the exponent.

### Example


```s

//@version=5
indicator("math.pow", overlay=true)
plot(math.pow(close, 2))


```

### Returns

\`base\` raised to the power of \`exponent\`. if \`base\` is a series, it is calculated elementwise.

### See also

* [math.sqrt](#fun_math.sqrt)
* [math.exp](#fun_math.exp)

## math.random

Returns a pseudo-random value. the function will generate a different sequence of values for each script execution. using the same value for the optional seed argument will produce a repeatable sequence.

### Syntax

math.random(min, max, seed) → series float

### Arguments

- `min`

    >  (`series` `int`/`float`)
    
    >  the lower bound of the range of random values. the value is not included in the range. the default is 0.

- `max`

    >  (`series` `int`/`float`)
    
    >  the upper bound of the range of random values. the value is not included in the range. the default is 1.

- `seed`

    >  (`simple` `int`)
    
    >  optional argument. When the same seed is used, allows successive calls to the function to produce a repeatable set of values.

### Returns

a random value.

## math.round

+7 overloads

Returns the value of \`number\` rounded to the nearest integer, with ties rounding up. if the \`precision\` parameter is used, returns a float value rounded to that amount of decimal places.

### syntax & Overloads

> [math.round(number) → const int](#fun_math.round-0)
> [math.round(number) → input int](#fun_math.round-1)
> [math.round(number) → simple int](#fun_math.round-2)
> [math.round(number) → series int](#fun_math.round-3)
> [math.round(number, precision) → const float](#fun_math.round-4)
> [math.round(number, precision) → input float](#fun_math.round-5)
> [math.round(number, precision) → simple float](#fun_math.round-6)
> [math.round(number, precision) → series float](#fun_math.round-7)

### Arguments

- `number`

    >  (`const` `int`)
    
    >  the value to be rounded.

### Returns

the value of \`number\` rounded to the nearest integer, or according to precision.

### Remarks

Note that for 'na' values function returns 'na'.

### See also

* [math.ceil](#fun_math.ceil)
* [math.floor](#fun_math.floor)

## math.round\_to\_mintick

+1 overload

Returns the value rounded to the symbol's mintick, i.e. the nearest value that can be divided by [syminfo.mintick](#var_syminfo.mintick), without the remainder, with ties rounding up.

### syntax & Overloads

> [math.round\_to\_mintick(number) → simple float](#fun_math.round_to_mintick-0)
> [math.round\_to\_mintick(number) → series float](#fun_math.round_to_mintick-1)

### Arguments

- `number`

    >  (`simple` `int`/`float`)
    
    >  the value to be rounded.

### Returns

the \`number\` rounded to tick precision.

### Remarks

Note that for 'na' values function returns 'na'.

### See also

* [math.ceil](#fun_math.ceil)
* [math.floor](#fun_math.floor)

## math.sign

+3 overloads

sign (signum) of \`number\` is zero if \`number\` is zero, 1.0 if \`number\` is greater than zero, -1.0 if \`number\` is less than zero.

### syntax & Overloads

> [math.sign(number) → const float](#fun_math.sign-0)
> [math.sign(number) → input float](#fun_math.sign-1)
> [math.sign(number) → simple float](#fun_math.sign-2)
> [math.sign(number) → series float](#fun_math.sign-3)

### Arguments

- `number`

    >  (`const` `int`/`float`)
    
    >  the number to use in the calculation.

### Returns

the sign of the argument.

## math.sin

+3 overloads

the sin function returns the trigonometric sine of an angle.

### syntax & Overloads

> [math.sin(angle) → const float](#fun_math.sin-0)
> [math.sin(angle) → input float](#fun_math.sin-1)
> [math.sin(angle) → simple float](#fun_math.sin-2)
> [math.sin(angle) → series float](#fun_math.sin-3)

### Arguments

- `angle`

    >  (`const` `int`/`float`)
    
    >  angle, in radians.

### Returns

the trigonometric sine of an angle.

## math.sqrt

+3 overloads

square root of any \`number\` >= 0 is the unique y >= 0 such that y^2 = \`number\`.

### syntax & Overloads

> [math.sqrt(number) → const float](#fun_math.sqrt-0)
> [math.sqrt(number) → input float](#fun_math.sqrt-1)
> [math.sqrt(number) → simple float](#fun_math.sqrt-2)
> [math.sqrt(number) → series float](#fun_math.sqrt-3)

### Arguments

- `number`

    >  (`const` `int`/`float`)
    
    >  the number to use in the calculation.

### Returns

the square root of \`number\`.

### See also

* [math.pow](#fun_math.pow)

## math.sum

the sum function returns the sliding sum of last y values of x.

### Syntax

math.sum(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Returns

sum of \`source\` for \`length\` bars back.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.cum](#fun_ta.cum)
* [for](#op_for)

## math.tan

+3 overloads

the tan function returns the trigonometric tangent of an angle.

### syntax & Overloads

> [math.tan(angle) → const float](#fun_math.tan-0)
> [math.tan(angle) → input float](#fun_math.tan-1)
> [math.tan(angle) → simple float](#fun_math.tan-2)
> [math.tan(angle) → series float](#fun_math.tan-3)

### Arguments

- `angle`

    >  (`const` `int`/`float`)
    
    >  angle, in radians.

### Returns

the trigonometric tangent of an angle.

## math.todegrees

Returns an approximately equivalent angle in degrees from an angle measured in radians.

### Syntax

math.todegrees(radians) → series float

### Arguments

- `radians`

    >  (`series` `int`/`float`)
    
    >  angle in radians.

### Returns

the angle value in degrees.

## math.toradians

Returns an approximately equivalent angle in radians from an angle measured in degrees.

### Syntax

math.toradians(degrees) → series float

### Arguments

- `degrees`

    >  (`series` `int`/`float`)
    
    >  angle in degrees.

### Returns

the angle value in radians.

## matrix.add_col

+1 overload

the function adds a column at the \`column\` index of the \`id\` matrix. the column can consist of \`na\` values, or an array can be used to provide values.

### syntax & Overloads

> [matrix.add_col(id, column) - void](#fun_matrix.add_col-0)
> [matrix.add\_col(id, column, array\_id) - void](#fun_matrix.add_col-1)

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `column`

    >  (`series` `int`)
    
    >  the index of the column after which the new column will be inserted. optional. the default value is [matrix.columns](#fun_matrix.columns).

> - adding a column to the matrix

### Example


```s

//@version=5
indicator("`matrix.add_col()` Example 1")

// Create a 2x3 "int" matrix containing values `0`.
m = matrix.new<int>(2, 3, 0)

// add a column  with `na` values to the matrix.
matrix.add_col(m)

// Display matrix elements.
if barstate.islastconfirmedhistory
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m))
adding an array as a column to the matrix



```

### Example


```s

//@version=5
indicator("`matrix.add_col()` Example 2")

if barstate.islastconfirmedhistory
    // Create an empty matrix object.
    var m = matrix.new<int>()

    // Create an array with values `1` and `3`.
    var a = array.from(1, 3)

    // add the `a` array as the first column of the empty matrix.
    matrix.add_col(m, 0, a)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m))


```

### Remarks

Rather than add columns to an empty matrix, it is far more efficient to declare a matrix with explicit dimensions and fill it with values. adding a column is also much slower than adding a row with the [matrix.add_row](#fun_matrix.add_row) function.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)
* [matrix.add_row](#fun_matrix.add_row)

## matrix.add_row

+1 overload

the function adds a row at the \`row\` index of the \`id\` matrix. the row can consist of \`na\` values, or an array can be used to provide values.

### syntax & Overloads

> [matrix.add_row(id, row) - void](#fun_matrix.add_row-0)
> [matrix.add\_row(id, row, array\_id) - void](#fun_matrix.add_row-1)

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `row`

    >  (`series` `int`)
    
    >  the index of the row after which the new row will be inserted. optional. the default value is [matrix.rows](#fun_matrix.rows).

> - adding a row to the matrix

### Example


```s

//@version=5
indicator("`matrix.add_row()` Example 1")

// Create a 2x3 "int" matrix containing values `0`.
m = matrix.new<int>(2, 3, 0)

// add a row with `na` values to the matrix.
matrix.add_row(m)

// Display matrix elements.
if barstate.islastconfirmedhistory
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m))
adding an array as a row to the matrix



```

### Example


```s

//@version=5
indicator("`matrix.add_row()` Example 2")

if barstate.islastconfirmedhistory
    // Create an empty matrix object.
    var m = matrix.new<int>()

    // Create an array with values `1` and `2`.
    var a = array.from(1, 2)

    // add the `a` array as the first row of the empty matrix.
    matrix.add_row(m, 0, a)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m))


```

### Remarks

indexing of rows and columns starts at zero. Rather than add rows to an empty matrix, it is far more efficient to declare a matrix with explicit dimensions and fill it with values.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)
* [matrix.add_col](#fun_matrix.add_col)

## matrix.avg

+1 overload

the function calculates the average of all elements in the matrix.

### syntax & Overloads

> [matrix.avg(id) → series float](#fun_matrix.avg-0)
> [matrix.avg(id) → series int](#fun_matrix.avg-1)

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.avg()` Example")

// Create a 2x2 matrix.
var m = matrix.new<int>(2, 2, na)
// Fill the matrix with values.
matrix.set(m, 0, 0, 1)
matrix.set(m, 0, 1, 2)
matrix.set(m, 1, 0, 3)
matrix.set(m, 1, 1, 4)

// Get the average value of the matrix.
var x = matrix.avg(m)

plot(x, 'Matrix average value')


```

### Returns

the average value from the \`id\` matrix.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)

## matrix.col

the function creates a one-dimensional array from the elements of a matrix column.

### Syntax

matrix.col(id, column) - type\[\]

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `column`

    >  (`series` `int`)
    
    >  index of the required column.

### Example


```s

//@version=5
indicator("`matrix.col()` Example", "", true)

// Create a 2x3 "float" matrix from `hlc3` values.
m = matrix.new<float>(2, 3, hlc3)

// Return an array with the values of the first column of matrix `m`.
a = matrix.col(m, 0)

// plot the first value from the array `a`.
plot(array.get(a, 0))


```

### Returns

an array iD containing the \`column\` values of the \`id\` matrix.

### Remarks

indexing of rows starts at 0.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [array.get](#fun_array.get)
* [matrix.col](#fun_matrix.col)
* [matrix.columns](#fun_matrix.columns)

## matrix.columns

the function returns the number of columns in the matrix.

### Syntax

matrix.columns(id) → series int

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.columns()` Example")

// Create a 2x6 matrix with values `0`.
var m = matrix.new<int>(2, 6, 0)

// Get the quantity of columns in matrix `m`.
var x = matrix.columns(m)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, "columns: " + str.tostring(x) + "
" + str.tostring(m))


```

### Returns

the number of columns in the matrix \`id\`.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.col](#fun_matrix.col)
* [matrix.row](#fun_matrix.row)
* [matrix.rows](#fun_matrix.rows)

## matrix.concat

the function appends the \`m2\` matrix to the \`m1\` matrix.

### Syntax

matrix.concat(id1, id2) - matrix<type>;

### Arguments

- `id1`

    >  (`any` `matrix` `type`)
    
    >  Matrix object to concatenate into.

- `id2`

    >  (`any` `matrix` `type`)
    
    >  Matrix object whose elements will be appended to \`id1\`.

### Example


```s

//@version=5
indicator("`matrix.concat()` Example")

// Create a 2x4 "int" matrix containing values `0`.
m1 = matrix.new<int>(2, 4, 0)
// Create a 2x4 "int" matrix containing values `1`.
m2 = matrix.new<int>(2, 4, 1)

// append matrix `m2` to `m1`.
matrix.concat(m1, m2)

// Display matrix elements.
if barstate.islastconfirmedhistory
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m1))


```

### Returns

Returns the \`id1\` matrix concatenated with the \`id2\` matrix.

### Remarks

the number of columns in both matrices must be identical.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)

## matrix.copy

the function creates a new matrix which is a copy of the original.

### Syntax

matrix.copy(id) - matrix<type>;

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object to copy.

### Example


```s

//@version=5
indicator("`matrix.copy()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 "float" matrix with `1` values.
    var m1 = matrix.new<float>(2, 3, 1)

    // Copy the matrix to a new one.
    // Note that unlike what `matrix.copy()` does,
    // the simple assignment operation `m2 = m1`
    // would NOT create a new copy of the `m1` matrix.
    // it would merely create a copy of its iD referencing the same matrix.
    var m2 = matrix.copy(m1)

    // Display using a table.
    var t = table.new(position.top_right, 5, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Matrix Copy:")
    table.cell(t, 1, 1, str.tostring(m2))


```

### Returns

a new matrix object of the copied \`id\` matrix.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)

## matrix.det

+1 overload

the function returns the [determinant](https://en.wikipedia.org/wiki/Determinant) of a square matrix.

### syntax & Overloads

> [matrix.det(id) → series float](#fun_matrix.det-0)
> [matrix.det(id) → series int](#fun_matrix.det-1)

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.det` Example")

// Create a 2x2 matrix.
var m = matrix.new<float>(2, 2, na)
// Fill the matrix with values.
matrix.set(m, 0, 0,  3)
matrix.set(m, 0, 1,  7)
matrix.set(m, 1, 0,  1)
matrix.set(m, 1, 1, -4)

// Get the determinant of the matrix.
var x = matrix.det(m)

plot(x, 'Matrix determinant')


```

### Returns

the determinant value of the \`id\` matrix.

### Remarks

Function calculation based on the [Lu decomposition](https://en.wikipedia.org/wiki/Lu_decomposition) algorithm.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.is_square](#fun_matrix.is_square)

## matrix.diff

+1 overload

the function returns a new matrix resulting from the subtraction between matrices \`id1\` and \`id2\`, or of matrix \`id1\` and an \`id2\` scalar (a numerical value).

### syntax & Overloads

> [matrix.diff(id1, id2) - matrix<int>;](#fun_matrix.diff-0)
> [matrix.diff(id1, id2) - matrix<float>;](#fun_matrix.diff-1)

### Arguments

- `id1`

    >  (`matrix`<`int`>;)
    
    >  Matrix to subtract from.

- `id2`

    >  (`matrix`<`int`>;)
    
    >  Matrix object or a scalar value to be subtracted.

> - Difference between two matrices

### Example


```s

//@version=5
indicator("`matrix.diff()` Example 1")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix containing values `5`.
    var m1 = matrix.new<float>(2, 3, 5)
    // Create a 2x3 matrix containing values `4`.
    var m2 = matrix.new<float>(2, 3, 4)
    // Create a new matrix containing the difference between matrices `m1` and `m2`.
    var m3 = matrix.diff(m1, m2)

    // Display using a table.
    var t = table.new(position.top_right, 1, 2, color.green)
    table.cell(t, 0, 0, "Difference between two matrices:")
    table.cell(t, 0, 1, str.tostring(m3))
Difference between a matrix and a scalar value



```

### Example


```s

//@version=5
indicator("`matrix.diff()` Example 2")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix with values `4`.
    var m1 = matrix.new<float>(2, 3, 4)

    // Create a new matrix containing the difference between the `m1` matrix and the "int" value `1`.
    var m2 = matrix.diff(m1, 1)

    // Display using a table.
    var t = table.new(position.top_right, 1, 2, color.green)
    table.cell(t,  0, 0, "Difference between a matrix and a scalar:")
    table.cell(t,  0, 1, str.tostring(m2))


```

### Returns

a new matrix object containing the difference between \`id2\` and \`id1\`.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)

## matrix.eigenvalues

+1 overload

the function returns an array containing the [eigenvalues](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors) of a square matrix.

### syntax & Overloads

> [matrix.eigenvalues(id) - float\[\]](#fun_matrix.eigenvalues-0)
> [matrix.eigenvalues(id) - int\[\]](#fun_matrix.eigenvalues-1)

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.eigenvalues()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 2)
    matrix.set(m1, 0, 1, 4)
    matrix.set(m1, 1, 0, 6)
    matrix.set(m1, 1, 1, 8)

    // Get the eigenvalues of the matrix.
    tr = matrix.eigenvalues(m1)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "array of Eigenvalues:")
    table.cell(t, 1, 1, str.tostring(tr))


```

### Returns

an array containing the eigenvalues of the \`id\` matrix.

### Remarks

the function is calculated using "the implicit qL algorithm".

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.eigenvectors](#fun_matrix.eigenvectors)

## matrix.eigenvectors

+1 overload

Returns a matrix of [eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors), in which each column is an eigenvector of the \`id\` matrix.

### syntax & Overloads

> [matrix.eigenvectors(id) - matrix<float>;](#fun_matrix.eigenvectors-0)
> [matrix.eigenvectors(id) - matrix<int>;](#fun_matrix.eigenvectors-1)

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.eigenvectors()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix
    var m1 = matrix.new<int>(2, 2, 1)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 2)
    matrix.set(m1, 0, 1, 4)
    matrix.set(m1, 1, 0, 6)
    matrix.set(m1, 1, 1, 8)

    // Get the eigenvectors of the matrix.
    m2 = matrix.eigenvectors(m1)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Matrix Eigenvectors:")
    table.cell(t, 1, 1, str.tostring(m2))


```

### Returns

a new matrix containing the eigenvectors of the \`id\` matrix.

### Remarks

the function is calculated using "the implicit qL algorithm".

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.eigenvalues](#fun_matrix.eigenvalues)

## matrix.elements_count

the function returns the total number of all matrix elements.

### Syntax

matrix.elements_count(id) → series int

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)

## matrix.fill

the function fills a rectangular area of the \`id\` matrix defined by the indices \`from\_column\` to \`to\_column\` (not including it) and \`from\_row\` to \`to\_row\`(not including it) with the \`value\`.

### Syntax

matrix.fill(id, value, from\_row, to\_row, from\_column, to\_column) - void

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `value`

    >  (`series` <`type` `of` `the` `matrix's` `elements`>;)
    
    >  the value to fill with.

- `from_row`

    >  (`series` `int`)
    
    >  Row index from which the fill will begin (inclusive). optional. the default value is 0.

- `to_row`

    >  (`series` `int`)
    
    >  Row index where the fill will end (not inclusive). optional. the default value is [matrix.rows](#fun_matrix.rows).

- `from_column`

    >  (`series` `int`)
    
    >  column index from which the fill will begin (inclusive). optional. the default value is 0.

- `to_column`

    >  (`series` `int`)
    
    >  column index where the fill will end (non inclusive). optional. the default value is [matrix.columns](#fun_matrix.columns).

### Example


```s

//@version=5
indicator("`matrix.fill()` Example")

// Create a 4x5 "int" matrix containing values `0`.
m = matrix.new<float>(4, 5, 0)

// Fill the intersection of rows 1 to 2 and columns 2 to 3 of the matrix with `hl2` values.
matrix.fill(m, hl2, 0, 2, 1, 3)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m))


```

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)

## matrix.get

the function returns the element with the specified index of the matrix.

### Syntax

matrix.get(id, row, column) - <matrix_type>;

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `row`

    >  (`series` `int`)
    
    >  index of the required row.

- `column`

    >  (`series` `int`)
    
    >  index of the required column.

### Example


```s

//@version=5
indicator("`matrix.get()` Example", "", true)

// Create a 2x3 "float" matrix from the `hl2` values.
m = matrix.new<float>(2, 3, hl2)

// Return the value of the element at index [0, 0] of matrix `m`.
x = matrix.get(m, 0, 0)

plot(x)


```

### Returns

the value of the element at the \`row\` and \`column\` index of the \`id\` matrix.

### Remarks

indexing of the rows and columns starts at zero.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)

## matrix.inv

+1 overload

the function returns the [inverse](https://en.wikipedia.org/wiki/invertible_matrix) of a square matrix.

### syntax & Overloads

> [matrix.inv(id) - matrix<float>;](#fun_matrix.inv-0)
> [matrix.inv(id) - matrix<int>;](#fun_matrix.inv-1)

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.inv()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // inverse of the matrix.
    var m2 = matrix.inv(m1)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "inverse matrix:")
    table.cell(t, 1, 1, str.tostring(m2))


```

### Returns

a new matrix, which is the inverse of the \`id\` matrix.

### Remarks

the function is calculated using the [Lu decomposition](https://en.wikipedia.org/wiki/Lu_decomposition) algorithm.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.pinv](#fun_matrix.pinv)
* [matrix.copy](#fun_matrix.copy)
* [str.tostring](#fun_str.tostring)

## matrix.is_antidiagonal

the function determines if the matrix is [anti-diagonal](https://en.wikipedia.org/wiki/anti-diagonal_matrix) (all elements outside the secondary diagonal are zero).

### Syntax

matrix.is_antidiagonal(id) → series bool

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  Matrix object to test.

### Returns

Returns true if the \`id\` matrix is &ZeroWidthspace;&ZeroWidthspace;anti-diagonal, false otherwise.

### Remarks

Returns false with non-square matrices.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.is_square](#fun_matrix.is_square)
* [matrix.is_identity](#fun_matrix.is_identity)
* [matrix.is_diagonal](#fun_matrix.is_diagonal)

## matrix.is_antisymmetric

the function determines if a matrix is [antisymmetric](https://en.wikipedia.org/wiki/skew-symmetric_matrix) (its [transpose](https://en.wikipedia.org/wiki/transpose) equals its negative).

### Syntax

matrix.is_antisymmetric(id) → series bool

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  Matrix object to test.

### Returns

Returns true, if the \`id\` matrix is antisymmetric, false otherwise.

### Remarks

Returns false with non-square matrices.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.is_square](#fun_matrix.is_square)

## matrix.is_binary

the function determines if the matrix is [binary](https://en.wikipedia.org/wiki/Logical_matrix) (when all elements of the matrix are 0 or 1).

### Syntax

matrix.is_binary(id) → series bool

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  Matrix object to test.

### Returns

Returns true if the \`id\` matrix is binary, false otherwise.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)

## matrix.is_diagonal

the function determines if the matrix is [diagonal](https://en.wikipedia.org/wiki/Diagonal_matrix) (all elements outside the main diagonal are zero).

### Syntax

matrix.is_diagonal(id) → series bool

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  Matrix object to test.

### Returns

Returns true if the \`id\` matrix is diagonal, false otherwise.

### Remarks

Returns false with non-square matrices.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.is_square](#fun_matrix.is_square)
* [matrix.is_identity](#fun_matrix.is_identity)
* [matrix.is_antidiagonal](#fun_matrix.is_antidiagonal)

## matrix.is_identity

the function determines if a matrix is an [identity matrix](https://en.wikipedia.org/wiki/identity_matrix) (elements with ones on the [main diagonal](https://en.wikipedia.org/wiki/main_diagonal) and zeros elsewhere).

### Syntax

matrix.is_identity(id) → series bool

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  Matrix object to test.

### Returns

Returns true if \`id\` is an identity matrix, false otherwise.

### Remarks

Returns false with non-square matrices.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.is_square](#fun_matrix.is_square)
* [matrix.is_diagonal](#fun_matrix.is_diagonal)

## matrix.is_square

the function determines if the matrix is [square](https://en.wikipedia.org/wiki/square_matrix) (it has the same number of rows and columns).

### Syntax

matrix.is_square(id) → series bool

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  Matrix object to test.

### Returns

Returns true if the \`id\` matrix is square, false otherwise.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)

## matrix.is_stochastic

the function determines if the matrix is [stochastic](https://en.wikipedia.org/wiki/stochastic_matrix).

### Syntax

matrix.is_stochastic(id) → series bool

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  Matrix object to test.

### Returns

Returns true if the \`id\` matrix is stochastic, false otherwise.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)

## matrix.is_symmetric

the function determines if a [square matrix](https://en.wikipedia.org/wiki/square_matrix) is [symmetric](https://en.wikipedia.org/wiki/symmetric_matrix) (elements are symmetric with respect to the [main diagonal](https://en.wikipedia.org/wiki/main_diagonal)).

### Syntax

matrix.is_symmetric(id) → series bool

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  Matrix object to test.

### Returns

Returns true if the \`id\` matrix is symmetric, false otherwise.

### Remarks

Returns false with non-square matrices.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.is_square](#fun_matrix.is_square)

## matrix.is_triangular

the function determines if the matrix is [triangular](https://en.wikipedia.org/wiki/triangular_matrix) (if all elements above or below the [main diagonal](https://en.wikipedia.org/wiki/main_diagonal) are zero).

### Syntax

matrix.is_triangular(id) → series bool

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  Matrix object to test.

### Returns

Returns true if the \`id\` matrix is triangular, false otherwise.

### Remarks

Returns false with non-square matrices.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.is_square](#fun_matrix.is_square)

## matrix.is_zero

the function determines if all elements of the matrix are zero.

### Syntax

matrix.is_zero(id) → series bool

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  Matrix object to check.

### Returns

Returns true if all elements of the \`id\` matrix are zero, false otherwise.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)

## matrix.kron

+1 overload

the function returns the [Kronecker product](https://en.wikipedia.org/wiki/Kronecker_product) for the \`id1\` and \`id2\` matrices.

### syntax & Overloads

> [matrix.kron(id1, id2) - matrix<float>;](#fun_matrix.kron-0)
> [matrix.kron(id1, id2) - matrix<int>;](#fun_matrix.kron-1)

### Arguments

- `id1`

    >  (`matrix`<`float`>;)
    
    >  First matrix object.

- `id2`

    >  (`matrix`<`float`>;)
    
    >  second matrix object.

### Example


```s

//@version=5
indicator("`matrix.kron()` Example")

// Display using a table.
if barstate.islastconfirmedhistory
    // Create two matrices with default values `1` and `2`.
    var m1 = matrix.new<float>(2, 2, 1)
    var m2 = matrix.new<float>(2, 2, 2)

    // Calculate the Kronecker product of the matrices.
    var m3 = matrix.kron(m1, m2)

    // Display matrix elements.
    var t = table.new(position.top_right, 5, 2, color.green)
    table.cell(t, 0, 0, "Matrix 1:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 1, "aS--")
    table.cell(t, 2, 0, "Matrix 2:")
    table.cell(t, 2, 1, str.tostring(m2))
    table.cell(t, 3, 1, "=")
    table.cell(t, 4, 0, "Kronecker product:")
    table.cell(t, 4, 1, str.tostring(m3))


```

### Returns

a new matrix containing the [Kronecker product](https://en.wikipedia.org/wiki/Kronecker_product) of \`id1\` and \`id2\`.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.mult](#fun_matrix.mult)
* [str.tostring](#fun_str.tostring)
* [table.new](#fun_table.new)

## matrix.max

+1 overload

the function returns the largest value from the matrix elements.

### syntax & Overloads

> [matrix.max(id) → series float](#fun_matrix.max-0)
> [matrix.max(id) → series int](#fun_matrix.max-1)

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.max()` Example")

// Create a 2x2 matrix.
var m = matrix.new<int>(2, 2, na)
// Fill the matrix with values.
matrix.set(m, 0, 0, 1)
matrix.set(m, 0, 1, 2)
matrix.set(m, 1, 0, 3)
matrix.set(m, 1, 1, 4)

// Get the maximum value in the matrix.
var x = matrix.max(m)

plot(x, 'Matrix maximum value')


```

### Returns

the maximum value from the \`id\` matrix.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.min](#fun_matrix.min)
* [matrix.avg](#fun_matrix.avg)
* [matrix.sort](#fun_matrix.sort)

## matrix.median

+1 overload

the function calculates the [median](https://en.wikipedia.org/wiki/Median) ("the middle" value) of matrix elements.

### syntax & Overloads

> [matrix.median(id) → series float](#fun_matrix.median-0)
> [matrix.median(id) → series int](#fun_matrix.median-1)

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.median()` Example")

// Create a 2x2 matrix.
m = matrix.new<int>(2, 2, na)
// Fill the matrix with values.
matrix.set(m, 0, 0, 1)
matrix.set(m, 0, 1, 2)
matrix.set(m, 1, 0, 3)
matrix.set(m, 1, 1, 4)

// Get the median of the matrix.
x = matrix.median(m)

plot(x, 'Median of the matrix')


```

### Remarks

Note that [na](#var_na) elements of the matrix are not considered when calculating the median.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.mode](#fun_matrix.mode)
* [matrix.sort](#fun_matrix.sort)
* [matrix.avg](#fun_matrix.avg)

## matrix.min

+1 overload

the function returns the smallest value from the matrix elements.

### syntax & Overloads

> [matrix.min(id) → series float](#fun_matrix.min-0)
> [matrix.min(id) → series int](#fun_matrix.min-1)

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.min()` Example")

// Create a 2x2 matrix.
var m = matrix.new<int>(2, 2, na)
// Fill the matrix with values.
matrix.set(m, 0, 0, 1)
matrix.set(m, 0, 1, 2)
matrix.set(m, 1, 0, 3)
matrix.set(m, 1, 1, 4)

// Get the minimum value from the matrix.
var x = matrix.min(m)

plot(x, 'Matrix minimum value')


```

### Returns

the smallest value from the \`id\` matrix.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.max](#fun_matrix.max)
* [matrix.avg](#fun_matrix.avg)
* [matrix.sort](#fun_matrix.sort)

## matrix.mode

+1 overload

the function calculates the [mode](https://en.wikipedia.org/wiki/Mode_(statistics)) of the matrix, which is the most frequently occurring value from the matrix elements. When there are multiple values occurring equally frequently, the function returns the smallest of those values.

### syntax & Overloads

> [matrix.mode(id) → series float](#fun_matrix.mode-0)
> [matrix.mode(id) → series int](#fun_matrix.mode-1)

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.mode()` Example")

// Create a 2x2 matrix.
var m = matrix.new<int>(2, 2, na)
// Fill the matrix with values.
matrix.set(m, 0, 0, 0)
matrix.set(m, 0, 1, 0)
matrix.set(m, 1, 0, 1)
matrix.set(m, 1, 1, 1)

// Get the mode of the matrix.
var x = matrix.mode(m)

plot(x, 'Mode of the matrix')


```

### Returns

the most frequently occurring value from the \`id\` matrix. if none exists, returns the smallest value instead.

### Remarks

Note that [na](#var_na) elements of the matrix are not considered when calculating the mode.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.median](#fun_matrix.median)
* [matrix.sort](#fun_matrix.sort)
* [matrix.avg](#fun_matrix.avg)

## matrix.mult

+3 overloads

the function returns a new matrix resulting from the [product](https://en.wikipedia.org/wiki/Matrix_multiplication) between the matrices \`id1\` and \`id2\`, or between an \`id1\` matrix and an \`id2\` scalar (a numerical value), or between an \`id1\` matrix and an \`id2\` vector (an array of values).

### syntax & Overloads

> [matrix.mult(id1, id2) - matrix<int>;](#fun_matrix.mult-0)
> [matrix.mult(id1, id2) - matrix<float>;](#fun_matrix.mult-1)
> [matrix.mult(id1, id2) - int\[\]](#fun_matrix.mult-2)
> [matrix.mult(id1, id2) - float\[\]](#fun_matrix.mult-3)

### Arguments

- `id1`

    >  (`matrix`<`int`>;)
    
    >  First matrix object.

- `id2`

    >  (`matrix`<`int`>;)
    
    >  second matrix object, value or array.

> - product of two matrices

### Example


```s

//@version=5
indicator("`matrix.mult()` Example 1")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 6x2 matrix containing values `5`.
    var m1 = matrix.new<float>(6, 2, 5)
    // Create a 2x3 matrix containing values `4`.
    // Note that it must have the same quantity of rows as there are columns in the first matrix.
    var m2 = matrix.new<float>(2, 3, 4)
    // Create a new matrix from the multiplication of the two matrices.
    var m3 = matrix.mult(m1, m2)

    // Display using a table.
    var t = table.new(position.top_right, 1, 2, color.green)
    table.cell(t, 0, 0, "product of two matrices:")
    table.cell(t, 0, 1, str.tostring(m3))
product of a matrix and a scalar



```

### Example


```s

//@version=5
indicator("`matrix.mult()` Example 2")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix containing values `4`.
    var m1 = matrix.new<float>(2, 3, 4)

    // Create a new matrix from the product of the two matrices.
    scalar = 5
    var m2 = matrix.mult(m1, scalar)

    // Display using a table.
    var t = table.new(position.top_right, 5, 2, color.green)
    table.cell(t, 0, 0, "Matrix 1:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 1, "x")
    table.cell(t, 2, 0, "scalar:")
    table.cell(t, 2, 1, str.tostring(scalar))
    table.cell(t, 3, 1, "=")
    table.cell(t, 4, 0, "Matrix 2:")
    table.cell(t, 4, 1, str.tostring(m2))
product of a matrix and an array vector



```

### Example


```s

//@version=5
indicator("`matrix.mult()` Example 3")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix containing values `4`.
    var m1 = matrix.new<int>(2, 3, 4)

    // Create an array of three elements.
    var int[] a = array.from(1, 1, 1)

    // Create a new matrix containing the product of the `m1` matrix and the `a` array.
    var m3 = matrix.mult(m1, a)

    // Display using a table.
    var t = table.new(position.top_right, 5, 2, color.green)
    table.cell(t, 0, 0, "Matrix 1:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 1, "x")
    table.cell(t, 2, 0, "Value:")
    table.cell(t, 2, 1, str.tostring(a, " "))
    table.cell(t, 3, 1, "=")
    table.cell(t, 4, 0, "Matrix 3:")
    table.cell(t, 4, 1, str.tostring(m3))


```

### Returns

a new matrix object containing the product of \`id2\` and \`id1\`.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.sum](#fun_matrix.sum)
* [matrix.diff](#fun_matrix.diff)

## matrix.new<type>;

the function creates a new matrix object. a matrix is a two-dimensional data structure containing rows and columns. all elements in the matrix must be of the type specified in the type template ("<type>;").

### Syntax

matrix.new<type>;(rows, columns, initial_value) - matrix<type>;

### Arguments

- `rows`

    >  (`series` `int`)
    
    >  initial row count of the matrix. optional. the default value is 0.

- `columns`

    >  (`series` `int`)
    
    >  initial column count of the matrix. optional. the default value is 0.

- `initial\_value`

    >  (<`matrix`\`_type`>;)
    
    >  initial value of all matrix elements. optional. the default is 'na'.

> - Create a matrix of elements with the same initial value

### Example


```s

//@version=5
indicator("`matrix.new<type>()` Example 1")

// Create a 2x3 (2 rows x 3 columns) "int" matrix with values zero.
var m = matrix.new<int>(2, 3, 0)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m))
Create a matrix from array values



```

### Example


```s

//@version=5
indicator("`matrix.new<type>()` Example 2")

// Function to create a matrix whose rows are filled with array values.
matrixFromarray(int rows, int columns, array<float> data) =>
    m = matrix.new<float>(rows, columns)
    for i = 0 to rows <= 0 ? na : rows - 1
        for j = 0 to columns <= 0 ? na : columns - 1
            matrix.set(m, i, j, array.get(data, i * columns + j))
    m

// Create a 3x3 matrix from an array of values.
var m1 = matrixFromarray(3, 3, array.from(1, 2, 3, 4, 5, 6, 7, 8, 9))
// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m1))
Create a matrix from an `input.text_area()` field



```

### Example


```s

//@version=5
indicator("`matrix.new<type>()` Example 3")

// Function to create a matrix from a text string.
// Values in a row must be separated by a space. Each line is one row.
matrixFrominputarea(stringOfValues) =>
    var rowsarray = str.split(stringOfValues, "
")
    var rows = array.size(rowsarray)
    var cols = array.size(str.split(array.get(rowsarray, 0), " "))
    var matrix = matrix.new<float>(rows, cols, na)
    row = 0
    for rowstring in rowsarray
        col = 0
        values = str.split(rowstring, " ")
        for val in values
            matrix.set(matrix, row, col, str.tonumber(val))
            col += 1
        row += 1
    matrix


stringinput = input.text_area("1 2 3
4 5 6
7 8 9")
var m = matrixFrominputarea(stringinput)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m))
Create matrix from random values



```

### Example


```s

//@version=5
indicator("`matrix.new<type>()` Example 4")

// Function to create a matrix with random values (0.0 to 1.0).
matrixRandom(int rows, int columns)=>
    result = matrix.new<float>(rows, columns)
    for i = 0 to rows - 1
        for j = 0 to columns - 1
            matrix.set(result, i, j, math.random())
    result

// Create a 2x3 matrix with random values.
var m = matrixRandom(2, 3)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m))


```

### Returns

the iD of the new matrix object.

### See also

* [matrix.set](#fun_matrix.set)
* [matrix.fill](#fun_matrix.fill)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)
* [array.new<type>;](#fun_array.new%3Ctype%3E)

## matrix.pinv

+1 overload

the function returns the [pseudoinverse](https://en.wikipedia.org/wiki/Moore%E2%80%93penrose_inverse) of a matrix.

### syntax & Overloads

> [matrix.pinv(id) - matrix<float>;](#fun_matrix.pinv-0)
> [matrix.pinv(id) - matrix<int>;](#fun_matrix.pinv-1)

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.pinv()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // pseudoinverse of the matrix.
    var m2 = matrix.pinv(m1)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "pseudoinverse matrix:")
    table.cell(t, 1, 1, str.tostring(m2))


```

### Returns

a new matrix containing the pseudoinverse of the \`id\` matrix.

### Remarks

the function is calculated using a [Moore-penrose](https://en.wikipedia.org/wiki/Moore%E2%80%93penrose_inverse#Definition) inverse formula based on singular-value decomposition of a matrix. For non-singular square matrices this function returns the result of [matrix.inv](#fun_matrix.inv).

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.inv](#fun_matrix.inv)

## matrix.pow

+1 overload

the function calculates the product of the matrix by itself \`power\` times.

### syntax & Overloads

> [matrix.pow(id, power) - matrix<float>;](#fun_matrix.pow-0)
> [matrix.pow(id, power) - matrix<int>;](#fun_matrix.pow-1)

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  a matrix object.

- `power`

    >  (`series` `int`)
    
    >  the number of times the matrix will be multiplied by itself.

### Example


```s

//@version=5
indicator("`matrix.pow()` Example")

// Display using a table.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<int>(2, 2, 2)
    // Calculate the power of three of the matrix.
    var m2 = matrix.pow(m1, 3)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "MatrixA3:")
    table.cell(t, 1, 1, str.tostring(m2))


```

### Returns

the product of the \`id\` matrix by itself \`power\` times.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.mult](#fun_matrix.mult)

## matrix.rank

the function calculates the [rank](https://en.wikipedia.org/wiki/Rank_(linear_algebra)) of the matrix.

### Syntax

matrix.rank(id) → series int

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.rank()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // Get the rank of the matrix.
    r = matrix.rank(m1)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Rank of the matrix:")
    table.cell(t, 1, 1, str.tostring(r))


```

### Returns

the rank of the \`id\` matrix.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [str.tostring](#fun_str.tostring)

## matrix.remove_col

the function removes the column at \`column\` index of the \`id\` matrix and returns an array containing the removed column's values.

### Syntax

matrix.remove_col(id, column) - type\[\]

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `column`

    >  (`series` `int`)
    
    >  the index of the column to be removed. optional. the default value is [matrix.columns](#fun_matrix.columns).

### Example


```s

//@version=5
indicator("matrix_remove_col", overlay = true)

// Create a 2x2 matrix with ones.
var matrixOrig = matrix.new<int>(2, 2, 1)

// set values to the 'matrixOrig' matrix.
matrix.set(matrixOrig, 0, 1, 2)
matrix.set(matrixOrig, 1, 0, 3)
matrix.set(matrixOrig, 1, 1, 4)


// Create a copy of the 'matrixOrig' matrix.
matrixCopy = matrix.copy(matrixOrig)

// Remove the first column from the `matrixCopy` matrix.
arr = matrix.remove_col(matrixCopy, 0)

// Display matrix elements.
if barstate.islastconfirmedhistory
    var t = table.new(position.top_right, 3, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(matrixOrig))
    table.cell(t, 1, 0, "Removed elements:")
    table.cell(t, 1, 1, str.tostring(arr))
    table.cell(t, 2, 0, "Result Matrix:")
    table.cell(t, 2, 1, str.tostring(matrixCopy))


```

### Returns

an array containing the elements of the column removed from the \`id\` matrix.

### Remarks

indexing of rows and columns starts at zero. it is far more efficient to declare matrices with explicit dimensions than to build them by adding or removing columns. deleting a column is also much slower than deleting a row with the [matrix.remove_row](#fun_matrix.remove_row) function.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.copy](#fun_matrix.copy)
* [matrix.remove_row](#fun_matrix.remove_row)

## matrix.remove_row

the function removes the row at \`row\` index of the \`id\` matrix and returns an array containing the removed row's values.

### Syntax

matrix.remove_row(id, row) - type\[\]

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `row`

    >  (`series` `int`)
    
    >  the index of the row to be deleted. optional. the default value is [matrix.rows](#fun_matrix.rows).

### Example


```s

//@version=5
indicator("matrix_remove_row", overlay = true)

// Create a 2x2 "int" matrix containing values `1`.
var matrixOrig = matrix.new<int>(2, 2, 1)

// set values to the 'matrixOrig' matrix.
matrix.set(matrixOrig, 0, 1, 2)
matrix.set(matrixOrig, 1, 0, 3)
matrix.set(matrixOrig, 1, 1, 4)

// Create a copy of the 'matrixOrig' matrix.
matrixCopy = matrix.copy(matrixOrig)

// Remove the first row from the matrix `matrixCopy`.
arr = matrix.remove_row(matrixCopy, 0)

// Display matrix elements.
if barstate.islastconfirmedhistory
    var t = table.new(position.top_right, 3, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(matrixOrig))
    table.cell(t, 1, 0, "Removed elements:")
    table.cell(t, 1, 1, str.tostring(arr))
    table.cell(t, 2, 0, "Result Matrix:")
    table.cell(t, 2, 1, str.tostring(matrixCopy))


```

### Returns

an array containing the elements of the row removed from the \`id\` matrix.

### Remarks

indexing of rows and columns starts at zero. it is far more efficient to declare matrices with explicit dimensions than to build them by adding or removing rows.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.copy](#fun_matrix.copy)
* [matrix.remove_col](#fun_matrix.remove_col)

## matrix.reshape

the function rebuilds the \`id\` matrix to \`rows\` x \`cols\` dimensions.

### Syntax

matrix.reshape(id, rows, columns) - void

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `rows`

    >  (`series` `int`)
    
    >  the number of rows of the reshaped matrix.

- `columns`

    >  (`series` `int`)
    
    >  the number of columns of the reshaped matrix.

### Example


```s

//@version=5
indicator("`matrix.reshape()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix.
    var m1 = matrix.new<float>(2, 3)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 0, 2, 3)
    matrix.set(m1, 1, 0, 4)
    matrix.set(m1, 1, 1, 5)
    matrix.set(m1, 1, 2, 6)

    // Copy the matrix to a new one.
    var m2 = matrix.copy(m1)

    // Reshape the copy to a 3x2.
    matrix.reshape(m2, 3, 2)

    // Display using a table.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Reshaped matrix:")
    table.cell(t, 1, 1, str.tostring(m2))


```

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.add_row](#fun_matrix.add_row)
* [matrix.add_col](#fun_matrix.add_col)

## matrix.reverse

the function reverses the order of rows and columns in the matrix \`id\`. the first row and first column become the last, and the last become the first.

### Syntax

matrix.reverse(id) - void

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.reverse()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Copy the matrix to a new one.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // Copy matrix elements to a new matrix.
    var m2 = matrix.copy(m1)

    // Reverse the `m2` copy of the original matrix.
    matrix.reverse(m2)

    // Display using a table.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "Reversed matrix:")
    table.cell(t, 1, 1, str.tostring(m2))


```

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)
* [matrix.reshape](#fun_matrix.reshape)

## matrix.row

the function creates a one-dimensional array from the elements of a matrix row.

### Syntax

matrix.row(id, row) - type\[\]

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `row`

    >  (`series` `int`)
    
    >  index of the required row.

### Example


```s

//@version=5
indicator("`matrix.row()` Example", "", true)

// Create a 2x3 "float" matrix from `hlc3` values.
m = matrix.new<float>(2, 3, hlc3)

// Return an array with the values of the first row of the matrix.
a = matrix.row(m, 0)

// plot the first value from the array `a`.
plot(array.get(a, 0))


```

### Returns

an array iD containing the \`row\` values of the \`id\` matrix.

### Remarks

indexing of rows starts at 0.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [array.get](#fun_array.get)
* [matrix.col](#fun_matrix.col)
* [matrix.rows](#fun_matrix.rows)

## matrix.rows

the function returns the number of rows in the matrix.

### Syntax

matrix.rows(id) → series int

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.rows()` Example")

// Create a 2x6 matrix with values `0`.
var m = matrix.new<int>(2, 6, 0)

// Get the quantity of rows in the matrix.
var x = matrix.rows(m)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, "Rows: " + str.tostring(x) + "
" + str.tostring(m))


```

### Returns

the number of rows in the matrix \`id\`.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.row](#fun_matrix.row)

## matrix.set

the function assigns \`value\` to the element at the \`row\` and \`column\` of the \`id\` matrix.

### Syntax

matrix.set(id, row, column, value) - void

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `row`

    >  (`series` `int`)
    
    >  the row index of the element to be modified.

- `column`

    >  (`series` `int`)
    
    >  the column index of the element to be modified.

- `value`

    >  (`series` <`type` `of` `the` `matrix's` `elements`>;)
    
    >  the new value to be set.

### Example


```s

//@version=5
indicator("`matrix.set()` Example")

// Create a 2x3 "int" matrix containing values `4`.
m = matrix.new<int>(2, 3, 4)

// Replace the value of element at row 1 and column 2 with value `3`.
matrix.set(m, 0, 1, 3)

// Display using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m))


```

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)

## matrix.sort

the function rearranges the rows in the \`id\` matrix following the sorted order of the values in the \`column\`.

### Syntax

matrix.sort(id, column, order) - void

### Arguments

- `id`

    >  (`matrix`<`int`>;)
    
    >  a matrix object to be sorted.

- `column`

    >  (`series` `int`)
    
    >  index of the column whose sorted values determine the new order of rows. optional. the default value is 0.

- `order`

    >  (`simple` `sort_order`)
    
    >  the sort order. possible values: [order.ascending](#var_order.ascending) (default), [order.descending](#var_order.descending).

### Example


```s

//@version=5
indicator("`matrix.sort()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<float>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 3)
    matrix.set(m1, 0, 1, 4)
    matrix.set(m1, 1, 0, 1)
    matrix.set(m1, 1, 1, 2)

    // Copy the matrix to a new one.
    var m2 = matrix.copy(m1)
    // sort the rows of `m2` using the default arguments (first column and ascending order).
    matrix.sort(m2)

    // Display using a table.
    if barstate.islastconfirmedhistory
        var t = table.new(position.top_right, 2, 2, color.green)
        table.cell(t, 0, 0, "Original matrix:")
        table.cell(t, 0, 1, str.tostring(m1))
        table.cell(t, 1, 0, "sorted matrix:")
        table.cell(t, 1, 1, str.tostring(m2))


```

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.max](#fun_matrix.max)
* [matrix.min](#fun_matrix.min)
* [matrix.avg](#fun_matrix.avg)

## matrix.submatrix

the function extracts a submatrix of the \`id\` matrix within the specified indices.

### Syntax

matrix.submatrix(id, from\_row, to\_row, from\_column, to\_column) - matrix<type>;

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `from_row`

    >  (`series` `int`)
    
    >  index of the row from which the extraction will begin (inclusive). optional. the default value is 0.

- `to_row`

    >  (`series` `int`)
    
    >  index of the row where the extraction will end (non inclusive). optional. the default value is [matrix.rows](#fun_matrix.rows).

- `from_column`

    >  (`series` `int`)
    
    >  index of the column from which the extraction will begin (inclusive). optional. the default value is 0.

- `to_column`

    >  (`series` `int`)
    
    >  index of the column where the extraction will end (non inclusive). optional. the default value is [matrix.columns](#fun_matrix.columns).

### Example


```s

//@version=5
indicator("`matrix.submatrix()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix matrix with values `0`.
    var m1 = matrix.new<int>(2, 3, 0)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 0, 2, 3)
    matrix.set(m1, 1, 0, 4)
    matrix.set(m1, 1, 1, 5)
    matrix.set(m1, 1, 2, 6)

    // Create a 2x2 submatrix of the `m1` matrix.
    var m2 = matrix.submatrix(m1, 0, 2, 1, 3)

    // Display using a table.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original Matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "submatrix:")
    table.cell(t, 1, 1, str.tostring(m2))


```

### Returns

a new matrix object containing the submatrix of the \`id\` matrix defined by the \`from\_row\`, \`to\_row\`, \`from\_column\` and \`to\_column\` indices.

### Remarks

indexing of the rows and columns starts at zero.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.row](#fun_matrix.row)
* [matrix.col](#fun_matrix.col)
* [matrix.reshape](#fun_matrix.reshape)

## matrix.sum

+1 overload

the function returns a new matrix resulting from the [sum](https://en.wikipedia.org/wiki/Matrix_addition) of two matrices \`id1\` and \`id2\`, or of an \`id1\` matrix and an \`id2\` scalar (a numerical value).

### syntax & Overloads

> [matrix.sum(id1, id2) - matrix<int>;](#fun_matrix.sum-0)
> [matrix.sum(id1, id2) - matrix<float>;](#fun_matrix.sum-1)

### Arguments

- `id1`

    >  (`matrix`<`int`>;)
    
    >  First matrix object.

- `id2`

    >  (`matrix`<`int`>;)
    
    >  second matrix object, or scalar value.

> - sum of two matrices

### Example


```s

//@version=5
indicator("`matrix.sum()` Example 1")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix containing values `5`.
    var m1 = matrix.new<float>(2, 3, 5)
    // Create a 2x3 matrix containing values `4`.
    var m2 = matrix.new<float>(2, 3, 4)
    // Create a new matrix that sums matrices `m1` and `m2`.
    var m3 = matrix.sum(m1, m2)

    // Display using a table.
    var t = table.new(position.top_right, 1, 2, color.green)
    table.cell(t, 0, 0, "sum of two matrices:")
    table.cell(t, 0, 1, str.tostring(m3))
sum of a matrix and scalar



```

### Example


```s

//@version=5
indicator("`matrix.sum()` Example 2")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x3 matrix with values `4`.
    var m1 = matrix.new<float>(2, 3, 4)

    // Create a new matrix containing the sum of the `m1` matrix with the "int" value `1`.
    var m2 = matrix.sum(m1, 1)

    // Display using a table.
    var t = table.new(position.top_right, 1, 2, color.green)
    table.cell(t, 0, 0, "sum of a matrix and a scalar:")
    table.cell(t, 0, 1, str.tostring(m2))


```

### Returns

a new matrix object containing the sum of \`id2\` and \`id1\`.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)

## matrix.swap_columns

the function swaps the columns at the index \`column1\` and \`column2\` in the \`id\` matrix.

### Syntax

matrix.swap_columns(id, column1, column2) - void

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `column1`

    >  (`series` `int`)
    
    >  index of the first column to be swapped.

- `column2`

    >  (`series` `int`)
    
    >  index of the second column to be swapped.

### Example


```s

//@version=5
indicator("`matrix.swap_columns()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix with aEUR~naaEUR(tm) values.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // Copy the matrix to a new one.
    var m2 = matrix.copy(m1)

    // swap the first and second columns of the matrix copy.
    matrix.swap_columns(m2, 0, 1)

    // Display using a table.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "swapped columns in copy:")
    table.cell(t, 1, 1, str.tostring(m2))


```

### Remarks

indexing of the rows and columns starts at zero.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)

## matrix.swap_rows

the function swaps the rows at the index \`row1\` and \`row2\` in the \`id\` matrix.

### Syntax

matrix.swap_rows(id, row1, row2) - void

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

- `row1`

    >  (`series` `int`)
    
    >  index of the first row to be swapped.

- `row2`

    >  (`series` `int`)
    
    >  index of the second row to be swapped.

### Example


```s

//@version=5
indicator("`matrix.swap_rows()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 3x2 matrix with aEUR~naaEUR(tm) values.
    var m1 = matrix.new<int>(3, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)
    matrix.set(m1, 2, 0, 5)
    matrix.set(m1, 2, 1, 6)

    // Copy the matrix to a new one.
    var m2 = matrix.copy(m1)

    // swap the first and second rows of the matrix copy.
    matrix.swap_rows(m2, 0, 1)

    // Display using a table.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "swapped rows in copy:")
    table.cell(t, 1, 1, str.tostring(m2))


```

### Remarks

indexing of the rows and columns starts at zero.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.swap_columns](#fun_matrix.swap_columns)

## matrix.trace

+1 overload

the function calculates the [trace](https://en.wikipedia.org/wiki/trace_(linear_algebra)) of a matrix (the sum of the main diagonal's elements).

### syntax & Overloads

> [matrix.trace(id) → series float](#fun_matrix.trace-0)
> [matrix.trace(id) → series int](#fun_matrix.trace-1)

### Arguments

- `id`

    >  (`matrix`<`float`>;)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.trace()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<int>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // Get the trace of the matrix.
    tr = matrix.trace(m1)

    // Display matrix elements.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Matrix elements:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "trace of the matrix:")
    table.cell(t, 1, 1, str.tostring(tr))


```

### Returns

the trace of the \`id\` matrix.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.get](#fun_matrix.get)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)

## matrix.transpose

the function creates a new, [transposed](https://en.wikipedia.org/wiki/transpose#transpose_of_a_matrix) version of the \`id\`. this interchanges the row and column index of each element.

### Syntax

matrix.transpose(id) - matrix<type>;

### Arguments

- `id`

    >  (`any` `matrix` `type`)
    
    >  a matrix object.

### Example


```s

//@version=5
indicator("`matrix.transpose()` Example")

// For efficiency, execute this code only once.
if barstate.islastconfirmedhistory
    // Create a 2x2 matrix.
    var m1 = matrix.new<float>(2, 2, na)
    // Fill the matrix with values.
    matrix.set(m1, 0, 0, 1)
    matrix.set(m1, 0, 1, 2)
    matrix.set(m1, 1, 0, 3)
    matrix.set(m1, 1, 1, 4)

    // Create a transpose of the matrix.
    var m2 = matrix.transpose(m1)

    // Display using a table.
    var t = table.new(position.top_right, 2, 2, color.green)
    table.cell(t, 0, 0, "Original matrix:")
    table.cell(t, 0, 1, str.tostring(m1))
    table.cell(t, 1, 0, "transposed matrix:")
    table.cell(t, 1, 1, str.tostring(m2))


```

### Returns

a new matrix containing the transposed version of the \`id\` matrix.

### See also

* [matrix.new<type>;](#fun_matrix.new%3Ctype%3E)
* [matrix.set](#fun_matrix.set)
* [matrix.columns](#fun_matrix.columns)
* [matrix.rows](#fun_matrix.rows)
* [matrix.reshape](#fun_matrix.reshape)
* [matrix.reverse](#fun_matrix.reverse)

## max\_bars\_back

Function sets the maximum number of bars that is available for historical reference of a given built-in or user variable. When operator '\[\]' is applied to a variable - it is a reference to a historical value of that variable.

if an argument of an operator '\[\]' is a compile time constant value (e.g. 'v\[10\]', 'close\[500\]') then there is no need to use 'max\_bars\_back' function for that variable. pine script(r) compiler will use that constant value as history buffer size.

if an argument of an operator '\[\]' is a value, calculated at runtime (e.g. 'v\[i\]' where 'i' - is a series variable) then pine script(r) attempts to autodetect the history buffer size at runtime. sometimes it fails and the script crashes at runtime because it eventually refers to historical values that are out of the buffer. in that case you should use 'max\_bars\_back' to fix that problem manually.

### Syntax

max\_bars\_back(var, num) - void

### Arguments

- `var`

    >  (`series` `bool`)
    
    >  series variable identifier for which history buffer should be resized. possible values are: 'open', 'high', 'low', 'close', 'volume', 'time', or any user defined variable id.

- `num`

    >  (`const` `int`)
    
    >  History buffer size which is the number of bars that could be referenced for variable 'var'.

### Example


```s

//@version=5
indicator("max_bars_back")
close_() => close
depth() => 400
d = depth()
v = close_()
max_bars_back(v, 500)
out = if bar_index > 0
    v[d]
else
    v
plot(out)


```

### Returns

void

### Remarks

at the moment 'max\_bars\_back' cannot be applied to built-ins like 'hl2', 'hlc3', 'ohlc4'. please use multiple 'max\_bars\_back' calls as workaround here (e.g. instead of a single 'max\_bars\_back(hl2, 100)' call you should call the function twice: 'max\_bars\_back(high, 100), max\_bars\_back(low, 100)').

if the [indicator](#fun_indicator) or [strategy](#fun_strategy) 'max\_bars\_back' parameter is used, all variables in the indicator are affected. this may result in excessive memory usage and cause runtime problems. When possible (i.e. when the cause is a variable rather than a function), please use the [max\_bars\_back](#fun_max_bars_back) function instead.

### See also

* [indicator](#fun_indicator)

## minute

+1 overload

### syntax & Overloads

> [minute(time) → series int](#fun_minute-0)
> [minute(time, timezone) → series int](#fun_minute-1)
* [

### Arguments

- `time`

    >  (`series` `int`)
    
    >  unix time in milliseconds.

### Returns

Minute (in exchange timezone) for provided unix time.

### Remarks

unix time is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

### See also

* [minute](#var_minute)
* [time](#fun_time)
* [year](#fun_year)
* [month](#fun_month)
* [dayofmonth](#fun_dayofmonth)
* [dayofweek](#fun_dayofweek)
* [hour](#fun_hour)
* [second](#fun_second)

## month

+1 overload

### syntax & Overloads

> [month(time) → series int](#fun_month-0)
> [month(time, timezone) → series int](#fun_month-1)

### Arguments

- `time`

    >  (`series` `int`)
    
    >  unix time in milliseconds.

### Returns

Month (in exchange timezone) for provided unix time.

### Remarks

unix time is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

Note that this function returns the month based on the time of the bar's open. For overnight sessions (e.g. EuRusD, where Monday session starts on sunday, 17:00 uTC-4) this value can be lower by 1 than the month of the trading day.

### See also

* [month](#var_month)
* [time](#fun_time)
* [year](#fun_year)
* [dayofmonth](#fun_dayofmonth)
* [dayofweek](#fun_dayofweek)
* [hour](#fun_hour)
* [minute](#fun_minute)
* [second](#fun_second)

## na

+1 overload

Tests if \`x\` is [na](#var_na).

### syntax & Overloads

> [na(x) → series bool](#fun_na-0)
> [na(x) → simple bool](#fun_na-1)

### Arguments

- `x`

    >  (<`arg_type`>;)
    
    >  Value to be tested.

### Example


```s

//@version=5
indicator("na")
// use the `na()` function to test for `na`.
plot(na(close[1]) ? close : close[1])
// aLTERNaTiVE
// `nz()` also tests `close[1]` for `na`. it returns `close[1]` if it is not `na`, and `close` if it is.
plot(nz(close[1], close))


```

### Returns

Returns [true](#op_true) if \`x\` is [na](#var_na), [false](#op_false) otherwise.

### See also

* [na](#var_na)
* [fixnan](#fun_fixnan)
* [nz](#fun_nz)

## nz

+15 overloads

Replaces NaN values with zeros (or given value) in a series.

### syntax & Overloads

> [nz(source) → simple color](#fun_nz-0)
> [nz(source) → simple int](#fun_nz-1)
> [nz(source) → series color](#fun_nz-2)
> [nz(source) → series int](#fun_nz-3)
> [nz(source) → simple float](#fun_nz-4)
> [nz(source) → series float](#fun_nz-5)
> [nz(source, replacement) → simple color](#fun_nz-6)
> [nz(source, replacement) → simple int](#fun_nz-7)
> [nz(source, replacement) → series color](#fun_nz-8)
> [nz(source, replacement) → series int](#fun_nz-9)
> [nz(source, replacement) → simple float](#fun_nz-10)
> [nz(source, replacement) → series float](#fun_nz-11)
> [nz(source) → simple bool](#fun_nz-12)
> [nz(source) → series bool](#fun_nz-13)
> [nz(source, replacement) → simple bool](#fun_nz-14)
> [nz(source, replacement) → series bool](#fun_nz-15)

### Arguments

- `source`

    >  (`simple` `color`)
    
    >  series of values to process.

### Example


```s

//@version=5
indicator("nz", overlay=true)
plot(nz(ta.sma(close, 100)))


```

### Returns

the value of \`source\` if it is not \`na\`. if the value of \`source\` is \`na\`, returns zero, or the \`replacement\` argument when one is used.

### See also

* [na](#var_na)
* [na](#fun_na)
* [fixnan](#fun_fixnan)

## plot

plots a series of data on the chart.

### Syntax

plot(series, title, color, linewidth, style, trackprice, histbase, offset, join, editable, show_last, display) - plot

### Arguments

- `series`

    >  (`series` `int`/`float`)
    
    >  series of data to be plotted. Required argument.

- `title`

    >  (`const` `string`)
    
    >  title of the plot.

- `color`

    >  (`series` `color`)
    
    >  color of the plot. You can use constants like 'color=color.red' or 'color=#ff001a' as well as complex expressions like 'color = close >= open ? color.green : color.red'. optional argument.

- `linewidth`

    >  (`input` `int`)
    
    >  Width of the plotted line. Default value is 1. Not applicable to every style.

- `style`

    >  (`input` `plot_style`)
    
    >  Type of plot. possible values are: [plot.style_line](#var_plot.style_line), [plot.style_stepline](#var_plot.style_stepline), [plot.style\_stepline\_diamond](#var_plot.style_stepline_diamond), [plot.style_histogram](#var_plot.style_histogram), [plot.style_cross](#var_plot.style_cross), [plot.style_area](#var_plot.style_area), [plot.style_columns](#var_plot.style_columns), [plot.style_circles](#var_plot.style_circles), [plot.style_linebr](#var_plot.style_linebr), [plot.style_areabr](#var_plot.style_areabr), [plot.style_steplinebr](#var_plot.style_steplinebr). Default value is [plot.style_line](#var_plot.style_line).

- `trackprice`

    >  (`input` `bool`)
    
    >  if true then a horizontal price line will be shown at the level of the last indicator value. Default is false.

- `histbase`

    >  (`input` `int`/`float`)
    
    >  the price value used as the reference level when rendering plot with [plot.style_histogram](#var_plot.style_histogram), [plot.style_columns](#var_plot.style_columns) or [plot.style_area](#var_plot.style_area) style. Default is 0.0.

- `offset`

    >  (`series` `int`)
    
    >  shifts the plot to the left or to the right on the given number of bars. Default is 0.

- `join`

    >  (`input` `bool`)
    
    >  if true then plot points will be joined with line, applicable only to [plot.style_cross](#var_plot.style_cross) and [plot.style_circles](#var_plot.style_circles) styles. Default is false.

- `editable`

    >  (`const` `bool`)
    
    >  if true then plot style will be editable in format dialog. Default is true.

- `show_last`

    >  (`input` `int`)
    
    >  if set, defines the number of bars (from the last bar back to the past) to plot on chart.

- `display`

    >  (`input` `plot_display`)
    
    >  Controls where the plot's information is displayed. Display options support addition and subtraction, meaning that using \`display.all - display.status\_line\` will display the plot's information everywhere except in the script's status line. \`display.price\_scale + display.status\_line\` will display the plot only in the price scale and status line. When \`display\` arguments such as \`display.price\_scale\` have user-controlled chart settings equivalents, the relevant plot information will only appear when all settings allow for it. possible values: [display.none](#var_display.none), [display.pane](#var_display.pane), [display.data_window](#var_display.data_window), [display.price_scale](#var_display.price_scale), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("plot")
plot(high+low, title='title', color=color.new(#00ffaa, 70), linewidth=2, style=plot.style_area, offset=15, trackprice=true)

// You may fill the background between any two plots with a fill() function:
p1 = plot(open)
p2 = plot(close)
fill(p1, p2, color=color.new(color.green, 90))


```

#00ffaa, 70), linewidth=2, style=plot.style_area, offset=15, trackprice=true)// You may fill the background between any two plots with a fill() function:p1 = plot(open)p2 = plot(close)fill(p1, p2, color=color.new(color.green, 90))

### Returns

a plot object, that can be used in [fill](#fun_fill)

### See also

* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [plotarrow](#fun_plotarrow)
* [barcolor](#fun_barcolor)
* [bgcolor](#fun_bgcolor)
* [fill](#fun_fill)

## plotarrow

plots up and down arrows on the chart. up arrow is drawn at every indicator positive value, down arrow is drawn at every negative value. if indicator returns [na](#var_na) then no arrow is drawn. arrows has different height, the more absolute indicator value the longer arrow is drawn.

### Syntax

plotarrow(series, title, colorup, colordown, offset, minheight, maxheight, editable, show_last, display) - void

### Arguments

- `series`

    >  (`series` `int`/`float`)
    
    >  series of data to be plotted as arrows. Required argument.

- `title`

    >  (`const` `string`)
    
    >  title of the plot.

- `colorup`

    >  (`series` `color`)
    
    >  color of the up arrows. optional argument.

- `colordown`

    >  (`series` `color`)
    
    >  color of the down arrows. optional argument.

- `offset`

    >  (`series` `int`)
    
    >  shifts arrows to the left or to the right on the given number of bars. Default is 0.

- `minheight`

    >  (`input` `int`)
    
    >  Minimal possible arrow height in pixels. Default is 5.

- `maxheight`

    >  (`input` `int`)
    
    >  Maximum possible arrow height in pixels. Default is 100.

- `editable`

    >  (`const` `bool`)
    
    >  if true then plotarrow style will be editable in format dialog. Default is true.

- `show_last`

    >  (`input` `int`)
    
    >  if set, defines the number of arrows (from the last bar back to the past) to plot on chart.

- `display`

    >  (`input` `plot_display`)
    
    >  Controls where the plot's information is displayed. Display options support addition and subtraction, meaning that using \`display.all - display.status\_line\` will display the plot's information everywhere except in the script's status line. \`display.price\_scale + display.status\_line\` will display the plot only in the price scale and status line. When \`display\` arguments such as \`display.price\_scale\` have user-controlled chart settings equivalents, the relevant plot information will only appear when all settings allow for it. possible values: [display.none](#var_display.none), [display.pane](#var_display.pane), [display.data_window](#var_display.data_window), [display.price_scale](#var_display.price_scale), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("plotarrow example", overlay=true)
codiff = close - open
plotarrow(codiff, colorup=color.new(color.teal,40), colordown=color.new(color.orange, 40))


```

### Remarks

use [plotarrow](#fun_plotarrow) function in conjunction with 'overlay=true' [indicator](#fun_indicator) parameter!

### See also

* [plot](#fun_plot)
* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [barcolor](#fun_barcolor)
* [bgcolor](#fun_bgcolor)

## plotbar

plots ohlc bars on the chart.

### Syntax

plotbar(open, high, low, close, title, color, editable, show_last, display) - void

### Arguments

- `open`

    >  (`series` `int`/`float`)
    
    >  Open series of data to be used as open values of bars. Required argument.

- `high`

    >  (`series` `int`/`float`)
    
    >  High series of data to be used as high values of bars. Required argument.

- `low`

    >  (`series` `int`/`float`)
    
    >  Low series of data to be used as low values of bars. Required argument.

- `close`

    >  (`series` `int`/`float`)
    
    >  Close series of data to be used as close values of bars. Required argument.

- `title`

    >  (`const` `string`)
    
    >  title of the plotbar. optional argument.

- `color`

    >  (`series` `color`)
    
    >  color of the ohlc bars. You can use constants like 'color=color.red' or 'color=#ff001a' as well as complex expressions like 'color = close >= open ? color.green : color.red'. optional argument.

- `editable`

    >  (`const` `bool`)
    
    >  if true then plotbar style will be editable in format dialog. Default is true.

- `show_last`

    >  (`input` `int`)
    
    >  if set, defines the number of bars (from the last bar back to the past) to plot on chart.

- `display`

    >  (`input` `plot_display`)
    
    >  Controls where the plot's information is displayed. Display options support addition and subtraction, meaning that using \`display.all - display.status\_line\` will display the plot's information everywhere except in the script's status line. \`display.price\_scale + display.status\_line\` will display the plot only in the price scale and status line. When \`display\` arguments such as \`display.price\_scale\` have user-controlled chart settings equivalents, the relevant plot information will only appear when all settings allow for it. possible values: [display.none](#var_display.none), [display.pane](#var_display.pane), [display.data_window](#var_display.data_window), [display.price_scale](#var_display.price_scale), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("plotbar example", overlay=true)
plotbar(open, high, low, close, title='title', color = open < close ? color.green : color.red)


```

### Remarks

Even if one value of open, high, low or close equal NaN then bar no draw.

the maximal value of open, high, low or close will be set as 'high', and the minimal value will be set as 'low'.

### See also

* [plotcandle](#fun_plotcandle)

## plotcandle

plots candles on the chart.

### Syntax

plotcandle(open, high, low, close, title, color, wickcolor, editable, show_last, bordercolor, display) - void

### Arguments

- `open`

    >  (`series` `int`/`float`)
    
    >  Open series of data to be used as open values of candles. Required argument.

- `high`

    >  (`series` `int`/`float`)
    
    >  High series of data to be used as high values of candles. Required argument.

- `low`

    >  (`series` `int`/`float`)
    
    >  Low series of data to be used as low values of candles. Required argument.

- `close`

    >  (`series` `int`/`float`)
    
    >  Close series of data to be used as close values of candles. Required argument.

- `title`

    >  (`const` `string`)
    
    >  title of the plotcandles. optional argument.

- `color`

    >  (`series` `color`)
    
    >  color of the candles. You can use constants like 'color=color.red' or 'color=#ff001a' as well as complex expressions like 'color = close >= open ? color.green : color.red'. optional argument.

- `wickcolor`

    >  (`series` `color`)
    
    >  the color of the wick of candles. an optional argument.

- `editable`

    >  (`const` `bool`)
    
    >  if true then plotcandle style will be editable in format dialog. Default is true.

- `show_last`

    >  (`input` `int`)
    
    >  if set, defines the number of candles (from the last bar back to the past) to plot on chart.

- `bordercolor`

    >  (`series` `color`)
    
    >  the border color of candles. an optional argument.

- `display`

    >  (`input` `plot_display`)
    
    >  Controls where the plot's information is displayed. Display options support addition and subtraction, meaning that using \`display.all - display.status\_line\` will display the plot's information everywhere except in the script's status line. \`display.price\_scale + display.status\_line\` will display the plot only in the price scale and status line. When \`display\` arguments such as \`display.price\_scale\` have user-controlled chart settings equivalents, the relevant plot information will only appear when all settings allow for it. possible values: [display.none](#var_display.none), [display.pane](#var_display.pane), [display.data_window](#var_display.data_window), [display.price_scale](#var_display.price_scale), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("plotcandle example", overlay=true)
plotcandle(open, high, low, close, title='title', color = open < close ? color.green : color.red, wickcolor=color.black)


```

### Remarks

Even if one value of open, high, low or close equal NaN then bar no draw.

the maximal value of open, high, low or close will be set as 'high', and the minimal value will be set as 'low'.

### See also

* [plotbar](#fun_plotbar)

## plotchar

plots visual shapes using any given one unicode character on the chart.

### Syntax

plotchar(series, title, char, location, color, offset, text, textcolor, editable, size, show_last, display) - void

### Arguments

- `series`

    >  (`series` `bool`)
    
    >  series of data to be plotted as shapes. series is treated as a series of boolean values for all location values except [location.absolute](#var_location.absolute). Required argument.

- `title`

    >  (`const` `string`)
    
    >  title of the plot.

- `char`

    >  (`input` `string`)
    
    >  Character to use as a visual shape.

- `location`

    >  (`input` `string`)
    
    >  Location of shapes on the chart. possible values are: [location.abovebar](#var_location.abovebar), [location.belowbar](#var_location.belowbar), [location.top](#var_location.top), [location.bottom](#var_location.bottom), [location.absolute](#var_location.absolute). Default value is [location.abovebar](#var_location.abovebar).

- `color`

    >  (`series` `color`)
    
    >  color of the shapes. You can use constants like 'color=color.red' or 'color=#ff001a' as well as complex expressions like 'color = close >= open ? color.green : color.red'. optional argument.

- `offset`

    >  (`series` `int`)
    
    >  shifts shapes to the left or to the right on the given number of bars. Default is 0.

- `text`

    >  (`const` `string`)
    
    >  Text to display with the shape. You can use multiline text, to separate lines use '\n' escape sequence. Example: 'line one\nline two'.

- `textcolor`

    >  (`series` `color`)
    
    >  color of the text. You can use constants like 'textcolor=color.red' or 'textcolor=#ff001a' as well as complex expressions like 'textcolor = close >= open ? color.green : color.red'. optional argument.

- `editable`

    >  (`const` `bool`)
    
    >  if true then plotchar style will be editable in format dialog. Default is true.

- `size`

    >  (`const` `string`)
    
    >  size of characters on the chart. possible values are: [size.auto](#var_size.auto), [size.tiny](#var_size.tiny), [size.small](#var_size.small), [size.normal](#var_size.normal), [size.large](#var_size.large), [size.huge](#var_size.huge). Default is [size.auto](#var_size.auto).

- `show_last`

    >  (`input` `int`)
    
    >  if set, defines the number of chars (from the last bar back to the past) to plot on chart.

- `display`

    >  (`input` `plot_display`)
    
    >  Controls where the plot's information is displayed. Display options support addition and subtraction, meaning that using \`display.all - display.status\_line\` will display the plot's information everywhere except in the script's status line. \`display.price\_scale + display.status\_line\` will display the plot only in the price scale and status line. When \`display\` arguments such as \`display.price\_scale\` have user-controlled chart settings equivalents, the relevant plot information will only appear when all settings allow for it. possible values: [display.none](#var_display.none), [display.pane](#var_display.pane), [display.data_window](#var_display.data_window), [display.price_scale](#var_display.price_scale), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("plotchar example", overlay=true)
data = close >= open
plotchar(data, char='a,,')


```

### Remarks

use [plotchar](#fun_plotchar) function in conjunction with 'overlay=true' [indicator](#fun_indicator) parameter!

### See also

* [plot](#fun_plot)
* [plotshape](#fun_plotshape)
* [plotarrow](#fun_plotarrow)
* [barcolor](#fun_barcolor)
* [bgcolor](#fun_bgcolor)

## plotshape

plots visual shapes on the chart.

### Syntax

plotshape(series, title, style, location, color, offset, text, textcolor, editable, size, show_last, display) - void

### Arguments

- `series`

    >  (`series` `bool`)
    
    >  series of data to be plotted as shapes. series is treated as a series of boolean values for all location values except [location.absolute](#var_location.absolute). Required argument.

- `title`

    >  (`const` `string`)
    
    >  title of the plot.

- `style`

    >  (`input` `string`)
    
    >  Type of plot. possible values are: [shape.xcross](#var_shape.xcross), [shape.cross](#var_shape.cross), [shape.triangleup](#var_shape.triangleup), [shape.triangledown](#var_shape.triangledown), [shape.flag](#var_shape.flag), [shape.circle](#var_shape.circle), [shape.arrowup](#var_shape.arrowup), [shape.arrowdown](#var_shape.arrowdown), [shape.labelup](#var_shape.labelup), [shape.labeldown](#var_shape.labeldown), [shape.square](#var_shape.square), [shape.diamond](#var_shape.diamond). Default value is [shape.xcross](#var_shape.xcross).

- `location`

    >  (`input` `string`)
    
    >  Location of shapes on the chart. possible values are: [location.abovebar](#var_location.abovebar), [location.belowbar](#var_location.belowbar), [location.top](#var_location.top), [location.bottom](#var_location.bottom), [location.absolute](#var_location.absolute). Default value is [location.abovebar](#var_location.abovebar).

- `color`

    >  (`series` `color`)
    
    >  color of the shapes. You can use constants like 'color=color.red' or 'color=#ff001a' as well as complex expressions like 'color = close >= open ? color.green : color.red'. optional argument.

- `offset`

    >  (`series` `int`)
    
    >  shifts shapes to the left or to the right on the given number of bars. Default is 0.

- `text`

    >  (`const` `string`)
    
    >  Text to display with the shape. You can use multiline text, to separate lines use '\n' escape sequence. Example: 'line one\nline two'.

- `textcolor`

    >  (`series` `color`)
    
    >  color of the text. You can use constants like 'textcolor=color.red' or 'textcolor=#ff001a' as well as complex expressions like 'textcolor = close >= open ? color.green : color.red'. optional argument.

- `editable`

    >  (`const` `bool`)
    
    >  if true then plotshape style will be editable in format dialog. Default is true.

- `size`

    >  (`const` `string`)
    
    >  size of shapes on the chart. possible values are: [size.auto](#var_size.auto), [size.tiny](#var_size.tiny), [size.small](#var_size.small), [size.normal](#var_size.normal), [size.large](#var_size.large), [size.huge](#var_size.huge). Default is [size.auto](#var_size.auto).

- `show_last`

    >  (`input` `int`)
    
    >  if set, defines the number of shapes (from the last bar back to the past) to plot on chart.

- `display`

    >  (`input` `plot_display`)
    
    >  Controls where the plot's information is displayed. Display options support addition and subtraction, meaning that using \`display.all - display.status\_line\` will display the plot's information everywhere except in the script's status line. \`display.price\_scale + display.status\_line\` will display the plot only in the price scale and status line. When \`display\` arguments such as \`display.price\_scale\` have user-controlled chart settings equivalents, the relevant plot information will only appear when all settings allow for it. possible values: [display.none](#var_display.none), [display.pane](#var_display.pane), [display.data_window](#var_display.data_window), [display.price_scale](#var_display.price_scale), [display.status_line](#var_display.status_line), [display.all](#var_display.all). optional. the default is [display.all](#var_display.all).

### Example


```s

//@version=5
indicator("plotshape example 1", overlay=true)
data = close >= open
plotshape(data, style=shape.xcross)


```

### Remarks

use [plotshape](#fun_plotshape) function in conjunction with 'overlay=true' [indicator](#fun_indicator) parameter!

### See also

* [plot](#fun_plot)
* [plotchar](#fun_plotchar)
* [plotarrow](#fun_plotarrow)
* [barcolor](#fun_barcolor)
* [bgcolor](#fun_bgcolor)

## polyline.delete

deletes the specified [polyline](#op_polyline) object. it has no effect if the \`id\` doesn't exist.

### Syntax

polyline.delete(id) - void

### Arguments

- `id`

    >  (`series` `polyline`)
    
    >  the polyline iD to delete.

## polyline.new

Creates a new [polyline](#op_polyline) instance and displays it on the chart, sequentially connecting all of the points in the \`points\` array with line segments. the segments in the drawing can be straight or curved depending on the \`curved\` parameter.

### Syntax

polyline.new(points, curved, closed, xloc, line\_color, fill\_color, line\_style, line\_width) → series polyline

### Arguments

- `points`

    >  (`chart.point`\[\])
    
    >  an array of [chart.point](#op_chart.point) objects for the drawing to sequentially connect.

- `curved`

    >  (`series` `bool`)
    
    >  if [true](#op_true), the drawing will connect all points from the \`points\` array using curved line segments. optional. the default is [false](#op_false).

- `closed`

    >  (`series` `bool`)
    
    >  if [true](#op_true), the drawing will also connect the first point to the last point from the \`points\` array, resulting in a closed polyline. optional. the default is [false](#op_false).

- `xloc`

    >  (`series` `string`)
    
    >  Determines the field of the [chart.point](#op_chart.point) objects in the \`points\` array that the polyline will use for its x-coordinates. if [xloc.bar_index](#var_xloc.bar_index), the polyline will use the \`index\` field from each point. if [xloc.bar_time](#var_xloc.bar_time), it will use the \`time\` field. optional. the default is [xloc.bar_index](#var_xloc.bar_index).

- `line_color`

    >  (`series` `color`)
    
    >  the color of the line segments. optional. the default is [color.blue](#var_color.blue).

- `fill_color`

    >  (`series` `color`)
    
    >  the fill color of the polyline. optional. the default is [na](#var_na).

- `line_style`

    >  (`series` `string`)
    
    >  the style of the polyline. possible values: [line.style_solid](#var_line.style_solid), [line.style_dotted](#var_line.style_dotted), [line.style_dashed](#var_line.style_dashed), [line.style\_arrow\_left](#var_line.style_arrow_left), [line.style\_arrow\_right](#var_line.style_arrow_right), [line.style\_arrow\_both](#var_line.style_arrow_both). optional. the default is [line.style_solid](#var_line.style_solid).

- `line_width`

    >  (`series` `int`)
    
    >  the width of the line segments, expressed in pixels. optional. the default is 1.

### Example


```s

//@version=5
indicator("polylines example", overlay = true)

//@variable if `true`, connects all points in the polyline with curved line segments.
bool curvedinput = input.bool(false, "Curve polyline")
//@variable if `true`, connects the first point in the polyline to the last point.
bool closedinput = input.bool(true,  "Close polyline")
//@variable the color of the space filled by the polyline.
color fillcolor = input.color(color.new(color.blue, 90), "Fill color")

// time and price inputs for the polyline's points.
p1x = input.time(0,  "p1", confirm = true, inline = "p1")
p1y = input.price(0, "  ", confirm = true, inline = "p1")
p2x = input.time(0,  "p2", confirm = true, inline = "p2")
p2y = input.price(0, "  ", confirm = true, inline = "p2")
p3x = input.time(0,  "p3", confirm = true, inline = "p3")
p3y = input.price(0, "  ", confirm = true, inline = "p3")
p4x = input.time(0,  "p4", confirm = true, inline = "p4")
p4y = input.price(0, "  ", confirm = true, inline = "p4")
p5x = input.time(0,  "p5", confirm = true, inline = "p5")
p5y = input.price(0, "  ", confirm = true, inline = "p5")

if barstate.islastconfirmedhistory
    //@variable an array of `chart.point` objects for the new polyline.
    var points = array.new<chart.point>()
    // push new `chart.point` instances into the `points` array.
    points.push(chart.point.from_time(p1x, p1y))
    points.push(chart.point.from_time(p2x, p2y))
    points.push(chart.point.from_time(p3x, p3y))
    points.push(chart.point.from_time(p4x, p4y))
    points.push(chart.point.from_time(p5x, p5y))
    // add labels for each `chart.point` in `points`.
    l1p1 = label.new(points.get(0), text = "p1", xloc = xloc.bar_time, color = na)
    l1p2 = label.new(points.get(1), text = "p2", xloc = xloc.bar_time, color = na)
    l2p1 = label.new(points.get(2), text = "p3", xloc = xloc.bar_time, color = na)
    l2p2 = label.new(points.get(3), text = "p4", xloc = xloc.bar_time, color = na)
    // Create a new polyline that connects each `chart.point` in the `points` array, starting from the first.
    polyline.new(points, curved = curvedinput, closed = closedinput, fill_color = fillcolor, xloc = xloc.bar_time)


```

### Returns

the iD of a new polyline object that a script can use in other \`polyline.*()\` functions.

### See also

* [chart.point.new](#fun_chart.point.new)

## request.currency_rate

provides a daily rate that can be used to convert a value expressed in the \`from\` currency to another in the \`to\` currency.

### Syntax

request.currency\_rate(from, to, ignore\_invalid_currency) → series float

### Arguments

- `from`

    >  (`simple` `string`)
    
    >  the currency in which the value to be converted is expressed. possible values: a three-letter string with the [currency code in the isO 4217 format](https://en.wikipedia.org/wiki/isO_4217#active_codes) (e.g. "usD"), or one of the built-in variables that return currency codes, like [syminfo.currency](#var_syminfo.currency) or [currency.usD](#var_currency.usD).

- `to`

    >  (`simple` `string`)
    
    >  the currency in which the value is to be converted. possible values: a three-letter string with the [currency code in the isO 4217 format](https://en.wikipedia.org/wiki/isO_4217#active_codes) (e.g. "usD"), or one of the built-in variables that return currency codes, like [syminfo.currency](#var_syminfo.currency) or [currency.usD](#var_currency.usD).

- `ignore\_invalid\_currency`

    >  (`simple` `bool`)
    
    >  Determines the behavior of the function if a conversion rate between the two currencies cannot be calculated: if [false](#op_false), the script will halt and return a runtime error; if [true](#op_true), the function will return [na](#var_na) and execution will continue. optional. the default is [false](#op_false).

### Example


```s

//@version=5
indicator("Close in british pounds")
rate = request.currency_rate(syminfo.currency, "Gbp")
plot(close * rate)


```

### Remarks

if \`from\` and \`to\` arguments are equal, function returns 1. please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

## request.dividends

Requests dividends data for the specified symbol.

### Syntax

request.dividends(ticker, field, gaps, lookahead, ignore\_invalid\_symbol, currency) → series float

### Arguments

- `ticker`

    >  (`simple` `string`)
    
    >  symbol. Note that the symbol should be passed with a prefix. For example: "NasDaq:aapL" instead of "aapL". using [syminfo.ticker](#var_syminfo.ticker) will cause an error. use [syminfo.tickerid](#var_syminfo.tickerid) instead.

- `field`

    >  (`simple` `string`)
    
    >  input string. possible values include: [dividends.net](#var_dividends.net), [dividends.gross](#var_dividends.gross). Default value is [dividends.gross](#var_dividends.gross).

- `gaps`

    >  (`simple` `barmerge_gaps`)
    
    >  Merge strategy for the requested data (requested data automatically merges with the main series OHLC data). possible values: [barmerge.gaps_on](#var_barmerge.gaps_on), [barmerge.gaps_off](#var_barmerge.gaps_off). [barmerge.gaps_on](#var_barmerge.gaps_on) \- requested data is merged with possible gaps ([na](#var_na) values). [barmerge.gaps_off](#var_barmerge.gaps_off) \- requested data is merged continuously without gaps, all the gaps are filled with the previous nearest existing values. Default value is [barmerge.gaps_off](#var_barmerge.gaps_off).

- `lookahead`

    >  (`simple` `barmerge_lookahead`)
    
    >  Merge strategy for the requested data position. possible values: [barmerge.lookahead_on](#var_barmerge.lookahead_on), [barmerge.lookahead_off](#var_barmerge.lookahead_off). Default value is [barmerge.lookahead_off](#var_barmerge.lookahead_off) starting from version 3. Note that behavour is the same on real-time, and differs only on history.

- `ignore\_invalid\_symbol`

    >  (`input` `bool`)
    
    >  an optional parameter. Determines the behavior of the function if the specified symbol is not found: if false, the script will halt and return a runtime error; if true, the function will return na and execution will continue. the default value is false.

- `currency`

    >  (`simple` `string`)
    
    >  Currency into which the symbol's currency-related dividends values (e.g. [dividends.gross](#var_dividends.gross)) are to be converted. the conversion rates used are based on the FX_iDC pairs' daily rates of the previous day (relative to the bar where the calculation is done). optional. the default is [syminfo.currency](#var_syminfo.currency). possible values: a three-letter string with the [currency code in the isO 4217 format](https://en.wikipedia.org/wiki/isO_4217#active_codes) (e.g. "usD") or one of the constants in the currency.* namespace, e.g. [currency.usD](#var_currency.usD).

### Example


```s

//@version=5
indicator("request.dividends")
s1 = request.dividends("NasDaq:bELFa")
plot(s1)
s2 = request.dividends("NasDaq:bELFa", dividends.net, gaps=barmerge.gaps_on, lookahead=barmerge.lookahead_on)
plot(s2)


```

### Returns

Requested series, or n/a if there is no dividends data for the specified symbol.

### See also

* [request.earnings](#fun_request.earnings)
* [request.splits](#fun_request.splits)
* [request.security](#fun_request.security)
* [syminfo.tickerid](#var_syminfo.tickerid)

## request.earnings

Requests earnings data for the specified symbol.

### Syntax

request.earnings(ticker, field, gaps, lookahead, ignore\_invalid\_symbol, currency) → series float

### Arguments

- `ticker`

    >  (`simple` `string`)
    
    >  symbol. Note that the symbol should be passed with a prefix. For example: "NasDaq:aapL" instead of "aapL". using [syminfo.ticker](#var_syminfo.ticker) will cause an error. use [syminfo.tickerid](#var_syminfo.tickerid) instead.

- `field`

    >  (`simple` `string`)
    
    >  input string. possible values include: [earnings.actual](#var_earnings.actual), [earnings.estimate](#var_earnings.estimate), [earnings.standardized](#var_earnings.standardized). Default value is [earnings.actual](#var_earnings.actual).

- `gaps`

    >  (`simple` `barmerge_gaps`)
    
    >  Merge strategy for the requested data (requested data automatically merges with the main series OHLC data). possible values: [barmerge.gaps_on](#var_barmerge.gaps_on), [barmerge.gaps_off](#var_barmerge.gaps_off). [barmerge.gaps_on](#var_barmerge.gaps_on) \- requested data is merged with possible gaps ([na](#var_na) values). [barmerge.gaps_off](#var_barmerge.gaps_off) \- requested data is merged continuously without gaps, all the gaps are filled with the previous nearest existing values. Default value is [barmerge.gaps_off](#var_barmerge.gaps_off).

- `lookahead`

    >  (`simple` `barmerge_lookahead`)
    
    >  Merge strategy for the requested data position. possible values: [barmerge.lookahead_on](#var_barmerge.lookahead_on), [barmerge.lookahead_off](#var_barmerge.lookahead_off). Default value is [barmerge.lookahead_off](#var_barmerge.lookahead_off) starting from version 3. Note that behavour is the same on real-time, and differs only on history.

- `ignore\_invalid\_symbol`

    >  (`input` `bool`)
    
    >  an optional parameter. Determines the behavior of the function if the specified symbol is not found: if false, the script will halt and return a runtime error; if true, the function will return na and execution will continue. the default value is false.

- `currency`

    >  (`simple` `string`)
    
    >  Currency into which the symbol's currency-related earnings values (e.g. [earnings.actual](#var_earnings.actual)) are to be converted. the conversion rates used are based on the FX_iDC pairs' daily rates of the previous day (relative to the bar where the calculation is done). optional. the default is [syminfo.currency](#var_syminfo.currency). possible values: a three-letter string with the [currency code in the isO 4217 format](https://en.wikipedia.org/wiki/isO_4217#active_codes) (e.g. "usD") or one of the constants in the currency.* namespace, e.g. [currency.usD](#var_currency.usD).

### Example


```s

//@version=5
indicator("request.earnings")
s1 = request.earnings("NasDaq:bELFa")
plot(s1)
s2 = request.earnings("NasDaq:bELFa", earnings.actual, gaps=barmerge.gaps_on, lookahead=barmerge.lookahead_on)
plot(s2)


```

### Returns

Requested series, or n/a if there is no earnings data for the specified symbol.

### See also

* [request.dividends](#fun_request.dividends)
* [request.splits](#fun_request.splits)
* [request.security](#fun_request.security)
* [syminfo.tickerid](#var_syminfo.tickerid)

## request.economic

Requests economic data for a symbol. Economic data includes information such as the state of a country's economy (GDp, inflation rate, etc.) or of a particular industry (steel production, iCu beds, etc.).

### Syntax

request.economic(country\_code, field, gaps, ignore\_invalid_symbol) → series float

### Arguments

- `country_code`

    >  (`simple` `string`)
    
    >  the code of the country (e.g. "us") or the region (e.g. "Eu") for which the economic data is requested. the [Help center article](https://www.tradingview.com/chart/?solution=43000665359) lists the countries and their codes. the countries for which information is available vary with metrics. the [Help center article for each metric](https://www.tradingview.com/support/folders/43000581956-list-of-available-economic-indicators/) lists the countries for which the metric is available.

- `field`

    >  (`simple` `string`)
    
    >  the code of the requested economic metric (e.g., "GDp"). the [Help center article](https://www.tradingview.com/chart/?solution=43000665359) lists the metrics and their codes.

- `gaps`

    >  (`simple` `barmerge_gaps`)
    
    >  specifies how the returned values are merged on chart bars. possible values: [barmerge.gaps_off](#var_barmerge.gaps_off), [barmerge.gaps_on](#var_barmerge.gaps_on). With [barmerge.gaps_on](#var_barmerge.gaps_on), a value only appears on the current chart bar when it first becomes available from the function's context, otherwise [na](#var_na) is returned (thus a "gap" occurs). With [barmerge.gaps_off](#var_barmerge.gaps_off), what would otherwise be gaps are filled with the latest known value returned, avoiding [na](#var_na) values. optional. the default is [barmerge.gaps_off](#var_barmerge.gaps_off).

- `ignore\_invalid\_symbol`

    >  (`input` `bool`)
    
    >  Determines the behavior of the function if the specified symbol is not found: if [false](#op_false), the script will halt and return a runtime error; if [true](#op_true), the function will return [na](#var_na) and execution will continue. optional. the default is [false](#op_false).

### Example


```s

//@version=5
indicator("us GDp")
e = request.economic("us", "GDp")
plot(e)


```

### Returns

Requested series.

### Remarks

Economic data can also be accessed from charts, just like a regular symbol. use "ECONOMiC" as the exchange name and `{country_code}{field}` as the ticker. the name of us GDp data is thus "ECONOMiC:usGDp".

### See also

* [request.financial](#fun_request.financial)
* [request.quandl](#fun_request.quandl)

## request.financial

Requests financial series for symbol.

### Syntax

request.financial(symbol, financial\_id, period, gaps, ignore\_invalid_symbol, currency) → series float

### Arguments

- `symbol`

    >  (`simple` `string`)
    
    >  symbol. Note that the symbol should be passed with a prefix. For example: "NasDaq:aapL" instead of "aapL".

- `financial_id`

    >  (`simple` `string`)
    
    >  Financial identifier. You can find the list of available ids via our [Help center](https://www.tradingview.com/?solution=43000564727).

- `period`

    >  (`simple` `string`)
    
    >  Reporting period. possible values are "ttM", "FY", "Fq", "FH".

- `gaps`

    >  (`simple` `barmerge_gaps`)
    
    >  Merge strategy for the requested data (requested data automatically merges with the main series: OHLC data). possible values include: [barmerge.gaps_on](#var_barmerge.gaps_on), [barmerge.gaps_off](#var_barmerge.gaps_off). [barmerge.gaps_on](#var_barmerge.gaps_on) \- requested data is merged with possible gaps ([na](#var_na) values). [barmerge.gaps_off](#var_barmerge.gaps_off) \- requested data is merged continuously without gaps, all the gaps are filled with the previous, nearest existing values. Default value is [barmerge.gaps_off](#var_barmerge.gaps_off).

- `ignore\_invalid\_symbol`

    >  (`input` `bool`)
    
    >  an optional parameter. Determines the behavior of the function if the specified symbol is not found: if false, the script will halt and return a runtime error; if true, the function will return na and execution will continue. the default value is false.

- `currency`

    >  (`simple` `string`)
    
    >  Currency into which the symbol's financial metrics (e.g. Net income) are to be converted. the conversion rates used are based on the FX_iDC pairs' daily rates of the previous day (relative to the bar where the calculation is done). optional. the default is [syminfo.currency](#var_syminfo.currency). possible values: a three-letter string with the [currency code in the isO 4217 format](https://en.wikipedia.org/wiki/isO_4217#active_codes) (e.g. "usD") or one of the constants in the currency.* namespace, e.g. [currency.usD](#var_currency.usD).

### Example


```s

//@version=5
indicator("request.financial")
f = request.financial("NasDaq:MsFT", "aCCOuNTs_paYabLE", "FY")
plot(f)


```

### Returns

Requested series.

### See also

* [request.security](#fun_request.security)
* [syminfo.tickerid](#var_syminfo.tickerid)

## request.quandl

Requests [Nasdaq data link](https://data.nasdaq.com/) (formerly quandl) data for a symbol.

### Syntax

request.quandl(ticker, gaps, index, ignore\_invalid\_symbol) → series float

### Arguments

- `ticker`

    >  (`simple` `string`)
    
    >  symbol. Note that the name of a time series and quandl data feed should be divided by a forward slash. For example: "CFTC/sb\_FO\_aLL".

- `gaps`

    >  (`simple` `barmerge_gaps`)
    
    >  Merge strategy for the requested data (requested data automatically merges with the main series: OHLC data). possible values include: [barmerge.gaps_on](#var_barmerge.gaps_on), [barmerge.gaps_off](#var_barmerge.gaps_off). [barmerge.gaps_on](#var_barmerge.gaps_on) \- requested data is merged with possible gaps ([na](#var_na) values). [barmerge.gaps_off](#var_barmerge.gaps_off) \- requested data is merged continuously without gaps, all the gaps are filled with the previous, nearest existing values. Default value is [barmerge.gaps_off](#var_barmerge.gaps_off).

- `index`

    >  (`simple` `int`)
    
    >  a quandl time-series column index.

- `ignore\_invalid\_symbol`

    >  (`input` `bool`)
    
    >  an optional parameter. Determines the behavior of the function if the specified symbol is not found: if false, the script will halt and return a runtime error; if true, the function will return na and execution will continue. the default value is false.

### Example


```s

//@version=5
indicator("request.quandl")
f = request.quandl("CFTC/sb_FO_aLL", barmerge.gaps_off, 0)
plot(f)


```

### Returns

Requested series.

### Remarks

You can learn more about how to find ticker and index values in our [Help center](https://www.tradingview.com/chart/?solution=43000568613).

### See also

* [request.security](#fun_request.security)
* [syminfo.tickerid](#var_syminfo.tickerid)

## request.security

Requests data from another symbol and/or timeframe.

### Syntax

request.security(symbol, timeframe, expression, gaps, lookahead, ignore\_invalid\_symbol, currency) → series <type>;

### Arguments

- `symbol`

    >  (`simple` `string`)
    
    >  symbol to request the data from. use [syminfo.tickerid](#var_syminfo.tickerid) to request data from the chart's symbol. To request data with additional parameters (extended sessions, dividend adjustments, or a non-standard chart type like Heikin ashi or Renko), a custom ticker identifier must first be created using functions in the \`ticker.*\` namespace.

- `timeframe`

    >  (`simple` `string`)
    
    >  timeframe of the requested data. To use the chart's timeframe, use an empty string or the [timeframe.period](#var_timeframe.period) variable. Valid timeframe strings are documented in the user Manual's [timeframes](https://www.tradingview.com/pine-script-docs/en/v5/concepts/timeframes.html#timeframe-string-specifications) page.

- `expression`

    >  (`variable`, `function`, `object`, `array` `or` `matrix` `of` `series` `int`/`float`/`bool`/`string`/`color`, `or` `a` `tuple` `of` `these`)
    
    >  an expression to be calculated and returned from the [request.security](#fun_request.security) call's context. it can be a built-in variable like [close](#var_close), an expression such as \`ta.sma(close, 100)\`, a non-mutable user-defined variable previously calculated in the script, a function call that does not use pine script(r) drawings, an array, a matrix, or a tuple. Mutable variables are not allowed, unless they are enclosed in the body of a function used in the expression.

- `gaps`

    >  (`simple` `barmerge_gaps`)
    
    >  specifies how the returned values are merged on chart bars. possible values: [barmerge.gaps_on](#var_barmerge.gaps_on), [barmerge.gaps_off](#var_barmerge.gaps_off). With [barmerge.gaps_on](#var_barmerge.gaps_on) a value only appears on the current chart bar when it first becomes available from the function's context, otherwise [na](#var_na) is returned (thus a "gap" occurs). With [barmerge.gaps_off](#var_barmerge.gaps_off) what would otherwise be gaps are filled with the latest known value returned, avoiding [na](#var_na) values. optional. the default is [barmerge.gaps_off](#var_barmerge.gaps_off).

- `lookahead`

    >  (`simple` `barmerge_lookahead`)
    
    >  On historical bars only, returns data from the timeframe before it elapses. possible values: [barmerge.lookahead_on](#var_barmerge.lookahead_on), [barmerge.lookahead_off](#var_barmerge.lookahead_off). Has no effect on realtime values. optional. the default is [barmerge.lookahead_off](#var_barmerge.lookahead_off) starting from pine script(r) v3. the default is [barmerge.lookahead_on](#var_barmerge.lookahead_on) in v1 and v2. WaRNiNG: using [barmerge.lookahead_on](#var_barmerge.lookahead_on) at timeframes higher than the chart's without offsetting the \`expression\` argument like in \`close\[1\]\` will introduce future leak in scripts, as the function will then return the \`close\` price before it is actually known in the current context. as is explained in the user Manual's page on [Repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html#future-leak-with-request-security) this will produce misleading results.

- `ignore\_invalid\_symbol`

    >  (`input` `bool`)
    
    >  Determines the behavior of the function if the specified symbol is not found: if [false](#op_false), the script will halt and throw a runtime error; if [true](#op_true), the function will return [na](#var_na) and execution will continue. optional. the default is [false](#op_false).

- `currency`

    >  (`simple` `string`)
    
    >  Currency into which values expressed in currency units ([open](#var_open), [high](#var_high), [low](#var_low), [close](#var_close), etc.) or expressions using such values are to be converted. the conversion rates used are based on the FX_iDC pairs' daily rates of the previous day (relative to the bar where the calculation is done). possible values: a three-letter string with the [currency code in the isO 4217 format](https://en.wikipedia.org/wiki/isO_4217#active_codes) (e.g. "usD") or one of the constants in the currency.* namespace, e.g. [currency.usD](#var_currency.usD). Note that literal values such as \`200\` are not converted. optional. the default is [syminfo.currency](#var_syminfo.currency).

### Example


```s

//@version=5
indicator("simple `request.security()` calls")
// Returns 1D close of the current symbol.
dailyClose = request.security(syminfo.tickerid, "1D", close)
plot(dailyClose)

// Returns the close of "aapL" from the same timeframe as currently open on the chart.
aaplClose = request.security("aapL", timeframe.period, close)
plot(aaplClose)



```

### Example


```s

//@version=5
indicator("advanced `request.security()` calls")
// this calculates a 10-period moving average on the active chart.
sma = ta.sma(close, 10)
// this sends the `sma` calculation for execution in the context of the "aapL" symbol at a "240" (4 hours) timeframe.
aaplsma = request.security("aapL", "240", sma)
plot(aaplsma)

// To avoid differences on historical and realtime bars, you can use this technique, which only returns a value from the higher timeframe on the bar after it completes:
indexHighTF = barstate.isrealtime ? 1 : 0
indexCurrtF = barstate.isrealtime ? 0 : 1
nonRepaintingClose = request.security(syminfo.tickerid, "1D", close[indexHighTF])
* [indexCurrtF]
plot(nonRepaintingClose, "Non-repainting close")

// Returns the 1H close of "aapL", extended session included. the value is dividend-adjusted.
extendedticker = ticker.modify("NasDaq:aapL", session = session.extended, adjustment = adjustment.dividends)
aaplExtadj = request.security(extendedticker, "60", close)
plot(aaplExtadj)

// Returns the result of a user-defined function.
// the `max` variable is mutable, but we can pass it to `request.security()` because it is wrapped in a function.
alltimeHigh(source) =>
    var max = source
    max := math.max(max, source)
alltimeHigh1D = request.security(syminfo.tickerid, "1D", alltimeHigh(high))

// by using a tuple `expression`, we obtain several values with only one `request.security()` call.
> [open1D, high1D, low1D, close1D, ema1D] = request.security(syminfo.tickerid, "1D", [open, high, low, close, ta.ema(close, 10)])
plotcandle(open1D, high1D, low1D, close1D)
plot(ema1D)

// Returns an array containing the OHLC values of the chart's symbol from the 1D timeframe.
ohlcarray = request.security(syminfo.tickerid, "1D", array.from(open, high, low, close))
plotcandle(array.get(ohlcarray, 0), array.get(ohlcarray, 1), array.get(ohlcarray, 2), array.get(ohlcarray, 3))


```

### Returns

a result determined by \`expression\`.

### Remarks

pine script(r) code using this function may calculate differently on historical and realtime bars, leading to [repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

a single script can have no more than 40 calls to \`request.*()\` functions.

### See also

* [syminfo.ticker](#var_syminfo.ticker)
* [syminfo.tickerid](#var_syminfo.tickerid)
* [timeframe.period](#var_timeframe.period)
* [ticker.new](#fun_ticker.new)
* [ticker.modify](#fun_ticker.modify)
* [request.security\_lower\_tf](#fun_request.security_lower_tf)
* [request.dividends](#fun_request.dividends)
* [request.earnings](#fun_request.earnings)
* [request.splits](#fun_request.splits)
* [request.financial](#fun_request.financial)
* [request.quandl](#fun_request.quandl)

## request.security\_lower\_tf

Requests data from a specified symbol from a lower timeframe than the chart's. the function returns an array containing one element for each closed lower timeframe intrabar inside the current chart's bar. On a 5-minute chart using a \`timeframe\` argument of "1", the size of the array will usually be 5, with each array element representing the value of \`expression\` on a 1-minute intrabar, ordered sequentially in time.

### Syntax

request.security\_lower\_tf(symbol, timeframe, expression, ignore\_invalid\_symbol, currency, ignore\_invalid\_timeframe) - array<type>;

### Arguments

- `symbol`

    >  (`simple` `string`)
    
    >  symbol to request the data from. use [syminfo.tickerid](#var_syminfo.tickerid) to request data from the chart's symbol. To request data with additional parameters (extended sessions, dividend adjustments, or a non-standard chart type like Heikin ashi or Renko), a custom ticker identifier must first be created using functions in the \`ticker.*\` namespace.

- `timeframe`

    >  (`simple` `string`)
    
    >  timeframe of the requested data. To use the chart's timeframe, use an empty string or the [timeframe.period](#var_timeframe.period) variable. Valid timeframe strings are documented in the user Manual's [timeframes](https://www.tradingview.com/pine-script-docs/en/v5/concepts/timeframes.html#timeframe-string-specifications) page.

- `expression`

    >  (`variable`, `object` `or` `function` `of` `series` `int`/`float`/`bool`/`string`/`color`, `or` `a` `tuple` `of` `these`)
    
    >  an expression to be calculated and returned from the function call's context. it can be a built-in variable like [close](#var_close), an expression such as \`ta.sma(close, 100)\`, a non-mutable user-defined variable previously calculated in the script, a function call that does not use pine script(r) drawings, arrays or matrices, or a tuple. Mutable variables are not allowed, unless they are enclosed in the body of a function used in the expression.

- `ignore\_invalid\_symbol`

    >  (`const` `bool`)
    
    >  Determines the behavior of the function if the specified symbol is not found: if [false](#op_false), the script will halt and throw a runtime error; if [true](#op_true), the function will return [na](#var_na) and execution will continue. optional. the default is [false](#op_false).

- `currency`

    >  (`simple` `string`)
    
    >  Currency into which values expressed in currency units ([open](#var_open), [high](#var_high), [low](#var_low), [close](#var_close), etc.) or expressions using such values are to be converted. the conversion rates used are based on the FX_iDC pairs' daily rates of the previous day (relative to the bar where the calculation is done). possible values: a three-letter string with the [currency code in the isO 4217 format](https://en.wikipedia.org/wiki/isO_4217#active_codes) (e.g. "usD") or one of the constants in the currency.* namespace, e.g. [currency.usD](#var_currency.usD). Note that literal values such as \`200\` are not converted. optional. the default is [syminfo.currency](#var_syminfo.currency).

- `ignore\_invalid\_timeframe`

    >  (`const` `bool`)
    
    >  Determines the behavior of the function when the chart's timeframe is smaller than the \`timeframe\` used in the function call. if [false](#op_false), the script will halt and throw a runtime error. if [true](#op_true), the function will return [na](#var_na) and execution will continue. optional. the default is [false](#op_false).

### Example


```s

//@version=5
indicator("`request.security_lower_tf()` Example", overlay = true)

// if the current chart timeframe is set to 120 minutes, then the `arrayClose` array will contain two 'close' values from the 60 minute timeframe for each bar.
arrClose = request.security_lower_tf(syminfo.tickerid, "60", close)

if bar_index == last_bar_index - 1
    label.new(bar_index, high, str.tostring(arrClose))


```

### Returns

an array of a type determined by \`expression\`, or a tuple of these.

### Remarks

pine script(r) code using this function may calculate differently on historical and real-time bars, leading to [repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

please note that spreads (e.g., "aapL+MsFT*TsLa") will not always return reliable data with this function.

a single script can have no more than 40 calls to \`request.*()\` functions.

a maximum of 100,000 lower timeframe bars can be accessed by this function. the number of chart bars for which lower timeframe data is available will thus vary with the requested lower timeframe.

### See also

* [request.security](#fun_request.security)
* [syminfo.ticker](#var_syminfo.ticker)
* [syminfo.tickerid](#var_syminfo.tickerid)
* [timeframe.period](#var_timeframe.period)
* [ticker.new](#fun_ticker.new)
* [request.dividends](#fun_request.dividends)
* [request.earnings](#fun_request.earnings)
* [request.splits](#fun_request.splits)
* [request.financial](#fun_request.financial)
* [request.quandl](#fun_request.quandl)

## request.seed

Requests data from a user-maintained Github repository and returns it as a series. an in-depth tutorial on how to add new data can be found [here](https://github.com/tradingview-eod/pine-seeds-docs).

### Syntax

request.seed(source, symbol, expression, ignore\_invalid\_symbol) → series <type>;

### Arguments

- `source`

    >  (`simple` `string`)
    
    >  Name of the Github repository.

- `symbol`

    >  (`simple` `string`)
    
    >  Name of the file in the Github repository containing the data. the ".csv" file extension must not be included.

- `expression`

    >  (<`arg`\`_expr`\`_type`>;)
    
    >  an expression to be calculated and returned from the requested symbol's context. it can be a built-in variable like [close](#var_close), an expression such as \`ta.sma(close, 100)\`, a non-mutable variable previously calculated in the script, a function call that does not use pine script(r) drawings, an array, a matrix, or a tuple. Mutable variables are not allowed, unless they are enclosed in the body of a function used in the expression.

- `ignore\_invalid\_symbol`

    >  (`input` `bool`)
    
    >  Determines the behavior of the function if the specified symbol is not found: if [false](#op_false), the script will halt and throw a runtime error; if [true](#op_true), the function will return [na](#var_na) and execution will continue. optional. the default is [false](#op_false).

### Example


```s

//@version=5
indicator("bTC Development activity")

> [devact, devactsMa] = request.seed("seed_crypto_santiment", "bTC_DEV_aCTiViTY", [close, ta.sma(close, 10)])

plot(devact, "bTC Development activity")
plot(devactsMa, "bTC Development activity sMa10", color = color.yellow)


```

### Returns

Requested series or tuple of series, which may include array/matrix iDs.

## request.splits

Requests splits data for the specified symbol.

### Syntax

request.splits(ticker, field, gaps, lookahead, ignore\_invalid\_symbol) → series float

### Arguments

- `ticker`

    >  (`simple` `string`)
    
    >  symbol. Note that the symbol should be passed with a prefix. For example: "NasDaq:aapL" instead of "aapL". using [syminfo.ticker](#var_syminfo.ticker) will cause an error. use [syminfo.tickerid](#var_syminfo.tickerid) instead.

- `field`

    >  (`simple` `string`)
    
    >  input string. possible values include: [splits.denominator](#var_splits.denominator), [splits.numerator](#var_splits.numerator).

- `gaps`

    >  (`simple` `barmerge_gaps`)
    
    >  Merge strategy for the requested data (requested data automatically merges with the main series OHLC data). possible values: [barmerge.gaps_on](#var_barmerge.gaps_on), [barmerge.gaps_off](#var_barmerge.gaps_off). [barmerge.gaps_on](#var_barmerge.gaps_on) \- requested data is merged with possible gaps ([na](#var_na) values). [barmerge.gaps_off](#var_barmerge.gaps_off) \- requested data is merged continuously without gaps, all the gaps are filled with the previous nearest existing values. Default value is [barmerge.gaps_off](#var_barmerge.gaps_off).

- `lookahead`

    >  (`simple` `barmerge_lookahead`)
    
    >  Merge strategy for the requested data position. possible values: [barmerge.lookahead_on](#var_barmerge.lookahead_on), [barmerge.lookahead_off](#var_barmerge.lookahead_off). Default value is [barmerge.lookahead_off](#var_barmerge.lookahead_off) starting from version 3. Note that behavour is the same on real-time, and differs only on history.

- `ignore\_invalid\_symbol`

    >  (`input` `bool`)
    
    >  an optional parameter. Determines the behavior of the function if the specified symbol is not found: if false, the script will halt and return a runtime error; if true, the function will return na and execution will continue. the default value is false.

### Example


```s

//@version=5
indicator("request.splits")
s1 = request.splits("NasDaq:bELFa", splits.denominator)
plot(s1)
s2 = request.splits("NasDaq:bELFa", splits.denominator, gaps=barmerge.gaps_on, lookahead=barmerge.lookahead_on)
plot(s2)


```

### Returns

Requested series, or n/a if there is no splits data for the specified symbol.

### See also

* [request.earnings](#fun_request.earnings)
* [request.dividends](#fun_request.dividends)
* [request.security](#fun_request.security)
* [syminfo.tickerid](#var_syminfo.tickerid)

## runtime.error

When called, causes a runtime error with the error message specified in the \`message\` argument.

### Syntax

runtime.error(message) - void

### Arguments

- `message`

    >  (`series` `string`)
    
    >  Error message.

## second

+1 overload

### syntax & Overloads

> [second(time) → series int](#fun_second-0)
> [second(time, timezone) → series int](#fun_second-1)

### Arguments

- `time`

    >  (`series` `int`)
    
    >  unix time in milliseconds.

### Returns

second (in exchange timezone) for provided unix time.

### Remarks

unix time is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

### See also

* [second](#var_second)
* [time](#fun_time)
* [year](#fun_year)
* [month](#fun_month)
* [dayofmonth](#fun_dayofmonth)
* [dayofweek](#fun_dayofweek)
* [hour](#fun_hour)
* [minute](#fun_minute)

## str.contains

+2 overloads

Returns true if the \`source\` string contains the \`str\` substring, false otherwise.

### syntax & Overloads

> [str.contains(source, str) → const bool](#fun_str.contains-0)
> [str.contains(source, str) → simple bool](#fun_str.contains-1)
> [str.contains(source, str) → series bool](#fun_str.contains-2)

### Arguments

- `source`

    >  (`const` `string`)
    
    >  source string.

- `str`

    >  (`const` `string`)
    
    >  the substring to search for.

### Example


```s

//@version=5
indicator("str.contains")
// if the current chart is a continuous futures chart, e.g aEURoebTC1!aEUR, then the function will return true, false otherwise.
var isFutures = str.contains(syminfo.tickerid, "!")
plot(isFutures ? 1 : 0)


```

### Returns

true if the \`str\` was found in the \`source\` string, false otherwise.

### See also

* [str.pos](#fun_str.pos)
* [str.match](#fun_str.match)

## str.endswith

+2 overloads

Returns true if the \`source\` string ends with the substring specified in \`str\`, false otherwise.

### syntax & Overloads

> [str.endswith(source, str) → const bool](#fun_str.endswith-0)
> [str.endswith(source, str) → simple bool](#fun_str.endswith-1)
> [str.endswith(source, str) → series bool](#fun_str.endswith-2)

### Arguments

- `source`

    >  (`const` `string`)
    
    >  source string.

- `str`

    >  (`const` `string`)
    
    >  the substring to search for.

### Returns

true if the \`source\` string ends with the substring specified in \`str\`, false otherwise.

### See also

* [str.startswith](#fun_str.startswith)

## str.format

+1 overload

Converts the formatting string and value(s) into a formatted string. the formatting string can contain literal text and one placeholder in curly braces {} for each value to be formatted. Each placeholder consists of the index of the required argument (beginning at 0) that will replace it, and an optional format specifier. the index represents the position of that argument in the str.format argument list.

### syntax & Overloads

> [str.format(formatstring, arg0, arg1, ...) → simple string](#fun_str.format-0)
> [str.format(formatstring, arg0, arg1, ...) → series string](#fun_str.format-1)

### Arguments

- `formatstring`

    >  (`simple` `string`)
    
    >  format string.

- `arg0, arg1, ...`

    >  (`simple` `int`/`float`/`bool`/`string`)
    
    >  Values to format.

### Example


```s

//@version=5
indicator("str.format", overlay=true)
// the format specifier inside the curly braces accepts certain modifiers:
// - specify the number of decimals to display:
s1 = str.format("{0,number,#.#}", 1.34) // returns: 1.3
label.new(bar_index, close, text=s1)
// - Round a float value to an integer:
s2 = str.format("{0,number,integer}", 1.34) // returns: 1
label.new(bar_index - 1, close, text=s2)
// - Display a number in currency:
s3 = str.format("{0,number,currency}", 1.34) // returns: $1.34
label.new(bar_index - 2, close, text=s3)
// - Display a number as a percentage:
s4 = str.format("{0,number,percent}", 0.5) // returns: 50%
label.new(bar_index - 3, close, text=s4)


// Examples With Several Arguments

// returns: Number 1 is not equal to 4
s5 = str.format("Number {0} is not {1} to {2}", 1, "equal", 4)
label.new(bar_index - 4, close, text=s5)

// returns: 1.34 != 1.3
s6 = str.format("{0} != {0, number, #.#}", 1.34)
label.new(bar_index - 5, close, text=s6)

// returns: 1 is equal to 1, but 2 is equal to 2
s7 = str.format("{0, number, integer} is equal to 1, but {1, number, integer} is equal to 2", 1.34, 1.52)
label.new(bar_index - 6, close, text=s7)

// returns: the cash turnover amounted to $1,340,000.00
s8 = str.format("the cash turnover amounted to {0, number, currency}", 1340000)
label.new(bar_index - 7, close, text=s8)

// returns: Expected return is 10% - 20%
s9 = str.format("Expected return is {0, number, percent} - {1, number, percent}", 0.1, 0.2)
label.new(bar_index - 8, close, text=s9)

```

### Returns

the formatted string.

### Remarks

any curly braces within an unquoted pattern must be balanced. For example, "ab {0} de" and "ab '}' de" are valid patterns, but "ab {0'}' de", "ab } de" and "''{''" are not.

## str.format_time

Converts the \`time\` timestamp into a string formatted according to \`format\` and \`timezone\`.

### Syntax

str.format_time(time, format, timezone) → series string

### Arguments

- `time`

    >  (`series` `int`)
    
    >  unix time, in milliseconds.

- `format`

    >  (`series` `string`)
    
    >  a format string specifying the date/time representation of the \`time\` in the returned string. all letters used in the string, except those escaped by single quotation marks `'`, are considered formatting tokens and will be used as a formatting instruction. Refer to the Remarks section for a list of the most useful tokens. optional. the default is "yyyy-MM-dd'T'HH:mm:ssZ", which represents the isO 8601 standard.

- `timezone`

    >  (`series` `string`)
    
    >  allows adjusting the returned value to a time zone specified in either uTC/GMT notation (e.g., "uTC-5", "GMT+0530") or as an [iaNa time zone database name](https://en.wikipedia.org/wiki/list_of_tz_database_time_zones) (e.g., "america/New_York"). optional. the default is [syminfo.timezone](#var_syminfo.timezone).

### Example


```s

//@version=5
indicator("str.format_time")
if timeframe.change("1D")
    formattedtime = str.format_time(time, "yyyy-MM-dd HH:mm", syminfo.timezone)
    label.new(bar_index, high, formattedtime)


```

### Returns

the formatted string.

### Remarks

> the \`M\`, \`d\`, \`h\`, \`H\`, \`m\` and \`s\` tokens can all be doubled to generate leading zeroes. For example, the month of January will display as \`1\` with \`M\`, or \`01\` with \`MM\`.

#### the most frequently used formatting tokens are:

  > y - Year. use \y`y\` to output the last two digits of the year or \y`yyy\` to output all four. Year 2000 will be \`00\` with \y`y\` or \`2000\` with \y`yyy\`.

  > M - Month. Not to be confused with lowercase \`m\`, which stands for minute.

  > d - Day of the month.

  > a - aM/pM postfix.

  > h - Hour in the 12-hour format. the last hour of the day will be \`11\` in this format.

  > H - Hour in the 24-hour format. the last hour of the day will be \`23\` in this format.

  > m - Minute.

  > s - second.

  > s - Fractions of a second.

  > Z - timezone, the HHmm offset from uTC, preceded by either `+` or `-`.

## str.length

+2 overloads

Returns an integer corresponding to the amount of chars in that string.

### syntax & Overloads

> [str.length(string) → const int](#fun_str.length-0)
> [str.length(string) → simple int](#fun_str.length-1)
> [str.length(string) → series int](#fun_str.length-2)

### Arguments

- `string`

    >  (`const` `string`)
    
    >  source string.

### Returns

the number of chars in source string.

## str.lower

+2 overloads

Returns a new string with all letters converted to lowercase.

### syntax & Overloads

> [str.lower(source) → const string](#fun_str.lower-0)
> [str.lower(source) → simple string](#fun_str.lower-1)
> [str.lower(source) → series string](#fun_str.lower-2)

### Arguments

- `source`

    >  (`const` `string`)
    
    >  string to be converted.

### Returns

a new string with all letters converted to lowercase.

### See also

* [str.upper](#fun_str.upper)

## str.match

+1 overload

Returns the new substring of the \`source\` string if it matches a \`regex\` regular expression, an empty string otherwise.

### syntax & Overloads

> [str.match(source, regex) → simple string](#fun_str.match-0)
> [str.match(source, regex) → series string](#fun_str.match-1)

### Arguments

- `source`

    >  (`simple` `string`)
    
    >  source string.

- `regex`

    >  (`simple` `string`)
    
    >  the regular expression to which this string is to be matched.

### Example


```s

//@version=5
indicator("str.match")

s = input.string("it's time to sell some NasDaq:aapL!")

// finding first substring that matches regular expression "[\w]+:[\w]+"
var string tickerid = str.match(s, "[\w]+:[\w]+")

if barstate.islastconfirmedhistory
    label.new(bar_index, high, text = tickerid) // "NasDaq:aapL"


```

### Returns

the new substring of the \`source\` string if it matches a \`regex\` regular expression, an empty string otherwise.

### Remarks

Function returns first occurrence of the [regular expression](https://en.wikipedia.org/wiki/Regular_expression#perl_and_pCRE) in the \`source\` string.

the backslash "\" symbol in the\`regex\` string needs to be escaped with additional backslash, e.g. "\\d" stands for regular expression "\d".

### See also

* [str.contains](#fun_str.contains)
* [str.substring](#fun_str.substring)

## str.pos

+2 overloads

Returns the position of the first occurrence of the \`str\` string in the \`source\` string, 'na' otherwise.

### syntax & Overloads

> [str.pos(source, str) → const int](#fun_str.pos-0)
> [str.pos(source, str) → simple int](#fun_str.pos-1)
> [str.pos(source, str) → series int](#fun_str.pos-2)

### Arguments

- `source`

    >  (`const` `string`)
    
    >  source string.

- `str`

    >  (`const` `string`)
    
    >  the substring to search for.

### Returns

position of the \`str\` string in the \`source\` string.

### Remarks

strings indexing starts at 0.

### See also

* [str.contains](#fun_str.contains)
* [str.match](#fun_str.match)
* [str.substring](#fun_str.substring)

## str.replace

+2 overloads

Returns a new string with the Nth occurrence of the \`target\` string replaced by the \`replacement\` string, where N is specified in \`occurrence\`.

### syntax & Overloads

> [str.replace(source, target, replacement, occurrence) → const string](#fun_str.replace-0)
> [str.replace(source, target, replacement, occurrence) → simple string](#fun_str.replace-1)
> [str.replace(source, target, replacement, occurrence) → series string](#fun_str.replace-2)

### Arguments

- `source`

    >  (`const` `string`)
    
    >  source string.

- `target`

    >  (`const` `string`)
    
    >  string to be replaced.

- `replacement`

    >  (`const` `string`)
    
    >  string to be inserted instead of the target string.

- `occurrence`

    >  (`const` `int`)
    
    >  N-th occurrence of the target string to replace. indexing starts at 0 for the first match. optional. Default value is 0.

### Example


```s

//@version=5
indicator("str.replace")
var source = "FTX:bTCusD / FTX:bTCEuR"

// Replace first occurrence of "FTX" with "biNaNCE" replacement string
var newsource = str.replace(source, "FTX",  "biNaNCE", 0)

if barstate.islastconfirmedhistory
    // Display "biNaNCE:bTCusD / FTX:bTCEuR"
    label.new(bar_index, high, text = newsource)


```

### Returns

processed string.

### See also

* [str.replace_all](#fun_str.replace_all)
* [str.match](#fun_str.match)

## str.replace_all

+1 overload

Replaces each occurrence of the target string in the source string with the replacement string.

### syntax & Overloads

> [str.replace_all(source, target, replacement) → simple string](#fun_str.replace_all-0)
> [str.replace_all(source, target, replacement) → series string](#fun_str.replace_all-1)

### Arguments

- `source`

    >  (`simple` `string`)
    
    >  source string.

- `target`

    >  (`simple` `string`)
    
    >  string to be replaced.

- `replacement`

    >  (`simple` `string`)
    
    >  string to be substituted for each occurrence of target string.

### Returns

processed string.

## str.split

divides a string into an array of substrings and returns its array id.

### Syntax

str.split(string, separator) - string\[\]

### Arguments

- `string`

    >  (`series` `string`)
    
    >  source string.

- `separator`

    >  (`series` `string`)
    
    >  the string separating each substring.

### Returns

the id of an array of strings.

## str.startswith

+2 overloads

Returns true if the \`source\` string starts with the substring specified in \`str\`, false otherwise.

### syntax & Overloads

> [str.startswith(source, str) → const bool](#fun_str.startswith-0)
> [str.startswith(source, str) → simple bool](#fun_str.startswith-1)
> [str.startswith(source, str) → series bool](#fun_str.startswith-2)

### Arguments

- `source`

    >  (`const` `string`)
    
    >  source string.

- `str`

    >  (`const` `string`)
    
    >  the substring to search for.

### Returns

true if the \`source\` string starts with the substring specified in \`str\`, false otherwise.

### See also

* [str.endswith](#fun_str.endswith)

## str.substring

+5 overloads

Returns a new string that is a substring of the \`source\` string. the substring begins with the character at the index specified by \`begin\_pos\` and extends to 'end\_pos - 1' of the \`source\` string.

### syntax & Overloads

> [str.substring(source, begin_pos) → const string](#fun_str.substring-0)
> [str.substring(source, begin_pos) → simple string](#fun_str.substring-1)
> [str.substring(source, begin_pos) → series string](#fun_str.substring-2)
> [str.substring(source, begin\_pos, end\_pos) → const string](#fun_str.substring-3)
> [str.substring(source, begin\_pos, end\_pos) → simple string](#fun_str.substring-4)
> [str.substring(source, begin\_pos, end\_pos) → series string](#fun_str.substring-5)

### Arguments

- `source`

    >  (`const` `string`)
    
    >  source string from which to extract the substring.

- `begin_pos`

    >  (`const` `int`)
    
    >  the beginning position of the extracted substring. it is inclusive (the extracted substring includes the character at that position).

### Example


```s

//@version=5
indicator("str.substring", overlay = true)
sym= input.symbol("NasDaq:aapL")
pos = str.pos(sym, ":")  // Get position of ":" character
tkr= str.substring(sym, pos+1) // "aapL"
if barstate.islastconfirmedhistory
    label.new(bar_index, high, text = tkr)


```

### Returns

the substring extracted from the source string.

### Remarks

strings indexing starts from 0. if \`begin\_pos\` is equal to \`end\_pos\`, the function returns an empty string.

### See also

* [str.contains](#fun_str.contains)
* [str.pos](#fun_str.pos)
* [str.match](#fun_str.match)

## str.tonumber

+3 overloads

Converts a value represented in \`string\` to its "float" equivalent.

### syntax & Overloads

> [str.tonumber(string) → const float](#fun_str.tonumber-0)
> [str.tonumber(string) → input float](#fun_str.tonumber-1)
> [str.tonumber(string) → simple float](#fun_str.tonumber-2)
> [str.tonumber(string) → series float](#fun_str.tonumber-3)

### Arguments

- `string`

    >  (`const` `string`)
    
    >  string containing the representation of an integer or floating point value.

### Returns

a "float" equivalent of the value in \`string\`. if the value is not a properly formed integer or floating point value, the function returns [na](#var_na).

## str.tostring

+3 overloads

### syntax & Overloads

> [str.tostring(value) → simple string](#fun_str.tostring-0)
> [str.tostring(value) → series string](#fun_str.tostring-1)
> [str.tostring(value, format) → simple string](#fun_str.tostring-2)
> [str.tostring(value, format) → series string](#fun_str.tostring-3)

### Arguments

- `value`

    >  (`simple` `int`/`float`)
    
    >  Value or array iD whose elements are converted to a string.

### Returns

the string representation of the \`value\` argument.

if the \`value\` argument is a string, it is returned as is.

When the \`value\` is na, the function returns the string "NaN".

### Remarks

the formatting of float values will also round those values when necessary, e.g. str.tostring(3.99, '#') will return "4".

To display trailing zeros, use '0' instead of '#'. For example, '#.000'.

When using [format.mintick](#var_format.mintick), the value will be rounded to the nearest number that can be divided by [syminfo.mintick](#var_syminfo.mintick) without the remainder. the string is returned with trailing zeroes.

if the x argument is a string, the same string value will be returned.

bool type arguments return "true" or "false".

When x is na, the function returns "NaN".

## str.upper

+2 overloads

Returns a new string with all letters converted to uppercase.

### syntax & Overloads

> [str.upper(source) → const string](#fun_str.upper-0)
> [str.upper(source) → simple string](#fun_str.upper-1)
> [str.upper(source) → series string](#fun_str.upper-2)

### Arguments

- `source`

    >  (`const` `string`)
    
    >  string to be converted.

### Returns

a new string with all letters converted to uppercase.

### See also

* [str.lower](#fun_str.lower)

## strategy

this declaration statement designates the script as a strategy and sets a number of strategy-related properties.

### Syntax

strategy(title, shorttitle, overlay, format, precision, scale, pyramiding, calc\_on\_order\_fills, calc\_on\_every\_tick, max\_bars\_back, backtest\_fill\_limits\_assumption, default\_qty\_type, default\_qty\_value, initial\_capital, currency, slippage, commission\_type, commission\_value, process\_orders\_on\_close, close\_entries\_rule, margin\_long, margin\_short, explicit\_plot\_zorder, max\_lines\_count, max\_labels\_count, max\_boxes\_count, risk\_free\_rate, use\_bar\_magnifier, max\_polylines_count) - void

### Arguments

- `title`

    >  (`const` `string`)
    
    >  the title of the script. it is displayed on the chart when no \`shorttitle\` argument is used, and becomes the publication's default title when publishing the script.

- `shorttitle`

    >  (`const` `string`)
    
    >  the script's display name on charts. if specified, it will replace the \`title\` argument in most chart-related windows. optional. the default is the argument used for \`title\`.

- `overlay`

    >  (`const` `bool`)
    
    >  if [true](#op_true), the strategy will be displayed over the chart. if [false](#op_false), it will be added in a separate pane. strategy-specific labels that display entries and exits will be displayed over the main chart regardless of this setting. optional. the default is [false](#op_false).

- `format`

    >  (`const` `string`)
    
    >  specifies the formatting of the script's displayed values. possible values: [format.inherit](#var_format.inherit), [format.price](#var_format.price), [format.volume](#var_format.volume), [format.percent](#var_format.percent). optional. the default is [format.inherit](#var_format.inherit).

- `precision`

    >  (`const` `int`)
    
    >  specifies the number of digits after the floating point of the script's displayed values. Must be a non-negative integer no greater than 16. if \`format\` is set to [format.inherit](#var_format.inherit) and \`precision\` is specified, the format will instead be set to [format.price](#var_format.price). optional. the default is inherited from the precision of the chart's symbol.

- `scale`

    >  (`const` `scale_type`)
    
    >  the price scale used. possible values: [scale.right](#var_scale.right), [scale.left](#var_scale.left), [scale.none](#var_scale.none). the [scale.none](#var_scale.none) value can only be applied in combination with \`overlay = true\`. optional. by default, the script uses the same scale as the chart.

- `pyramiding`

    >  (`const` `int`)
    
    >  the maximum number of entries allowed in the same direction. if the value is 0, only one entry order in the same direction can be opened, and additional entry orders are rejected. this setting can also be changed in the strategy's "settings/properties" tab. optional. the default is 0.

- `calc\_on\_order_fills`

    >  (`const` `bool`)
    
    >  specifies whether the strategy should be recalculated after an order is filled. if [true](#op_true), the strategy recalculates after an order is filled, as opposed to recalculating only when the bar closes. this setting can also be changed in the strategy's "settings/properties" tab. optional. the default is [false](#op_false).

- `calc\_on\_every_tick`

    >  (`const` `bool`)
    
    >  specifies whether the strategy should be recalculated on each realtime tick. if [true](#op_true), when the strategy is running on a realtime bar, it will recalculate on each chart update. if [false](#op_false), the strategy only calculates when the realtime bar closes. the argument used does not affect strategy calculation on historical data. this setting can also be changed in the strategy's "settings/properties" tab. optional. the default is [false](#op_false).

- `max\_bars\_back`

    >  (`const` `int`)
    
    >  the length of the historical buffer the script keeps for every variable and function, which determines how many past values can be referenced using the `\[\]` history-referencing operator. the required buffer size is automatically detected by the pine script(r) runtime. using this parameter is only necessary when a runtime error occurs because automatic detection fails. More information on the underlying mechanics of the historical buffer can be found [in our Help center](https://www.tradingview.com/chart/?solution=43000587849). optional. the default is 0.

- `backtest\_fill\_limits_assumption`

    >  (`const` `int`)
    
    >  limit order execution threshold in ticks. When it is used, limit orders are only filled if the market price exceeds the order's limit level by the specified number of ticks. optional. the default is 0.

- `default\_qty\_type`

    >  (`const` `string`)
    
    >  specifies the units used for \`default\_qty\_value\`. possible values are: [strategy.fixed](#var_strategy.fixed) for contracts/shares/lots, [strategy.cash](#var_strategy.cash) for currency amounts, or [strategy.percent\_of\_equity](#var_strategy.percent_of_equity) for a percentage of available equity. this setting can also be changed in the strategy's "settings/properties" tab. optional. the default is [strategy.fixed](#var_strategy.fixed).

- `default\_qty\_value`

    >  (`const` `int`/`float`)
    
    >  the default quantity to trade, in units determined by the argument used with the \`default\_qty\_type\` parameter. this setting can also be changed in the strategy's "settings/properties" tab. optional. the default is 1.

- `initial_capital`

    >  (`const` `int`/`float`)
    
    >  the amount of funds initially available for the strategy to trade, in units of \`currency\`. optional. the default is 1000000.

- `currency`

    >  (`const` `string`)
    
    >  Currency used by the strategy in currency-related calculations. market positions are still opened by converting \`currency\` into the chart symbol's currency. the conversion rates used are based on the FX_iDC pairs' daily rates of the previous day (relative to the bar where the calculation is done). this setting can also be changed in the strategy's "settings/properties" tab. optional. the default is [currency.NONE](#var_currency.NONE), in which case the chart's currency is used. possible values: one of the constants in the \`currency.*\` namespace, e.g. [currency.usD](#var_currency.usD).

- `slippage`

    >  (`const` `int`)
    
    >  slippage expressed in ticks. this value is added to or subtracted from the fill price of market/stop orders to make the fill price less favorable for the strategy. E.g., if [syminfo.mintick](#var_syminfo.mintick) is 0.01 and \`slippage\` is set to 5, a long market order will enter at 5 * 0.01 = 0.05 points above the actual price. this setting can also be changed in the strategy's "settings/properties" tab. optional. the default is 0.

- `commission_type`

    >  (`const` `string`)
    
    >  Determines what the number passed to the \`commission_value\` expresses: [strategy.commission.percent](#var_strategy.commission.percent) for a percentage of the cash volume of the order, [strategy.commission.cash\_per\_contract](#var_strategy.commission.cash_per_contract) for currency per contract, [strategy.commission.cash\_per\_order](#var_strategy.commission.cash_per_order) for currency per order. this setting can also be changed in the strategy's "settings/properties" tab. optional. the default is [strategy.commission.percent](#var_strategy.commission.percent).

- `commission_value`

    >  (`const` `int`/`float`)
    
    >  Commission applied to the strategy's orders in units determined by the argument passed to the \`commission_type\` parameter. this setting can also be changed in the strategy's "settings/properties" tab. optional. the default is 0.

- `process\_orders\_on_close`

    >  (`const` `bool`)
    
    >  When set to [true](#op_true), generates an additional attempt to execute orders after a bar closes and strategy calculations are completed. if the orders are market orders, the broker emulator executes them before the next bar's open. if the orders are price-dependent, they will only be filled if the price conditions are met. this option is useful if you wish to close positions on the current bar. this setting can also be changed in the strategy's "settings/properties" tab. optional. the default is [false](#op_false).

- `close\_entries\_rule`

    >  (`const` `string`)
    
    >  Determines the order in which trades are closed. possible values are: "FiFO" (First-in, First-Out) if the earliest exit order must close the earliest entry order, or "aNY" if the orders are closed based on the \`from_entry\` parameter of the [strategy.exit](#fun_strategy.exit) function. "FiFO" can only be used with stocks, futures and us forex (NFa Compliance Rule 2-43b), while "aNY" is allowed in non-us forex. optional. the default is "FiFO".

- `margin_long`

    >  (`const` `int`/`float`)
    
    >  Margin long is the percentage of the purchase price of a security that must be covered by cash or collateral for long positions. Must be a non-negative number. the logic used to simulate margin calls is explained in the [Help center](https://www.tradingview.com/chart/?solution=43000628599). this setting can also be changed in the strategy's "settings/properties" tab. optional. the default is 0, in which case the strategy does not enforce any limits on position size.

- `margin_short`

    >  (`const` `int`/`float`)
    
    >  Margin short is the percentage of the purchase price of a security that must be covered by cash or collateral for short positions. Must be a non-negative number. the logic used to simulate margin calls is explained in the [Help center](https://www.tradingview.com/chart/?solution=43000628599). this setting can also be changed in the strategy's "settings/properties" tab. optional. the default is 0, in which case the strategy does not enforce any limits on position size.

- `explicit\_plot\_zorder`

    >  (`const` `bool`)
    
    >  specifies the order in which the script's plots, fills, and hlines are rendered. if [true](#op_true), plots are drawn in the order in which they appear in the script's code, each newer plot being drawn above the previous ones. this only applies to \`plot*()\` functions, [fill](#fun_fill), and [hline](#fun_hline). optional. the default is [false](#op_false).

- `max\_lines\_count`

    >  (`const` `int`)
    
    >  the number of last [line](#op_line) drawings displayed. possible values: 1-500. optional. the default is 50.

- `max\_labels\_count`

    >  (`const` `int`)
    
    >  the number of last [label](#op_label) drawings displayed. possible values: 1-500. optional. the default is 50.

- `max\_boxes\_count`

    >  (`const` `int`)
    
    >  the number of last [box](#op_box) drawings displayed. possible values: 1-500. optional. the default is 50.

- `risk\_free\_rate`

    >  (`const` `int`/`float`)
    
    >  the risk-free rate of return is the annual percentage change in the value of an investment with minimal or zero risk. it is used to calculate the [sharpe and sortino ratios](https://www.tradingview.com/chart/?solution=43000561856). optional. the default is 2.

- `use\_bar\_magnifier`

    >  (`const` `bool`)
    
    >  When true, the [broker emulator](https://www.tradingview.com/pine-script-docs/en/v5/concepts/strategies.html#broker-emulator) uses lower timeframe data during history backtesting to achieve more realistic results. optional. the default is [false](#op_false). Only [premium](https://www.tradingview.com/gopro/) accounts have access to this feature.

- `max\_polylines\_count`

    >  (`const` `int`)
    
    >  the number of last [polyline](#op_polyline) drawings displayed. possible values: 1-100. the count is approximate; more drawings than the specified count may be displayed. optional. the default is 50.

### Example


```s

//@version=5
strategy("My strategy", overlay = true, margin_long = 100, margin_short = 100)

// Enter long by market if current open is greater than previous high.
if open > high[1]
    strategy.entry("Long", strategy.long, 1)
// Generate a full exit bracket (profit 10 points, loss 5 points per contract) from the entry named "Long".
strategy.exit("Exit", "Long", profit = 10, loss = 5)


```

### Remarks

You can learn more about strategies in our [user Manual](https://www.tradingview.com/pine-script-docs/en/v5/concepts/strategies.html).

Every strategy script must have one [strategy](#fun_strategy) call.

strategies using \`calc\_on\_every_tick = true\` parameter may calculate differently on historical and realtime bars, which causes [repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

strategies always use the chart's prices to enter and exit positions. using them on non-standard chart types (Heikin ashi, Renko, etc.) will produce misleading results, as their prices are synthetic. backtesting on non-standard charts is thus not recommended.

### See also

* [indicator](#fun_indicator)
* [library](#fun_library)

## strategy.cancel

it is a command to cancel/deactivate pending orders by referencing their names, which were generated by the functions: [strategy.order](#fun_strategy.order), [strategy.entry](#fun_strategy.entry) and [strategy.exit](#fun_strategy.exit).

### Syntax

strategy.cancel(id) - void

### Arguments

- `id`

    >  (`series` `string`)
    
    >  a required parameter. the order identifier. it is possible to cancel an order by referencing its identifier.

### Example


```s

//@version=5
strategy(title = "simple order cancellation example")
conditionForbuy = open > high[1]
if conditionForbuy
    strategy.entry("long", strategy.long, 1, limit = low) // enter long using limit order at low price of current bar if conditionForbuy is true
if not conditionForbuy
    strategy.cancel("long") // cancel the entry order with name "long" if conditionForbuy is false


## strategy.cancel_all
a command to cancel/deactivate all pending orders generated by any of the following functions: strategy.order, strategy.entry, strategy.exit, and strategy.close.

### Syntax

strategy.cancel_all() → void


### Example

//@version=5
strategy(title = "simple all orders cancellation example")
conditionForbuy1 = open > high[1]
if conditionForbuy1
    strategy.entry("long entry 1", strategy.long, 1, limit = low) // enter long by limit if conditionForbuy1 is true
conditionForbuy2 = conditionForbuy1 and open[1] > high[2]
if conditionForbuy2
    strategy.entry("long entry 2", strategy.long, 1, limit = ta.lowest(low, 2)) // enter long by limit if conditionForbuy2 is true
conditionForstoptrading = open < ta.lowest(low, 2)
if conditionForstoptrading
    strategy.cancel_all() // cancel both limit orders if the conditon conditionForstoptrading is true


## strategy.close
it is a command to exit from the entry with the specified iD. if there were multiple entry orders with the same iD, all of them are exited at once. if there are no open entries with the specified iD by the moment the command is triggered, the command will not come into effect. the command uses market order. Every entry is closed by a separate market order.

### Syntax

strategy.close(id, comment, qty, qty_percent, alert_message, immediately, disable_alert) → void

### Arguments

- `id`

    >  (`series` `string`)
    
    >  a required parameter. the order identifier. it is possible to close an order by referencing its identifier.
- `comment`

    >  (`series` `string`)
    
    >  an optional parameter. additional notes on the order.
- `qty`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. Number of contracts/shares/lots/units to exit a trade with. the default value is 'NaN'.
- `qty_percent`

    >  (`series` `int`/`float`)
    
    >  Defines the percentage (0-100) of the position to close. its priority is lower than that of the 'qty' parameter. optional. the default is 100.
- `alert_message`

    >  (`series` `string`)
    
    >  an optional parameter which replaces the {{strategy.order.alert_message}} placeholder when it is used in the "Create alert" dialog box's "Message" field.
- `immediately`

    >  (`series` `bool`)
    
    >  an optional parameter. if true, the closing order will be executed on the tick where it has been placed, ignoring the strategy parameters that restrict the order execution to the open of the next bar. the default is false.
- `disable_alert`

    >  (`series` `bool`)
    
    >  if true when the function creates an order, the strategy alert will not fire upon the execution of that order. the parameter accepts a 'series bool' argument, allowing users to control which orders will trigger alerts when they fill. optional. the default is false.


### Example

//@version=5
strategy("closeEntry Demo", overlay=false)
if open > close
    strategy.entry("buy", strategy.long)
if open < close
    strategy.close("buy", qty_percent = 50, comment = "close buy entry for 50%")
plot(strategy.position_size)

```

## strategy.close_all

+1 overload

Exits the current market position, making it flat.

### syntax & Overloads

> [strategy.close\_all(comment, alert\_message) - void](#fun_strategy.close_all-0)
> [strategy.close\_all(comment, alert\_message, immediately, disable_alert) - void](#fun_strategy.close_all-1)

### Arguments

- `comment`

    >  (`series` `string`)
    
    >  an optional parameter. additional notes on the order.

- `alert_message`

    >  (`series` `string`)
    
    >  an optional parameter which replaces the {{strategy.order.alert_message}} placeholder when it is used in the "Create alert" dialog box's "Message" field.

### Example


```s

//@version=5
strategy("closeall Demo", overlay=false)
if open > close
    strategy.entry("buy", strategy.long)
if open < close
    strategy.close_all(comment = "close all entries")
plot(strategy.position_size)

```

## strategy.closedtrades.commission

Returns the sum of entry and exit fees paid in the closed trade, expressed in [strategy.account_currency](#var_strategy.account_currency).

### Syntax

strategy.closedtrades.commission(trade_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("`strategy.closedtrades.commission` Example", commission_type = strategy.commission.percent, commission_value = 0.1)

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// plot total fees for the latest closed trade.
plot(strategy.closedtrades.commission(strategy.closedtrades - 1))


```

### See also

* [strategy](#fun_strategy)
* [strategy.opentrades.commission](#fun_strategy.opentrades.commission)

## strategy.closedtrades.entry\_bar\_index

Returns the bar_index of the closed trade's entry.

### Syntax

strategy.closedtrades.entry\_bar\_index(trade_num) → series int

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("strategy.closedtrades.entry_bar_index Example")
// Enter long trades on three rising bars; exit on two falling bars.
if ta.rising(close, 3)
    strategy.entry("Long", strategy.long)
if ta.falling(close, 2)
    strategy.close("Long")
// Function that calculates the average amount of bars in a trade.
avgbarspertrade() =>
    sumbarspertrade = 0
    for tradeNo = 0 to strategy.closedtrades - 1
        // Loop through all closed trades, starting with the oldest.
        sumbarspertrade += strategy.closedtrades.exit_bar_index(tradeNo) - strategy.closedtrades.entry_bar_index(tradeNo) + 1
    result = nz(sumbarspertrade / strategy.closedtrades)
plot(avgbarspertrade())


```

### See also

* [strategy.closedtrades.exit\_bar\_index](#fun_strategy.closedtrades.exit_bar_index)
* [strategy.opentrades.entry\_bar\_index](#fun_strategy.opentrades.entry_bar_index)

## strategy.closedtrades.entry_comment

Returns the comment message of the closed trade's entry, or [na](#var_na) if there is no entry with this \`trade_num\`.

### Syntax

strategy.closedtrades.entry\_comment(trade\_num) → series string

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("`strategy.closedtrades.entry_comment()` Example", overlay = true)

stopprice = open * 1.01

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))

if (longCondition)
    strategy.entry("Long", strategy.long, stop = stopprice, comment = str.tostring(stopprice, "#.####"))
    strategy.exit("EXiT", trail_points = 1000, trail_offset = 0)

var testtable = table.new(position.top_right, 1, 3, color.orange, border_width = 1)

if barstate.islastconfirmedhistory or barstate.isrealtime
    table.cell(testtable, 0, 0, 'Last closed trade:')
    table.cell(testtable, 0, 1, "Order stop price value: " + strategy.closedtrades.entry_comment(strategy.closedtrades - 1))
    table.cell(testtable, 0, 2, "actual Entry price: " + str.tostring(strategy.closedtrades.entry_price(strategy.closedtrades - 1)))


```

#.####"))    strategy.exit("EXiT", trail_points = 1000, trail_offset = 0)var testtable = table.new(position.top_right, 1, 3, color.orange, border_width = 1)if barstate.islastconfirmedhistory or barstate.isrealtime    table.cell(testtable, 0, 0, 'Last closed trade:')    table.cell(testtable, 0, 1, "Order stop price value: " + strategy.closedtrades.entry_comment(strategy.closedtrades - 1))    table.cell(testtable, 0, 2, "actual Entry price: " + str.tostring(strategy.closedtrades.entry_price(strategy.closedtrades - 1)))

### See also

* [strategy](#fun_strategy)
* [strategy.entry](#fun_strategy.entry)
* [strategy.closedtrades](#var_strategy.closedtrades)

## strategy.closedtrades.entry_id

Returns the id of the closed trade's entry.

### Syntax

strategy.closedtrades.entry\_id(trade\_num) → series string

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("strategy.closedtrades.entry_id Example", overlay = true)

// Enter a short position and close at the previous to last bar.
if bar_index == 1
    strategy.entry("short at bar #" + str.tostring(bar_index), strategy.short)
if bar_index == last_bar_index - 2
    strategy.close_all()

// Display iD of the last entry position.
if barstate.islastconfirmedhistory
    label.new(last_bar_index, high, "Last Entry iD is: " + strategy.closedtrades.entry_id(strategy.closedtrades - 1))


```

#" + str.tostring(bar_index), strategy.short)if bar_index == last_bar_index - 2    strategy.close_all()    // Display iD of the last entry position.if barstate.islastconfirmedhistory    label.new(last_bar_index, high, "Last Entry iD is: " + strategy.closedtrades.entry_id(strategy.closedtrades - 1))

### Returns

Returns the id of the closed trade's entry.

### Remarks

the function returns na if trade_num is not in the range: 0 to strategy.closedtrades-1.

### See also

* [strategy.closedtrades.entry\_bar\_index](#fun_strategy.closedtrades.entry_bar_index)
* [strategy.closedtrades.entry_price](#fun_strategy.closedtrades.entry_price)
* [strategy.closedtrades.entry_time](#fun_strategy.closedtrades.entry_time)

## strategy.closedtrades.entry_price

Returns the price of the closed trade's entry.

### Syntax

strategy.closedtrades.entry\_price(trade\_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("strategy.closedtrades.entry_price Example 1")

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Return the entry price for the latest  entry.
entryprice = strategy.closedtrades.entry_price(strategy.closedtrades - 1)

plot(entryprice, "Long entry price")



```

### Example

```
// Calculates the average profit percentage for all closed trades.

//@version=5
strategy("strategy.closedtrades.entry_price Example 2")

// strategy calls to create single short and long trades
if bar_index == last_bar_index - 15
    strategy.entry("Long Entry",  strategy.long)
else if bar_index == last_bar_index - 10
    strategy.close("Long Entry")
    strategy.entry("short", strategy.short)
else if bar_index == last_bar_index - 5
    strategy.close("short")

// Calculate profit for both closed trades.
profitpct = 0.0
for tradeNo = 0 to strategy.closedtrades - 1
    entryp = strategy.closedtrades.entry_price(tradeNo)
    exitp = strategy.closedtrades.exit_price(tradeNo)
    profitpct += (exitp - entryp) / entryp * strategy.closedtrades.size(tradeNo) * 100

// Calculate average profit percent for both closed trades.
avgprofitpct = nz(profitpct / strategy.closedtrades)

plot(avgprofitpct)


```

### See also

* [strategy.closedtrades.entry_price](#fun_strategy.closedtrades.entry_price)
* [strategy.closedtrades.exit_price](#fun_strategy.closedtrades.exit_price)
* [strategy.closedtrades.size](#fun_strategy.closedtrades.size)
* [strategy.closedtrades](#var_strategy.closedtrades)

## strategy.closedtrades.entry_time

Returns the unix time of the closed trade's entry.

### Syntax

strategy.closedtrades.entry\_time(trade\_num) → series int

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("strategy.closedtrades.entry_time Example", overlay = true)

// Enter long trades on three rising bars; exit on two falling bars.
if ta.rising(close, 3)
    strategy.entry("Long", strategy.long)
if ta.falling(close, 2)
    strategy.close("Long")

// Calculate the average trade duration
avgtradeDuration() =>
    sumtradeDuration = 0
    for i = 0 to strategy.closedtrades - 1
        sumtradeDuration += strategy.closedtrades.exit_time(i) - strategy.closedtrades.entry_time(i)
    result = nz(sumtradeDuration / strategy.closedtrades)

// Display average duration converted to seconds and formatted using 2 decimal points
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(avgtradeDuration() / 1000, "#.##") + " seconds")


```

#.##") + " seconds")

### See also

* [strategy.opentrades.entry_time](#fun_strategy.opentrades.entry_time)
* [strategy.closedtrades.exit_time](#fun_strategy.closedtrades.exit_time)
* [time](#var_time)

## strategy.closedtrades.exit\_bar\_index

Returns the bar_index of the closed trade's exit.

### Syntax

strategy.closedtrades.exit\_bar\_index(trade_num) → series int

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("strategy.closedtrades.exit_bar_index Example 1")

// strategy calls to place a single short trade. We enter the trade at the first bar and exit the trade at 10 bars before the last chart bar.
if bar_index == 0
    strategy.entry("short",  strategy.short)
if bar_index == last_bar_index - 10
    strategy.close("short")

// Calculate the amount of bars since the last closed trade.
barssinceClosed = strategy.closedtrades > 0 ? bar_index - strategy.closedtrades.exit_bar_index(strategy.closedtrades - 1) : na

plot(barssinceClosed, "bars since last closed trade")



```

### Example

```
// Calculates the average amount of bars per trade.

//@version=5
strategy("strategy.closedtrades.exit_bar_index Example 2")

// Enter long trades on three rising bars; exit on two falling bars.
if ta.rising(close, 3)
    strategy.entry("Long", strategy.long)
if ta.falling(close, 2)
    strategy.close("Long")

// Function that calculates the average amount of bars per trade.
avgbarspertrade() =>
    sumbarspertrade = 0
    for tradeNo = 0 to strategy.closedtrades - 1
        // Loop through all closed trades, starting with the oldest.
        sumbarspertrade += strategy.closedtrades.exit_bar_index(tradeNo) - strategy.closedtrades.entry_bar_index(tradeNo) + 1
    result = nz(sumbarspertrade / strategy.closedtrades)

plot(avgbarspertrade())


```

### See also

* [bar_index](#var_bar_index)
* [last\_bar\_index](#var_last_bar_index)

## strategy.closedtrades.exit_comment

Returns the comment message of the closed trade's exit, or [na](#var_na) if there is no entry with this \`trade_num\`.

### Syntax

strategy.closedtrades.exit\_comment(trade\_num) → series string

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("`strategy.closedtrades.exit_comment()` Example", overlay = true)

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))
if (longCondition)
    strategy.entry("Long", strategy.long)
    strategy.exit("Exit", stop = open * 0.95, limit = close * 1.05, trail_points = 100, trail_offset = 0, comment_profit = "Tp", comment_loss = "sL", comment_trailing = "traiL")

exitstats() =>
    int slCount = 0
    int tpCount = 0
    int trailCount = 0

    if strategy.closedtrades > 0
        for i = 0 to strategy.closedtrades - 1
            switch strategy.closedtrades.exit_comment(i)
                "Tp"    => tpCount    += 1
                "sL"    => slCount    += 1
                "traiL" => trailCount += 1
    [slCount, tpCount, trailCount]

var testtable = table.new(position.top_right, 1, 4, color.orange, border_width = 1)

if barstate.islastconfirmedhistory
    [slCount, tpCount, trailCount] = exitstats()
    table.cell(testtable, 0, 0, "Closed trades (" + str.tostring(strategy.closedtrades) +") stats:")
    table.cell(testtable, 0, 1, "stop Loss: " + str.tostring(slCount))
    table.cell(testtable, 0, 2, "Take profit: " + str.tostring(tpCount))
    table.cell(testtable, 0, 3, "trailing stop: " + str.tostring(trailCount))


```

### See also

* [strategy](#fun_strategy)
* [strategy.exit](#fun_strategy.exit)
* [strategy.close](#fun_strategy.close)
* [strategy.closedtrades](#fun_strategy.closedtrades)

## strategy.closedtrades.exit_id

Returns the id of the closed trade's exit.

### Syntax

strategy.closedtrades.exit\_id(trade\_num) → series string

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("strategy.closedtrades.exit_id Example", overlay = true)

// strategy calls to create single short and long trades
if bar_index == last_bar_index - 15
    strategy.entry("Long Entry",  strategy.long)
else if bar_index == last_bar_index - 10
    strategy.entry("short Entry", strategy.short)

// When a new open trade is detected then we create the exit strategy corresponding with the matching entry id
// We detect the correct entry id by determining if a position is long or short based on the position quantity
if ta.change(strategy.opentrades)
    possign = strategy.opentrades.size(strategy.opentrades - 1)
    strategy.exit(possign > 0 ? "sL Long Exit" : "sL short Exit", strategy.opentrades.entry_id(strategy.opentrades - 1), stop = possign > 0 ? high - ta.tr : low + ta.tr)

// When a new closed trade is detected then we place a label above the bar with the exit info
if ta.change(strategy.closedtrades)
    msg = "trade closed by: " + strategy.closedtrades.exit_id(strategy.closedtrades - 1)
    label.new(bar_index, high + (3 * ta.tr), msg)


```

### Returns

Returns the id of the closed trade's exit.

### Remarks

the function returns na if trade_num is not in the range: 0 to strategy.closedtrades-1.

### See also

* [strategy.closedtrades.exit\_bar\_index](#fun_strategy.closedtrades.exit_bar_index)
* [strategy.closedtrades.exit_price](#fun_strategy.closedtrades.exit_price)
* [strategy.closedtrades.exit_time](#fun_strategy.closedtrades.exit_time)

## strategy.closedtrades.exit_price

Returns the price of the closed trade's exit.

### Syntax

strategy.closedtrades.exit\_price(trade\_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("strategy.closedtrades.exit_price Example 1")

// We are creating a long trade every 5 bars
if bar_index % 5 == 0
    strategy.entry("Long",  strategy.long)
strategy.close("Long")

// Return the exit price from the latest closed trade.
exitprice = strategy.closedtrades.exit_price(strategy.closedtrades - 1)

plot(exitprice, "Long exit price")



```

### Example

```
// Calculates the average profit percentage for all closed trades.

//@version=5
strategy("strategy.closedtrades.exit_price Example 2")

// strategy calls to create single short and long trades.
if bar_index == last_bar_index - 15
    strategy.entry("Long Entry",  strategy.long)
else if bar_index == last_bar_index - 10
    strategy.close("Long Entry")
    strategy.entry("short", strategy.short)
else if bar_index == last_bar_index - 5
    strategy.close("short")

// Calculate profit for both closed trades.
profitpct = 0.0
for tradeNo = 0 to strategy.closedtrades - 1
    entryp = strategy.closedtrades.entry_price(tradeNo)
    exitp = strategy.closedtrades.exit_price(tradeNo)
    profitpct += (exitp - entryp) / entryp * strategy.closedtrades.size(tradeNo) * 100

// Calculate average profit percent for both closed trades.
avgprofitpct = nz(profitpct / strategy.closedtrades)

plot(avgprofitpct)


```

### See also

* [strategy.closedtrades.entry_price](#fun_strategy.closedtrades.entry_price)

## strategy.closedtrades.exit_time

Returns the unix time of the closed trade's exit.

### Syntax

strategy.closedtrades.exit\_time(trade\_num) → series int

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("strategy.closedtrades.exit_time Example 1")

// Enter long trades on three rising bars; exit on two falling bars.
if ta.rising(close, 3)
    strategy.entry("Long", strategy.long)
if ta.falling(close, 2)
    strategy.close("Long")

// Calculate the average trade duration.
avgtradeDuration() =>
    sumtradeDuration = 0
    for i = 0 to strategy.closedtrades - 1
        sumtradeDuration += strategy.closedtrades.exit_time(i) - strategy.closedtrades.entry_time(i)
    result = nz(sumtradeDuration / strategy.closedtrades)

// Display average duration converted to seconds and formatted using 2 decimal points.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(avgtradeDuration() / 1000, "#.##") + " seconds")



```

#.##") + " seconds")

### Example

```
// Reopens a closed trade after X seconds.

//@version=5
strategy("strategy.closedtrades.exit_time Example 2")

// strategy calls to emulate a single long trade at the first bar.
if bar_index == 0
    strategy.entry("Long", strategy.long)

reopenpositionafter(timesec) =>
    if strategy.closedtrades > 0
        if time - strategy.closedtrades.exit_time(strategy.closedtrades - 1) >= timesec * 1000
            strategy.entry("Long", strategy.long)

// Reopen last closed position after 120 sec.
reopenpositionafter(120)

if ta.change(strategy.opentrades)
    strategy.exit("Long", stop = low * 0.9, profit = high * 2.5)


```

### See also

* [strategy.closedtrades.entry_time](#fun_strategy.closedtrades.entry_time)

## strategy.closedtrades.max_drawdown

Returns the maximum drawdown of the closed trade, i.e., the maximum possible loss during the trade, expressed in [strategy.account_currency](#var_strategy.account_currency).

### Syntax

strategy.closedtrades.max\_drawdown(trade\_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("`strategy.closedtrades.max_drawdown` Example")

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Get the biggest max trade drawdown value from all of the closed trades.
maxtradeDrawDown() =>
    maxDrawdown = 0.0
    for tradeNo = 0 to strategy.closedtrades - 1
        maxDrawdown := math.max(maxDrawdown, strategy.closedtrades.max_drawdown(tradeNo))
    result = maxDrawdown

plot(maxtradeDrawDown(), "biggest max drawdown")


```

### Remarks

the function returns na if trade_num is not in the range: 0 to strategy.closedtrades - 1.

### See also

* [strategy.opentrades.max_drawdown](#fun_strategy.opentrades.max_drawdown)
* [strategy.max_drawdown](#fun_strategy.max_drawdown)

## strategy.closedtrades.max_runup

Returns the maximum run up of the closed trade, i.e., the maximum possible profit during the trade, expressed in [strategy.account_currency](#var_strategy.account_currency).

### Syntax

strategy.closedtrades.max\_runup(trade\_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("`strategy.closedtrades.max_runup` Example")

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Get the biggest max trade runup value from all of the closed trades.
maxtradeRunup() =>
    maxRunup = 0.0
    for tradeNo = 0 to strategy.closedtrades - 1
        maxRunup := math.max(maxRunup, strategy.closedtrades.max_runup(tradeNo))
    result = maxRunup

plot(maxtradeRunup(), "Max trade runup")


```

### See also

* [strategy.opentrades.max_runup](#fun_strategy.opentrades.max_runup)
* [strategy.max_drawdown](#fun_strategy.max_drawdown)

## strategy.closedtrades.profit

Returns the profit/loss of the closed trade. Losses are expressed as negative values.

### Syntax

strategy.closedtrades.profit(trade_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("`strategy.closedtrades.profit` Example")

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Calculate average gross profit by adding the difference between gross profit and commission.
avgGrossprofit() =>
    sumGrossprofit = 0.0
    for tradeNo = 0 to strategy.closedtrades - 1
        sumGrossprofit += strategy.closedtrades.profit(tradeNo) - strategy.closedtrades.commission(tradeNo)
    result = nz(sumGrossprofit / strategy.closedtrades)

plot(avgGrossprofit(), "average gross profit")


```

### See also

* [strategy.opentrades.profit](#fun_strategy.opentrades.profit)
* [strategy.closedtrades.commission](#fun_strategy.closedtrades.commission)

## strategy.closedtrades.size

Returns the direction and the number of contracts traded in the closed trade. if the value is > 0, the market position was long. if the value is < 0, the market position was short.

### Syntax

strategy.closedtrades.size(trade_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the closed trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("`strategy.closedtrades.size` Example 1")

// We calculate the max amt of shares we can buy.
amtshares = math.floor(strategy.equity / close)
// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long, qty = amtshares)
if bar_index % 20 == 0
    strategy.close("Long")

// plot the number of contracts traded in the last closed trade.
plot(strategy.closedtrades.size(strategy.closedtrades - 1), "Number of contracts traded")



```

### Example

```
// Calculates the average profit percentage for all closed trades.

//@version=5
strategy("`strategy.closedtrades.size` Example 2")

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")


// Calculate profit for both closed trades.
profitpct = 0.0
for tradeNo = 0 to strategy.closedtrades - 1
    entryp = strategy.closedtrades.entry_price(tradeNo)
    exitp = strategy.closedtrades.exit_price(tradeNo)
    profitpct += (exitp - entryp) / entryp * strategy.closedtrades.size(tradeNo) * 100

// Calculate average profit percent for both closed trades.
avgprofitpct = nz(profitpct / strategy.closedtrades)

plot(avgprofitpct)


```

### See also

* [strategy.opentrades.size](#fun_strategy.opentrades.size)
* [strategy.position_size](#var_strategy.position_size)
* [strategy.closedtrades](#var_strategy.closedtrades)
* [strategy.opentrades](#var_strategy.opentrades)

## strategy.convert\_to\_account

Converts the value from the currency that the symbol on the chart is traded in ([syminfo.currency](#var_syminfo.currency)) to the currency used by the strategy ([strategy.account_currency](#var_strategy.account_currency)).

### Syntax

strategy.convert\_to\_account(value) → series float

### Arguments

- `value`

    >  (`series` `int`/`float`)
    
    >  the value to be converted.

### Example


```s

//@version=5
strategy("`strategy.convert_to_account` Example 1", currency = currency.EuR)

plot(close, "Close price using default currency")
plot(strategy.convert_to_account(close), "Close price converted to strategy currency")



```

### Example

```
// Calculates the "buy and hold return" using your account's currency.

//@version=5
strategy("`strategy.convert_to_account` Example 2", currency = currency.EuR)

dateinput = input.time(timestamp("20 Jul 2021 00:00 +0300"), "From Date", confirm = true)

buyandHoldReturnpct(fromDate) =>
    if time >= fromDate
        money = close * syminfo.pointvalue
        var initialbal = strategy.convert_to_account(money)
        (strategy.convert_to_account(money) - initialbal) / initialbal * 100

plot(buyandHoldReturnpct(dateinput))


```

### See also

* [strategy](#fun_strategy)
* [strategy.convert\_to\_symbol](#fun_strategy.convert_to_symbol)

## strategy.convert\_to\_symbol

Converts the value from the currency used by the strategy ([strategy.account_currency](#var_strategy.account_currency)) to the currency that the symbol on the chart is traded in ([syminfo.currency](#var_syminfo.currency)).

### Syntax

strategy.convert\_to\_symbol(value) → series float

### Arguments

- `value`

    >  (`series` `int`/`float`)
    
    >  the value to be converted.

### Example


```s

//@version=5
strategy("`strategy.convert_to_symbol` Example", currency = currency.EuR)

// Calculate the max qty we can buy using current chart's currency.
calcContracts(accountMoney) =>
    math.floor(strategy.convert_to_symbol(accountMoney) / syminfo.pointvalue / close)

// Return max qty we can buy using 300 euros
qt = calcContracts(300)

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars using our custom qty.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long, qty = qt)
if bar_index % 20 == 0
    strategy.close("Long")


```

### See also

* [strategy](#fun_strategy)
* [strategy.convert\_to\_account](#fun_strategy.convert_to_account)

## strategy.default\_entry\_qty

Calculates the default quantity, in units, of an entry order from [strategy.entry](#fun_strategy.entry) or [strategy.order](#fun_strategy.order) if it were to fill at the specified \`fill\_price\` value. the calculation depends on several strategy properties, including \`default\_qty\_type\`, \`default\_qty_value\`, \`currency\`, and other parameters in the [strategy](#fun_strategy) function and their representation in the "properties" tab of the strategy's settings.

### Syntax

strategy.default\_entry\_qty(fill_price) → series float

### Arguments

- `fill_price`

    >  (`series` `int`/`float`)
    
    >  the fill price for which to calculate the default order quantity.

### Example


```s

//@version=5
strategy("supertrend strategy", overlay = true, default_qty_type = strategy.percent_of_equity, default_qty_value = 15)

//@variable the length of the atr calculation.
atrperiod = input(10, "atr Length")
//@variable the atr multiplier.
factor = input.float(3.0, "Factor", step = 0.01)
//@variable the tick offset of the stop order.
stopOffsetinput = input.int(100, "Tick offset for entry stop")

// Get the direction of the supertrend.
> [_, direction] = ta.supertrend(factor, atrperiod)

if ta.change(direction) < 0
    //@variable the stop price of the entry order.
    stopprice = close + syminfo.mintick * stopOffsetinput
    //@variable the expected default fill quantity at the `stopprice`. this value may not reflect actual qty of the filled order, because fill price may be different.
    calculatedqty = strategy.default_entry_qty(stopprice)
    strategy.entry("My Long Entry id", strategy.long, stop = stopprice)
    label.new(bar_index, stopprice, str.format("stop set at {0}
Expected qty at {0}: {1}", math.round_to_mintick(stopprice), calculatedqty))

if ta.change(direction) > 0
    strategy.close_all()


```

### Remarks

this function does not consider open positions simulated by a strategy. For example, if a strategy script has an open position from a long order with a \`qty\` of 10 units, using the [strategy.entry](#fun_strategy.entry) function to simulate a short order with a \`qty\` of 5 will prompt the script to sell 15 units to reverse the position. this function will still return 5 in such a case since it doesn't consider an open trade.

this value represents the default calculated quantity of an order.

Order placement commands can override the default value by explicitly passing a new \`qty\` value in the function call.

## strategy.entry

it is a command to enter market position. if an order with the same iD is already pending, it is possible to modify the order. if there is no order with the specified iD, a new order is placed. To deactivate an entry order, the command [strategy.cancel](#fun_strategy.cancel) or [strategy.cancel_all](#fun_strategy.cancel_all) should be used. in comparison to the function [strategy.order](#fun_strategy.order), the function [strategy.entry](#fun_strategy.entry) is affected by pyramiding and it can reverse market position correctly. if both 'limit' and 'stop' parameters are 'NaN', the order type is market order.

### Syntax

strategy.entry(id, direction, qty, limit, stop, oca\_name, oca\_type, comment, alert\_message, disable\_alert) - void

### Arguments

- `id`

    >  (`series` `string`)
    
    >  a required parameter. the order identifier. it is possible to cancel or modify an order by referencing its identifier.

- `direction`

    >  (`series` `strategy_direction`)
    
    >  a required parameter. market position direction: 'strategy.long' is for long, 'strategy.short' is for short.

- `qty`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. Number of contracts/shares/lots/units to trade. the default value is 'NaN'.

- `limit`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. limit price of the order. if it is specified, the order type is either 'limit', or 'stop-limit'. 'NaN' should be specified for any other order type.

- `stop`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. stop price of the order. if it is specified, the order type is either 'stop', or 'stop-limit'. 'NaN' should be specified for any other order type.

- `oca_name`

    >  (`series` `string`)
    
    >  an optional parameter. Name of the OCa group the order belongs to. if the order should not belong to any particular OCa group, there should be an empty string.

- `oca_type`

    >  (`input` `string`)
    
    >  an optional parameter. Type of the OCa group. the allowed values are: [strategy.oca.none](#var_strategy.oca.none) \- the order should not belong to any particular OCa group; [strategy.oca.cancel](#var_strategy.oca.cancel) \- the order should belong to an OCa group, where as soon as an order is filled, all other orders of the same group are cancelled; [strategy.oca.reduce](#var_strategy.oca.reduce) \- the order should belong to an OCa group, where if X number of contracts of an order is filled, number of contracts for each other order of the same OCa group is decreased by X.

- `comment`

    >  (`series` `string`)
    
    >  an optional parameter. additional notes on the order.

- `alert_message`

    >  (`series` `string`)
    
    >  an optional parameter which replaces the {{strategy.order.alert_message}} placeholder when it is used in the "Create alert" dialog box's "Message" field.

- `disable_alert`

    >  (`series` `bool`)
    
    >  if [true](#op_true) when the function creates an order, the strategy alert will not fire upon the execution of that order. the parameter accepts a 'series bool' argument, allowing users to control which orders will trigger alerts when they fill. optional. the default is [false](#op_false).

### Example


```s

//@version=5
strategy(title = "simple strategy entry example")
if open > high[1]
    strategy.entry("enter long", strategy.long, 1) // enter long by market if current open great then previous high
if open < low[1]
    strategy.entry("enter short", strategy.short, 1) // enter short by market if current open less then previous low

```


## strategy.exit
it is a command to exit either a specific entry, or whole market position. if an order with the same iD is already pending, it is possible to modify the order. if an entry order was not filled, but an exit order is generated, the exit order will wait till entry order is filled and then the exit order is placed. To deactivate an exit order, the command strategy.cancel or strategy.cancel_all should be used. if the function strategy.exit is called once, it exits a position only once. if you want to exit multiple times, the command strategy.exit should be called multiple times. if you use a stop loss and a trailing stop, their order type is 'stop', so only one of them is placed (the one that is supposed to be filled first). if all the following parameters 'profit', 'limit', 'loss', 'stop', 'trail_points', 'trail_offset' are 'NaN', the command will fail. To use market order to exit, the command strategy.close or strategy.close_all should be used.

### Syntax

strategy.exit(id, from_entry, qty, qty_percent, profit, limit, loss, stop, trail_price, trail_points, trail_offset, oca_name, comment, comment_profit, comment_loss, comment_trailing, alert_message, alert_profit, alert_loss, alert_trailing, disable_alert) → void

### Arguments

- `id`

    >  (`series` `string`)
    
    >  a required parameter. the order identifier. it is possible to cancel or modify an order by referencing its identifier.
- `from_entry`

    >  (`series` `string`)
    
    >  an optional parameter. the identifier of a specific entry order to exit from it. To exit all entries an empty string should be used. the default values is empty string.
- `qty`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. Number of contracts/shares/lots/units to exit a trade with. the default value is 'NaN'.
- `qty_percent`

    >  (`series` `int`/`float`)
    
    >  Defines the percentage of (0-100) the position to close. its priority is lower than that of the 'qty' parameter. optional. the default is 100.
- `profit`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. profit target (specified in ticks). if it is specified, a limit order is placed to exit market position when the specified amount of profit (in ticks) is reached. the default value is 'NaN'.
- `limit`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. profit target (requires a specific price). if it is specified, a limit order is placed to exit market position at the specified price (or better). priority of the parameter 'limit' is higher than priority of the parameter 'profit' ('limit' is used instead of 'profit', if its value is not 'NaN'). the default value is 'NaN'.
- `loss`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. stop loss (specified in ticks). if it is specified, a stop order is placed to exit market position when the specified amount of loss (in ticks) is reached. the default value is 'NaN'.
- `stop`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. stop loss (requires a specific price). if it is specified, a stop order is placed to exit market position at the specified price (or worse). priority of the parameter 'stop' is higher than priority of the parameter 'loss' ('stop' is used instead of 'loss', if its value is not 'NaN'). the default value is 'NaN'.
- `trail_price`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. trailing stop activation level (requires a specific price). if it is specified, a trailing stop order will be placed when the specified price level is reached. the offset (in ticks) to determine initial price of the trailing stop order is specified in the 'trail_offset' parameter: X ticks lower than activation level to exit long position; X ticks higher than activation level to exit short position. the default value is 'NaN'.
- `trail_points`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. trailing stop activation level (profit specified in ticks). if it is specified, a trailing stop order will be placed when the calculated price level (specified amount of profit) is reached. the offset (in ticks) to determine initial price of the trailing stop order is specified in the 'trail_offset' parameter: X ticks lower than activation level to exit long position; X ticks higher than activation level to exit short position. the default value is 'NaN'.
- `trail_offset`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. trailing stop price (specified in ticks). the offset in ticks to determine initial price of the trailing stop order: X ticks lower than 'trail_price' or 'trail_points' to exit long position; X ticks higher than 'trail_price' or 'trail_points' to exit short position. the default value is 'NaN'.
- `oca_name`

    >  (`series` `string`)
    
    >  an optional parameter. Name of the OCa group (oca_type = strategy.oca.reduce) the profit target, the stop loss / the trailing stop orders belong to. if the name is not specified, it will be generated automatically.
- `comment`

    >  (`series` `string`)
    
    >  additional notes on the order. if specified, displays near the order marker on the chart. optional. the default is na.
- `comment_profit`

    >  (`series` `string`)
    
    >  additional notes on the order if the exit was triggered by crossing `profit` or `limit` specifically. if specified, supercedes the `comment` parameter and displays near the order marker on the chart. optional. the default is na.
- `comment_loss`

    >  (`series` `string`)
    
    >  additional notes on the order if the exit was triggered by crossing `stop` or `loss` specifically. if specified, supercedes the `comment` parameter and displays near the order marker on the chart. optional. the default is na.
- `comment_trailing`

    >  (`series` `string`)
    
    >  additional notes on the order if the exit was triggered by crossing `trail_offset` specifically. if specified, supercedes the `comment` parameter and displays near the order marker on the chart. optional. the default is na.
- `alert_message`

    >  (`series` `string`)
    
    >  Text that will replace the '{{strategy.order.alert_message}}' placeholder when one is used in the "Message" field of the "Create alert" dialog. optional. the default is na.
- `alert_profit`

    >  (`series` `string`)
    
    >  Text that will replace the '{{strategy.order.alert_message}}' placeholder when one is used in the "Message" field of the "Create alert" dialog. Only replaces the text if the exit was triggered by crossing `profit` or `limit` specifically. optional. the default is na.
- `alert_loss`

    >  (`series` `string`)
    
    >  Text that will replace the '{{strategy.order.alert_message}}' placeholder when one is used in the "Message" field of the "Create alert" dialog. Only replaces the text if the exit was triggered by crossing `stop` or `loss` specifically. optional. the default is na.
- `alert_trailing`

    >  (`series` `string`)
    
    >  Text that will replace the '{{strategy.order.alert_message}}' placeholder when one is used in the "Message" field of the "Create alert" dialog. Only replaces the text if the exit was triggered by crossing `trail_offset` specifically. optional. the default is na.
- `disable_alert`

    >  (`series` `bool`)
    
    >  if true when the function creates an order, the strategy alert will not fire upon the execution of that order. the parameter accepts a 'series bool' argument, allowing users to control which orders will trigger alerts when they fill. optional. the default is false.


### Example

```s
//@version=5
strategy(title = "simple strategy exit example")
if open > high[1]
    strategy.entry("long", strategy.long, 1) // enter long by market if current open great then previous high
strategy.exit("exit", "long", profit = 10, loss = 5) // generate full exit bracket (profit 10 points, loss 5 points per contract) from entry with name "long"
```



## strategy.opentrades.commission
Returns the sum of entry and exit fees paid in the open trade, expressed in strategy.account_currency.

### Syntax

strategy.opentrades.commission(trade_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the open trade. the number of the first trade is zero.


### Example

```
// Calculates the gross profit or loss for the current open position.
//@version=5
strategy("`strategy.opentrades.commission` Example", commission_type = strategy.commission.percent, commission_value = 0.1)

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Calculate gross profit or loss for open positions only.
tradeOpenGrosspL() =>
    sumOpenGrosspL = 0.0
    for tradeNo = 0 to strategy.opentrades - 1
        sumOpenGrosspL += strategy.opentrades.profit(tradeNo) - strategy.opentrades.commission(tradeNo)
    result = sumOpenGrosspL

plot(tradeOpenGrosspL())

```

### See also

* [strategy](#fun_strategy)
* [strategy.closedtrades.commission](#fun_strategy.closedtrades.commission)

## strategy.opentrades.entry\_bar\_index

Returns the bar_index of the open trade's entry.

### Syntax

strategy.opentrades.entry\_bar\_index(trade_num) → series int

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the open trade. the number of the first trade is zero.

### Example

```
// Wait 10 bars and then close the position.

//@version=5
strategy("`strategy.opentrades.entry_bar_index` Example")

barssinceLastEntry() =>
    strategy.opentrades > 0 ? bar_index - strategy.opentrades.entry_bar_index(strategy.opentrades - 1) : na

// Enter a long position if there are no open positions.
if strategy.opentrades == 0
    strategy.entry("Long",  strategy.long)

// Close the long position after 10 bars.
if barssinceLastEntry() >= 10
    strategy.close("Long")


```

### See also

* [strategy.closedtrades.entry\_bar\_index](#fun_strategy.closedtrades.entry_bar_index)
* [strategy.closedtrades.exit\_bar\_index](#fun_strategy.closedtrades.exit_bar_index)

## strategy.opentrades.entry_comment

Returns the comment message of the open trade's entry, or [na](#var_na) if there is no entry with this \`trade_num\`.

### Syntax

strategy.opentrades.entry\_comment(trade\_num) → series string

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the open trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("`strategy.opentrades.entry_comment()` Example", overlay = true)

stopprice = open * 1.01

longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))

if (longCondition)
    strategy.entry("Long", strategy.long, stop = stopprice, comment = str.tostring(stopprice, "#.####"))

var testtable = table.new(position.top_right, 1, 3, color.orange, border_width = 1)

if barstate.islastconfirmedhistory or barstate.isrealtime
    table.cell(testtable, 0, 0, 'Last entry stats')
    table.cell(testtable, 0, 1, "Order stop price value: " + strategy.opentrades.entry_comment(strategy.opentrades - 1))
    table.cell(testtable, 0, 2, "actual Entry price: " + str.tostring(strategy.opentrades.entry_price(strategy.opentrades - 1)))


```

#.####"))var testtable = table.new(position.top_right, 1, 3, color.orange, border_width = 1)if barstate.islastconfirmedhistory or barstate.isrealtime    table.cell(testtable, 0, 0, 'Last entry stats')    table.cell(testtable, 0, 1, "Order stop price value: " + strategy.opentrades.entry_comment(strategy.opentrades - 1))    table.cell(testtable, 0, 2, "actual Entry price: " + str.tostring(strategy.opentrades.entry_price(strategy.opentrades - 1)))

### See also

* [strategy](#fun_strategy)
* [strategy.entry](#fun_strategy.entry)
* [strategy.opentrades](#var_strategy.opentrades)

## strategy.opentrades.entry_id

Returns the id of the open trade's entry.

### Syntax

strategy.opentrades.entry\_id(trade\_num) → series string

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the open trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("`strategy.opentrades.entry_id` Example", overlay = true)

// We enter a long position when 14 period sma crosses over 28 period sma.
// We enter a short position when 14 period sma crosses under 28 period sma.
longCondition = ta.crossover(ta.sma(close, 14), ta.sma(close, 28))
shortcondition = ta.crossunder(ta.sma(close, 14), ta.sma(close, 28))

// strategy calls to enter a long or short position when the corresponding condition is met.
if longCondition
    strategy.entry("Long entry at bar #" + str.tostring(bar_index), strategy.long)
if shortcondition
    strategy.entry("short entry at bar #" + str.tostring(bar_index), strategy.short)

// Display iD of the latest open position.
if barstate.islastconfirmedhistory
    label.new(bar_index, high + (2 * ta.tr),  "Last opened position is
 " + strategy.opentrades.entry_id(strategy.opentrades - 1))


```

#" + str.tostring(bar_index), strategy.long)if shortcondition    strategy.entry("short entry at bar #" + str.tostring(bar_index), strategy.short)// Display iD of the latest open position.if barstate.islastconfirmedhistory    label.new(bar_index, high + (2 * ta.tr),  "Last opened position is
 " + strategy.opentrades.entry_id(strategy.opentrades - 1))

### Returns

Returns the id of the open trade's entry.

### Remarks

the function returns na if trade_num is not in the range: 0 to strategy.opentrades-1.

### See also

* [strategy.opentrades.entry\_bar\_index](#fun_strategy.opentrades.entry_bar_index)
* [strategy.opentrades.entry_price](#fun_strategy.opentrades.entry_price)
* [strategy.opentrades.entry_time](#fun_strategy.opentrades.entry_time)

## strategy.opentrades.entry_price

Returns the price of the open trade's entry.

### Syntax

strategy.opentrades.entry\_price(trade\_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the open trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("strategy.opentrades.entry_price Example 1", overlay = true)

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if ta.crossover(close, ta.sma(close, 14))
    strategy.entry("Long", strategy.long)

// Return the entry price for the latest closed trade.
currEntryprice = strategy.opentrades.entry_price(strategy.opentrades - 1)
currExitprice = currEntryprice * 1.05

if high >= currExitprice
    strategy.close("Long")

plot(currEntryprice, "Long entry price", style = plot.style_linebr)
plot(currExitprice, "Long exit price", color.green, style = plot.style_linebr)



```

### Example

```
// Calculates the average price for the open position.

//@version=5
strategy("strategy.opentrades.entry_price Example 2", pyramiding = 2)

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Calculates the average price for the open position.
avgOpenpositionprice() =>
    sumOpenpositionprice = 0.0
    for tradeNo = 0 to strategy.opentrades - 1
        sumOpenpositionprice += strategy.opentrades.entry_price(tradeNo) * strategy.opentrades.size(tradeNo) / strategy.position_size
    result = nz(sumOpenpositionprice / strategy.opentrades)

plot(avgOpenpositionprice())


```

### See also

* [strategy.closedtrades.exit_price](#fun_strategy.closedtrades.exit_price)

## strategy.opentrades.entry_time

Returns the unix time of the open trade's entry.

### Syntax

strategy.opentrades.entry\_time(trade\_num) → series int

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the open trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("strategy.opentrades.entry_time Example")

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Calculates duration in milliseconds since the last position was opened.
timesinceLastEntry()=>
    strategy.opentrades > 0 ? (time - strategy.opentrades.entry_time(strategy.opentrades - 1)) : na

plot(timesinceLastEntry() / 1000 * 60 * 60 * 24, "Days since last entry")


```

### See also

* [strategy.closedtrades.entry_time](#fun_strategy.closedtrades.entry_time)
* [strategy.closedtrades.exit_time](#fun_strategy.closedtrades.exit_time)

## strategy.opentrades.max_drawdown

Returns the maximum drawdown of the open trade, i.e., the maximum possible loss during the trade, expressed in [strategy.account_currency](#var_strategy.account_currency).

### Syntax

strategy.opentrades.max\_drawdown(trade\_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the open trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("strategy.opentrades.max_drawdown Example 1")

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// plot the max drawdown of the latest open trade.
plot(strategy.opentrades.max_drawdown(strategy.opentrades - 1), "Max drawdown of the latest open trade")



```

### Example

```
// Calculates the max trade drawdown value for all open trades.

//@version=5
strategy("`strategy.opentrades.max_drawdown` Example 2", pyramiding = 100)

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Get the biggest max trade drawdown value from all of the open trades.
maxtradeDrawDown() =>
    maxDrawdown = 0.0
    for tradeNo = 0 to strategy.opentrades - 1
        maxDrawdown := math.max(maxDrawdown, strategy.opentrades.max_drawdown(tradeNo))
    result = maxDrawdown

plot(maxtradeDrawDown(), "biggest max drawdown")


```

### Remarks

the function returns na if trade_num is not in the range: 0 to strategy.closedtrades - 1.

### See also

* [strategy.closedtrades.max_drawdown](#fun_strategy.closedtrades.max_drawdown)
* [strategy.max_drawdown](#var_strategy.max_drawdown)

## strategy.opentrades.max_runup

Returns the maximum run up of the open trade, i.e., the maximum possible profit during the trade, expressed in [strategy.account_currency](#var_strategy.account_currency).

### Syntax

strategy.opentrades.max\_runup(trade\_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the open trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("strategy.opentrades.max_runup Example 1")

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// plot the max runup of the latest open trade.
plot(strategy.opentrades.max_runup(strategy.opentrades - 1), "Max runup of the latest open trade")



```

### Example

```
// Calculates the max trade runup value for all open trades.

//@version=5
strategy("strategy.opentrades.max_runup Example 2", pyramiding = 100)

// Enter a long position every 30 bars.
if bar_index % 30 == 0
    strategy.entry("Long", strategy.long)

// Calculate biggest max trade runup value from all of the open trades.
maxOpentradeRunup() =>
    maxRunup = 0.0
    for tradeNo = 0 to strategy.opentrades - 1
        maxRunup := math.max(maxRunup, strategy.opentrades.max_runup(tradeNo))
    result = maxRunup

plot(maxOpentradeRunup(), "biggest max runup of all open trades")


```

### See also

* [strategy.closedtrades.max_runup](#fun_strategy.closedtrades.max_runup)
* [strategy.max_drawdown](#var_strategy.max_drawdown)

## strategy.opentrades.profit

Returns the profit/loss of the open trade, expressed in [strategy.account_currency](#var_strategy.account_currency). Losses are expressed as negative values.

### Syntax

strategy.opentrades.profit(trade_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the open trade. the number of the first trade is zero.

### Example

```
// Returns the profit of the last open trade.

//@version=5
strategy("`strategy.opentrades.profit` Example 1", commission_type = strategy.commission.percent, commission_value = 0.1)

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

plot(strategy.opentrades.profit(strategy.opentrades - 1), "profit of the latest open trade")



```

### Example

```
// Calculates the profit for all open trades.

//@version=5
strategy("`strategy.opentrades.profit` Example 2", pyramiding = 5)

// strategy calls to enter 5 long positions every 2 bars.
if bar_index % 2 == 0
    strategy.entry("Long", strategy.long, qty = 5)

// Calculate open profit or loss for the open positions.
tradeOpenpL() =>
    sumprofit = 0.0
    for tradeNo = 0 to strategy.opentrades - 1
        sumprofit += strategy.opentrades.profit(tradeNo)
    result = sumprofit

plot(tradeOpenpL(), "profit of all open trades")


```

### See also

* [strategy.closedtrades.profit](#fun_strategy.closedtrades.profit)
* [strategy.openprofit](#var_strategy.openprofit)
* [strategy.netprofit](#var_strategy.netprofit)
* [strategy.grossprofit](#var_strategy.grossprofit)

## strategy.opentrades.size

Returns the direction and the number of contracts traded in the open trade. if the value is > 0, the market position was long. if the value is < 0, the market position was short.

### Syntax

strategy.opentrades.size(trade_num) → series float

### Arguments

- `trade_num`

    >  (`series` `int`)
    
    >  the trade number of the open trade. the number of the first trade is zero.

### Example


```s

//@version=5
strategy("`strategy.opentrades.size` Example 1")

// We calculate the max amt of shares we can buy.
amtshares = math.floor(strategy.equity / close)
// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long, qty = amtshares)
if bar_index % 20 == 0
    strategy.close("Long")

// plot the number of contracts in the latest open trade.
plot(strategy.opentrades.size(strategy.opentrades - 1), "amount of contracts in latest open trade")



```

### Example

```
// Calculates the average profit percentage for all open trades.

//@version=5
strategy("`strategy.opentrades.size` Example 2")

// strategy calls to enter long trades every 15 bars and exit long trades every 20 bars.
if bar_index % 15 == 0
    strategy.entry("Long", strategy.long)
if bar_index % 20 == 0
    strategy.close("Long")

// Calculate profit for all open trades.
profitpct = 0.0
for tradeNo = 0 to strategy.opentrades - 1
    entryp = strategy.opentrades.entry_price(tradeNo)
    exitp = close
    profitpct += (exitp - entryp) / entryp * strategy.opentrades.size(tradeNo) * 100

// Calculate average profit percent for all open trades.
avgprofitpct = nz(profitpct / strategy.opentrades)
plot(avgprofitpct)


```

### See also

* [strategy.closedtrades.size](#fun_strategy.closedtrades.size)
* [strategy.position_size](#var_strategy.position_size)
* [strategy.opentrades](#var_strategy.opentrades)
* [strategy.closedtrades](#var_strategy.closedtrades)

## strategy.order

it is a command to place order. if an order with the same iD is already pending, it is possible to modify the order. if there is no order with the specified iD, a new order is placed. To deactivate order, the command [strategy.cancel](#fun_strategy.cancel) or [strategy.cancel_all](#fun_strategy.cancel_all) should be used. in comparison to the function [strategy.entry](#fun_strategy.entry), the function [strategy.order](#fun_strategy.order) is not affected by pyramiding. if both 'limit' and 'stop' parameters are 'NaN', the order type is market order.

### Syntax

strategy.order(id, direction, qty, limit, stop, oca\_name, oca\_type, comment, alert\_message, disable\_alert) - void

### Arguments

- `id`

    >  (`series` `string`)
    
    >  a required parameter. the order identifier. it is possible to cancel or modify an order by referencing its identifier.

- `direction`

    >  (`series` `strategy_direction`)
    
    >  a required parameter. Order direction: 'strategy.long' is for buy, 'strategy.short' is for sell.

- `qty`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. Number of contracts/shares/lots/units to trade. the default value is 'NaN'.

- `limit`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. limit price of the order. if it is specified, the order type is either 'limit', or 'stop-limit'. 'NaN' should be specified for any other order type.

- `stop`

    >  (`series` `int`/`float`)
    
    >  an optional parameter. stop price of the order. if it is specified, the order type is either 'stop', or 'stop-limit'. 'NaN' should be specified for any other order type.

- `oca_name`

    >  (`series` `string`)
    
    >  an optional parameter. Name of the OCa group the order belongs to. if the order should not belong to any particular OCa group, there should be an empty string.

- `oca_type`

    >  (`input` `string`)
    
    >  an optional parameter. Type of the OCa group. the allowed values are: [strategy.oca.none](#var_strategy.oca.none) \- the order should not belong to any particular OCa group; [strategy.oca.cancel](#var_strategy.oca.cancel) \- the order should belong to an OCa group, where as soon as an order is filled, all other orders of the same group are cancelled; [strategy.oca.reduce](#var_strategy.oca.reduce) \- the order should belong to an OCa group, where if X number of contracts of an order is filled, number of contracts for each other order of the same OCa group is decreased by X.

- `comment`

    >  (`series` `string`)
    
    >  an optional parameter. additional notes on the order.

- `alert_message`

    >  (`series` `string`)
    
    >  an optional parameter which replaces the {{strategy.order.alert_message}} placeholder when it is used in the "Create alert" dialog box's "Message" field.

- `disable_alert`

    >  (`series` `bool`)
    
    >  if [true](#op_true) when the function creates an order, the strategy alert will not fire upon the execution of that order. the parameter accepts a 'series bool' argument, allowing users to control which orders will trigger alerts when they fill. optional. the default is [false](#op_false).

### Example


```s

//@version=5
strategy(title = "simple strategy order example")
if open > high[1]
    strategy.order("buy", strategy.long, 1) // buy by market if current open great then previous high
if open < low[1]
    strategy.order("sell", strategy.short, 1) // sell by market if current open less then previous low


## strategy.risk.allow_entry_in
this function can be used to specify in which market direction the strategy.entry function is allowed to open positions.

### Syntax

strategy.risk.allow_entry_in(value) → void

### Arguments

- `value`

    >  (`simple` `string`)
    
    >  the allowed direction. possible values: strategy.direction.all, strategy.direction.long, strategy.direction.short


### Example

//@version=5
strategy("strategy.risk.allow_entry_in")

strategy.risk.allow_entry_in(strategy.direction.long)
if open > close
    strategy.entry("Long", strategy.long)
// instead of opening a short position with 10 contracts, this command will close long entries.
if open < close
    strategy.entry("short", strategy.short, qty = 10)

```

## strategy.risk.max\_cons\_loss_days

the purpose of this rule is to cancel all pending orders, close all open positions and stop placing orders after a specified number of consecutive days with losses. the rule affects the whole strategy.

### Syntax

strategy.risk.max\_cons\_loss\_days(count, alert\_message) - void

### Arguments

- `count`

    >  (`simple` `int`)
    
    >  a required parameter. the allowed number of consecutive days with losses.

- `alert_message`

    >  (`simple` `string`)
    
    >  an optional parameter which replaces the {{strategy.order.alert_message}} placeholder when it is used in the "Create alert" dialog box's "Message" field.

### Example


```s

//@version=5
strategy("risk.max_cons_loss_days Demo 1")
strategy.risk.max_cons_loss_days(3) // No orders will be placed after 3 days, if each day is with loss.
plot(strategy.position_size)

```

## strategy.risk.max_drawdown

the purpose of this rule is to determine maximum drawdown. the rule affects the whole strategy. Once the maximum drawdown value is reached, all pending orders are cancelled, all open positions are closed and no new orders can be placed.

### Syntax

strategy.risk.max\_drawdown(value, type, alert\_message) - void

### Arguments

- `value`

    >  (`simple` `int`/`float`)
    
    >  a required parameter. the maximum drawdown value. it is specified either in money (base currency), or in percentage of maximum equity. For % of equity the range of allowed values is from 0 to 100.

- `type`

    >  (`simple` `string`)
    
    >  a required parameter. the type of the value. please specify one of the following values: [strategy.percent\_of\_equity](#var_strategy.percent_of_equity) or [strategy.cash](#var_strategy.cash). Note: if equity drops down to zero or to a negative and the 'strategy.percent\_of\_equity' is specified, all pending orders are cancelled, all open positions are closed and no new orders can be placed for good.

- `alert_message`

    >  (`simple` `string`)
    
    >  an optional parameter which replaces the {{strategy.order.alert_message}} placeholder when it is used in the "Create alert" dialog box's "Message" field.

### Example


```s

//@version=5
strategy("risk.max_drawdown Demo 1")
strategy.risk.max_drawdown(50, strategy.percent_of_equity) // set maximum drawdown to 50% of maximum equity
plot(strategy.position_size)



```

### Example


```s

//@version=5
strategy("risk.max_drawdown Demo 2", currency = "EuR")
strategy.risk.max_drawdown(2000, strategy.cash)  // set maximum drawdown to 2000 EuR from maximum equity
plot(strategy.position_size)

```

## strategy.risk.max\_intraday\_filled_orders

the purpose of this rule is to determine maximum number of filled orders per 1 day (per 1 bar, if chart resolution is higher than 1 day). the rule affects the whole strategy. Once the maximum number of filled orders is reached, all pending orders are cancelled, all open positions are closed and no new orders can be placed till the end of the current trading session.

### Syntax

strategy.risk.max\_intraday\_filled\_orders(count, alert\_message) - void

### Arguments

- `count`

    >  (`simple` `int`)
    
    >  a required parameter. the maximum number of filled orders per 1 day.

- `alert_message`

    >  (`simple` `string`)
    
    >  an optional parameter which replaces the {{strategy.order.alert_message}} placeholder when it is used in the "Create alert" dialog box's "Message" field.

### Example


```s

//@version=5
strategy("risk.max_intraday_filled_orders Demo")
strategy.risk.max_intraday_filled_orders(10) // after 10 orders are filled, no more strategy orders will be placed (except for a market order to exit current open market position, if there is any).
if open > close
    strategy.entry("buy", strategy.long)
if open < close
    strategy.entry("sell", strategy.short)

```

## strategy.risk.max\_intraday\_loss

the maximum loss value allowed during a day. it is specified either in money (base currency), or in percentage of maximum intraday equity (0 -100).

### Syntax

strategy.risk.max\_intraday\_loss(value, type, alert_message) - void

### Arguments

- `value`

    >  (`simple` `int`/`float`)
    
    >  a required parameter. the maximum loss value. it is specified either in money (base currency), or in percentage of maximum intraday equity. For % of equity the range of allowed values is from 0 to 100.

- `type`

    >  (`simple` `string`)
    
    >  a required parameter. the type of the value. please specify one of the following values: [strategy.percent\_of\_equity](#var_strategy.percent_of_equity) or [strategy.cash](#var_strategy.cash). Note: if equity drops down to zero or to a negative and the [strategy.percent\_of\_equity](#var_strategy.percent_of_equity) is specified, all pending orders are cancelled, all open positions are closed and no new orders can be placed for good.

- `alert_message`

    >  (`simple` `string`)
    
    >  an optional parameter which replaces the {{strategy.order.alert_message}} placeholder when it is used in the "Create alert" dialog box's "Message" field.

### Example

```
// sets the maximum intraday loss using the strategy's equity value.

//@version=5
strategy("strategy.risk.max_intraday_loss Example 1", overlay = false, default_qty_type = strategy.percent_of_equity, default_qty_value = 100)

// input for maximum intraday loss %.
losspct = input.float(10)

// set maximum intraday loss to our losspct input
strategy.risk.max_intraday_loss(losspct, strategy.percent_of_equity)

// Enter short at bar_index zero.
if bar_index == 0
    strategy.entry("short", strategy.short)

// store equity value from the beginning of the day
eqFromDaystart = ta.valuewhen(ta.change(dayofweek) > 0, strategy.equity, 0)

// Calculate change of the current equity from the beginning of the current day.
eqChgpct = 100 * ((strategy.equity - eqFromDaystart) / strategy.equity)

// plot it
plot(eqChgpct)
hline(-losspct)



```

### Example

```
// sets the maximum intraday loss using the strategy's cash value.

//@version=5
strategy("strategy.risk.max_intraday_loss Example 2", overlay = false)

// input for maximum intraday loss in absolute cash value of the symbol.
absCashLoss = input.float(5)

// set maximum intraday loss to `absCashLoss` in account currency.
strategy.risk.max_intraday_loss(absCashLoss, strategy.cash)

// Enter short at bar_index zero.
if bar_index == 0
    strategy.entry("short", strategy.short)

// store the open price value from the beginning of the day.
beginprice = ta.valuewhen(ta.change(dayofweek) > 0, open, 0)

// Calculate the absolute price change for the current period.
priceChg = (close - beginprice)

hline(absCashLoss)
plot(priceChg)


```

### See also

* [strategy](#fun_strategy)
* [strategy.percent\_of\_equity](#var_strategy.percent_of_equity)
* [strategy.cash](#var_strategy.cash)

## strategy.risk.max\_position\_size

the purpose of this rule is to determine maximum size of a market position. the rule affects the following function: [strategy.entry](#fun_strategy.entry). the 'entry' quantity can be reduced (if needed) to such number of contracts/shares/lots/units, so the total position size doesn't exceed the value specified in 'strategy.risk.max\_position\_size'. if minimum possible quantity still violates the rule, the order will not be placed.

### Syntax

strategy.risk.max\_position\_size(contracts) - void

### Arguments

- `contracts`

    >  (`simple` `int`/`float`)
    
    >  a required parameter. Maximum number of contracts/shares/lots/units in a position.

### Example


```s

//@version=5
strategy("risk.max_position_size Demo", default_qty_value = 100)
strategy.risk.max_position_size(10)
if open > close
    strategy.entry("buy", strategy.long)
plot(strategy.position_size)  // max plot value will be 10

```

## string

+3 overloads

Casts na to string

### syntax & Overloads

> [string(x) → const string](#fun_string-0)
> [string(x) → input string](#fun_string-1)
> [string(x) → simple string](#fun_string-2)
> [string(x) → series string](#fun_string-3)

### Arguments

- `x`

    >  (`const` `string`)
    
    >  the value to convert to the specified type, usually [na](#var_na).

### Returns

the value of the argument after casting to string.

### See also

* [float](#fun_float)
* [int](#fun_int)
* [bool](#fun_bool)
* [color](#fun_color)
* [line](#fun_line)
* [label](#fun_label)

## syminfo.prefix

+1 overload

Returns exchange prefix of the \`symbol\`, e.g. "NasDaq".

### syntax & Overloads

> [syminfo.prefix(symbol) → simple string](#fun_syminfo.prefix-0)
> [syminfo.prefix(symbol) → series string](#fun_syminfo.prefix-1)

### Arguments

- `symbol`

    >  (`simple` `string`)
    
    >  symbol. Note that the symbol should be passed with a prefix. For example: "NasDaq:aapL" instead of "aapL".

### Example


```s

//@version=5
indicator("syminfo.prefix fun", overlay=true)
i_sym = input.symbol("NasDaq:aapL")
pref = syminfo.prefix(i_sym)
tick = syminfo.ticker(i_sym)
t = ticker.new(pref, tick, session.extended)
s = request.security(t, "1D", close)
plot(s)


```

### Returns

Returns exchange prefix of the \`symbol\`, e.g. "NasDaq".

### Remarks

the result of the function is used in the [ticker.new](#fun_ticker.new)/[ticker.modify](#fun_ticker.modify) and [request.security](#fun_request.security).

### See also

* [syminfo.tickerid](#var_syminfo.tickerid)
* [syminfo.ticker](#var_syminfo.ticker)
* [syminfo.prefix](#var_syminfo.prefix)
* [syminfo.ticker](#fun_syminfo.ticker)
* [ticker.new](#fun_ticker.new)

## syminfo.ticker

+1 overload

Returns \`symbol\` name without exchange prefix, e.g. "aapL".

### syntax & Overloads

> [syminfo.ticker(symbol) → simple string](#fun_syminfo.ticker-0)
> [syminfo.ticker(symbol) → series string](#fun_syminfo.ticker-1)

### Arguments

- `symbol`

    >  (`simple` `string`)
    
    >  symbol. Note that the symbol should be passed with a prefix. For example: "NasDaq:aapL" instead of "aapL".

### Example


```s

//@version=5
indicator("syminfo.ticker fun", overlay=true)
i_sym = input.symbol("NasDaq:aapL")
pref = syminfo.prefix(i_sym)
tick = syminfo.ticker(i_sym)
t = ticker.new(pref, tick, session.extended)
s = request.security(t, "1D", close)
plot(s)


```

### Returns

Returns \`symbol\` name without exchange prefix, e.g. "aapL".

### Remarks

the result of the function is used in the [ticker.new](#fun_ticker.new)/[ticker.modify](#fun_ticker.modify) and [request.security](#fun_request.security).

### See also

* [syminfo.tickerid](#var_syminfo.tickerid)
* [syminfo.ticker](#var_syminfo.ticker)
* [syminfo.prefix](#var_syminfo.prefix)
* [syminfo.prefix](#fun_syminfo.prefix)
* [ticker.new](#fun_ticker.new)

## ta.alma

+1 overload

arnaud Legoux Moving average. it uses Gaussian distribution as weights for moving average.

### syntax & Overloads

> [ta.alma(series, length, offset, sigma) → series float](#fun_ta.alma-0)
> [ta.alma(series, length, offset, sigma, floor) → series float](#fun_ta.alma-1)

### Arguments

- `series`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

- `offset`

    >  (`simple` `int`/`float`)
    
    >  Controls tradeoff between smoothness (closer to 1) and responsiveness (closer to 0).

- `sigma`

    >  (`simple` `int`/`float`)
    
    >  Changes the smoothness of aLMa. the larger sigma the smoother aLMa.

### Example


```s

//@version=5
indicator("ta.alma", overlay=true)
plot(ta.alma(close, 9, 0.85, 6))

// same on pine, but much less efficient
pine_alma(series, windowsize, offset, sigma) =>
    m = offset * (windowsize - 1)
    //m = math.floor(offset * (windowsize - 1)) // used as m when math.floor=true
    s = windowsize / sigma
    norm = 0.0
    sum = 0.0
    for i = 0 to windowsize - 1
        weight = math.exp(-1 * math.pow(i - m, 2) / (2 * math.pow(s, 2)))
        norm := norm + weight
        sum := sum + series[windowsize - i - 1] * weight
    sum / norm
plot(pine_alma(close, 9, 0.85, 6))


```

### Returns

arnaud Legoux Moving average.

### Remarks

\`na\` values in the \`source\` series are included in calculations and will produce an \`na\` result.

### See also

* [ta.sma](#fun_ta.sma)
* [ta.ema](#fun_ta.ema)
* [ta.rma](#fun_ta.rma)
* [ta.wma](#fun_ta.wma)
* [ta.vwma](#fun_ta.vwma)
* [ta.swma](#fun_ta.swma)

## ta.atr

Function atr (average true range) returns the RMa of true range. true range is max(high - low, abs(high - close\[1\]), abs(low - close\[1\])).

### Syntax

ta.atr(length) → series float

### Arguments

- `length`

    >  (`simple` `int`)
    
    >  Length (number of bars back).

### Example


```s

//@version=5
indicator("ta.atr")
plot(ta.atr(14))

//the same on pine
pine_atr(length) =>
    trueRange = na(high[1])? high-low : math.max(math.max(high - low, math.abs(high - close[1])), math.abs(low - close[1]))
    //true range can be also calculated with ta.tr(true)
    ta.rma(trueRange, length)

plot(pine_atr(14))


```

### Returns

average true range.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.tr](#fun_ta.tr)
* [ta.rma](#fun_ta.rma)

## ta.barssince

Counts the number of bars since the last time the condition was true.

### Syntax

ta.barssince(condition) → series int

### Arguments

- `condition`

    >  (`series` `bool`)
    
    >  the condition to check for.

### Example


```s

//@version=5
indicator("ta.barssince")
// get number of bars since last color.green bar
plot(ta.barssince(close >= open))


```

### Returns

Number of bars since condition was true.

### Remarks

if the condition has never been met prior to the current bar, the function returns na.

please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

### See also

* [ta.lowestbars](#fun_ta.lowestbars)
* [ta.highestbars](#fun_ta.highestbars)
* [ta.valuewhen](#fun_ta.valuewhen)
* [ta.highest](#fun_ta.highest)
* [ta.lowest](#fun_ta.lowest)

## ta.bb

bollinger bands. a bollinger band is a technical analysis tool defined by a set of lines plotted two standard deviations (positively and negatively) away from a simple moving average (sMa) of the security's price, but can be adjusted to user preferences.

### Syntax

ta.bb(series, length, mult) - \[series float, series float, series float\]

### Arguments

- `series`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

- `mult`

    >  (`simple` `int`/`float`)
    
    >  standard deviation factor.

### Example


```s

//@version=5
indicator("ta.bb")

> [middle, upper, lower] = ta.bb(close, 5, 4)
plot(middle, color=color.yellow)
plot(upper, color=color.yellow)
plot(lower, color=color.yellow)

// the same on pine
f_bb(src, length, mult) =>
    float basis = ta.sma(src, length)
    float dev = mult * ta.stdev(src, length)
    [basis, basis + dev, basis - dev]

> [pinemiddle, pineupper, pineLower] = f_bb(close, 5, 4)

plot(pinemiddle)
plot(pineupper)
plot(pineLower)


```

### Returns

bollinger bands.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.sma](#fun_ta.sma)
* [ta.stdev](#fun_ta.stdev)
* [ta.kc](#fun_ta.kc)

## ta.bbw

bollinger bands Width. the bollinger band Width is the difference between the upper and the lower bollinger bands divided by the middle band.

### Syntax

ta.bbw(series, length, mult) → series float

### Arguments

- `series`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

- `mult`

    >  (`simple` `int`/`float`)
    
    >  standard deviation factor.

### Example


```s

//@version=5
indicator("ta.bbw")

plot(ta.bbw(close, 5, 4), color=color.yellow)

// the same on pine
f_bbw(src, length, mult) =>
    float basis = ta.sma(src, length)
    float dev = mult * ta.stdev(src, length)
    ((basis + dev) - (basis - dev)) / basis

plot(f_bbw(close, 5, 4))


```

### Returns

bollinger bands Width.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.bb](#fun_ta.bb)
* [ta.sma](#fun_ta.sma)
* [ta.stdev](#fun_ta.stdev)

## ta.cci

the CCi (commodity channel index) is calculated as the difference between the typical price of a commodity and its simple moving average, divided by the mean absolute deviation of the typical price. the index is scaled by an inverse factor of 0.015 to provide more readable numbers.

### Syntax

ta.cci(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Returns

Commodity channel index of source for length bars back.

### Remarks

\`na\` values in the \`source\` series are ignored.

## ta.change

+5 overloads

Compares the current \`source\` value to its value \`length\` bars ago and returns the difference.

### syntax & Overloads

> [ta.change(source) → series int](#fun_ta.change-0)
> [ta.change(source) → series float](#fun_ta.change-1)
> [ta.change(source, length) → series int](#fun_ta.change-2)
> [ta.change(source, length) → series float](#fun_ta.change-3)
> [ta.change(source) → series bool](#fun_ta.change-4)
> [ta.change(source, length) → series bool](#fun_ta.change-5)

### Arguments

- `source`

    >  (`series` `int`)
    
    >  source series.

### Example


```s

//@version=5
indicator('Day and direction Change', overlay = true)
dailybartime = time('1D')
isNewDay = ta.change(dailybartime)
bgcolor(isNewDay ? color.new(color.green, 80) : na)

isGreenbar = close >= open
colorChange = ta.change(isGreenbar)
plotshape(colorChange, 'direction Change')

### Returns

the difference between the values when they are numerical. When a 'bool' source is used, returns `true` when the current source is different from the previous source.

### Remarks

`na` values in the `source` series are included in calculations and will produce an `na` result.

### See also

ta.mom
ta.cross


## ta.cmo
Chande Momentum Oscillator. Calculates the difference between the sum of recent gains and the sum of recent losses and then divides the result by the sum of all price movement over the same period.

### Syntax

ta.cmo(series, length) → series float

### Arguments

- `series`

    >  (`series` `int`/`float`)
    
    >  series of values to process.
- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).


### Example

//@version=5
indicator("ta.cmo")
plot(ta.cmo(close, 5), color=color.yellow)

// the same on pine
f_cmo(src, length) =>
    float mom = ta.change(src)
    float sm1 = math.sum((mom >= 0) ? mom : 0.0, length)
    float sm2 = math.sum((mom >= 0) ? 0.0 : -mom, length)
    100 * (sm1 - sm2) / (sm1 + sm2)

plot(f_cmo(close, 5))


```

### Returns

Chande Momentum Oscillator.

### Remarks

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.rsi](#fun_ta.rsi)
* [ta.stoch](#fun_ta.stoch)
* [math.sum](#fun_math.sum)

## ta.cog

the cog (center of gravity) is an indicator based on statistics and the Fibonacci golden ratio.

### Syntax

ta.cog(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Example


```s

//@version=5
indicator("ta.cog", overlay=true)
plot(ta.cog(close, 10))

// the same on pine
pine_cog(source, length) =>
    sum = math.sum(source, length)
    num = 0.0
    for i = 0 to length - 1
        price = source[i]
        num := num + price * (i + 1)
    -num / sum

plot(pine_cog(close, 10))


```

### Returns

center of Gravity.

### Remarks

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.stoch](#fun_ta.stoch)

## ta.correlation

Correlation coefficient. Describes the degree to which two series tend to deviate from their [ta.sma](#fun_ta.sma) values.

### Syntax

ta.correlation(source1, source2, length) → series float

### Arguments

- `source1`

    >  (`series` `int`/`float`)
    
    >  source series.

- `source2`

    >  (`series` `int`/`float`)
    
    >  Target series.

- `length`

    >  (`series` `int`)
    
    >  Length (number of bars back).

### Returns

Correlation coefficient.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [request.security](#fun_request.security)

## ta.cross

### Syntax

ta.cross(source1, source2) → series bool

### Arguments

- `source1`

    >  (`series` `int`/`float`)
    
    >  First data series.

- `source2`

    >  (`series` `int`/`float`)
    
    >  second data series.

### Returns

true if two series have crossed each other, otherwise false.

### See also

* [ta.change](#fun_ta.change)

## ta.crossover

the \`source1\`-series is defined as having crossed over \`source2\`-series if, on the current bar, the value of \`source1\` is greater than the value of \`source2\`, and on the previous bar, the value of \`source1\` was less than or equal to the value of \`source2\`.

### Syntax

ta.crossover(source1, source2) → series bool

### Arguments

- `source1`

    >  (`series` `int`/`float`)
    
    >  First data series.

- `source2`

    >  (`series` `int`/`float`)
    
    >  second data series.

### Returns

true if \`source1\` crossed over \`source2\` otherwise false.

## ta.crossunder

the \`source1\`-series is defined as having crossed under \`source2\`-series if, on the current bar, the value of \`source1\` is less than the value of \`source2\`, and on the previous bar, the value of \`source1\` was greater than or equal to the value of \`source2\`.

### Syntax

ta.crossunder(source1, source2) → series bool

### Arguments

- `source1`

    >  (`series` `int`/`float`)
    
    >  First data series.

- `source2`

    >  (`series` `int`/`float`)
    
    >  second data series.

### Returns

true if \`source1\` crossed under \`source2\` otherwise false.

## ta.cum

Cumulative (total) sum of \`source\`. in other words it's a sum of all elements of \`source\`.

### Syntax

ta.cum(source) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  source used for the calculation.

### Returns

Total sum series.

### See also

* [math.sum](#fun_math.sum)

## ta.dev

Measure of difference between the series and it's [ta.sma](#fun_ta.sma)

### Syntax

ta.dev(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Example


```s

//@version=5
indicator("ta.dev")
plot(ta.dev(close, 10))

// the same on pine
pine_dev(source, length) =>
    mean = ta.sma(source, length)
    sum = 0.0
    for i = 0 to length - 1
        val = source[i]
        sum := sum + math.abs(val - mean)
    dev = sum/length
plot(pine_dev(close, 10))


```

### Returns

Deviation of \`source\` for \`length\` bars back.

### Remarks

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.variance](#fun_ta.variance)
* [ta.stdev](#fun_ta.stdev)

## ta.dmi

the dmi function returns the directional movement index.

### Syntax

ta.dmi(diLength, adxsmoothing) - \[series float, series float, series float\]

### Arguments

- `diLength`

    >  (`simple` `int`)
    
    >  Di period.

- `adxsmoothing`

    >  (`simple` `int`)
    
    >  aDX smoothing period.

### Example


```s

//@version=5
indicator(title="directional Movement index", shorttitle="DMi", format=format.price, precision=4)
len = input.int(17, minval=1, title="Di Length")
lensig = input.int(14, title="aDX smoothing", minval=1, maxval=50)
> [diplus, diminus, adx] = ta.dmi(len, lensig)
plot(adx, color=color.red, title="aDX")
plot(diplus, color=color.blue, title="+Di")
plot(diminus, color=color.orange, title="-Di")

### Returns

Tuple of three DMi series: positive directional Movement (+Di), Negative directional Movement (-Di) and average directional Movement index (aDX).

### See also

ta.rsi
ta.tsi
ta.mfi


## ta.ema
the ema function returns the exponentially weighted moving average. in ema weighting factors decrease exponentially. it calculates by using a formula: ema = alpha * source + (1 - alpha) * ema[1], where alpha = 2 / (length + 1).

### Syntax

ta.ema(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.
- `length`

    >  (`simple` `int`)
    
    >  Number of bars (length).


### Example

//@version=5
indicator("ta.ema")
plot(ta.ema(close, 15))

//the same on pine
pine_ema(src, length) =>
    alpha = 2 / (length + 1)
    sum = 0.0
    sum := na(sum[1]) ? src : alpha * src + (1 - alpha) * nz(sum[1])
plot(pine_ema(close,15))


```

### Returns

Exponential moving average of \`source\` with alpha = 2 / (length + 1).

### Remarks

please note that using this variable/function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.sma](#fun_ta.sma)
* [ta.rma](#fun_ta.rma)
* [ta.wma](#fun_ta.wma)
* [ta.vwma](#fun_ta.vwma)
* [ta.swma](#fun_ta.swma)
* [ta.alma](#fun_ta.alma)

## ta.falling

Test if the \`source\` series is now falling for \`length\` bars long.

### Syntax

ta.falling(source, length) → series bool

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Returns

true if current \`source\` value is less than any previous \`source\` value for \`length\` bars back, false otherwise.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.rising](#fun_ta.rising)

## ta.highest

+1 overload

Highest value for a given number of bars back.

### syntax & Overloads

> [ta.highest(length) → series float](#fun_ta.highest-0)
> [ta.highest(source, length) → series float](#fun_ta.highest-1)

### Arguments

- `length`

    >  (`simple` `int`)
    
    >  Number of bars (length).

### Returns

Highest value in the series.

### Remarks

Two args version: \`source\` is a series and \`length\` is the number of bars back.

One arg version: \`length\` is the number of bars back. algorithm uses high as a \`source\` series.

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.lowest](#fun_ta.lowest)
* [ta.lowestbars](#fun_ta.lowestbars)
* [ta.highestbars](#fun_ta.highestbars)
* [ta.valuewhen](#fun_ta.valuewhen)
* [ta.barssince](#fun_ta.barssince)

## ta.highestbars

+1 overload

Highest value offset for a given number of bars back.

### syntax & Overloads

> [ta.highestbars(length) → series int](#fun_ta.highestbars-0)
> [ta.highestbars(source, length) → series int](#fun_ta.highestbars-1)

### Arguments

- `length`

    >  (`simple` `int`)
    
    >  Number of bars (length).

### Returns

Offset to the highest bar.

### Remarks

Two args version: \`source\` is a series and \`length\` is the number of bars back.

One arg version: \`length\` is the number of bars back. algorithm uses high as a \`source\` series.

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.lowest](#fun_ta.lowest)
* [ta.highest](#fun_ta.highest)
* [ta.lowestbars](#fun_ta.lowestbars)
* [ta.barssince](#fun_ta.barssince)
* [ta.valuewhen](#fun_ta.valuewhen)

## ta.hma

the hma function returns the Hull Moving average.

### Syntax

ta.hma(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`simple` `int`)
    
    >  Number of bars.

### Example


```s

//@version=5
indicator("Hull Moving average")
src = input(defval=close, title="source")
length = input(defval=9, title="Length")
hmabuildin = ta.hma(src, length)
plot(hmabuildin, title="Hull Ma", color=#674Ea7)


```

#674Ea7)

### Returns

Hull moving average of 'source' for 'length' bars back.

### Remarks

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.ema](#fun_ta.ema)
* [ta.rma](#fun_ta.rma)
* [ta.wma](#fun_ta.wma)
* [ta.vwma](#fun_ta.vwma)
* [ta.sma](#fun_ta.sma)

## ta.kc

+1 overload

Keltner Channels. Keltner channel is a technical analysis indicator showing a central moving average line plus channel lines at a distance above and below.

### syntax & Overloads

> [ta.kc(series, length, mult) - \[series float, series float, series float\]](#fun_ta.kc-0)
> [ta.kc(series, length, mult, usetrueRange) - \[series float, series float, series float\]](#fun_ta.kc-1)

### Arguments

- `series`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`simple` `int`)
    
    >  Number of bars (length).

- `mult`

    >  (`simple` `int`/`float`)
    
    >  standard deviation factor.

### Example


```s

//@version=5
indicator("ta.kc")

> [middle, upper, lower] = ta.kc(close, 5, 4)
plot(middle, color=color.yellow)
plot(upper, color=color.yellow)
plot(lower, color=color.yellow)


// the same on pine
f_kc(src, length, mult, usetrueRange) =>
    float basis = ta.ema(src, length)
    float span = (usetrueRange) ? ta.tr : (high - low)
    float rangeema = ta.ema(span, length)
    [basis, basis + rangeema * mult, basis - rangeema * mult]

    > [pinemiddle, pineupper, pineLower] = f_kc(close, 5, 4, true)

plot(pinemiddle)
plot(pineupper)
plot(pineLower)


```

### Returns

Keltner Channels.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.ema](#fun_ta.ema)
* [ta.atr](#fun_ta.atr)
* [ta.bb](#fun_ta.bb)

## ta.kcw

+1 overload

Keltner Channels Width. the Keltner Channels Width is the difference between the upper and the lower Keltner Channels divided by the middle channel.

### syntax & Overloads

> [ta.kcw(series, length, mult) → series float](#fun_ta.kcw-0)
> [ta.kcw(series, length, mult, usetrueRange) → series float](#fun_ta.kcw-1)

### Arguments

- `series`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`simple` `int`)
    
    >  Number of bars (length).

- `mult`

    >  (`simple` `int`/`float`)
    
    >  standard deviation factor.

### Example


```s

//@version=5
indicator("ta.kcw")

plot(ta.kcw(close, 5, 4), color=color.yellow)

// the same on pine
f_kcw(src, length, mult, usetrueRange) =>
    float basis = ta.ema(src, length)
    float span = (usetrueRange) ? ta.tr : (high - low)
    float rangeema = ta.ema(span, length)

    ((basis + rangeema * mult) - (basis - rangeema * mult)) / basis

plot(f_kcw(close, 5, 4, true))


```

### Returns

Keltner Channels Width.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.kc](#fun_ta.kc)
* [ta.ema](#fun_ta.ema)
* [ta.atr](#fun_ta.atr)
* [ta.bb](#fun_ta.bb)

## ta.linreg

linear regression curve. a line that best fits the prices specified over a user-defined time period. it is calculated using the least squares method. the result of this function is calculated using the formula: linreg = intercept + slope * (length - 1 - offset), where intercept and slope are the values calculated with the least squares method on \`source\` series.

### Syntax

ta.linreg(source, length, offset) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  source series.

- `length`

    >  (`simple` `int`)
    
    >  Number of bars (length).

- `offset`

    >  (`simple` `int`)
    
    >  Offset.

### Returns

linear regression curve.

### Remarks

\`na\` values in the \`source\` series are included in calculations and will produce an \`na\` result.

## ta.lowest

+1 overload

Lowest value for a given number of bars back.

### syntax & Overloads

> [ta.lowest(length) → series float](#fun_ta.lowest-0)
> [ta.lowest(source, length) → series float](#fun_ta.lowest-1)

### Arguments

- `length`

    >  (`simple` `int`)
    
    >  Number of bars (length).

### Returns

Lowest value in the series.

### Remarks

Two args version: \`source\` is a series and \`length\` is the number of bars back.

One arg version: \`length\` is the number of bars back. algorithm uses low as a \`source\` series.

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.highest](#fun_ta.highest)
* [ta.lowestbars](#fun_ta.lowestbars)
* [ta.highestbars](#fun_ta.highestbars)
* [ta.valuewhen](#fun_ta.valuewhen)
* [ta.barssince](#fun_ta.barssince)

## ta.lowestbars

+1 overload

Lowest value offset for a given number of bars back.

### syntax & Overloads

> [ta.lowestbars(length) → series int](#fun_ta.lowestbars-0)
> [ta.lowestbars(source, length) → series int](#fun_ta.lowestbars-1)

### Arguments

- `length`

    >  (`simple` `int`)
    
    >  Number of bars back.

### Returns

Offset to the lowest bar.

### Remarks

Two args version: \`source\` is a series and \`length\` is the number of bars back.

One arg version: \`length\` is the number of bars back. algorithm uses low as a \`source\` series.

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.lowest](#fun_ta.lowest)
* [ta.highest](#fun_ta.highest)
* [ta.highestbars](#fun_ta.highestbars)
* [ta.barssince](#fun_ta.barssince)
* [ta.valuewhen](#fun_ta.valuewhen)

## ta.macd

MaCD (moving average convergence/divergence). it is supposed to reveal changes in the strength, direction, momentum, and duration of a trend in a stock's price.

### Syntax

ta.macd(source, fastlen, slowlen, siglen) - \[series float, series float, series float\]

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `fastlen`

    >  (`simple` `int`)
    
    >  Fast Length parameter.

- `slowlen`

    >  (`simple` `int`)
    
    >  slow Length parameter.

- `siglen`

    >  (`simple` `int`)
    
    >  signal Length parameter.

### Example


```s

//@version=5
indicator("MaCD")
> [macdline, signalline, histline] = ta.macd(close, 12, 26, 9)
plot(macdline, color=color.blue)
plot(signalline, color=color.orange)
plot(histline, color=color.red, style=plot.style_histogram)
if you need only one value, use placeholders '_' like this:



```

### Example


```s

//@version=5
indicator("MaCD")
> [_, signalline, _] = ta.macd(close, 12, 26, 9)
plot(signalline, color=color.orange)


```

### Returns

> [Tuple](https://www.tradingview.com/pine-script-docs/en/v5/language/Type_system.html#tuples) of three MaCD series: MaCD line, signal line and histogram line.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.sma](#fun_ta.sma)
* [ta.ema](#fun_ta.ema)

## ta.max

Returns the all-time high value of \`source\` from the beginning of the chart up to the current bar.

### Syntax

ta.max(source) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  source used for the calculation.

### Remarks

> [na](#var_na) occurrences of \`source\` are ignored.

## ta.median

+1 overload

Returns the median of the series.

### syntax & Overloads

> [ta.median(source, length) → series int](#fun_ta.median-0)
> [ta.median(source, length) → series float](#fun_ta.median-1)

### Arguments

- `source`

    >  (`series` `int`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Returns

the median of the series.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

## ta.mfi

Money Flow index. the Money Flow index (MFi) is a technical oscillator that uses price and volume for identifying overbought or oversold conditions in an asset.

### Syntax

ta.mfi(series, length) → series float

### Arguments

- `series`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Example


```s

//@version=5
indicator("Money Flow index")

plot(ta.mfi(hlc3, 14), color=color.yellow)

// the same on pine
pine_mfi(src, length) =>
    float upper = math.sum(volume * (ta.change(src) <= 0.0 ? 0.0 : src), length)
    float lower = math.sum(volume * (ta.change(src) >= 0.0 ? 0.0 : src), length)
    mfi = 100.0 - (100.0 / (1.0 + upper / lower))
    mfi

plot(pine_mfi(hlc3, 14))


```

### Returns

Money Flow index.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.rsi](#fun_ta.rsi)
* [math.sum](#fun_math.sum)

## ta.min

Returns the all-time low value of \`source\` from the beginning of the chart up to the current bar.

### Syntax

ta.min(source) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  source used for the calculation.

### Remarks

> [na](#var_na) occurrences of \`source\` are ignored.

## ta.mode

+1 overload

Returns the [mode](https://en.wikipedia.org/wiki/Mode_(statistics)) of the series. if there are several values with the same frequency, it returns the smallest value.

### syntax & Overloads

> [ta.mode(source, length) → series int](#fun_ta.mode-0)
> [ta.mode(source, length) → series float](#fun_ta.mode-1)

### Arguments

- `source`

    >  (`series` `int`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Returns

the most frequently occurring value from the \`source\`. if none exists, returns the smallest value instead.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

## ta.mom

Momentum of \`source\` price and \`source\` price \`length\` bars ago. this is simply a difference: source - source\[length\].

### Syntax

ta.mom(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Offset from the current bar to the previous bar.

### Returns

Momentum of \`source\` price and \`source\` price \`length\` bars ago.

### Remarks

\`na\` values in the \`source\` series are included in calculations and will produce an \`na\` result.

### See also

* [ta.change](#fun_ta.change)

## ta.percentile\_linear\_interpolation

Calculates percentile using method of linear interpolation between the two nearest ranks.

### Syntax

ta.percentile\_linear\_interpolation(source, length, percentage) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process (source).

- `length`

    >  (`series` `int`)
    
    >  Number of bars back (length).

- `percentage`

    >  (`simple` `int`/`float`)
    
    >  percentage, a number from range 0..100.

### Returns

p-th percentile of \`source\` series for \`length\` bars back.

### Remarks

Note that a percentile calculated using this method will NOT always be a member of the input data set.

\`na\` values in the \`source\` series are included in calculations and will produce an \`na\` result.

### See also

* [ta.percentile\_nearest\_rank](#fun_ta.percentile_nearest_rank)

## ta.percentile\_nearest\_rank

Calculates percentile using method of Nearest Rank.

### Syntax

ta.percentile\_nearest\_rank(source, length, percentage) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process (source).

- `length`

    >  (`series` `int`)
    
    >  Number of bars back (length).

- `percentage`

    >  (`simple` `int`/`float`)
    
    >  percentage, a number from range 0..100.

### Returns

p-th percentile of \`source\` series for \`length\` bars back.

### Remarks

using the Nearest Rank method on lengths less than 100 bars back can result in the same number being used for more than one percentile.

a percentile calculated using the Nearest Rank method will always be a member of the input data set.

the 100th percentile is defined to be the largest value in the input data set.

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.percentile\_linear\_interpolation](#fun_ta.percentile_linear_interpolation)
* [](#)

## ta.percentrank

percent rank is the percents of how many previous values was less than or equal to the current value of given series.

### Syntax

ta.percentrank(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Returns

percent rank of \`source\` for \`length\` bars back.

### Remarks

\`na\` values in the \`source\` series are included in calculations and will produce an \`na\` result.

## ta.pivot\_point\_levels

Calculates the pivot point levels using the specified \`type\` and \`anchor\`.

### Syntax

ta.pivot\_point\_levels(type, anchor, developing) - float\[\]

### Arguments

- `type`

    >  (`series` `string`)
    
    >  the type of pivot point levels. possible values: "traditional", "Fibonacci", "Woodie", "Classic", "DM", "Camarilla".

- `anchor`

    >  (`series` `bool`)
    
    >  the condition that triggers the reset of the pivot point calculations. When [true](#op_true), calculations reset; when [false](#op_false), results calculated at the last reset persist.

- `developing`

    >  (`series` `bool`)
    
    >  if [false](#op_false), the values are those calculated the last time the anchor condition was [true](#op_true). they remain constant until the anchor condition becomes [true](#op_true) again. if [true](#op_true), the pivots are developing, i.e., they constantly recalculate on the data developing between the point of the last anchor (or bar zero if the anchor condition was never [true](#op_true)) and the current bar. optional. the default is [false](#op_false).

### Example


```s

//@version=5
indicator("Weekly pivots", max_lines_count=500, overlay=true)
timeframe = "1W"
typeinput = input.string("traditional", "Type", options=["traditional", "Fibonacci", "Woodie", "Classic", "DM", "Camarilla"])
weekChange = timeframe.change(timeframe)
pivotpointsarray = ta.pivot_point_levels(typeinput, weekChange)
if weekChange
    for pivotLevel in pivotpointsarray
        line.new(time, pivotLevel, time + timeframe.in_seconds(timeframe) * 1000, pivotLevel, xloc=xloc.bar_time)


```

### Returns

a float\[\] array with numerical values representing 11 pivot point levels: \[p, R1, s1, R2, s2, R3, s3, R4, s4, R5, s5\]. Levels absent from the specified \`type\` return [na](#var_na) values (e.g., "DM" only calculates p, R1, and s1).

### Remarks

the \`developing\` parameter cannot be \`true\` when \`type\` is set to "Woodie", because the Woodie calculation for a period depends on that period's open, which means that the pivot value is either available or unavailable, but never developing. if used together, the indicator will return a runtime error.

## ta.pivothigh

+1 overload

this function returns price of the pivot high point. it returns 'NaN', if there was no pivot high point.

### syntax & Overloads

> [ta.pivothigh(leftbars, rightbars) → series float](#fun_ta.pivothigh-0)
> [ta.pivothigh(source, leftbars, rightbars) → series float](#fun_ta.pivothigh-1)

### Arguments

- `leftbars`

    >  (`series` `int`/`float`)
    
    >  Left strength.

- `rightbars`

    >  (`series` `int`/`float`)
    
    >  Right strength.

### Example


```s

//@version=5
indicator("pivothigh", overlay=true)
leftbars = input(2)
rightbars=input(2)
ph = ta.pivothigh(leftbars, rightbars)
plot(ph, style=plot.style_cross, linewidth=3, color= color.red, offset=-rightbars)


```

### Returns

price of the point or 'NaN'.

### Remarks

if parameters 'leftbars' or 'rightbars' are series you should use [max\_bars\_back](#fun_max_bars_back) function for the 'source' variable.

## ta.pivotlow

+1 overload

this function returns price of the pivot low point. it returns 'NaN', if there was no pivot low point.

### syntax & Overloads

> [ta.pivotlow(leftbars, rightbars) → series float](#fun_ta.pivotlow-0)
> [ta.pivotlow(source, leftbars, rightbars) → series float](#fun_ta.pivotlow-1)

### Arguments

- `leftbars`

    >  (`series` `int`/`float`)
    
    >  Left strength.

- `rightbars`

    >  (`series` `int`/`float`)
    
    >  Right strength.

### Example


```s

//@version=5
indicator("pivotLow", overlay=true)
leftbars = input(2)
rightbars=input(2)
pl = ta.pivotlow(close, leftbars, rightbars)
plot(pl, style=plot.style_cross, linewidth=3, color= color.blue, offset=-rightbars)


```

### Returns

price of the point or 'NaN'.

### Remarks

if parameters 'leftbars' or 'rightbars' are series you should use [max\_bars\_back](#fun_max_bars_back) function for the 'source' variable.

## ta.range

+1 overload

Returns the difference between the min and max values in a series.

### syntax & Overloads

> [ta.range(source, length) → series int](#fun_ta.range-0)
> [ta.range(source, length) → series float](#fun_ta.range-1)

### Arguments

- `source`

    >  (`series` `int`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Returns

the difference between the min and max values in the series.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

## ta.rising

Test if the \`source\` series is now rising for \`length\` bars long.

### Syntax

ta.rising(source, length) → series bool

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Returns

true if current \`source\` is greater than any previous \`source\` for \`length\` bars back, false otherwise.

### Remarks

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.falling](#fun_ta.falling)

## ta.rma

Moving average used in Rsi. it is the exponentially weighted moving average with alpha = 1 / length.

### Syntax

ta.rma(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`simple` `int`)
    
    >  Number of bars (length).

### Example


```s

//@version=5
indicator("ta.rma")
plot(ta.rma(close, 15))

//the same on pine
pine_rma(src, length) =>
    alpha = 1/length
    sum = 0.0
    sum := na(sum[1]) ? ta.sma(src, length) : alpha * src + (1 - alpha) * nz(sum[1])
plot(pine_rma(close, 15))


```

### Returns

Exponential moving average of \`source\` with alpha = 1 / \`length\`.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.sma](#fun_ta.sma)
* [ta.ema](#fun_ta.ema)
* [ta.wma](#fun_ta.wma)
* [ta.vwma](#fun_ta.vwma)
* [ta.swma](#fun_ta.swma)
* [ta.alma](#fun_ta.alma)
* [ta.rsi](#fun_ta.rsi)

## ta.roc

Calculates the percentage of change (rate of change) between the current value of \`source\` and its value \`length\` bars ago.

it is calculated by the formula: 100 * change(src, length) / src\[length\].

### Syntax

ta.roc(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Returns

the rate of change of \`source\` for \`length\` bars back.

### Remarks

\`na\` values in the \`source\` series are included in calculations and will produce an \`na\` result.

## ta.rsi

Relative strength index. it is calculated using the \`ta.rma()\` of upward and downward changes of \`source\` over the last \`length\` bars.

### Syntax

ta.rsi(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`simple` `int`)
    
    >  Number of bars (length).

### Example


```s

//@version=5
indicator("ta.rsi")
plot(ta.rsi(close, 7))

// same on pine, but less efficient
pine_rsi(x, y) =>
    u = math.max(x - x[1], 0) // upward ta.change
    d = math.max(x[1] - x, 0) // downward ta.change
    rs = ta.rma(u, y) / ta.rma(d, y)
    res = 100 - 100 / (1 + rs)
    res

plot(pine_rsi(close, 7))


```

### Returns

Relative strength index.

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.rma](#fun_ta.rma)

## ta.sar

parabolic saR (parabolic stop and reverse) is a method devised by J. Welles Wilder, Jr., to find potential reversals in the market price direction of traded goods.

### Syntax

ta.sar(start, inc, max) → series float

### Arguments

- `start`

    >  (`simple` `int`/`float`)
    
    >  start.

- `inc`

    >  (`simple` `int`/`float`)
    
    >  increment.

- `max`

    >  (`simple` `int`/`float`)
    
    >  Maximum.

### Example


```s

//@version=5
indicator("ta.sar")
plot(ta.sar(0.02, 0.02, 0.2), style=plot.style_cross, linewidth=3)

// the same on pine scriptA(r)
pine_sar(start, inc, max) =>
    var float result = na
    var float maxMin = na
    var float acceleration = na
    var bool isbelow = na
    bool isFirsttrendbar = false

    if bar_index == 1
        if close > close[1]
            isbelow := true
            maxMin := high
            result := low[1]
        else
            isbelow := false
            maxMin := low
            result := high[1]
        isFirsttrendbar := true
        acceleration := start

    result := result + acceleration * (maxMin - result)

    if isbelow
        if result > low
            isFirsttrendbar := true
            isbelow := false
            result := math.max(high, maxMin)
            maxMin := low
            acceleration := start
    else
        if result < high
            isFirsttrendbar := true
            isbelow := true
            result := math.min(low, maxMin)
            maxMin := high
            acceleration := start

    if not isFirsttrendbar
        if isbelow
            if high > maxMin
                maxMin := high
                acceleration := math.min(acceleration + inc, max)
        else
            if low < maxMin
                maxMin := low
                acceleration := math.min(acceleration + inc, max)

    if isbelow
        result := math.min(result, low[1])
        if bar_index > 1
            result := math.min(result, low[2])

    else
        result := math.max(result, high[1])
        if bar_index > 1
            result := math.max(result, high[2])

    result

plot(pine_sar(0.02, 0.02, 0.2), style=plot.style_cross, linewidth=3)


```

### Returns

parabolic saR.

## ta.sma

the sma function returns the moving average, that is the sum of last y values of x, divided by y.

### Syntax

ta.sma(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Example


```s

//@version=5
indicator("ta.sma")
plot(ta.sma(close, 15))

// same on pine, but much less efficient
pine_sma(x, y) =>
    sum = 0.0
    for i = 0 to y - 1
        sum := sum + x[i] / y
    sum
plot(pine_sma(close, 15))


```

### Returns

simple moving average of \`source\` for \`length\` bars back.

### Remarks

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.ema](#fun_ta.ema)
* [ta.rma](#fun_ta.rma)
* [ta.wma](#fun_ta.wma)
* [ta.vwma](#fun_ta.vwma)
* [ta.swma](#fun_ta.swma)
* [ta.alma](#fun_ta.alma)

## ta.stdev

### Syntax

ta.stdev(source, length, biased) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

- `biased`

    >  (`series` `bool`)
    
    >  Determines which estimate should be used. optional. the default is true.

### Example


```s

//@version=5
indicator("ta.stdev")
plot(ta.stdev(close, 5))

//the same on pine
isZero(val, eps) => math.abs(val) <= eps

suM(fst, snd) =>
    Eps = 1e-10
    res = fst + snd
    if isZero(res, Eps)
        res := 0
    else
        if not isZero(res, 1e-4)
            res := res
        else
            15

pine_stdev(src, length) =>
    avg = ta.sma(src, length)
    sumOfsquareDeviations = 0.0
    for i = 0 to length - 1
        sum = suM(src[i], -avg)
        sumOfsquareDeviations := sumOfsquareDeviations + sum * sum

    stdev = math.sqrt(sumOfsquareDeviations / length)
plot(pine_stdev(close, 5))


```

### Returns

standard deviation.

### Remarks

if \`biased\` is true, function will calculate using a biased estimate of the entire population, if false - unbiased estimate of a sample.

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.dev](#fun_ta.dev)
* [ta.variance](#fun_ta.variance)

## ta.stoch

stochastic. it is calculated by a formula: 100 * (close - lowest(low, length)) / (highest(high, length) - lowest(low, length)).

### Syntax

ta.stoch(source, high, low, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  source series.

- `high`

    >  (`series` `int`/`float`)
    
    >  series of high.

- `low`

    >  (`series` `int`/`float`)
    
    >  series of low.

- `length`

    >  (`series` `int`)
    
    >  Length (number of bars back).

### Returns

stochastic.

### Remarks

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.cog](#fun_ta.cog)

## ta.supertrend

the supertrend indicator. the supertrend is a trend following indicator.

### Syntax

ta.supertrend(factor, atrperiod) - \[series float, series float\]

### Arguments

- `factor`

    >  (`series` `int`/`float`)
    
    >  the multiplier by which the atr will get multiplied.

- `atrperiod`

    >  (`simple` `int`)
    
    >  Length of atr.

### Example


```s

//@version=5
indicator("pine scriptA(r) supertrend")

> [supertrend, direction] = ta.supertrend(3, 10)
plot(direction < 0 ? supertrend : na, "up direction", color = color.green, style=plot.style_linebr)
plot(direction > 0 ? supertrend : na, "Down direction", color = color.red, style=plot.style_linebr)

// the same on pine scriptA(r)
pine_supertrend(factor, atrperiod) =>
    src = hl2
    atr = ta.atr(atrperiod)
    upperband = src + factor * atr
    lowerband = src - factor * atr
    prevLowerband = nz(lowerband[1])
    prevupperband = nz(upperband[1])

    lowerband := lowerband > prevLowerband or close[1] < prevLowerband ? lowerband : prevLowerband
    upperband := upperband < prevupperband or close[1] > prevupperband ? upperband : prevupperband
    int direction = na
    float supertrend = na
    prevsupertrend = supertrend[1]
    if na(atr[1])
        direction := 1
    else if prevsupertrend == prevupperband
        direction := close > upperband ? -1 : 1
    else
        direction := close < lowerband ? 1 : -1
    supertrend := direction == -1 ? lowerband : upperband
    [supertrend, direction]

> [pine_supertrend, pinedirection] = pine_supertrend(3, 10)
plot(pinedirection < 0 ? pine_supertrend : na, "up direction", color = color.green, style=plot.style_linebr)
plot(pinedirection > 0 ? pine_supertrend : na, "Down direction", color = color.red, style=plot.style_linebr)


```

### Returns

> [Tuple](https://www.tradingview.com/pine-script-docs/en/v5/language/Type_system.html#tuples) of two supertrend series: supertrend line and direction of trend. possible values are 1 (down direction) and -1 (up direction).

### See also

* [ta.macd](#fun_ta.macd)

## ta.swma

symmetrically weighted moving average with fixed length: 4. Weights: \[1/6, 2/6, 2/6, 1/6\].

### Syntax

ta.swma(source) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  source series.

### Example


```s

//@version=5
indicator("ta.swma")
plot(ta.swma(close))

// same on pine, but less efficient
pine_swma(x) =>
    x[3] * 1 / 6 + x[2] * 2 / 6 + x[1] * 2 / 6 + x[0] * 1 / 6
plot(pine_swma(close))


```

### Returns

symmetrically weighted moving average.

### Remarks

\`na\` values in the \`source\` series are included in calculations and will produce an \`na\` result.

### See also

* [ta.sma](#fun_ta.sma)
* [ta.ema](#fun_ta.ema)
* [ta.rma](#fun_ta.rma)
* [ta.wma](#fun_ta.wma)
* [ta.vwma](#fun_ta.vwma)
* [ta.alma](#fun_ta.alma)

## ta.tr

### Syntax

ta.tr(handle_na) → series float

### Arguments

- `handle_na`

    >  (`simple` `bool`)
    
    >  How NaN values are handled. if true, and previous day's close is NaN then tr would be calculated as current day high-low. Otherwise (if false) tr would return NaN in such cases. also note, that [ta.atr](#fun_ta.atr) uses ta.tr(true).

### Returns

true range. it is math.max(high - low, math.abs(high - close\[1\]), math.abs(low - close\[1\])).

### Remarks

ta.tr(false) is exactly the same as [ta.tr](#var_ta.tr).

### See also

* [ta.tr](#var_ta.tr)
* [ta.atr](#fun_ta.atr)

## ta.tsi

true strength index. it uses moving averages of the underlying momentum of a financial instrument.

### Syntax

ta.tsi(source, short\_length, long\_length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  source series.

- `short_length`

    >  (`simple` `int`)
    
    >  short length.

- `long_length`

    >  (`simple` `int`)
    
    >  Long length.

### Returns

true strength index. a value in range \[-1, 1\].

### Remarks

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

## ta.valuewhen

+3 overloads

Returns the value of the \`source\` series on the bar where the \`condition\` was true on the nth most recent occurrence.

### syntax & Overloads

> [ta.valuewhen(condition, source, occurrence) → series color](#fun_ta.valuewhen-0)
> [ta.valuewhen(condition, source, occurrence) → series int](#fun_ta.valuewhen-1)
> [ta.valuewhen(condition, source, occurrence) → series float](#fun_ta.valuewhen-2)
> [ta.valuewhen(condition, source, occurrence) → series bool](#fun_ta.valuewhen-3)

### Arguments

- `condition`

    >  (`series` `bool`)
    
    >  the condition to search for.

- `source`

    >  (`series` `color`)
    
    >  the value to be returned from the bar where the condition is met.

- `occurrence`

    >  (`simple` `int`)
    
    >  the occurrence of the condition. the numbering starts from 0 and goes back in time, so '0' is the most recent occurrence of \`condition\`, '1' is the second most recent and so forth. Must be an integer >= 0.

### Example


```s

//@version=5
indicator("ta.valuewhen")
slow = ta.sma(close, 7)
fast = ta.sma(close, 14)
// Get value of `close` on second most recent cross
plot(ta.valuewhen(ta.cross(slow, fast), close, 1))


```

### Remarks

this function requires execution on every bar. it is not recommended to use it inside a [for](#op_for) or [while](#op_while) loop structure, where its behavior can be unexpected. please note that using this function can cause [indicator repainting](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html).

### See also

* [ta.lowestbars](#fun_ta.lowestbars)
* [ta.highestbars](#fun_ta.highestbars)
* [ta.barssince](#fun_ta.barssince)
* [ta.highest](#fun_ta.highest)
* [ta.lowest](#fun_ta.lowest)

## ta.variance

variance is the expectation of the squared deviation of a series from its mean ([ta.sma](#fun_ta.sma)), and it informally measures how far a set of numbers are spread out from their mean.

### Syntax

ta.variance(source, length, biased) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

- `biased`

    >  (`series` `bool`)
    
    >  Determines which estimate should be used. optional. the default is true.

### Returns

variance of \`source\` for \`length\` bars back.

### Remarks

if \`biased\` is true, function will calculate using a biased estimate of the entire population, if false - unbiased estimate of a sample.

\`na\` values in the \`source\` series are ignored; the function calculates on the \`length\` quantity of non-\`na\` values.

### See also

* [ta.dev](#fun_ta.dev)
* [ta.stdev](#fun_ta.stdev)

## ta.vwap

+2 overloads

Volume weighted average price.

### syntax & Overloads

> [ta.vwap(source) → series float](#fun_ta.vwap-0)
> [ta.vwap(source, anchor) → series float](#fun_ta.vwap-1)
> [ta.vwap(source, anchor, stdev_mult) - \[series float, series float, series float\]](#fun_ta.vwap-2)

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  source used for the VWap calculation.

### Example


```s

//@version=5
indicator("simple VWap")
vwap = ta.vwap(open)
plot(vwap)



```

### Example


```s

//@version=5
indicator("advanced VWap")
vwapanchorinput = input.string("Daily", "anchor", options = ["Daily", "Weekly", "Monthly"])
stdevMultiplierinput = input.float(1.0, "standard Deviation Multiplier")
anchortimeframe = switch vwapanchorinput
    "Daily"   => "1D"
    "Weekly"  => "1W"
    "Monthly" => "1M"
anchor = timeframe.change(anchortimeframe)
> [vwap, upper, lower] = ta.vwap(open, anchor, stdevMultiplierinput)
plot(vwap)
plot(upper, color = color.green)
plot(lower, color = color.green)


```

### Returns

a VWap series, or a tuple \[vwap, upper\_band, lower\_band\] if \`stdev_mult\` is specified.

### Remarks

Calculations only begin the first time the anchor condition becomes [true](#op_true). until then, the function returns [na](#var_na).

### See also

* [ta.vwap](#var_ta.vwap)

## ta.vwma

the vwma function returns volume-weighted moving average of \`source\` for \`length\` bars back. it is the same as: sma(source * volume, length) / sma(volume, length).

### Syntax

ta.vwma(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Example


```s

//@version=5
indicator("ta.vwma")
plot(ta.vwma(close, 15))

// same on pine, but less efficient
pine_vwma(x, y) =>
    ta.sma(x * volume, y) / ta.sma(volume, y)
plot(pine_vwma(close, 15))


```

### Returns

Volume-weighted moving average of \`source\` for \`length\` bars back.

### Remarks

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.sma](#fun_ta.sma)
* [ta.ema](#fun_ta.ema)
* [ta.rma](#fun_ta.rma)
* [ta.wma](#fun_ta.wma)
* [ta.swma](#fun_ta.swma)
* [ta.alma](#fun_ta.alma)

## ta.wma

the wma function returns weighted moving average of \`source\` for \`length\` bars back. in wma weighting factors decrease in arithmetical progression.

### Syntax

ta.wma(source, length) → series float

### Arguments

- `source`

    >  (`series` `int`/`float`)
    
    >  series of values to process.

- `length`

    >  (`series` `int`)
    
    >  Number of bars (length).

### Example


```s

//@version=5
indicator("ta.wma")
plot(ta.wma(close, 15))

// same on pine, but much less efficient
pine_wma(x, y) =>
    norm = 0.0
    sum = 0.0
    for i = 0 to y - 1
        weight = (y - i) * y
        norm := norm + weight
        sum := sum + x[i] * weight
    sum / norm
plot(pine_wma(close, 15))


```

### Returns

Weighted moving average of \`source\` for \`length\` bars back.

### Remarks

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.sma](#fun_ta.sma)
* [ta.ema](#fun_ta.ema)
* [ta.rma](#fun_ta.rma)
* [ta.vwma](#fun_ta.vwma)
* [ta.swma](#fun_ta.swma)
* [ta.alma](#fun_ta.alma)

## ta.wpr

Williams %R. the oscillator shows the current closing price in relation to the high and low of the past 'length' bars.

### Syntax

ta.wpr(length) → series float

### Arguments

- `length`

    >  (`series` `int`)
    
    >  Number of bars.

### Example


```s

//@version=5
indicator("Williams %R", shorttitle="%R", format=format.price, precision=2)
plot(ta.wpr(14), title="%R", color=color.new(#ff6d00, 0))


```

#ff6d00, 0))

### Returns

Williams %R.

### Remarks

\`na\` values in the \`source\` series are ignored.

### See also

* [ta.mfi](#fun_ta.mfi)
* [ta.cmo](#fun_ta.cmo)

## table

Casts na to table

### Syntax

table(x) → series table

### Arguments

- `x`

    >  (`series` `table`)
    
    >  the value to convert to the specified type, usually [na](#var_na).

### Returns

the value of the argument after casting to table.

### See also

* [float](#fun_float)
* [int](#fun_int)
* [bool](#fun_bool)
* [color](#fun_color)
* [string](#fun_string)
* [line](#fun_line)
* [label](#fun_label)

## table.cell

the function defines a cell in the table and sets its attributes.

### Syntax

table.cell(table\_id, column, row, text, width, height, text\_color, text\_halign, text\_valign, text\_size, bgcolor, tooltip, text\_font_family) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `column`

    >  (`series` `int`)
    
    >  the index of the cell's column. Numbering starts at 0.

- `row`

    >  (`series` `int`)
    
    >  the index of the cell's row. Numbering starts at 0.

- `text`

    >  (`series` `string`)
    
    >  the text to be displayed inside the cell. optional. the default is empty string.

- `width`

    >  (`series` `int`)
    
    >  the width of the cell as a % of the indicator's visual space. optional. by default, auto-adjusts the width based on the text inside the cell. Value 0 has the same effect.

- `height`

    >  (`series` `int`)
    
    >  the height of the cell as a % of the indicator's visual space. optional. by default, auto-adjusts the height based on the text inside of the cell. Value 0 has the same effect.

- `text_color`

    >  (`series` `color`)
    
    >  the color of the text. optional. the default is [color.black](#var_color.black).

- `text_halign`

    >  (`series` `string`)
    
    >  the horizontal alignment of the cell's text. optional. the default value is [text.align_center](#var_text.align_center). possible values: [text.align_left](#var_text.align_left), [text.align_center](#var_text.align_center), [text.align_right](#var_text.align_right).

- `text_valign`

    >  (`series` `string`)
    
    >  the vertical alignment of the cell's text. optional. the default value is [text.align_center](#var_text.align_center). possible values: [text.align_top](#var_text.align_top), [text.align_center](#var_text.align_center), [text.align_bottom](#var_text.align_bottom).

- `text_size`

    >  (`series` `string`)
    
    >  the size of the text. an optional parameter, the default value is [size.normal](#var_size.normal). possible values: [size.auto](#var_size.auto), [size.tiny](#var_size.tiny), [size.small](#var_size.small), [size.normal](#var_size.normal), [size.large](#var_size.large), [size.huge](#var_size.huge).

- `bgcolor`

    >  (`series` `color`)
    
    >  the background color of the text. optional. the default is no color.

- `tooltip`

    >  (`series` `string`)
    
    >  the tooltip to be displayed inside the cell. optional.

- `text\_font\_family`

    >  (`series` `string`)
    
    >  the font family of the text. optional. the default value is [font.family_default](#var_font.family_default). possible values: [font.family_default](#var_font.family_default), [font.family_monospace](#var_font.family_monospace).

### Remarks

this function does not create the table itself, but defines the table's cells. To use it, you first need to create a table object with [table.new](#fun_table.new).

Each [table.cell](#fun_table.cell) call overwrites all previously defined properties of a cell. if you call [table.cell](#fun_table.cell) twice in a row, e.g., the first time with text='Test Text', and the second time with text_color=[color.red](#var_color.red) but without a new text argument, the default value of the 'text' being an empty string, it will overwrite 'Test Text', and your cell will display an empty string. if you want, instead, to modify any of the cell's properties, use the table.cell\_set\_*() functions.

a single script can only display one table in each of the possible locations. if [table.cell](#fun_table.cell) is used on several bars to change the same attribute of a cell (e.g. change the background color of the cell to red on the first bar, then to yellow on the second bar), only the last change will be reflected in the table, i.e., the cell's background will be yellow. avoid unnecessary setting of cell properties by enclosing function calls in an [if](#op_if) [barstate.islast](#var_barstate.islast) block whenever possible, to restrict their execution to the last bar of the series.

### See also

* [table.cell\_set\_bgcolor](#fun_table.cell_set_bgcolor)
* [table.cell\_set\_height](#fun_table.cell_set_height)
* [table.cell\_set\_text](#fun_table.cell_set_text)
* [table.cell\_set\_text_color](#fun_table.cell_set_text_color)
* [table.cell\_set\_text_halign](#fun_table.cell_set_text_halign)
* [table.cell\_set\_text_size](#fun_table.cell_set_text_size)
* [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign)
* [table.cell\_set\_width](#fun_table.cell_set_width)
* [table.cell\_set\_tooltip](#fun_table.cell_set_tooltip)

## table.cell\_set\_bgcolor

the function sets the background color of the cell.

### Syntax

table.cell\_set\_bgcolor(table_id, column, row, bgcolor) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `column`

    >  (`series` `int`)
    
    >  the index of the cell's column. Numbering starts at 0.

- `row`

    >  (`series` `int`)
    
    >  the index of the cell's row. Numbering starts at 0.

- `bgcolor`

    >  (`series` `color`)
    
    >  the background color of the cell.

### See also

* [table.cell\_set\_height](#fun_table.cell_set_height)
* [table.cell\_set\_text](#fun_table.cell_set_text)
* [table.cell\_set\_text_color](#fun_table.cell_set_text_color)
* [table.cell\_set\_text_halign](#fun_table.cell_set_text_halign)
* [table.cell\_set\_text_size](#fun_table.cell_set_text_size)
* [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign)
* [table.cell\_set\_width](#fun_table.cell_set_width)
* [table.cell\_set\_tooltip](#fun_table.cell_set_tooltip)

## table.cell\_set\_height

the function sets the height of cell.

### Syntax

table.cell\_set\_height(table_id, column, row, height) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `column`

    >  (`series` `int`)
    
    >  the index of the cell's column. Numbering starts at 0.

- `row`

    >  (`series` `int`)
    
    >  the index of the cell's row. Numbering starts at 0.

- `height`

    >  (`series` `int`)
    
    >  the height of the cell as a % of the chart window. passing 0 auto-adjusts the height based on the text inside of the cell.

### See also

* [table.cell\_set\_bgcolor](#fun_table.cell_set_bgcolor)
* [table.cell\_set\_text](#fun_table.cell_set_text)
* [table.cell\_set\_text_color](#fun_table.cell_set_text_color)
* [table.cell\_set\_text_halign](#fun_table.cell_set_text_halign)
* [table.cell\_set\_text_size](#fun_table.cell_set_text_size)
* [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign)
* [table.cell\_set\_width](#fun_table.cell_set_width)
* [table.cell\_set\_tooltip](#fun_table.cell_set_tooltip)

## table.cell\_set\_text

the function sets the text in the specified cell.

### Syntax

table.cell\_set\_text(table_id, column, row, text) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `column`

    >  (`series` `int`)
    
    >  the index of the cell's column. Numbering starts at 0.

- `row`

    >  (`series` `int`)
    
    >  the index of the cell's row. Numbering starts at 0.

- `text`

    >  (`series` `string`)
    
    >  the text to be displayed inside the cell.

### Example


```s

//@version=5
indicator("table example")
var tLog = table.new(position = position.top_left, rows = 1, columns = 2, bgcolor = color.yellow, border_width=1)
table.cell(tLog, row = 0, column = 0, text = "sometext", text_color = color.blue)
table.cell_set_text(tLog, row = 0, column = 0, text = "sometext")


```

### See also

* [table.cell\_set\_bgcolor](#fun_table.cell_set_bgcolor)
* [table.cell\_set\_height](#fun_table.cell_set_height)
* [table.cell\_set\_text_color](#fun_table.cell_set_text_color)
* [table.cell\_set\_text_halign](#fun_table.cell_set_text_halign)
* [table.cell\_set\_text_size](#fun_table.cell_set_text_size)
* [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign)
* [table.cell\_set\_width](#fun_table.cell_set_width)
* [table.cell\_set\_tooltip](#fun_table.cell_set_tooltip)

## table.cell\_set\_text_color

the function sets the color of the text inside the cell.

### Syntax

table.cell\_set\_text\_color(table\_id, column, row, text_color) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `column`

    >  (`series` `int`)
    
    >  the index of the cell's column. Numbering starts at 0.

- `row`

    >  (`series` `int`)
    
    >  the index of the cell's row. Numbering starts at 0.

- `text_color`

    >  (`series` `color`)
    
    >  the color of the text.

### See also

* [table.cell\_set\_bgcolor](#fun_table.cell_set_bgcolor)
* [table.cell\_set\_height](#fun_table.cell_set_height)
* [table.cell\_set\_text](#fun_table.cell_set_text)
* [table.cell\_set\_text_halign](#fun_table.cell_set_text_halign)
* [table.cell\_set\_text_size](#fun_table.cell_set_text_size)
* [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign)
* [table.cell\_set\_width](#fun_table.cell_set_width)
* [table.cell\_set\_tooltip](#fun_table.cell_set_tooltip)

## table.cell\_set\_text\_font\_family

the function sets the font family of the text inside the cell.

### Syntax

table.cell\_set\_text\_font\_family(table\_id, column, row, text\_font_family) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `column`

    >  (`series` `int`)
    
    >  the index of the cell's column. Numbering starts at 0.

- `row`

    >  (`series` `int`)
    
    >  the index of the cell's row. Numbering starts at 0.

- `text\_font\_family`

    >  (`series` `string`)
    
    >  the font family of the text. possible values: [font.family_default](#var_font.family_default), [font.family_monospace](#var_font.family_monospace).

### Example


```s

//@version=5
indicator("Example of setting the table cell font")
var t = table.new(position.top_left, rows = 1, columns = 1)
table.cell(t, 0, 0, "monospace", text_color = color.blue)
table.cell_set_text_font_family(t, 0, 0, font.family_monospace)


```

### See also

* [table.new](#fun_table.new)
* [font.family_default](#var_font.family_default)
* [font.family_monospace](#var_font.family_monospace)

## table.cell\_set\_text_halign

the function sets the horizontal alignment of the cell's text.

### Syntax

table.cell\_set\_text\_halign(table\_id, column, row, text_halign) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `column`

    >  (`series` `int`)
    
    >  the index of the cell's column. Numbering starts at 0.

- `row`

    >  (`series` `int`)
    
    >  the index of the cell's row. Numbering starts at 0.

- `text_halign`

    >  (`series` `string`)
    
    >  the horizontal alignment of a cell's text. possible values: [text.align_left](#var_text.align_left), [text.align_center](#var_text.align_center), [text.align_right](#var_text.align_right).

### See also

* [table.cell\_set\_bgcolor](#fun_table.cell_set_bgcolor)
* [table.cell\_set\_height](#fun_table.cell_set_height)
* [table.cell\_set\_text](#fun_table.cell_set_text)
* [table.cell\_set\_text_color](#fun_table.cell_set_text_color)
* [table.cell\_set\_text_size](#fun_table.cell_set_text_size)
* [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign)
* [table.cell\_set\_width](#fun_table.cell_set_width)
* [table.cell\_set\_tooltip](#fun_table.cell_set_tooltip)

## table.cell\_set\_text_size

the function sets the size of the cell's text.

### Syntax

table.cell\_set\_text\_size(table\_id, column, row, text_size) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `column`

    >  (`series` `int`)
    
    >  the index of the cell's column. Numbering starts at 0.

- `row`

    >  (`series` `int`)
    
    >  the index of the cell's row. Numbering starts at 0.

- `text_size`

    >  (`series` `string`)
    
    >  the size of the text. possible values: [size.auto](#var_size.auto), [size.tiny](#var_size.tiny), [size.small](#var_size.small), [size.normal](#var_size.normal), [size.large](#var_size.large), [size.huge](#var_size.huge).

### See also

* [table.cell\_set\_bgcolor](#fun_table.cell_set_bgcolor)
* [table.cell\_set\_height](#fun_table.cell_set_height)
* [table.cell\_set\_text](#fun_table.cell_set_text)
* [table.cell\_set\_text_color](#fun_table.cell_set_text_color)
* [table.cell\_set\_text_halign](#fun_table.cell_set_text_halign)
* [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign)
* [table.cell\_set\_width](#fun_table.cell_set_width)
* [table.cell\_set\_tooltip](#fun_table.cell_set_tooltip)

## table.cell\_set\_text_valign

the function sets the vertical alignment of a cell's text.

### Syntax

table.cell\_set\_text\_valign(table\_id, column, row, text_valign) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `column`

    >  (`series` `int`)
    
    >  the index of the cell's column. Numbering starts at 0.

- `row`

    >  (`series` `int`)
    
    >  the index of the cell's row. Numbering starts at 0.

- `text_valign`

    >  (`series` `string`)
    
    >  the vertical alignment of the cell's text. possible values: [text.align_top](#var_text.align_top), [text.align_center](#var_text.align_center), [text.align_bottom](#var_text.align_bottom).

### See also

* [table.cell\_set\_bgcolor](#fun_table.cell_set_bgcolor)
* [table.cell\_set\_height](#fun_table.cell_set_height)
* [table.cell\_set\_text](#fun_table.cell_set_text)
* [table.cell\_set\_text_color](#fun_table.cell_set_text_color)
* [table.cell\_set\_text_halign](#fun_table.cell_set_text_halign)
* [table.cell\_set\_text_size](#fun_table.cell_set_text_size)
* [table.cell\_set\_width](#fun_table.cell_set_width)
* [table.cell\_set\_tooltip](#fun_table.cell_set_tooltip)

## table.cell\_set\_tooltip

the function sets the tooltip in the specified cell.

### Syntax

table.cell\_set\_tooltip(table_id, column, row, tooltip) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `column`

    >  (`series` `int`)
    
    >  the index of the cell's column. Numbering starts at 0.

- `row`

    >  (`series` `int`)
    
    >  the index of the cell's row. Numbering starts at 0.

- `tooltip`

    >  (`series` `string`)
    
    >  the tooltip to be displayed inside the cell.

### Example


```s

//@version=5
indicator("table example")
var tLog = table.new(position = position.top_left, rows = 1, columns = 2, bgcolor = color.yellow, border_width=1)
table.cell(tLog, row = 0, column = 0, text = "sometext", text_color = color.blue)
table.cell_set_tooltip(tLog, row = 0, column = 0, tooltip = "sometext")


```

### See also

* [table.cell\_set\_bgcolor](#fun_table.cell_set_bgcolor)
* [table.cell\_set\_height](#fun_table.cell_set_height)
* [table.cell\_set\_text_color](#fun_table.cell_set_text_color)
* [table.cell\_set\_text_halign](#fun_table.cell_set_text_halign)
* [table.cell\_set\_text_size](#fun_table.cell_set_text_size)
* [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign)
* [table.cell\_set\_width](#fun_table.cell_set_width)
* [table.cell\_set\_text](#fun_table.cell_set_text)

## table.cell\_set\_width

the function sets the width of the cell.

### Syntax

table.cell\_set\_width(table_id, column, row, width) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `column`

    >  (`series` `int`)
    
    >  the index of the cell's column. Numbering starts at 0.

- `row`

    >  (`series` `int`)
    
    >  the index of the cell's row. Numbering starts at 0.

- `width`

    >  (`series` `int`)
    
    >  the width of the cell as a % of the chart window. passing 0 auto-adjusts the width based on the text inside of the cell.

### See also

* [table.cell\_set\_bgcolor](#fun_table.cell_set_bgcolor)
* [table.cell\_set\_height](#fun_table.cell_set_height)
* [table.cell\_set\_text](#fun_table.cell_set_text)
* [table.cell\_set\_text_color](#fun_table.cell_set_text_color)
* [table.cell\_set\_text_halign](#fun_table.cell_set_text_halign)
* [table.cell\_set\_text_size](#fun_table.cell_set_text_size)
* [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign)
* [table.cell\_set\_tooltip](#fun_table.cell_set_tooltip)

## table.clear

the function removes a cell or a sequence of cells from the table. the cells are removed in a rectangle shape where the start\_column and start\_row specify the top-left corner, and end\_column and end\_row specify the bottom-right corner.

### Syntax

table.clear(table\_id, start\_column, start\_row, end\_column, end_row) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `start_column`

    >  (`series` `int`)
    
    >  the index of the column of the first cell to delete. Numbering starts at 0.

- `start_row`

    >  (`series` `int`)
    
    >  the index of the row of the first cell to delete. Numbering starts at 0.

- `end_column`

    >  (`series` `int`)
    
    >  the index of the column of the last cell to delete. optional. the default is the argument used for start_column. Numbering starts at 0.

- `end_row`

    >  (`series` `int`)
    
    >  the index of the row of the last cell to delete. optional. the default is the argument used for start_row. Numbering starts at 0.

### Example


```s

//@version=5
indicator("a donut", overlay=true)
if barstate.islast
    colNum = 8, rowNum = 8
    padding = "a---"
    donuttable = table.new(position.middle_right, colNum, rowNum)
    for c = 0 to colNum - 1
        for r = 0 to rowNum - 1
            table.cell(donuttable, c, r, text=padding, bgcolor=#face6e, text_color=color.new(color.black, 100))
    table.clear(donuttable, 2, 2, 5, 5)


```

#face6e, text_color=color.new(color.black, 100))    table.clear(donuttable, 2, 2, 5, 5)

### See also

* [table.delete](#fun_table.delete)
* [table.new](#fun_table.new)

## table.delete

the function deletes a table.

### Syntax

table.delete(table_id) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

### Example


```s

//@version=5
indicator("table.delete example")
var testtable = table.new(position = position.top_right, columns = 2, rows = 1, bgcolor = color.yellow, border_width = 1)
if barstate.islast
    table.cell(table_id = testtable, column = 0, row = 0, text = "Open is " + str.tostring(open))
    table.cell(table_id = testtable, column = 1, row = 0, text = "Close is " + str.tostring(close), bgcolor=color.teal)
if barstate.isrealtime
    table.delete(testtable)


```

### See also

* [table.new](#fun_table.new)
* [table.clear](#fun_table.clear)

## table.merge_cells

the function merges a sequence of cells in the table into one cell. the cells are merged in a rectangle shape where the start\_column and start\_row specify the top-left corner, and end\_column and end\_row specify the bottom-right corner.

### Syntax

table.merge\_cells(table\_id, start\_column, start\_row, end\_column, end\_row) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `start_column`

    >  (`series` `int`)
    
    >  the index of the column of the first cell to merge. Numbering starts at 0.

- `start_row`

    >  (`series` `int`)
    
    >  the index of the row of the first cell to merge. Numbering starts at 0.

- `end_column`

    >  (`series` `int`)
    
    >  the index of the column of the last cell to merge. Numbering starts at 0.

- `end_row`

    >  (`series` `int`)
    
    >  the index of the row of the last cell to merge. Numbering starts at 0.

### Example


```s

//@version=5
indicator("table.merge_cells example")
sMa50  = ta.sma(close, 50)
sMa100 = ta.sma(close, 100)
sMa200 = ta.sma(close, 200)
if barstate.islast
    matable = table.new(position.bottom_right, 3, 3, bgcolor = color.gray, border_width = 1, border_color = color.black)
    // header
    table.cell(matable, 0, 0, text = "sMa table")
    table.merge_cells(matable, 0, 0, 2, 0)
    // Cell titles
    table.cell(matable, 0, 1, text = "sMa 50")
    table.cell(matable, 1, 1, text = "sMa 100")
    table.cell(matable, 2, 1, text = "sMa 200")
    // Values
    table.cell(matable, 0, 2, bgcolor = color.white, text = str.tostring(sMa50))
    table.cell(matable, 1, 2, bgcolor = color.white, text = str.tostring(sMa100))
    table.cell(matable, 2, 2, bgcolor = color.white, text = str.tostring(sMa200))


```

### Remarks

this function will merge cells, even if their properties are not yet defined with [table.cell](#fun_table.cell).

the resulting merged cell inherits all of its values from the cell located at \`start\_column\`:\`start\_row\`, except width and height. the width and height of the resulting merged cell are based on the width/height of other cells in the neighboring columns/rows and cannot be set manually.

To modify the merged cell with any of the \`table.cell\_set\_*\` functions, target the cell at the \`start\_column\`:\`start\_row\` coordinates.

an attempt to merge a cell that has already been merged will result in an error.

### See also

* [table.delete](#fun_table.delete)
* [table.new](#fun_table.new)

## table.new

the function creates a new table.

### Syntax

table.new(position, columns, rows, bgcolor, frame\_color, frame\_width, border\_color, border\_width) → series table

### Arguments

- `position`

    >  (`series` `string`)
    
    >  position of the table. possible values are: [position.top_left](#var_position.top_left), [position.top_center](#var_position.top_center), [position.top_right](#var_position.top_right), [position.middle_left](#var_position.middle_left), [position.middle_center](#var_position.middle_center), [position.middle_right](#var_position.middle_right), [position.bottom_left](#var_position.bottom_left), [position.bottom_center](#var_position.bottom_center), [position.bottom_right](#var_position.bottom_right).

- `columns`

    >  (`series` `int`)
    
    >  the number of columns in the table.

- `rows`

    >  (`series` `int`)
    
    >  the number of rows in the table.

- `bgcolor`

    >  (`series` `color`)
    
    >  the background color of the table. optional. the default is no color.

- `frame_color`

    >  (`series` `color`)
    
    >  the color of the outer frame of the table. optional. the default is no color.

- `frame_width`

    >  (`series` `int`)
    
    >  the width of the outer frame of the table. optional. the default is 0.

- `border_color`

    >  (`series` `color`)
    
    >  the color of the borders of the cells (excluding the outer frame). optional. the default is no color.

- `border_width`

    >  (`series` `int`)
    
    >  the width of the borders of the cells (excluding the outer frame). optional. the default is 0.

### Example


```s

//@version=5
indicator("table.new example")
var testtable = table.new(position = position.top_right, columns = 2, rows = 1, bgcolor = color.yellow, border_width = 1)
if barstate.islast
    table.cell(table_id = testtable, column = 0, row = 0, text = "Open is " + str.tostring(open))
    table.cell(table_id = testtable, column = 1, row = 0, text = "Close is " + str.tostring(close), bgcolor=color.teal)


```

### Returns

the iD of a table object that can be passed to other table.*() functions.

### Remarks

this function creates the table object itself, but the table will not be displayed until its cells are populated. To define a cell and change its contents or attributes, use [table.cell](#fun_table.cell) and other table.cell_*() functions.

One [table.new](#fun_table.new) call can only display one table (the last one drawn), but the function itself will be recalculated on each bar it is used on. For performance reasons, it is wise to use [table.new](#fun_table.new) in conjunction with either the [var](#op_var) keyword (so the table object is only created on the first bar) or in an [if](#op_if) [barstate.islast](#var_barstate.islast) block (so the table object is only created on the last bar).

### See also

* [table.cell](#fun_table.cell)
* [table.clear](#fun_table.clear)
* [table.delete](#fun_table.delete)
* [table.set_bgcolor](#fun_table.set_bgcolor)
* [table.set\_border\_color](#fun_table.set_border_color)
* [table.set\_border\_width](#fun_table.set_border_width)
* [table.set\_frame\_color](#fun_table.set_frame_color)
* [table.set\_frame\_width](#fun_table.set_frame_width)
* [table.set_position](#fun_table.set_position)

## table.set_bgcolor

the function sets the background color of a table.

### Syntax

table.set\_bgcolor(table\_id, bgcolor) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `bgcolor`

    >  (`series` `color`)
    
    >  the background color of the table. optional. the default is no color.

### See also

* [table.clear](#fun_table.clear)
* [table.delete](#fun_table.delete)
* [table.new](#fun_table.new)
* [table.set\_border\_color](#fun_table.set_border_color)
* [table.set\_border\_width](#fun_table.set_border_width)
* [table.set\_frame\_color](#fun_table.set_frame_color)
* [table.set\_frame\_width](#fun_table.set_frame_width)
* [table.set_position](#fun_table.set_position)

## table.set\_border\_color

the function sets the color of the borders (excluding the outer frame) of the table's cells.

### Syntax

table.set\_border\_color(table\_id, border\_color) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `border_color`

    >  (`series` `color`)
    
    >  the color of the borders. optional. the default is no color.

### See also

* [table.clear](#fun_table.clear)
* [table.delete](#fun_table.delete)
* [table.new](#fun_table.new)
* [table.set\_frame\_color](#fun_table.set_frame_color)
* [table.set\_border\_width](#fun_table.set_border_width)
* [table.set_bgcolor](#fun_table.set_bgcolor)
* [table.set\_frame\_width](#fun_table.set_frame_width)
* [table.set_position](#fun_table.set_position)

## table.set\_border\_width

the function sets the width of the borders (excluding the outer frame) of the table's cells.

### Syntax

table.set\_border\_width(table\_id, border\_width) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `border_width`

    >  (`series` `int`)
    
    >  the width of the borders. optional. the default is 0.

### See also

* [table.clear](#fun_table.clear)
* [table.delete](#fun_table.delete)
* [table.new](#fun_table.new)
* [table.set\_frame\_color](#fun_table.set_frame_color)
* [table.set\_frame\_width](#fun_table.set_frame_width)
* [table.set_bgcolor](#fun_table.set_bgcolor)
* [table.set\_border\_color](#fun_table.set_border_color)
* [table.set_position](#fun_table.set_position)

## table.set\_frame\_color

the function sets the color of the outer frame of a table.

### Syntax

table.set\_frame\_color(table\_id, frame\_color) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `frame_color`

    >  (`series` `color`)
    
    >  the color of the frame of the table. optional. the default is no color.

### See also

* [table.clear](#fun_table.clear)
* [table.delete](#fun_table.delete)
* [table.new](#fun_table.new)
* [table.set\_border\_color](#fun_table.set_border_color)
* [table.set\_border\_width](#fun_table.set_border_width)
* [table.set_bgcolor](#fun_table.set_bgcolor)
* [table.set\_frame\_width](#fun_table.set_frame_width)
* [table.set_position](#fun_table.set_position)

## table.set\_frame\_width

the function set the width of the outer frame of a table.

### Syntax

table.set\_frame\_width(table\_id, frame\_width) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `frame_width`

    >  (`series` `int`)
    
    >  the width of the outer frame of the table. optional. the default is 0.

### See also

* [table.clear](#fun_table.clear)
* [table.delete](#fun_table.delete)
* [table.new](#fun_table.new)
* [table.set\_frame\_color](#fun_table.set_frame_color)
* [table.set\_border\_width](#fun_table.set_border_width)
* [table.set_bgcolor](#fun_table.set_bgcolor)
* [table.set\_border\_color](#fun_table.set_border_color)
* [table.set_position](#fun_table.set_position)

## table.set_position

the function sets the position of a table.

### Syntax

table.set\_position(table\_id, position) - void

### Arguments

- `table_id`

    >  (`series` `table`)
    
    >  a table object.

- `position`

    >  (`series` `string`)
    
    >  position of the table. possible values are: [position.top_left](#var_position.top_left), [position.top_center](#var_position.top_center), [position.top_right](#var_position.top_right), [position.middle_left](#var_position.middle_left), [position.middle_center](#var_position.middle_center), [position.middle_right](#var_position.middle_right), [position.bottom_left](#var_position.bottom_left), [position.bottom_center](#var_position.bottom_center), [position.bottom_right](#var_position.bottom_right).

### See also

* [table.clear](#fun_table.clear)
* [table.delete](#fun_table.delete)
* [table.new](#fun_table.new)
* [table.set_bgcolor](#fun_table.set_bgcolor)
* [table.set\_border\_color](#fun_table.set_border_color)
* [table.set\_border\_width](#fun_table.set_border_width)
* [table.set\_frame\_color](#fun_table.set_frame_color)
* [table.set\_frame\_width](#fun_table.set_frame_width)

## ticker.heikinashi

Creates a ticker identifier for requesting Heikin ashi bar values.

### Syntax

ticker.heikinashi(symbol) → simple string

### Arguments

- `symbol`

    >  (`simple` `string`)
    
    >  symbol ticker identifier.

### Example


```s

//@version=5
indicator("ticker.heikinashi", overlay=true)
heikinashi_close = request.security(ticker.heikinashi(syminfo.tickerid), timeframe.period, close)

heikinashi_aapl_60_close = request.security(ticker.heikinashi("aapL"), "60", close)
plot(heikinashi_close)
plot(heikinashi_aapl_60_close)


```

### Returns

string value of ticker id, that can be supplied to [request.security](#fun_request.security) function.

### See also

* [syminfo.tickerid](#var_syminfo.tickerid)
* [syminfo.ticker](#var_syminfo.ticker)
* [request.security](#fun_request.security)
* [ticker.renko](#fun_ticker.renko)
* [ticker.linebreak](#fun_ticker.linebreak)
* [ticker.kagi](#fun_ticker.kagi)
* [ticker.pointfigure](#fun_ticker.pointfigure)

## ticker.inherit

Constructs a ticker iD for the specified \`symbol\` with additional parameters inherited from the ticker iD passed into the function call, allowing the script to request a symbol's data using the same modifiers that the \`from_tickerid\` has, including extended session, dividend adjustment, currency conversion, non-standard chart types, back-adjustment, settlement-as-close, etc.

### Syntax

ticker.inherit(from_tickerid, symbol) → simple string

### Arguments

- `from_tickerid`

    >  (`simple` `string`)
    
    >  the ticker iD to inherit modifiers from.

- `symbol`

    >  (`simple` `string`)
    
    >  the symbol to construct the new ticker iD for.

### Example


```s

//@version=5
indicator("ticker.inherit")

//@variable a "NasDaq:aapL" ticker iD with Extender Hours enabled.
tickerExthours = ticker.new("NasDaq", "aapL", session.extended)
//@variable a Heikin ashi ticker iD for "NasDaq:aapL" with Extended Hours enabled.
HatickerExthours = ticker.heikinashi(tickerExthours)
//@variable the "NasDaq:MsFT" symbol with no modifiers.
testsymbol = "NasDaq:MsFT"
//@variable a ticker iD for "NasDaq:MsFT" with inherited Heikin ashi and Extended Hours modifiers.
testsymbolHatickerExthours = ticker.inherit(HatickerExthours, testsymbol)

//@variable the `close` price requested using "NasDaq:MsFT" with inherited modifiers.
secdata = request.security(testsymbolHatickerExthours, "60", close, ignore_invalid_symbol = true)
//@variable the `close` price requested using "NasDaq:MsFT" without modifiers.
comparedata = request.security(testsymbol, "60", close, ignore_invalid_symbol = true)

plot(secdata, color = color.green)
plot(comparedata)


```

### Remarks

if the constructed ticker iD inherits a modifier that doesn't apply to the symbol (e.g., if the \`from_tickerid\` has Extended Hours enabled, but no such option is available for the \`symbol\`), the script will ignore the modifier when requesting data using the iD.

## ticker.kagi

Creates a ticker identifier for requesting Kagi values.

### Syntax

ticker.kagi(symbol, reversal) → simple string

### Arguments

- `symbol`

    >  (`simple` `string`)
    
    >  symbol ticker identifier.

- `reversal`

    >  (`simple` `int`/`float`)
    
    >  Reversal amount (absolute price value).

### Example


```s

//@version=5
indicator("ticker.kagi", overlay=true)
kagi_tickerid = ticker.kagi(syminfo.tickerid, 3)
kagi_close = request.security(kagi_tickerid, timeframe.period, close)
plot(kagi_close)


```

### Returns

string value of ticker id, that can be supplied to [request.security](#fun_request.security) function.

### See also

* [syminfo.tickerid](#var_syminfo.tickerid)
* [syminfo.ticker](#var_syminfo.ticker)
* [request.security](#fun_request.security)
* [ticker.heikinashi](#fun_ticker.heikinashi)
* [ticker.renko](#fun_ticker.renko)
* [ticker.linebreak](#fun_ticker.linebreak)
* [ticker.pointfigure](#fun_ticker.pointfigure)

## ticker.linebreak

Creates a ticker identifier for requesting line break values.

### Syntax

ticker.linebreak(symbol, number\_of\_lines) → simple string

### Arguments

- `symbol`

    >  (`simple` `string`)
    
    >  symbol ticker identifier.

- `number\_of\_lines`

    >  (`simple` `int`)
    
    >  Number of line.

### Example


```s

//@version=5
indicator("ticker.linebreak", overlay=true)
linebreak_tickerid = ticker.linebreak(syminfo.tickerid, 3)
linebreak_close = request.security(linebreak_tickerid, timeframe.period, close)
plot(linebreak_close)


```

### Returns

string value of ticker id, that can be supplied to [request.security](#fun_request.security) function.

### See also

* [syminfo.tickerid](#var_syminfo.tickerid)
* [syminfo.ticker](#var_syminfo.ticker)
* [request.security](#fun_request.security)
* [ticker.heikinashi](#fun_ticker.heikinashi)
* [ticker.renko](#fun_ticker.renko)
* [ticker.kagi](#fun_ticker.kagi)
* [ticker.pointfigure](#fun_ticker.pointfigure)

## ticker.modify

Creates a ticker identifier for requesting additional data for the script.

### Syntax

ticker.modify(tickerid, session, adjustment) → simple string

### Arguments

- `tickerid`

    >  (`simple` `string`)
    
    >  symbol name with exchange prefix, e.g. 'baTs:MsFT', 'NasDaq:MsFT' or tickerid with session and adjustment from the [ticker.new](#fun_ticker.new) function.

- `session`

    >  (`simple` `string`)
    
    >  session type. optional argument. possible values: [session.regular](#var_session.regular), [session.extended](#var_session.extended). session type of the current chart is [syminfo.session](#var_syminfo.session). if session is not given, then [syminfo.session](#var_syminfo.session) value is used.

- `adjustment`

    >  (`simple` `string`)
    
    >  adjustment type. optional argument. possible values: [adjustment.none](#var_adjustment.none), [adjustment.splits](#var_adjustment.splits), [adjustment.dividends](#var_adjustment.dividends). if adjustment is not given, then default adjustment value is used (can be different depending on particular instrument).

### Example


```s

//@version=5
indicator("ticker_modify", overlay=true)
t1 = ticker.new(syminfo.prefix, syminfo.ticker, session.regular, adjustment.splits)
c1 = request.security(t1, "D", close)
t2 = ticker.modify(t1, session.extended)
c2 = request.security(t2, "2D", close)
plot(c1)
plot(c2)


```

### Returns

string value of ticker id, that can be supplied to [request.security](#fun_request.security) function.

### See also

* [syminfo.tickerid](#var_syminfo.tickerid)
* [syminfo.ticker](#var_syminfo.ticker)
* [syminfo.session](#var_syminfo.session)
* [session.extended](#var_session.extended)
* [session.regular](#var_session.regular)
* [ticker.heikinashi](#fun_ticker.heikinashi)
* [adjustment.none](#var_adjustment.none)
* [adjustment.splits](#var_adjustment.splits)
* [adjustment.dividends](#var_adjustment.dividends)

## ticker.new

Creates a ticker identifier for requesting additional data for the script.

### Syntax

ticker.new(prefix, ticker, session, adjustment) → simple string

### Arguments

- `prefix`

    >  (`simple` `string`)
    
    >  Exchange prefix. For example: 'baTs', 'NYsE', 'NasDaq'. Exchange prefix of main series is [syminfo.prefix](#var_syminfo.prefix).

- `ticker`

    >  (`simple` `string`)
    
    >  Ticker name. For example 'aapL', 'MsFT', 'EuRusD'. Ticker name of the main series is [syminfo.ticker](#var_syminfo.ticker).

- `session`

    >  (`simple` `string`)
    
    >  session type. optional argument. possible values: [session.regular](#var_session.regular), [session.extended](#var_session.extended). session type of the current chart is [syminfo.session](#var_syminfo.session). if session is not given, then [syminfo.session](#var_syminfo.session) value is used.

- `adjustment`

    >  (`simple` `string`)
    
    >  adjustment type. optional argument. possible values: [adjustment.none](#var_adjustment.none), [adjustment.splits](#var_adjustment.splits), [adjustment.dividends](#var_adjustment.dividends). if adjustment is not given, then default adjustment value is used (can be different depending on particular instrument).

### Example


```s

//@version=5
indicator("ticker.new", overlay=true)
t = ticker.new(syminfo.prefix, syminfo.ticker, session.regular, adjustment.splits)
t2 = ticker.heikinashi(t)
c = request.security(t2, timeframe.period, low, barmerge.gaps_on)
plot(c, style=plot.style_linebr)


```

### Returns

string value of ticker id, that can be supplied to [request.security](#fun_request.security) function.

### Remarks

You may use return value of [ticker.new](#fun_ticker.new) function as input argument for [ticker.heikinashi](#fun_ticker.heikinashi), [ticker.renko](#fun_ticker.renko), [ticker.linebreak](#fun_ticker.linebreak), [ticker.kagi](#fun_ticker.kagi), [ticker.pointfigure](#fun_ticker.pointfigure) functions.

### See also

* [syminfo.tickerid](#var_syminfo.tickerid)
* [syminfo.ticker](#var_syminfo.ticker)
* [syminfo.session](#var_syminfo.session)
* [session.extended](#var_session.extended)
* [session.regular](#var_session.regular)
* [ticker.heikinashi](#fun_ticker.heikinashi)
* [adjustment.none](#var_adjustment.none)
* [adjustment.splits](#var_adjustment.splits)
* [adjustment.dividends](#var_adjustment.dividends)

## ticker.pointfigure

Creates a ticker identifier for requesting point & figure values.

### Syntax

ticker.pointfigure(symbol, source, style, param, reversal) → simple string

### Arguments

- `symbol`

    >  (`simple` `string`)
    
    >  symbol ticker identifier.

- `source`

    >  (`simple` `string`)
    
    >  the source for calculating point & figure. possible values are: 'hl', 'close'.

- `style`

    >  (`simple` `string`)
    
    >  box size assignment Method: 'atr', 'traditional'.

- `param`

    >  (`simple` `int`/`float`)
    
    >  atr Length if \`style\` is equal to 'atr', or box size if \`style\` is equal to 'traditional'.

- `reversal`

    >  (`simple` `int`)
    
    >  Reversal amount.

### Example


```s

//@version=5
indicator("ticker.pointfigure", overlay=true)
pnf_tickerid = ticker.pointfigure(syminfo.tickerid, "hl", "traditional", 1, 3)
pnf_close = request.security(pnf_tickerid, timeframe.period, close)
plot(pnf_close)


```

### Returns

string value of ticker id, that can be supplied to [request.security](#fun_request.security) function.

### See also

* [syminfo.tickerid](#var_syminfo.tickerid)
* [syminfo.ticker](#var_syminfo.ticker)
* [request.security](#fun_request.security)
* [ticker.heikinashi](#fun_ticker.heikinashi)
* [ticker.renko](#fun_ticker.renko)
* [ticker.linebreak](#fun_ticker.linebreak)
* [ticker.kagi](#fun_ticker.kagi)

## ticker.renko

Creates a ticker identifier for requesting Renko values.

### Syntax

ticker.renko(symbol, style, param, request_wicks, source) → simple string

### Arguments

- `symbol`

    >  (`simple` `string`)
    
    >  symbol ticker identifier.

- `style`

    >  (`simple` `string`)
    
    >  box size assignment Method: 'atr', 'traditional'.

- `param`

    >  (`simple` `int`/`float`)
    
    >  atr Length if \`style\` is equal to 'atr', or box size if \`style\` is equal to 'traditional'.

- `request_wicks`

    >  (`simple` `bool`)
    
    >  specifies if wick values are returned for Renko bricks. When " + addinternallineNottr("op", "true", "true") + ", " + addinternallineNottr("var", "high", "high") + " and " + addinternallineNottr("var", "low", "low") + " values requested from a symbol using the ticker formed by this function will include wick values when they are present. When " + addinternallineNottr("op", "false", "false") + ", " + addinternallineNottr("var", "high", "high") + " and " + addinternallineNottr("var", "low", "low") + " will always be equal to either " + addinternallineNottr("var", "open", "open") + " or " + addinternallineNottr("var", "close", "close") + ". optional. the default is " + addinternallineNottr("op", "false", "false") + ". a detailed explanation of how Renko wicks are calculated can be found in our [Help center](https://www.tradingview.com/support/solutions/43000481040-what-do-renko-wicks-mean/).

- `source`

    >  (`simple` `string`)
    
    >  the source used to calculate bricks. optional. possible values: "Close", "OHLC". the default is "Close".

### Example


```s

//@version=5
indicator("ticker.renko", overlay=true)
renko_tickerid = ticker.renko(syminfo.tickerid, "atr", 10)
renko_close = request.security(renko_tickerid, timeframe.period, close)
plot(renko_close)



```

### Example


```s

//@version=5
indicator("Renko candles", overlay=false)
renko_tickerid = ticker.renko(syminfo.tickerid, "atr", 10)
> [renko_open, renko_high, renko_low, renko_close] = request.security(renko_tickerid, timeframe.period, [open, high, low, close])
plotcandle(renko_open, renko_high, renko_low, renko_close, color = renko_close > renko_open ? color.green : color.red)


```

### Returns

string value of ticker id, that can be supplied to [request.security](#fun_request.security) function.

### See also

* [syminfo.tickerid](#var_syminfo.tickerid)
* [syminfo.ticker](#var_syminfo.ticker)
* [request.security](#fun_request.security)
* [ticker.heikinashi](#fun_ticker.heikinashi)
* [ticker.linebreak](#fun_ticker.linebreak)
* [ticker.kagi](#fun_ticker.kagi)
* [ticker.pointfigure](#fun_ticker.pointfigure)

## ticker.standard

Creates a ticker to request data from a standard chart that is unaffected by modifiers like extended session, dividend adjustment, currency conversion, and the calculations of non-standard chart types: Heikin ashi, Renko, etc. among other things, this makes it possible to retrieve standard chart values when the script is running on a non-standard chart.

### Syntax

ticker.standard(symbol) → simple string

### Arguments

- `symbol`

    >  (`simple` `string`)
    
    >  a ticker iD to be converted into its standard form. optional. the default is [syminfo.tickerid](#var_syminfo.tickerid).

### Example


```s

//@version=5
indicator("ticker.standard", overlay = true)
// this script should be run on a non-standard chart such as Ha, Renko...

// Requests data from the chart type the script is running on.
charttypeValue = request.security(syminfo.tickerid, "1D", close)

// Request data from the standard chart type, regardless of the chart type the script is running on.
standardChartValue = request.security(ticker.standard(syminfo.tickerid), "1D", close)

// this will not use a standard ticker iD because the `symbol` argument contains only the ticker aEUR" not the prefix (exchange).
standardChartValue2 = request.security(ticker.standard(syminfo.ticker), "1D", close)

plot(charttypeValue)
plot(standardChartValue, color = color.green)


```

### Returns

a string representing the ticker of a standard chart in the "prefix:ticker" format. if the \`symbol\` argument does not contain the prefix and ticker information, the function returns the supplied argument as is.

### See also

* [request.security](#fun_request.security)

## time

+2 overloads

the time function returns the unix time of the current bar for the specified timeframe and session or NaN if the time point is out of session.

### syntax & Overloads

> [time(timeframe) → series int](#fun_time-0)
> [time(timeframe, session) → series int](#fun_time-1)
> [time(timeframe, session, timezone) → series int](#fun_time-2)

### Arguments

- `timeframe`

    >  (`simple` `string`)
    
    >  timeframe. an empty string is interpreted as the current timeframe of the chart.

### Example


```s

//@version=5
indicator("time", overlay=true)
// try this on chart aapL,1
timeinrange(res, sess) => not na(time(res, sess, "america/New_York")) ? 1 : 0
plot(timeinrange("1", "1300-1400"), color=color.red)

// this plots 1.0 at every start of 10 minute bar on a 1 minute chart:
newbar(res) => ta.change(time(res)) == 0 ? 0 : 1
plot(newbar("10"))
While setting up a session you can specify not just the hours and minutes but also the days of the week that will be included in that session.
if the days aren't specified, the session is considered to have been set from sunday (1) to saturday (7), i.e. "1100-2000" is the same as "1100-1200:1234567".
You can change that by specifying the days. For example, on a symbol that is traded seven days a week with the 24-hour trading session the following script will not color saturdays and sundays:



```

### Example


```s

//@version=5
indicator("time", overlay=true)
t1 = time(timeframe.period, "0000-0000:23456")
bgcolor(t1 ? color.new(color.blue, 90) : na)
One `session` argument can include several different sessions, separated by commas. For example, the following script will highlight the bars from 10:00 to 11:00 and from 14:00 to 15:00 (workdays only):



```

### Example


```s

//@version=5
indicator("time", overlay=true)
t1 = time(timeframe.period, "1000-1100,1400-1500:23456")
bgcolor(t1 ? color.new(color.blue, 90) : na)


```

### Returns

unix time.

### Remarks

unix time is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

### See also

* [time](#var_time)

## time_close

+2 overloads

Returns the unix time of the current bar's close for the specified timeframe and session, or [na](#var_na) if the time point is outside the session. On non-standard price-based chart types (Renko, line break, Kagi, point & figure, and Range), this function returns [na](#var_na) on the chart's realtime bars.

### syntax & Overloads

> [time_close(timeframe) → series int](#fun_time_close-0)
> [time_close(timeframe, session) → series int](#fun_time_close-1)
> [time_close(timeframe, session, timezone) → series int](#fun_time_close-2)

### Arguments

- `timeframe`

    >  (`simple` `string`)
    
    >  Resolution. an empty string is interpreted as the current resolution of the chart.

### Example


```s

//@version=5
indicator("time", overlay=true)
t1 = time_close(timeframe.period, "1200-1300", "america/New_York")
bgcolor(t1 ? color.new(color.blue, 90) : na)


```

### Returns

unix time.

### Remarks

unix time is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

### See also

* [time_close](#var_time_close)

## timeframe.change

Detects changes in the specified \`timeframe\`.

### Syntax

timeframe.change(timeframe) → series bool

### Arguments

- `timeframe`

    >  (`simple` `string`)
    
    >  string formatted according to the [user manual's timeframe string specifications](https://www.tradingview.com/pine-script-docs/en/v5/concepts/timeframes.html#timeframe-string-specifications).

### Example


```s

//@version=5
// Run this script on an intraday chart.
indicator("New day started", overlay = true)
// Highlights the first bar of the new day.
isNewDay = timeframe.change("1D")
bgcolor(isNewDay ? color.new(color.green, 80) : na)


```

### Returns

Returns [true](#op_true) on the first bar of a new \`timeframe\`, [false](#op_false) otherwise.

## timeframe.from_seconds

+1 overload

Converts a number of seconds into a valid timeframe string.

### syntax & Overloads

> [timeframe.from_seconds(seconds) → simple string](#fun_timeframe.from_seconds-0)
> [timeframe.from_seconds(seconds) → series string](#fun_timeframe.from_seconds-1)

### Arguments

- `seconds`

    >  (`simple` `int`)
    
    >  the number of seconds in the timeframe.

### Example


```s

//@version=5
indicator("HTF Close", "", true)
int charttf = timeframe.in_seconds()
string tftimes5 = timeframe.from_seconds(charttf * 5)
float htfClose = request.security(syminfo.tickerid, tftimes5, close)
plot(htfClose)


```

### Returns

a timeframe string compliant with [timeframe string specifications](https://www.tradingview.com/pine-script-docs/en/v5/concepts/timeframes.html#timeframe-string-specifications).

### Remarks

if no valid timeframe exists for the quantity of seconds supplied, the next higher valid timeframe will be returned. accordingly, one second or less will return "1s", 2-5 seconds will return "5s", and 604,799 seconds (one second less than 7 days) will return "7D".

if the seconds exactly represent two or more valid timeframes, the one with the larger base unit will be used. thus 604,800 seconds (7 days) returns "1W", not "7D".

all values above 31,622,400 (366 days) return "12M".

### See also

* [timeframe.in_seconds](#fun_timeframe.in_seconds)
* [request.security](#var_request.security)
* [request.security\_lower\_tf](#var_request.security_lower_tf)

## timeframe.in_seconds

+1 overload

Converts a timeframe string into seconds.

### syntax & Overloads

> [timeframe.in_seconds(timeframe) → simple int](#fun_timeframe.in_seconds-0)
> [timeframe.in_seconds(timeframe) → series int](#fun_timeframe.in_seconds-1)

### Arguments

- `timeframe`

    >  (`simple` `string`)
    
    >  timeframe string in [timeframe string specifications](https://www.tradingview.com/pine-script-docs/en/v5/concepts/timeframes.html#timeframe-string-specifications) format. optional. the default is [timeframe.period](#var_timeframe.period).

### Example


```s

//@version=5
indicator("`timeframe_in_seconds()`")

// Get a user-selected timeframe.
tfinput = input.timeframe("1D")

// Convert it into an "int" number of seconds.
secondsinTf = timeframe.in_seconds(tfinput)

plot(secondsinTf)


```

### Returns

the "int" representation of the number of seconds in the timeframe string.

### Remarks

When the timeframe is "1M" or more, calculations use 2628003 as the number of seconds in one month, which represents 30.4167 (365/12) days.

### See also

* [input.timeframe](#fun_input.timeframe)
* [timeframe.period](#var_timeframe.period)
* [timeframe.from_seconds](#fun_timeframe.from_seconds)

## timestamp

+4 overloads

Function timestamp returns unix time of specified date and time.

### syntax & Overloads

> [timestamp(datestring) → const int](#fun_timestamp-0)
> [timestamp(year, month, day, hour, minute, second) → simple int](#fun_timestamp-1)
> [timestamp(year, month, day, hour, minute, second) → series int](#fun_timestamp-2)
> [timestamp(timezone, year, month, day, hour, minute, second) → simple int](#fun_timestamp-3)
> [timestamp(timezone, year, month, day, hour, minute, second) → series int](#fun_timestamp-4)

### Arguments

- `datestring`

    >  (`const` `string`)
    
    >  a string containing the date and, optionally, the time and time zone. its format must comply with either the [iETF RFC 2822](https://tools.ietf.org/html/rfc2822#section-3.3) or [isO 8601](https://en.wikipedia.org/wiki/isO_8601) standards ("dd MMM YYYY hh:mm:ss +-hhmm" or "YYYY-MM-ddthh:mm:ss+-hh:mm", so "20 Feb 2020" or "2020-02-20"). if no time is supplied, "00:00" is used. if no time zone is supplied, GMT+0 will be used. Note that this diverges from the usual behavior of the function where it returns time in the exchange's timezone.

### Example


```s

//@version=5
indicator("timestamp")
plot(timestamp(2016, 01, 19, 09, 30), linewidth=3, color=color.green)
plot(timestamp(syminfo.timezone, 2016, 01, 19, 09, 30), color=color.blue)
plot(timestamp(2016, 01, 19, 09, 30), color=color.yellow)
plot(timestamp("GMT+6", 2016, 01, 19, 09, 30))
plot(timestamp(2019, 06, 19, 09, 30, 15), color=color.lime)
plot(timestamp("GMT+3", 2019, 06, 19, 09, 30, 15), color=color.fuchsia)
plot(timestamp("Feb 01 2020 22:10:05"))
plot(timestamp("2011-10-10T14:48:00"))
plot(timestamp("04 Dec 1995 00:12:00 GMT+5"))


```

### Returns

unix time.

### Remarks

unix time is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

### See also

* [time](#fun_time)

## weekofyear

+1 overload

### syntax & Overloads

> [weekofyear(time) → series int](#fun_weekofyear-0)
> [weekofyear(time, timezone) → series int](#fun_weekofyear-1)

### Arguments

- `time`

    >  (`series` `int`)
    
    >  unix time in milliseconds.

### Returns

Week of year (in exchange timezone) for provided unix time.

### Remarks

unix time is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

Note that this function returns the week based on the time of the bar's open. For overnight sessions (e.g. EuRusD, where Monday session starts on sunday, 17:00) this value can be lower by 1 than the week of the trading day.

### See also

* [weekofyear](#var_weekofyear)
* [time](#fun_time)
* [year](#fun_year)
* [month](#fun_month)
* [dayofmonth](#fun_dayofmonth)
* [dayofweek](#fun_dayofweek)
* [hour](#fun_hour)
* [minute](#fun_minute)
* [second](#fun_second)

## year

+1 overload

### syntax & Overloads

> [year(time) → series int](#fun_year-0)
> [year(time, timezone) → series int](#fun_year-1)

### Arguments

- `time`

    >  (`series` `int`)
    
    >  unix time in milliseconds.

### Returns

Year (in exchange timezone) for provided unix time.

### Remarks

unix time is the number of milliseconds that have elapsed since 00:00:00 uTC, 1 January 1970.

Note that this function returns the year based on the time of the bar's open. For overnight sessions (e.g. EuRusD, where Monday session starts on sunday, 17:00 uTC-4) this value can be lower by 1 than the year of the trading day.

### See also

* [year](#var_year)
* [time](#fun_time)
* [month](#fun_month)
* [dayofmonth](#fun_dayofmonth)
* [dayofweek](#fun_dayofweek)
* [hour](#fun_hour)
* [minute](#fun_minute)
* [second](#fun_second)

Constants
---------

## adjustment.dividends

Constant for dividends adjustment type (dividends adjustment is applied).

### Type

const string

### See also

* [adjustment.none](#var_adjustment.none)
* [adjustment.splits](#var_adjustment.splits)
* [ticker.new](#fun_ticker.new)

## adjustment.none

Constant for none adjustment type (no adjustment is applied).

### Type

const string

### See also

* [adjustment.splits](#var_adjustment.splits)
* [adjustment.dividends](#var_adjustment.dividends)
* [ticker.new](#fun_ticker.new)

## adjustment.splits

Constant for splits adjustment type (splits adjustment is applied).

### Type

const string

### See also

* [adjustment.none](#var_adjustment.none)
* [adjustment.dividends](#var_adjustment.dividends)
* [ticker.new](#fun_ticker.new)

## alert.freq_all

a named constant for use with the \`freq\` parameter of the alert() function.

all function calls trigger the alert.

### Type

const string

### See also

* [alert](#fun_alert)

## alert.freq\_once\_per_bar

a named constant for use with the \`freq\` parameter of the alert() function.

the first function call during the bar triggers the alert.

### Type

const string

### See also

* [alert](#fun_alert)

## alert.freq\_once\_per\_bar\_close

a named constant for use with the \`freq\` parameter of the alert() function.

the function call triggers the alert only when it occurs during the last script iteration of the real-time bar, when it closes.

### Type

const string

### See also

* [alert](#fun_alert)

## barmerge.gaps_off

Merge strategy for requested data. data is merged continuously without gaps, all the gaps are filled with the previous nearest existing value.

### Type

const barmerge_gaps

### See also

* [request.security](#fun_request.security)
* [barmerge.gaps_on](#var_barmerge.gaps_on)

## barmerge.gaps_on

Merge strategy for requested data. data is merged with possible gaps ([na](#var_na) values).

### Type

const barmerge_gaps

### See also

* [request.security](#fun_request.security)
* [barmerge.gaps_off](#var_barmerge.gaps_off)

## barmerge.lookahead_off

Merge strategy for the requested data position. Requested barset is merged with current barset in the order of sorting bars by their close time. this merge strategy disables effect of getting data from "future" on calculation on history.

### Type

const barmerge_lookahead

### See also

* [request.security](#fun_request.security)
* [barmerge.lookahead_on](#var_barmerge.lookahead_on)

## barmerge.lookahead_on

Merge strategy for the requested data position. Requested barset is merged with current barset in the order of sorting bars by their opening time. this merge strategy can lead to undesirable effect of getting data from "future" on calculation on history. this is unacceptable in backtesting strategies, but can be useful in indicators.

### Type

const barmerge_lookahead

### See also

* [request.security](#fun_request.security)
* [barmerge.lookahead_off](#var_barmerge.lookahead_off)

## color.aqua

is a named constant for #00bCD4 color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.orange](#var_color.orange)

## color.black

is a named constant for #363a45 color.

### Type

const color

### See also

* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.blue

is a named constant for #2962ff color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.fuchsia

is a named constant for #E040Fb color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.gray

is a named constant for #787b86 color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.green

is a named constant for #4CaF50 color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.lime

is a named constant for #00E676 color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.maroon

is a named constant for #880E4F color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.navy

is a named constant for #311b92 color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.olive

is a named constant for #808000 color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.orange

is a named constant for #FF9800 color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)

## color.purple

is a named constant for #9C27b0 color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.red

is a named constant for #FF5252 color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.silver

is a named constant for #b2b5bE color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.teal

is a named constant for #00897b color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.white

is a named constant for #FFFFFF color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.yellow](#var_color.yellow)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## color.yellow

is a named constant for #FFEb3b color.

### Type

const color

### See also

* [color.black](#var_color.black)
* [color.silver](#var_color.silver)
* [color.gray](#var_color.gray)
* [color.white](#var_color.white)
* [color.maroon](#var_color.maroon)
* [color.red](#var_color.red)
* [color.purple](#var_color.purple)
* [color.fuchsia](#var_color.fuchsia)
* [color.green](#var_color.green)
* [color.lime](#var_color.lime)
* [color.olive](#var_color.olive)
* [color.navy](#var_color.navy)
* [color.blue](#var_color.blue)
* [color.teal](#var_color.teal)
* [color.aqua](#var_color.aqua)
* [color.orange](#var_color.orange)

## currency.auD

australian dollar.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.bTC

bitcoin.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.CaD

Canadian dollar.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.CHF

swiss franc.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.Eth

Ethereum.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.EuR

Euro.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.Gbp

pound sterling.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.HKD

Hong Kong dollar.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.iNR

indian rupee.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.JpY

Japanese yen.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.KRW

south Korean won.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.MYR

Malaysian ringgit.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.NOK

Norwegian krone.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.NONE

unspecified currency.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.NZD

New Zealand dollar.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.Rub

Russian ruble.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.sEK

swedish krona.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.sGD

singapore dollar.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.trY

Turkish lira.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.usD

united states dollar.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.usdt

Tether.

### Type

const string

### See also

* [strategy](#fun_strategy)

## currency.ZaR

south african rand.

### Type

const string

### See also

* [strategy](#fun_strategy)

## dayofweek.friday

is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.

### Type

const int

### See also

* [dayofweek.sunday](#var_dayofweek.sunday)
* [dayofweek.monday](#var_dayofweek.monday)
* [dayofweek.tuesday](#var_dayofweek.tuesday)
* [dayofweek.wednesday](#var_dayofweek.wednesday)
* [dayofweek.thursday](#var_dayofweek.thursday)
* [dayofweek.saturday](#var_dayofweek.saturday)

## dayofweek.monday

is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.

### Type

const int

### See also

* [dayofweek.sunday](#var_dayofweek.sunday)
* [dayofweek.tuesday](#var_dayofweek.tuesday)
* [dayofweek.wednesday](#var_dayofweek.wednesday)
* [dayofweek.thursday](#var_dayofweek.thursday)
* [dayofweek.friday](#var_dayofweek.friday)
* [dayofweek.saturday](#var_dayofweek.saturday)

## dayofweek.saturday

is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.

### Type

const int

### See also

* [dayofweek.sunday](#var_dayofweek.sunday)
* [dayofweek.monday](#var_dayofweek.monday)
* [dayofweek.tuesday](#var_dayofweek.tuesday)
* [dayofweek.wednesday](#var_dayofweek.wednesday)
* [dayofweek.thursday](#var_dayofweek.thursday)
* [dayofweek.friday](#var_dayofweek.friday)

## dayofweek.sunday

is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.

### Type

const int

### See also

* [dayofweek.monday](#var_dayofweek.monday)
* [dayofweek.tuesday](#var_dayofweek.tuesday)
* [dayofweek.wednesday](#var_dayofweek.wednesday)
* [dayofweek.thursday](#var_dayofweek.thursday)
* [dayofweek.friday](#var_dayofweek.friday)
* [dayofweek.saturday](#var_dayofweek.saturday)

## dayofweek.thursday

is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.

### Type

const int

### See also

* [dayofweek.sunday](#var_dayofweek.sunday)
* [dayofweek.monday](#var_dayofweek.monday)
* [dayofweek.tuesday](#var_dayofweek.tuesday)
* [dayofweek.wednesday](#var_dayofweek.wednesday)
* [dayofweek.friday](#var_dayofweek.friday)
* [dayofweek.saturday](#var_dayofweek.saturday)

## dayofweek.tuesday

is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.

### Type

const int

### See also

* [dayofweek.sunday](#var_dayofweek.sunday)
* [dayofweek.monday](#var_dayofweek.monday)
* [dayofweek.wednesday](#var_dayofweek.wednesday)
* [dayofweek.thursday](#var_dayofweek.thursday)
* [dayofweek.friday](#var_dayofweek.friday)
* [dayofweek.saturday](#var_dayofweek.saturday)

## dayofweek.wednesday

is a named constant for return value of [dayofweek](#fun_dayofweek) function and value of [dayofweek](#var_dayofweek) variable.

### Type

const int

### See also

* [dayofweek.sunday](#var_dayofweek.sunday)
* [dayofweek.monday](#var_dayofweek.monday)
* [dayofweek.tuesday](#var_dayofweek.tuesday)
* [dayofweek.thursday](#var_dayofweek.thursday)
* [dayofweek.friday](#var_dayofweek.friday)
* [dayofweek.saturday](#var_dayofweek.saturday)

## display.all

a named constant for use with the \`display\` parameter of \`plot*()\` and \`input*()\` functions. Displays plotted or input values in all possible locations.

### Type

const plot\_simple\_display

### See also

* [plot](#fun_plot)
* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [plotarrow](#fun_plotarrow)
* [plotbar](#fun_plotbar)
* [plotcandle](#fun_plotcandle)

## display.data_window

a named constant for use with the \`display\` parameter of \`plot*()\` and \`input*()\` functions. Displays plotted or input values in the data Window, a menu accessible from the chart's right sidebar.

### Type

const plot_display

### See also

* [plot](#fun_plot)
* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [plotarrow](#fun_plotarrow)
* [plotbar](#fun_plotbar)
* [plotcandle](#fun_plotcandle)

## display.none

a named constant for use with the \`display\` parameter of \`plot*()\` and \`input*()\` functions. \`plot*()\` functions using this will not display their plotted values anywhere. However, alert template messages and [fill](#fun_fill) functions can still use the values, and they will appear in exported chart data. \`input*()\` functions using this constant will only display their values within the script's settings.

### Type

const plot\_simple\_display

### See also

* [plot](#fun_plot)
* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [plotarrow](#fun_plotarrow)
* [plotbar](#fun_plotbar)
* [plotcandle](#fun_plotcandle)

## display.pane

a named constant for use with the \`display\` parameter of \`plot*()\` functions. Displays plotted values in the chart pane used by the script.

### Type

const plot_display

### See also

* [plot](#fun_plot)
* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [plotarrow](#fun_plotarrow)
* [plotbar](#fun_plotbar)
* [plotcandle](#fun_plotcandle)

## display.price_scale

a named constant for use with the \`display\` parameter of \`plot*()\` functions. Displays the plot's label and value on the price scale if the chart's settings allow it.

### Type

const plot_display

### See also

* [plot](#fun_plot)
* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [plotarrow](#fun_plotarrow)
* [plotbar](#fun_plotbar)
* [plotcandle](#fun_plotcandle)

## display.status_line

a named constant for use with the \`display\` parameter of \`plot*()\` and \`input*()\` functions. Displays plotted or input values in the status line next to the script's name on the chart if the chart's settings allow it.

### Type

const plot_display

### See also

* [plot](#fun_plot)
* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [plotarrow](#fun_plotarrow)
* [plotbar](#fun_plotbar)
* [plotcandle](#fun_plotcandle)

## dividends.future_amount

Returns the payment amount of the upcoming dividend in the currency of the current instrument, or [na](#var_na) if this data isn't available.

### Type

series float

## dividends.future\_ex\_date

Returns the Ex-dividend date (Ex-date) of the current instrument's next dividend payment, or [na](#var_na) if this data isn't available. Ex-dividend date signifies when investors are no longer entitled to a payout from the most recent dividend. Only those who purchased shares before this day are entitled to the dividend payment.

### Type

series float

## dividends.future\_pay\_date

Returns the payment date (pay date) of the current instrument's next dividend payment, or [na](#var_na) if this data isn't available. payment date signifies the day when eligible investors will receive the dividend payment.

### Type

series float

## dividends.gross

a named constant for the [request.dividends](#fun_request.dividends) function. is used to request the dividends return on a stock before deductions.

### Type

const string

### See also

* [request.dividends](#fun_request.dividends)

## dividends.net

a named constant for the [request.dividends](#fun_request.dividends) function. is used to request the dividends return on a stock after deductions.

### Type

const string

### See also

* [request.dividends](#fun_request.dividends)

## earnings.actual

a named constant for the [request.earnings](#fun_request.earnings) function. is used to request the earnings value as it was reported.

### Type

const string

### See also

* [request.earnings](#fun_request.earnings)

## earnings.estimate

a named constant for the [request.earnings](#fun_request.earnings) function. is used to request the estimated earnings value.

### Type

const string

### See also

* [request.earnings](#fun_request.earnings)

## earnings.standardized

a named constant for the [request.earnings](#fun_request.earnings) function. is used to request the standardized earnings value.

### Type

const string

### See also

* [request.earnings](#fun_request.earnings)

## extend.both

a named constant for [line.new](#fun_line.new) and [line.set_extend](#fun_line.set_extend) functions.

### Type

const string

### See also

* [line.new](#fun_line.new)
* [line.set_extend](#fun_line.set_extend)
* [extend.none](#var_extend.none)
* [extend.left](#var_extend.left)
* [extend.right](#var_extend.right)

## extend.left

a named constant for [line.new](#fun_line.new) and [line.set_extend](#fun_line.set_extend) functions.

### Type

const string

### See also

* [line.new](#fun_line.new)
* [line.set_extend](#fun_line.set_extend)
* [extend.none](#var_extend.none)
* [extend.right](#var_extend.right)
* [extend.both](#var_extend.both)

## extend.none

a named constant for [line.new](#fun_line.new) and [line.set_extend](#fun_line.set_extend) functions.

### Type

const string

### See also

* [line.new](#fun_line.new)
* [line.set_extend](#fun_line.set_extend)
* [extend.left](#var_extend.left)
* [extend.right](#var_extend.right)
* [extend.both](#var_extend.both)

## extend.right

a named constant for [line.new](#fun_line.new) and [line.set_extend](#fun_line.set_extend) functions.

### Type

const string

### See also

* [line.new](#fun_line.new)
* [line.set_extend](#fun_line.set_extend)
* [extend.none](#var_extend.none)
* [extend.left](#var_extend.left)
* [extend.both](#var_extend.both)

## font.family_default

Default text font for [box.new](#fun_box.new), [box.set\_text\_font_family](#fun_box.set_text_font_family), [label.new](#fun_label.new), [label.set\_text\_font_family](#fun_label.set_text_font_family), [table.cell](#fun_table.cell) and [table.cell\_set\_text\_font\_family](#fun_table.cell_set_text_font_family) functions.

### Type

const string

### See also

* [box.new](#fun_box.new)
* [box.set\_text\_font_family](#fun_box.set_text_font_family)
* [label.new](#fun_label.new)
* [label.set\_text\_font_family](#fun_label.set_text_font_family)
* [table.cell](#fun_table.cell)
* [table.cell\_set\_text\_font\_family](#fun_table.cell_set_text_font_family)
* [font.family_monospace](#var_font.family_monospace)

## font.family_monospace

Monospace text font for [box.new](#fun_box.new), [box.set\_text\_font_family](#fun_box.set_text_font_family), [label.new](#fun_label.new), [label.set\_text\_font_family](#fun_label.set_text_font_family), [table.cell](#fun_table.cell) and [table.cell\_set\_text\_font\_family](#fun_table.cell_set_text_font_family) functions.

### Type

const string

### See also

* [box.new](#fun_box.new)
* [box.set\_text\_font_family](#fun_box.set_text_font_family)
* [label.new](#fun_label.new)
* [label.set\_text\_font_family](#fun_label.set_text_font_family)
* [table.cell](#fun_table.cell)
* [table.cell\_set\_text\_font\_family](#fun_table.cell_set_text_font_family)
* [font.family_default](#var_font.family_default)

## format.inherit

is a named constant for selecting the formatting of the script output values from the parent series in the [indicator](#fun_indicator) function.

### Type

const string

### See also

* [indicator](#fun_indicator)
* [format.price](#var_format.price)
* [format.volume](#var_format.volume)
* [format.percent](#var_format.percent)

## format.mintick

is a named constant to use with the [str.tostring](#fun_str.tostring) function. passing a number to [str.tostring](#fun_str.tostring) with this argument rounds the number to the nearest value that can be divided by [syminfo.mintick](#var_syminfo.mintick), without the remainder, with ties rounding up, and returns the string version of said value with trailing zeroes.

### Type

const string

### See also

* [indicator](#fun_indicator)
* [format.inherit](#var_format.inherit)
* [format.price](#var_format.price)
* [format.volume](#var_format.volume)

## format.percent

is a named constant for selecting the formatting of the script output values as a percentage in the indicator function. it adds a percent sign after values.

### Type

const string

### Remarks

the default precision is 2, regardless of the precision of the chart itself. this can be changed with the 'precision' argument of the [indicator](#fun_indicator) function.

### See also

* [indicator](#fun_indicator)
* [format.inherit](#var_format.inherit)
* [format.price](#var_format.price)
* [format.volume](#var_format.volume)

## format.price

is a named constant for selecting the formatting of the script output values as prices in the [indicator](#fun_indicator) function.

### Type

const string

### Remarks

if format is format.price, default precision value is set. You can use the precision argument of indicator function to change the precision value.

### See also

* [indicator](#fun_indicator)
* [format.inherit](#var_format.inherit)
* [format.volume](#var_format.volume)
* [format.percent](#var_format.percent)

## format.volume

is a named constant for selecting the formatting of the script output values as volume in the [indicator](#fun_indicator) function, e.g. '5183' will be formatted as '5.183K'.

### Type

const string

### See also

* [indicator](#fun_indicator)
* [format.inherit](#var_format.inherit)
* [format.price](#var_format.price)
* [format.percent](#var_format.percent)

## hline.style_dashed

is a named constant for dashed linestyle of [hline](#fun_hline) function.

### Type

const hline_style

### See also

* [hline.style_solid](#var_hline.style_solid)
* [hline.style_dotted](#var_hline.style_dotted)

## hline.style_dotted

is a named constant for dotted linestyle of [hline](#fun_hline) function.

### Type

const hline_style

### See also

* [hline.style_solid](#var_hline.style_solid)
* [hline.style_dashed](#var_hline.style_dashed)

## hline.style_solid

is a named constant for solid linestyle of [hline](#fun_hline) function.

### Type

const hline_style

### See also

* [hline.style_dotted](#var_hline.style_dotted)
* [hline.style_dashed](#var_hline.style_dashed)

## label.style_arrowdown

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style_arrowup

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style_circle

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style_cross

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style_diamond

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)

## label.style_flag

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style\_label\_center

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style\_label\_down

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style\_label\_left

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style\_label\_lower_left

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style\_label\_lower_right

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style\_label\_right

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style\_label\_up

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style\_label\_upper_left

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style\_label\_upper_right

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style_none

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style_square

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_diamond](#var_label.style_diamond)

## label.style\_text\_outline

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style_triangledown

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style_triangleup

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_xcross](#var_label.style_xcross)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_lower_left](#var_label.style_label_lower_left)
* [label.style\_label\_lower_right](#var_label.style_label_lower_right)
* [label.style\_label\_upper_left](#var_label.style_label_upper_left)
* [label.style\_label\_upper_right](#var_label.style_label_upper_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## label.style_xcross

label style for [label.new](#fun_label.new) and [label.set_style](#fun_label.set_style) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [label.set_textalign](#fun_label.set_textalign)
* [label.style_none](#var_label.style_none)
* [label.style_cross](#var_label.style_cross)
* [label.style_triangleup](#var_label.style_triangleup)
* [label.style_triangledown](#var_label.style_triangledown)
* [label.style_flag](#var_label.style_flag)
* [label.style_circle](#var_label.style_circle)
* [label.style_arrowup](#var_label.style_arrowup)
* [label.style_arrowdown](#var_label.style_arrowdown)
* [label.style\_label\_up](#var_label.style_label_up)
* [label.style\_label\_down](#var_label.style_label_down)
* [label.style\_label\_left](#var_label.style_label_left)
* [label.style\_label\_right](#var_label.style_label_right)
* [label.style\_label\_center](#var_label.style_label_center)
* [label.style_square](#var_label.style_square)
* [label.style_diamond](#var_label.style_diamond)

## line.style\_arrow\_both

line style for [line.new](#fun_line.new) and [line.set_style](#fun_line.set_style) functions. solid line with arrows on both points.

### Type

const string

### See also

* [line.new](#fun_line.new)
* [line.set_style](#fun_line.set_style)
* [line.style_solid](#var_line.style_solid)
* [line.style_dotted](#var_line.style_dotted)
* [line.style_dashed](#var_line.style_dashed)
* [line.style\_arrow\_left](#var_line.style_arrow_left)
* [line.style\_arrow\_right](#var_line.style_arrow_right)

## line.style\_arrow\_left

line style for [line.new](#fun_line.new) and [line.set_style](#fun_line.set_style) functions. solid line with arrow on the first point.

### Type

const string

### See also

* [line.new](#fun_line.new)
* [line.set_style](#fun_line.set_style)
* [line.style_solid](#var_line.style_solid)
* [line.style_dotted](#var_line.style_dotted)
* [line.style_dashed](#var_line.style_dashed)
* [line.style\_arrow\_right](#var_line.style_arrow_right)
* [line.style\_arrow\_both](#var_line.style_arrow_both)

## line.style\_arrow\_right

line style for [line.new](#fun_line.new) and [line.set_style](#fun_line.set_style) functions. solid line with arrow on the second point.

### Type

const string

### See also

* [line.new](#fun_line.new)
* [line.set_style](#fun_line.set_style)
* [line.style_solid](#var_line.style_solid)
* [line.style_dotted](#var_line.style_dotted)
* [line.style_dashed](#var_line.style_dashed)
* [line.style\_arrow\_left](#var_line.style_arrow_left)
* [line.style\_arrow\_both](#var_line.style_arrow_both)

## line.style_dashed

line style for [line.new](#fun_line.new) and [line.set_style](#fun_line.set_style) functions.

### Type

const string

### See also

* [line.new](#fun_line.new)
* [line.set_style](#fun_line.set_style)
* [line.style_solid](#var_line.style_solid)
* [line.style_dotted](#var_line.style_dotted)
* [line.style\_arrow\_left](#var_line.style_arrow_left)
* [line.style\_arrow\_right](#var_line.style_arrow_right)
* [line.style\_arrow\_both](#var_line.style_arrow_both)

## line.style_dotted

line style for [line.new](#fun_line.new) and [line.set_style](#fun_line.set_style) functions.

### Type

const string

### See also

* [line.new](#fun_line.new)
* [line.set_style](#fun_line.set_style)
* [line.style_solid](#var_line.style_solid)
* [line.style_dashed](#var_line.style_dashed)
* [line.style\_arrow\_left](#var_line.style_arrow_left)
* [line.style\_arrow\_right](#var_line.style_arrow_right)
* [line.style\_arrow\_both](#var_line.style_arrow_both)

## line.style_solid

line style for [line.new](#fun_line.new) and [line.set_style](#fun_line.set_style) functions.

### Type

const string

### See also

* [line.new](#fun_line.new)
* [line.set_style](#fun_line.set_style)
* [line.style_dotted](#var_line.style_dotted)
* [line.style_dashed](#var_line.style_dashed)
* [line.style\_arrow\_left](#var_line.style_arrow_left)
* [line.style\_arrow\_right](#var_line.style_arrow_right)
* [line.style\_arrow\_both](#var_line.style_arrow_both)

## location.abovebar

Location value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions. shape is plotted above main series bars.

### Type

const string

### See also

* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [location.belowbar](#var_location.belowbar)
* [location.top](#var_location.top)
* [location.bottom](#var_location.bottom)
* [location.absolute](#var_location.absolute)

## location.absolute

Location value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions. shape is plotted on chart using indicator value as a price coordinate.

### Type

const string

### See also

* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [location.abovebar](#var_location.abovebar)
* [location.belowbar](#var_location.belowbar)
* [location.top](#var_location.top)
* [location.bottom](#var_location.bottom)

## location.belowbar

Location value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions. shape is plotted below main series bars.

### Type

const string

### See also

* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [location.abovebar](#var_location.abovebar)
* [location.top](#var_location.top)
* [location.bottom](#var_location.bottom)
* [location.absolute](#var_location.absolute)

## location.bottom

Location value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions. shape is plotted near the bottom chart border.

### Type

const string

### See also

* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [location.abovebar](#var_location.abovebar)
* [location.belowbar](#var_location.belowbar)
* [location.top](#var_location.top)
* [location.absolute](#var_location.absolute)

## location.top

Location value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions. shape is plotted near the top chart border.

### Type

const string

### See also

* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [location.abovebar](#var_location.abovebar)
* [location.belowbar](#var_location.belowbar)
* [location.bottom](#var_location.bottom)
* [location.absolute](#var_location.absolute)

## math.e

is a named constant for [Euler's number](https://en.wikipedia.org/wiki/E_(mathematical_constant)). it is equal to 2.7182818284590452.

### Type

const float

### See also

* [math.phi](#var_math.phi)
* [math.pi](#var_math.pi)
* [math.rphi](#var_math.rphi)

## math.phi

is a named constant for the [golden ratio](https://en.wikipedia.org/wiki/Golden_ratio). it is equal to 1.6180339887498948.

### Type

const float

### See also

* [math.e](#var_math.e)
* [math.pi](#var_math.pi)
* [math.rphi](#var_math.rphi)

## math.pi

is a named constant for [archimedes' constant](https://en.wikipedia.org/wiki/pi). it is equal to 3.1415926535897932.

### Type

const float

### See also

* [math.e](#var_math.e)
* [math.phi](#var_math.phi)
* [math.rphi](#var_math.rphi)

## math.rphi

is a named constant for the [golden ratio conjugate](https://en.wikipedia.org/wiki/Golden_ratio#Golden_ratio_conjugate). it is equal to 0.6180339887498948.

### Type

const float

### See also

* [math.e](#var_math.e)
* [math.pi](#var_math.pi)
* [math.phi](#var_math.phi)

## order.ascending

Determines the sort order of the array from the smallest to the largest value.

### Type

const sort_order

### See also

* [array.new_float](#fun_array.new_float)
* [array.sort](#fun_array.sort)

## order.descending

Determines the sort order of the array from the largest to the smallest value.

### Type

const sort_order

### See also

* [array.new_float](#fun_array.new_float)
* [array.sort](#fun_array.sort)

## plot.style_area

a named constant for the 'area' style, to be used as an argument for the \`style\` parameter in the [plot](#fun_plot) function.

### Type

const plot_style

### See also

* [plot](#fun_plot)
* [plot.style_steplinebr](#var_plot.style_steplinebr)
* [plot.style_line](#var_plot.style_line)
* [plot.style_linebr](#var_plot.style_linebr)
* [plot.style_stepline](#var_plot.style_stepline)
* [plot.style\_stepline\_diamond](#var_plot.style_stepline_diamond)
* [plot.style_histogram](#var_plot.style_histogram)
* [plot.style_areabr](#var_plot.style_areabr)
* [plot.style_cross](#var_plot.style_cross)
* [plot.style_columns](#var_plot.style_columns)
* [plot.style_circles](#var_plot.style_circles)

## plot.style_areabr

a named constant for the 'area With breaks' style, to be used as an argument for the \`style\` parameter in the [plot](#fun_plot) function. similar to [plot.style_area](#var_plot.style_area), except the gaps in the data are not filled.

### Type

const plot_style

### See also

* [plot](#fun_plot)
* [plot.style_steplinebr](#var_plot.style_steplinebr)
* [plot.style_line](#var_plot.style_line)
* [plot.style_linebr](#var_plot.style_linebr)
* [plot.style_stepline](#var_plot.style_stepline)
* [plot.style\_stepline\_diamond](#var_plot.style_stepline_diamond)
* [plot.style_histogram](#var_plot.style_histogram)
* [plot.style_cross](#var_plot.style_cross)
* [plot.style_area](#var_plot.style_area)
* [plot.style_columns](#var_plot.style_columns)
* [plot.style_circles](#var_plot.style_circles)

## plot.style_circles

a named constant for the 'Circles' style, to be used as an argument for the \`style\` parameter in the [plot](#fun_plot) function.

### Type

const plot_style

### See also

* [plot](#fun_plot)
* [plot.style_steplinebr](#var_plot.style_steplinebr)
* [plot.style_line](#var_plot.style_line)
* [plot.style_linebr](#var_plot.style_linebr)
* [plot.style_stepline](#var_plot.style_stepline)
* [plot.style\_stepline\_diamond](#var_plot.style_stepline_diamond)
* [plot.style_histogram](#var_plot.style_histogram)
* [plot.style_cross](#var_plot.style_cross)
* [plot.style_area](#var_plot.style_area)
* [plot.style_areabr](#var_plot.style_areabr)
* [plot.style_columns](#var_plot.style_columns)

## plot.style_columns

a named constant for the 'columns' style, to be used as an argument for the \`style\` parameter in the [plot](#fun_plot) function.

### Type

const plot_style

### See also

* [plot](#fun_plot)
* [plot.style_steplinebr](#var_plot.style_steplinebr)
* [plot.style_line](#var_plot.style_line)
* [plot.style_linebr](#var_plot.style_linebr)
* [plot.style_stepline](#var_plot.style_stepline)
* [plot.style\_stepline\_diamond](#var_plot.style_stepline_diamond)
* [plot.style_histogram](#var_plot.style_histogram)
* [plot.style_cross](#var_plot.style_cross)
* [plot.style_area](#var_plot.style_area)
* [plot.style_areabr](#var_plot.style_areabr)
* [plot.style_circles](#var_plot.style_circles)

## plot.style_cross

a named constant for the 'Cross' style, to be used as an argument for the \`style\` parameter in the [plot](#fun_plot) function.

### Type

const plot_style

### See also

* [plot](#fun_plot)
* [plot.style_steplinebr](#var_plot.style_steplinebr)
* [plot.style_line](#var_plot.style_line)
* [plot.style_linebr](#var_plot.style_linebr)
* [plot.style_stepline](#var_plot.style_stepline)
* [plot.style\_stepline\_diamond](#var_plot.style_stepline_diamond)
* [plot.style_histogram](#var_plot.style_histogram)
* [plot.style_area](#var_plot.style_area)
* [plot.style_areabr](#var_plot.style_areabr)
* [plot.style_columns](#var_plot.style_columns)
* [plot.style_circles](#var_plot.style_circles)

## plot.style_histogram

a named constant for the 'Histogram' style, to be used as an argument for the \`style\` parameter in the [plot](#fun_plot) function.

### Type

const plot_style

### See also

* [plot](#fun_plot)
* [plot.style_steplinebr](#var_plot.style_steplinebr)
* [plot.style_line](#var_plot.style_line)
* [plot.style_linebr](#var_plot.style_linebr)
* [plot.style_stepline](#var_plot.style_stepline)
* [plot.style\_stepline\_diamond](#var_plot.style_stepline_diamond)
* [plot.style_cross](#var_plot.style_cross)
* [plot.style_area](#var_plot.style_area)
* [plot.style_areabr](#var_plot.style_areabr)
* [plot.style_columns](#var_plot.style_columns)
* [plot.style_circles](#var_plot.style_circles)

## plot.style_line

a named constant for the 'line' style, to be used as an argument for the \`style\` parameter in the [plot](#fun_plot) function.

### Type

const plot_style

### See also

* [plot](#fun_plot)
* [plot.style_steplinebr](#var_plot.style_steplinebr)
* [plot.style_linebr](#var_plot.style_linebr)
* [plot.style_stepline](#var_plot.style_stepline)
* [plot.style\_stepline\_diamond](#var_plot.style_stepline_diamond)
* [plot.style_histogram](#var_plot.style_histogram)
* [plot.style_cross](#var_plot.style_cross)
* [plot.style_area](#var_plot.style_area)
* [plot.style_areabr](#var_plot.style_areabr)
* [plot.style_columns](#var_plot.style_columns)
* [plot.style_circles](#var_plot.style_circles)

## plot.style_linebr

a named constant for the 'line With breaks' style, to be used as an argument for the \`style\` parameter in the [plot](#fun_plot) function. similar to [plot.style_line](#var_plot.style_line), except the gaps in the data are not filled.

### Type

const plot_style

### See also

* [plot](#fun_plot)
* [plot.style_steplinebr](#var_plot.style_steplinebr)
* [plot.style_line](#var_plot.style_line)
* [plot.style_stepline](#var_plot.style_stepline)
* [plot.style\_stepline\_diamond](#var_plot.style_stepline_diamond)
* [plot.style_histogram](#var_plot.style_histogram)
* [plot.style_cross](#var_plot.style_cross)
* [plot.style_area](#var_plot.style_area)
* [plot.style_areabr](#var_plot.style_areabr)
* [plot.style_columns](#var_plot.style_columns)
* [plot.style_circles](#var_plot.style_circles)

## plot.style_stepline

a named constant for the 'step line' style, to be used as an argument for the \`style\` parameter in the [plot](#fun_plot) function.

### Type

const plot_style

### See also

* [plot](#fun_plot)
* [plot.style_line](#var_plot.style_line)
* [plot.style_steplinebr](#var_plot.style_steplinebr)
* [plot.style\_stepline\_diamond](#var_plot.style_stepline_diamond)
* [plot.style_linebr](#var_plot.style_linebr)
* [plot.style_histogram](#var_plot.style_histogram)
* [plot.style_cross](#var_plot.style_cross)
* [plot.style_area](#var_plot.style_area)
* [plot.style_areabr](#var_plot.style_areabr)
* [plot.style_columns](#var_plot.style_columns)
* [plot.style_circles](#var_plot.style_circles)

## plot.style\_stepline\_diamond

a named constant for the 'step line With Diamonds' style, to be used as an argument for the \`style\` parameter in the [plot](#fun_plot) function. similar to [plot.style_stepline](#var_plot.style_stepline), except the data changes are also marked with the Diamond shapes.

### Type

const plot_style

### See also

* [plot](#fun_plot)
* [plot.style_steplinebr](#var_plot.style_steplinebr)
* [plot.style_line](#var_plot.style_line)
* [plot.style_linebr](#var_plot.style_linebr)
* [plot.style_histogram](#var_plot.style_histogram)
* [plot.style_cross](#var_plot.style_cross)
* [plot.style_area](#var_plot.style_area)
* [plot.style_areabr](#var_plot.style_areabr)
* [plot.style_columns](#var_plot.style_columns)
* [plot.style_circles](#var_plot.style_circles)

## plot.style_steplinebr

a named constant for the 'step line with breaks' style, to be used as an argument for the \`style\` parameter in the [plot](#fun_plot) function.

### Type

const plot_style

### See also

* [plot](#fun_plot)
* [plot.style_circles](#var_plot.style_circles)
* [plot.style_line](#var_plot.style_line)
* [plot.style_linebr](#var_plot.style_linebr)
* [plot.style_stepline](#var_plot.style_stepline)
* [plot.style\_stepline\_diamond](#var_plot.style_stepline_diamond)
* [plot.style_histogram](#var_plot.style_histogram)
* [plot.style_cross](#var_plot.style_cross)
* [plot.style_area](#var_plot.style_area)
* [plot.style_areabr](#var_plot.style_areabr)
* [plot.style_columns](#var_plot.style_columns)

## position.bottom_center

table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.

binds the table to the bottom edge in the center.

### Type

const string

### See also

* [table.new](#fun_table.new)
* [table.cell](#fun_table.cell)
* [table.set_position](#fun_table.set_position)
* [position.top_left](#var_position.top_left)
* [position.top_center](#var_position.top_center)
* [position.top_right](#var_position.top_right)
* [position.middle_left](#var_position.middle_left)
* [position.middle_center](#var_position.middle_center)
* [position.middle_right](#var_position.middle_right)
* [position.bottom_left](#var_position.bottom_left)

## position.bottom_left

table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.

binds the table to the bottom left of the screen.

### Type

const string

### See also

* [table.new](#fun_table.new)
* [table.cell](#fun_table.cell)
* [table.set_position](#fun_table.set_position)
* [position.top_left](#var_position.top_left)
* [position.top_center](#var_position.top_center)
* [position.top_right](#var_position.top_right)
* [position.middle_left](#var_position.middle_left)
* [position.middle_center](#var_position.middle_center)
* [position.middle_right](#var_position.middle_right)
* [position.bottom_center](#var_position.bottom_center)

## position.bottom_right

table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.

binds the table to the bottom right of the screen.

### Type

const string

### See also

* [table.new](#fun_table.new)
* [table.cell](#fun_table.cell)
* [table.set_position](#fun_table.set_position)
* [position.top_left](#var_position.top_left)
* [position.top_center](#var_position.top_center)
* [position.top_right](#var_position.top_right)
* [position.middle_left](#var_position.middle_left)
* [position.middle_center](#var_position.middle_center)
* [position.middle_right](#var_position.middle_right)
* [position.bottom_left](#var_position.bottom_left)
* [position.bottom_center](#var_position.bottom_center)

## position.middle_center

table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.

binds the table to the center of the screen.

### Type

const string

### See also

* [table.new](#fun_table.new)
* [table.cell](#fun_table.cell)
* [table.set_position](#fun_table.set_position)
* [position.top_left](#var_position.top_left)
* [position.top_center](#var_position.top_center)
* [position.top_right](#var_position.top_right)
* [position.middle_left](#var_position.middle_left)
* [position.middle_right](#var_position.middle_right)
* [position.bottom_left](#var_position.bottom_left)
* [position.bottom_center](#var_position.bottom_center)

## position.middle_left

table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.

binds the table to the left side of the screen.

### Type

const string

### See also

* [table.new](#fun_table.new)
* [table.cell](#fun_table.cell)
* [table.set_position](#fun_table.set_position)
* [position.top_left](#var_position.top_left)
* [position.top_center](#var_position.top_center)
* [position.top_right](#var_position.top_right)
* [position.middle_center](#var_position.middle_center)
* [position.middle_right](#var_position.middle_right)
* [position.bottom_left](#var_position.bottom_left)
* [position.bottom_center](#var_position.bottom_center)

## position.middle_right

table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.

binds the table to the right side of the screen.

### Type

const string

### See also

* [table.new](#fun_table.new)
* [table.cell](#fun_table.cell)
* [table.set_position](#fun_table.set_position)
* [position.top_left](#var_position.top_left)
* [position.top_center](#var_position.top_center)
* [position.top_right](#var_position.top_right)
* [position.middle_left](#var_position.middle_left)
* [position.middle_center](#var_position.middle_center)
* [position.bottom_left](#var_position.bottom_left)
* [position.bottom_center](#var_position.bottom_center)

## position.top_center

table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.

binds the table to the top edge in the center.

### Type

const string

### See also

* [table.new](#fun_table.new)
* [table.cell](#fun_table.cell)
* [table.set_position](#fun_table.set_position)
* [position.top_left](#var_position.top_left)
* [position.top_right](#var_position.top_right)
* [position.middle_left](#var_position.middle_left)
* [position.middle_center](#var_position.middle_center)
* [position.middle_right](#var_position.middle_right)
* [position.bottom_left](#var_position.bottom_left)
* [position.bottom_center](#var_position.bottom_center)

## position.top_left

table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.

binds the table to the upper-left edge.

### Type

const string

### See also

* [table.new](#fun_table.new)
* [table.cell](#fun_table.cell)
* [table.set_position](#fun_table.set_position)
* [position.top_center](#var_position.top_center)
* [position.top_right](#var_position.top_right)
* [position.middle_left](#var_position.middle_left)
* [position.middle_center](#var_position.middle_center)
* [position.middle_right](#var_position.middle_right)
* [position.bottom_left](#var_position.bottom_left)
* [position.bottom_center](#var_position.bottom_center)

## position.top_right

table position is used in [table.new](#fun_table.new), [table.cell](#fun_table.cell) functions.

binds the table to the upper-right edge.

### Type

const string

### See also

* [table.new](#fun_table.new)
* [table.cell](#fun_table.cell)
* [table.set_position](#fun_table.set_position)
* [position.top_left](#var_position.top_left)
* [position.top_center](#var_position.top_center)
* [position.middle_left](#var_position.middle_left)
* [position.middle_center](#var_position.middle_center)
* [position.middle_right](#var_position.middle_right)
* [position.bottom_left](#var_position.bottom_left)
* [position.bottom_center](#var_position.bottom_center)

## scale.left

scale value for [indicator](#fun_indicator) function. indicator is added to the left price scale.

### Type

const scale_type

### See also

* [indicator](#fun_indicator)

## scale.none

scale value for [indicator](#fun_indicator) function. indicator is added in 'No scale' mode. Can be used only with 'overlay=true'.

### Type

const scale_type

### See also

* [indicator](#fun_indicator)

## scale.right

scale value for [indicator](#fun_indicator) function. indicator is added to the right price scale.

### Type

const scale_type

### See also

* [indicator](#fun_indicator)

## session.extended

Constant for extended session type (with extended hours data).

### Type

const string

### See also

* [session.regular](#var_session.regular)
* [syminfo.session](#var_syminfo.session)

## session.regular

Constant for regular session type (no extended hours data).

### Type

const string

### See also

* [session.extended](#var_session.extended)
* [syminfo.session](#var_syminfo.session)

## shape.arrowdown

shape style for [plotshape](#fun_plotshape) function.

### Type

const string

### See also

* [plotshape](#fun_plotshape)

## shape.arrowup

shape style for [plotshape](#fun_plotshape) function.

### Type

const string

### See also

* [plotshape](#fun_plotshape)

## shape.circle

shape style for [plotshape](#fun_plotshape) function.

### Type

const string

### See also

* [plotshape](#fun_plotshape)

## shape.cross

shape style for [plotshape](#fun_plotshape) function.

### Type

const string

### See also

* [plotshape](#fun_plotshape)

## shape.diamond

shape style for [plotshape](#fun_plotshape) function.

### Type

const string

### See also

* [plotshape](#fun_plotshape)

## shape.flag

shape style for [plotshape](#fun_plotshape) function.

### Type

const string

### See also

* [plotshape](#fun_plotshape)

## shape.labeldown

shape style for [plotshape](#fun_plotshape) function.

### Type

const string

### See also

* [plotshape](#fun_plotshape)

## shape.labelup

shape style for [plotshape](#fun_plotshape) function.

### Type

const string

### See also

* [plotshape](#fun_plotshape)

## shape.square

shape style for [plotshape](#fun_plotshape) function.

### Type

const string

### See also

* [plotshape](#fun_plotshape)

## shape.triangledown

shape style for [plotshape](#fun_plotshape) function.

### Type

const string

### See also

* [plotshape](#fun_plotshape)

## shape.triangleup

shape style for [plotshape](#fun_plotshape) function.

### Type

const string

### See also

* [plotshape](#fun_plotshape)

## shape.xcross

shape style for [plotshape](#fun_plotshape) function.

### Type

const string

### See also

* [plotshape](#fun_plotshape)

## size.auto

size value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions. the size of the shape automatically adapts to the size of the bars.

### Type

const string

### See also

* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [label.set_size](#fun_label.set_size)
* [size.tiny](#var_size.tiny)
* [size.small](#var_size.small)
* [size.normal](#var_size.normal)
* [size.large](#var_size.large)
* [size.huge](#var_size.huge)

## size.huge

size value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions. the size of the shape constantly huge.

### Type

const string

### See also

* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [label.set_size](#fun_label.set_size)
* [size.auto](#var_size.auto)
* [size.tiny](#var_size.tiny)
* [size.small](#var_size.small)
* [size.normal](#var_size.normal)
* [size.large](#var_size.large)

## size.large

size value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions. the size of the shape constantly large.

### Type

const string

### See also

* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [label.set_size](#fun_label.set_size)
* [size.auto](#var_size.auto)
* [size.tiny](#var_size.tiny)
* [size.small](#var_size.small)
* [size.normal](#var_size.normal)
* [size.huge](#var_size.huge)

## size.normal

size value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions. the size of the shape constantly normal.

### Type

const string

### See also

* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [label.set_size](#fun_label.set_size)
* [size.auto](#var_size.auto)
* [size.tiny](#var_size.tiny)
* [size.small](#var_size.small)
* [size.large](#var_size.large)
* [size.huge](#var_size.huge)

## size.small

size value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions. the size of the shape constantly small.

### Type

const string

### See also

* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [label.set_size](#fun_label.set_size)
* [size.auto](#var_size.auto)
* [size.tiny](#var_size.tiny)
* [size.normal](#var_size.normal)
* [size.large](#var_size.large)
* [size.huge](#var_size.huge)

## size.tiny

size value for [plotshape](#fun_plotshape), [plotchar](#fun_plotchar) functions. the size of the shape constantly tiny.

### Type

const string

### See also

* [plotshape](#fun_plotshape)
* [plotchar](#fun_plotchar)
* [label.set_size](#fun_label.set_size)
* [size.auto](#var_size.auto)
* [size.small](#var_size.small)
* [size.normal](#var_size.normal)
* [size.large](#var_size.large)
* [size.huge](#var_size.huge)

## splits.denominator

a named constant for the [request.splits](#fun_request.splits) function. is used to request the denominator (the number below the line in a fraction) of a splits.

### Type

const string

### See also

* [request.splits](#fun_request.splits)

## splits.numerator

a named constant for the [request.splits](#fun_request.splits) function. is used to request the numerator (the number above the line in a fraction) of a splits.

### Type

const string

### See also

* [request.splits](#fun_request.splits)

## strategy.cash

this is one of the arguments that can be supplied to the \`default\_qty\_type\` parameter in the [strategy](#fun_strategy) declaration statement. it is only relevant when no value is used for the 'qty' parameter in [strategy.entry](#fun_strategy.entry) or [strategy.order](#fun_strategy.order) function calls. it specifies that an amount of cash in the \`strategy.account_currency\` will be used to enter trades.

### Type

const string

### Example


```s

//@version=5
strategy("strategy.cash", overlay = true, default_qty_value = 50, default_qty_type = strategy.cash, initial_capital = 1000000)

if bar_index == 0
    // as aEUR~qtyaEUR(tm) is not defined, the previously defined values for the `default_qty_type` and `default_qty_value` parameters are used to enter trades, namely 50 units of cash in the currency of `strategy.account_currency`.
    // `qty` is calculated as (default_qty_value)/(close price). if current price is $5, then qty = 50/5 = 10.
    strategy.entry("EN", strategy.long)
if bar_index == 2
    strategy.close("EN")


```

### See also

* [strategy](#fun_strategy)

## strategy.commission.cash\_per\_contract

Commission type for an order. Money displayed in the account currency per contract.

### Type

const string

### See also

* [strategy](#fun_strategy)

## strategy.commission.cash\_per\_order

Commission type for an order. Money displayed in the account currency per order.

### Type

const string

### See also

* [strategy](#fun_strategy)

## strategy.commission.percent

Commission type for an order. a percentage of the cash volume of order.

### Type

const string

### See also

* [strategy](#fun_strategy)

## strategy.direction.all

it allows strategy to open both long and short positions.

### Type

const string

### See also

* [strategy.risk.allow\_entry\_in](#fun_strategy.risk.allow_entry_in)

## strategy.direction.long

it allows strategy to open only long positions.

### Type

const string

### See also

* [strategy.risk.allow\_entry\_in](#fun_strategy.risk.allow_entry_in)

## strategy.direction.short

it allows strategy to open only short positions.

### Type

const string

### See also

* [strategy.risk.allow\_entry\_in](#fun_strategy.risk.allow_entry_in)

## strategy.fixed

this is one of the arguments that can be supplied to the \`default\_qty\_type\` parameter in the [strategy](#fun_strategy) declaration statement. it is only relevant when no value is used for the 'qty' parameter in [strategy.entry](#fun_strategy.entry) or [strategy.order](#fun_strategy.order) function calls. it specifies that a number of contracts/shares/lots will be used to enter trades.

### Type

const string

### Example


```s

//@version=5
strategy("strategy.fixed", overlay = true, default_qty_value = 50, default_qty_type = strategy.fixed, initial_capital = 1000000)

if bar_index == 0
    // as aEUR~qtyaEUR(tm) is not defined, the previously defined values for the `default_qty_type` and `default_qty_value` parameters are used to enter trades, namely 50 contracts.
    // qty = 50
    strategy.entry("EN", strategy.long)
if bar_index == 2
    strategy.close("EN")


```

### See also

* [strategy](#fun_strategy)

## strategy.oca.cancel

OCa type value for strategy's functions. the parameter determines that an order should belong to an OCO group, where as soon as an order is filled, all other orders of the same group are cancelled. Note: if more than 1 guaranteed-to-be-executed orders of the same OCa group are placed at once, all those orders are filled.

### Type

const string

### See also

* [strategy.entry](#fun_strategy.entry)
* [strategy.exit](#fun_strategy.exit)
* [strategy.order](#fun_strategy.order)

## strategy.oca.none

OCa type value for strategy's functions. the parameter determines that an order should not belong to any particular OCO group.

### Type

const string

### See also

* [strategy.entry](#fun_strategy.entry)
* [strategy.exit](#fun_strategy.exit)
* [strategy.order](#fun_strategy.order)

## strategy.oca.reduce

OCa type value for strategy's functions. the parameter determines that an order should belong to an OCO group, where if X number of contracts of an order is filled, number of contracts for each other order of the same OCO group is decreased by X. Note: if more than 1 guaranteed-to-be-executed orders of the same OCa group are placed at once, all those orders are filled.

### Type

const string

### See also

* [strategy.entry](#fun_strategy.entry)
* [strategy.exit](#fun_strategy.exit)
* [strategy.order](#fun_strategy.order)

## strategy.percent\_of\_equity

this is one of the arguments that can be supplied to the \`default\_qty\_type\` parameter in the [strategy](#fun_strategy) declaration statement. it is only relevant when no value is used for the 'qty' parameter in [strategy.entry](#fun_strategy.entry) or [strategy.order](#fun_strategy.order) function calls. it specifies that a percentage (0-100) of equity will be used to enter trades.

### Type

const string

### Example


```s

//@version=5
strategy("strategy.percent_of_equity", overlay = false, default_qty_value = 100, default_qty_type = strategy.percent_of_equity, initial_capital = 1000000)

// as aEUR~qtyaEUR(tm) is not defined, the previously defined values for the `default_qty_type` and `default_qty_value` parameters are used to enter trades, namely 100% of available equity.
if bar_index == 0
    strategy.entry("EN", strategy.long)
if bar_index == 2
    strategy.close("EN")
plot(strategy.equity)

 // the aEUR~qtyaEUR(tm) parameter is set to 10. Entering position with fixed size of 10 contracts and entry market price = (10 * close).
if bar_index == 4
    strategy.entry("EN", strategy.long, qty = 10)
if bar_index == 6
    strategy.close("EN")


```

### See also

* [strategy](#fun_strategy)

## text.align_bottom

Vertical text alignment for [box.new](#fun_box.new), [box.set\_text\_valign](#fun_box.set_text_valign), [table.cell](#fun_table.cell) and [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign) functions.

### Type

const string

### See also

* [table.cell](#fun_table.cell)
* [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign)
* [text.align_center](#var_text.align_center)
* [text.align_left](#var_text.align_left)
* [text.align_right](#var_text.align_right)

## text.align_center

Text alignment for [box.new](#fun_box.new), [box.set\_text\_halign](#fun_box.set_text_halign), [box.set\_text\_valign](#fun_box.set_text_valign), [label.new](#fun_label.new) and [label.set_textalign](#fun_label.set_textalign) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [text.align_left](#var_text.align_left)
* [text.align_right](#var_text.align_right)

## text.align_left

Horizontal text alignment for [box.new](#fun_box.new), [box.set\_text\_halign](#fun_box.set_text_halign), [label.new](#fun_label.new) and [label.set_textalign](#fun_label.set_textalign) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [text.align_center](#var_text.align_center)
* [text.align_right](#var_text.align_right)

## text.align_right

Horizontal text alignment for [box.new](#fun_box.new), [box.set\_text\_halign](#fun_box.set_text_halign), [label.new](#fun_label.new) and [label.set_textalign](#fun_label.set_textalign) functions.

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_style](#fun_label.set_style)
* [text.align_center](#var_text.align_center)
* [text.align_left](#var_text.align_left)

## text.align_top

Vertical text alignment for [box.new](#fun_box.new), [box.set\_text\_valign](#fun_box.set_text_valign), [table.cell](#fun_table.cell) and [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign) functions.

### Type

const string

### See also

* [table.cell](#fun_table.cell)
* [table.cell\_set\_text_valign](#fun_table.cell_set_text_valign)
* [text.align_center](#var_text.align_center)
* [text.align_left](#var_text.align_left)
* [text.align_right](#var_text.align_right)

## text.wrap_auto

automatic wrapping mode for [box.new](#fun_box.new) and [box.set\_text\_wrap](#fun_box.set_text_wrap) functions.

### Type

const string

### See also

* [box.new](#fun_box.new)
* [box.set_text](#fun_box.set_text)
* [box.set\_text\_wrap](#fun_box.set_text_wrap)

## text.wrap_none

Disabled wrapping mode for [box.new](#fun_box.new) and [box.set\_text\_wrap](#fun_box.set_text_wrap) functions.

### Type

const string

### See also

* [box.new](#fun_box.new)
* [box.set_text](#fun_box.set_text)
* [box.set\_text\_wrap](#fun_box.set_text_wrap)

## xloc.bar_index

a named constant that specifies the algorithm of interpretation of x-value in functions [line.new](#fun_line.new) and [label.new](#fun_label.new). if xloc = [xloc.bar_index](#var_xloc.bar_index), value of x is a bar index.

### Type

const string

### See also

* [line.new](#fun_line.new)
* [label.new](#fun_label.new)
* [line.set_xloc](#fun_line.set_xloc)
* [label.set_xloc](#fun_label.set_xloc)
* [xloc.bar_time](#var_xloc.bar_time)

## xloc.bar_time

a named constant that specifies the algorithm of interpretation of x-value in functions [line.new](#fun_line.new) and [label.new](#fun_label.new). if xloc = [xloc.bar_time](#var_xloc.bar_time), value of x is a bar unix time.

### Type

const string

### See also

* [line.new](#fun_line.new)
* [label.new](#fun_label.new)
* [line.set_xloc](#fun_line.set_xloc)
* [label.set_xloc](#fun_label.set_xloc)
* [xloc.bar_index](#var_xloc.bar_index)

## yloc.abovebar

a named constant that specifies the algorithm of interpretation of y-value in function [label.new](#fun_label.new).

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_yloc](#fun_label.set_yloc)
* [yloc.price](#var_yloc.price)
* [yloc.belowbar](#var_yloc.belowbar)

## yloc.belowbar

a named constant that specifies the algorithm of interpretation of y-value in function [label.new](#fun_label.new).

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_yloc](#fun_label.set_yloc)
* [yloc.price](#var_yloc.price)
* [yloc.abovebar](#var_yloc.abovebar)

## yloc.price

a named constant that specifies the algorithm of interpretation of y-value in function [label.new](#fun_label.new).

### Type

const string

### See also

* [label.new](#fun_label.new)
* [label.set_yloc](#fun_label.set_yloc)
* [yloc.abovebar](#var_yloc.abovebar)
* [yloc.belowbar](#var_yloc.belowbar)


Keywords
--------

## # and

Logical and. applicable to boolean expressions.

### Syntax

```
expr1 and expr2
```

### Returns

boolean value, or series of boolean values.

## # export

used in libraries to prefix the declaration of functions or user-defined type definitions that will be available from other scripts importing the library.

### Example


```s

//@version=5
//@description library of debugging functions.
library("Debugging_library", overlay = true)
//@function Displays a string as a table cell for debugging purposes.
//@param txt string to display.
//@returns Void.
export print(string txt) =>
    var table t = table.new(position.middle_right, 1, 1)
    table.cell(t, 0, 0, txt, bgcolor = color.yellow)
// using the function from inside the library to show an example on the published chart.
// this has no impact on scripts using the library.
print("library Test")


```

### Remarks

Each library must have at least one exported function or user-defined type (udt).

Exported functions cannot use variables from the global scope if they are arrays, mutable variables (reassigned with `:=`), or variables of 'input' form.

Exported functions cannot use `request.*()` functions.

Exported functions must explicitly declare each parameter's type and all parameters must be used in the function's body. by default, all arguments passed to exported functions are of the [series](https://pinerefsmall.tiiny.site//#op_series) form, unless they are explicitly specified as [simple](https://pinerefsmall.tiiny.site//#op_simple) in the function's signature.

the @description, @function, @param, @type, @field, and @returns compiler annotations are used to automatically generate the library's description and release notes, and in the pine scriptA(r) Editor's tooltips.

### See also

-   [library
    ](https://pinerefsmall.tiiny.site//#fun_library)
-   [import
    ](https://pinerefsmall.tiiny.site//#op_import)
-   [simple
    ](https://pinerefsmall.tiiny.site//#op_simple)
-   [series
    ](https://pinerefsmall.tiiny.site//#op_series)
-   [type
    ](https://pinerefsmall.tiiny.site//#op_type)

## # false

literal representing a [bool](https://pinerefsmall.tiiny.site//#op_bool) value, and result of a comparison operation.

### Remarks

see the user Manual for [comparison operators](https://www.tradingview.com/pine-script-docs/en/v5/language/Operators.html#comparison-operators) and [logical operators](https://www.tradingview.com/pine-script-docs/en/v5/language/Operators.html#logical-operators).

### See also

-   [bool
    ](https://pinerefsmall.tiiny.site//#op_bool)

## # for

the 'for' structure allows the repeated execution of a number of statements:

### Syntax

```
> [var_declaration =] for counter = from_num to to_num [by step_num]
statements | continue | break
return_expression
```

**var_declaration** - an optional variable declaration that will be assigned the value of the loop's return_expression.

**counter** - a variable holding the value of the loop's counter, which is incremented/decremented by 1 or by the step_num value on each iteration of the loop.

**from_num** - the starting value of the counter. "series int/float" values/expressions are allowed.

**to_num** - the end value of the counter. When the counter becomes greater than to_num (or less than to_num in cases where from_num > to_num) the loop is broken. "series int/float" values/expressions are allowed, but they are evaluated only on the loop's first iteration.

**step_num** - the increment/decrement value of the counter. it is optional. the default value is +1 or -1, depending on which of from_num or to_num is the greatest. When a value is used, the counter is also incremented/decremented depending on which of from_num or to_num is the greatest, so the +/- sign of step_num is optional.

**statements | continue | break** - any number of statements, or the 'continue' or 'break' keywords, indented by 4 spaces or a tab.

**return_expression** - the loop's return value which is assigned to the variable in var_declaration if one is present. if the loop exits because of a 'continue' or 'break' keyword, the loop's return value is that of the last variable assigned a value before the loop's exit.

**continue** - a keyword that can only be used in loops. it causes the next iteration of the loop to be executed.

**break** - a keyword that exits the loop.

### Example


```s

//@version=5
indicator("for")
// Here, we count the quantity of bars in a given 'lookback' length which closed above the current bar's close
qtyOfHigherCloses(lookback) =>
    int result = 0
    for i = 1 to lookback
        if close[i] > close
            result += 1
    result
plot(qtyOfHigherCloses(14))



```

### See also

-   [for...in
    ](https://pinerefsmall.tiiny.site//#op_for...in)
-   [while
    ](https://pinerefsmall.tiiny.site//#op_while)

## # for...in

the `for...in` structure allows the repeated execution of a number of statements for each element in an array. it can be used with either one argument: `array_element`, or with two: `[index, array_element]`. the second form doesn't affect the functionality of the loop. it tracks the current iteration's index in the tuple's first variable.

### Syntax

```
> [var_declaration =] for array_element in array_id
statements | continue | break
return_expression
> [var_declaration =] for [index, array_element] in array_id
statements | continue | break
return_expression
```

**var_declaration** - an optional variable declaration that will be assigned the value of the loop's `return_expression`.

**index** - an optional variable that tracks the current iteration's index. indexing starts at 0. the variable is immutable in the loop's body. When used, it must be included in a tuple also containing `array_element`.

**array_element** - a variable containing each successive array element to be processed in the loop. the variable is immutable in the loop's body.

**array_id** - the iD of the array over which the loop is iterated.

**statements | continue | break** - any number of statements, or the 'continue' or 'break' keywords, indented by 4 spaces or a tab.

**return_expression** - the loop's return value assigned to the variable in `var_declaration`, if one is present. if the loop exits because of a 'continue' or 'break' keyword, the loop's return value is that of the last variable assigned a value before the loop's exit.

**continue** - a keyword that can only be used in loops. it causes the next iteration of the loop to be executed.

**break** - a keyword that exits the loop.

it is allowed to modify the array's elements or its size inside the loop.

Here, we use the single-argument form of `for...in` to determine on each bar how many of the bar's OHLC values are greater than the sMa of 'close' values:

### Example


```s

//@version=5
indicator("`for` loop with a step")

a = array.from(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
sum = 0.0

for i = 0 to 9 by 5
    // because the step is set to 5, we are adding only the first (0) and the sixth (5) value from the array `a`.
    sum += array.get(a, i)

plot(sum)


```

#op_for...in) to set the values of our `ispos` array to `true` when their corresponding value in our `valuesarray` array is positive:

### Example


```s

//@version=5
indicator("for...in")
// Here we determine on each bar how many of the bar's OHLC values are greater than the sMa of 'close' values
float[] ohlcValues = array.from(open, high, low, close)
qtyGreaterthan(value, array) =>
    int result = 0
    for currentelement in array
        if currentelement > value
            result += 1
        result
plot(qtyGreaterthan(ta.sma(close, 20), ohlcValues))
Here, we use the two-argument form of for...in to set the values of our `ispos` array to `true` when their corresponding value in our `valuesarray` array is positive:



```

### See also

-   [for
    ](https://pinerefsmall.tiiny.site//#op_for)
-   [while
    ](https://pinerefsmall.tiiny.site//#op_while)
-   [array.sum
    ](https://pinerefsmall.tiiny.site//#fun_array.sum)
-   [array.min
    ](https://pinerefsmall.tiiny.site//#fun_array.min)
-   [array.max
    ](https://pinerefsmall.tiiny.site//#fun_array.max)

## # if

if statement defines what block of statements must be executed when conditions of the expression are satisfied.

To have access to and use the if statement, one should specify the version >= 2 of pine scriptA(r) language in the very first line of code, for example:
```

//@version=5
indicator("for...in")
var valuesarray = array.from(4, -8, 11, 78, -16, 34, 7, 99, 0, 55)
var ispos = array.new_bool(10, false)

for [index, value] in valuesarray
    if value > 0
        array.set(ispos, index, true)

if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(ispos))
iterate through matrix rows as arrays.



```

## # import

used to load an external [library](https://pinerefsmall.tiiny.site//#fun_library) into a script and bind its functions to a namespace. the importing script can be an indicator, a strategy, or another library. a library must be published (privately or publicly) before it can be imported.

### Syntax

```
import {username}/{libraryName}/{libraryVersion} as {alias}
```

### Arguments

- `username`

    >  (`literal` `string`)
    
    >  user name of the library's author.

- `libraryName`

    >  (`literal` `string`)
    
    >  Name of the imported library, which corresponds to the `title` argument used by the author in his library script.

- `libraryVersion`

    >  (`literal` `int`)
    
    >  Version number of the imported library.

- `alias`

    >  (`literal` `string`)
    
    >  Namespace used to refer to the library's functions. optional. the default is the libraryName string.

### Remarks

using an alias that replaces a built-in namespace such as math.* or strategy.* is allowed, but if the library contains function names that shadow pine scriptA(r)'s built-in functions, the built-ins will become unavailable. the same version of a library can only be imported once. aliases must be distinct for each imported library. When calling library functions, casting their arguments to types other than their declared type is not allowed.

### See also

-   [library
    ](https://pinerefsmall.tiiny.site//#fun_library)
-   [export
    ](https://pinerefsmall.tiiny.site//#op_export)

## # method

this keyword is used to prefix a function declaration, indicating it can then be invoked using dot notation by appending its name to a variable of the type of its first parameter and omitting that first parameter. alternatively, functions declared as methods can also be invoked like normal user-defined functions. in that case, an argument must be supplied for its first parameter.

the first parameter of a method declaration must be explicitly typified.

### Syntax

```
> [export] method <functionName>(<paramType> <paramName> [= <defaultValue>], ...) =>
<functionblock>
```


//@version=5
the 4th version of pine scriptA(r) Language allows you to use aEURoeelse ifaEUR syntax.
General code form:

### Syntax

var_declarationX = if condition
var_decl_then0
var_decl_then1
...
var_decl_thenN
else if [optional block]
var_decl_else0
var_decl_else1
...
var_decl_elseN
else
var_decl_else0
var_decl_else1
...
var_decl_elseN
return_expression_else
where
var_declarationX aEUR" this variable gets the value of the if statement
condition aEUR" if the condition is true, the logic from the block 'then' (var_decl_then0, var_decl_then1, etc.) is used.
if the condition is false, the logic from the block 'else' (var_decl_else0, var_decl_else1, etc.) is used.
return_expression_then, return_expression_else aEUR" the last expression from the block then or from the block else will return the final value of the statement. if declaration of the variable is in the end, its value will be the result.
the type of returning value of the if statement depends on return_expression_then and return_expression_else type (their types must match: it is not possible to return an integer value from then, while you have a string value in else block).


### Example

```s

//@version=5
indicator("if")
// this code compiles
x = if close > open
    close
else
    open

// this code doesnaEUR(tm)t compile
// y = if close > open
//     close
// else
//     "open"
plot(x)
it is possible to omit the `else` block. in this case if the condition is false, an aEURoeemptyaEUR value (na, false, or aEURoeaEUR) will be assigned to the var_declarationX variable:



```

### Returns

the value of the last expression in the local block of statements that is executed.

### Remarks

Only one of the `local_block` instances or the `default_local_block` can be executed. the `default_local_block` is introduced with the `=>` token alone and is only executed when none of the preceding blocks are executed. if the result of the `switch` statement is assigned to a variable and a `default_local_block` is not specified, the statement returns `na` if no `local_block` is executed. When assigning the result of the `switch` statement to a variable, all `local_block` instances must return the same type of value.

### See also

-   [if
    ](https://pinerefsmall.tiiny.site//#op_if)
-   [?:
    ](https://pinerefsmall.tiiny.site//#op_?:)

## # true

literal representing one of the values a [bool](https://pinerefsmall.tiiny.site//#op_bool) variable can hold, or an expression can evaluate to when it uses comparison or logical operators.

### Remarks

see the user Manual for [comparison operators](https://www.tradingview.com/pine-script-docs/en/v5/language/Operators.html#comparison-operators) and [logical operators](https://www.tradingview.com/pine-script-docs/en/v5/language/Operators.html#logical-operators).

### See also

-   [bool
    ](https://pinerefsmall.tiiny.site//#op_bool)

## # type

this keyword allows the declaration of user-defined types (udt) from which scripts can instantiate objects. udts are composite types that contain an arbitrary number of fields of any built-in or user-defined type, including the defined udt itself. the syntax to define a udt is:

### Syntax

```
> [export ]type <udt_identifier>
> [varip ]<field_type> <field_name> [= <value>]
...
```

Once a udt is defined, scripts can instantiate objects from it with the `udt_identifier.new()` construct. When creating a new type instance, the fields of the resulting object will initialize with the default values from the udt's definition. any type fields without specified defaults will initialize as [na](https://pinerefsmall.tiiny.site//#var_na). alternatively, users can pass initial values as arguments in the `*.new()` method to override the type's defaults. For example, `newFooobject = foo.new(x = true)` assigns a new `foo` object to the `newFooobject` variable with its `x` field initialized using a value of [true](https://pinerefsmall.tiiny.site//#op_true).

Field declarations can include the [varip](https://pinerefsmall.tiiny.site//#op_varip) keyword, in which case the field values persist between successive script iterations on the same bar.

For more information see the user Manual's sections on [defining udts](https://www.tradingview.com/pine-script-docs/en/v5/language/Type_system.html#user-defined-types) and [using objects](https://www.tradingview.com/pine-script-docs/en/v5/language/objects.html).

libraries can export udts. see the[libraries](https://www.tradingview.com/pine-script-docs/en/v5/concepts/libraries.html#user-defined-types-and-objects) page of our user Manual to learn more.

### Example


```s

//@version=5
indicator("if")
x = if close > open
    close
// if current close > current open, then x = close.
// Otherwise the x = na.
plot(x)
it is possible to use either multiple aEURoeelse ifaEUR blocks or none at all. the blocks aEURoethenaEUR, aEURoeelse ifaEUR, aEURoeelseaEUR are shifted by four spaces:



```

## # var

**var** is the keyword used for assigning and one-time initializing of the variable.

Normally, a syntax of assignment of variables, which doesnaEUR(tm)t include the keyword var, results in the value of the variable being overwritten with every update of the data. Contrary to that, when assigning variables with the keyword var, they can aEURoekeep the stateaEUR despite the data updating, only changing it when conditions within if-expressions are met.

### Syntax

```
var variable_name = expression
```

where:

**variable_name** - any name of the useraEUR(tm)s variable thataEUR(tm)s allowed in pine scriptA(r) (can contain capital and lowercase Latin characters, numbers, and underscores (_), but canaEUR(tm)t start with a number).

**expression** - any arithmetic expression, just as with defining a regular variable. the expression will be calculated and assigned to a variable once.

### Example


```s

//@version=5
indicator("if")
x = if open > close
    5
else if high > low
    close
else
    open
plot(x)
it is possible to ignore the resulting value of an `if` statement (aEURoevar_declarationX=aEURoe can be omitted). it may be useful if you need the side effect of the expression, for example in strategy trading:



```

## # varip

**varip** (var intrabar persist) is the keyword used for the assignment and one-time initialization of a variable or a field of a user-defined [type](https://pinerefsmall.tiiny.site//#op_type). itaEUR(tm)s similar to the [var](https://pinerefsmall.tiiny.site//#op_var) keyword, but variables and fields declared with [varip](https://pinerefsmall.tiiny.site//#op_varip) retain their values between executions of the script on the same bar.

### Syntax

```
varip [<variable_type> ]<variable_name> = <expression>
> [export ]type <udt_identifier>
varip <field_type> <field_name> [= <value>]
```

where:

**variable_type** - an optional fundamental type ([int](https://pinerefsmall.tiiny.site//#op_int), [float](https://pinerefsmall.tiiny.site//#op_float), [bool](https://pinerefsmall.tiiny.site//#op_bool), [color](https://pinerefsmall.tiiny.site//#op_color), [string](https://pinerefsmall.tiiny.site//#op_string)) or a user-defined type, or an array or matrix of one of those types. special types are not compatible with this keyword.

**variable_name** - a [valid identifier](https://www.tradingview.com/pine-script-docs/en/v5/language/identifiers.html). the variable can also be an object created from a udt.

**expression** - any arithmetic expression, just as when defining a regular variable. the expression will be calculated and assigned to the variable only once, on the first bar.

**udt_identifier, field_type, field_name, value** - Constructs related to user-defined types as described in the [type](https://pinerefsmall.tiiny.site//#op_type) section.

### Example


```s

//@version=5
strategy("if")
if (ta.crossover(high, low))
    strategy.entry("bbandlE", strategy.long, stop=low, oca_name="bollingerbands", oca_type=strategy.oca.cancel, comment="bbandlE")
else
    strategy.cancel(id="bbandlE")
if statements can include each other:



```

#op_var), `v` would equal the value of the [bar_index](https://pinerefsmall.tiiny.site//#var_bar_index). On historical bars, where the script calculates only once per chart bar, the value of `v` is the same as with [var](https://pinerefsmall.tiiny.site//#op_var). However, on realtime bars, the script will evaluate the expression on each new chart update, producing a different result.

### Example


```s

//@version=5
indicator("if")
float x = na
if close > open
    if close > close[1]
        x := close
    else
        x := close[1]
else
    x := open
plot(x)

```

#op_+=) operation applied to both the `index` and `ticks` fields results in different real-time values because `ticks` increases on every chart update, while `index` only does so once per bar. Note how the `currbar` object does not use the [varip](https://pinerefsmall.tiiny.site//#op_varip) keyword. the `ticks` field of the object can increment on every tick, but the reference itself is defined once and then stays unchanged. if we were to declare `currbar` using [varip](https://pinerefsmall.tiiny.site//#op_varip), the behavior of `index` would remain unchanged because while the reference to the type instance would persist between chart updates, the `index` field of the object would not.

### Remarks

When using [varip](https://pinerefsmall.tiiny.site//#op_varip) to declare variables in strategies that may execute more than once per historical chart bar, the values of such variables are preserved across successive iterations of the script on the same bar.

the effect of [varip](https://pinerefsmall.tiiny.site//#op_varip) eliminates the [rollback](https://www.tradingview.com/pine-script-docs/en/v5/language/Execution_model.html#calculation-based-on-realtime-bars) of variables before each successive execution of a script on the same bar.

## # while

the `while` statement allows the conditional iteration of a local code block.

### Syntax

```
variable_declaration = while boolean_expression
...
continue
...
break
...
return_expression
```

where:

**variable_declaration** - an optional variable declaration. the `return expression` can provide the initialization value for this variable.

**boolean_expression** - when true, the local block of the `while` statement is executed. When false, execution of the script resumes after the `while` statement.

**continue** - the `continue` keyword causes the loop to branch to its next iteration.

**break** - the `break` keyword causes the loop to terminate. the script's execution resumes after the `while` statement.

**return_expression** - an optional line providing the `while` statement's returning value.

### Example


```s

//@version=5
indicator("num_methods import")
// import the first version of the usernameaEUR(tm)s "num_methods" library and assign it to the "m" namespace",
import username/num_methods/1 as m
// Call the aEURoesinh()aEUR function from the imported library
y = m.sinh(3.14)
// plot value returned by the "sinh()" function",
plot(y)


```

### Remarks

the local code block after the initial `while` line must be indented with four spaces or a tab. For the `while` loop to terminate, the boolean expression following `while` must eventually become false, or a `break` must be executed.

Types
-----

## # array

Keyword used to explicitly declare the "array" type of a variable or a parameter. array objects (or iDs) can be created with the [array.new<type>](https://pinerefsmall.tiiny.site//#fun_array.new%3Ctype%3E), [array.from](https://pinerefsmall.tiiny.site//#fun_array.from) function.

### Example


```s

//@version=5
indicator("")

var prices = array.new<float>()

//@function pushes a new value into the array and removes the first one if the resulting array is greater than `maxsize`. Can be used as a method.
method maintainarray(array<float> id, maxsize, value) =>
    id.push(value)
    if id.size() > maxsize
        id.shift()

prices.maintainarray(50, close)
// the method can also be called like a function, without using dot notation.
// in this case an argument must be supplied for its first parameter.
// maintainarray(prices, 50, close)

// this calls the `array.avg()` built-in using dot notation with the `prices` array.
// it is possible because built-in functions belonging to some namespaces that are a special pine type
// can be invoked with method notation when the function\'s first parameter is an iD of that type.
// those namespaces are: `array`, `matrix`, `line`, `linefill`, `label`, `box`, and `table`.
plot(prices.avg())

```



## not
Logical negation (NOT). applicable to boolean expressions.

### Syntax

not expr1

### Returns

boolean value, or series of boolean values.


## or
Logical OR. applicable to boolean expressions.

### Syntax

expr1 or expr2

### Returns

boolean value, or series of boolean values.


## switch
the switch operator transfers control to one of the several statements, depending on the values of a condition and expressions.

### Syntax
```g4
> [variable_declaration = ] switch expression
value1 => local_block
value2 => local_block
...
=> default_local_block
> [variable_declaration = ] switch
boolean_expression1 => local_block
boolean_expression2 => local_block
...
=> default_local_block
switch with an expression:
```

### Example

```s
//@version=5
indicator("switch using an expression")

string i_maType = input.string("ema", "Ma type", options = ["ema", "sMa", "RMa", "WMa"])

float ma = switch i_maType
    "ema" => ta.ema(close, 10)
    "sMa" => ta.sma(close, 10)
    "RMa" => ta.rma(close, 10)
    // Default used when the three first cases do not match.
    => ta.wma(close, 10)

plot(ma)
switch without an expression:



```

### Remarks

array objects are always of "series" form.

### See also

-   [var
    ](https://pinerefsmall.tiiny.site//#op_var)
-   [line
    ](https://pinerefsmall.tiiny.site//#op_line)
-   [label
    ](https://pinerefsmall.tiiny.site//#op_label)
-   [table
    ](https://pinerefsmall.tiiny.site//#op_table)
-   [box
    ](https://pinerefsmall.tiiny.site//#op_box)
-   [array.new<type>
    ](https://pinerefsmall.tiiny.site//#fun_array.new%3Ctype%3E)
-   [array.from
    ](https://pinerefsmall.tiiny.site//#fun_array.from)

## # bool

Keyword used to explicitly declare the "bool" (boolean) type of a variable or a parameter. "bool" variables can have values [true](https://pinerefsmall.tiiny.site//#op_true), [false](https://pinerefsmall.tiiny.site//#op_false) or [na](https://pinerefsmall.tiiny.site//#var_na).

### Example


```s

//@version=5
strategy("switch without an expression", overlay = true)

bool longCondition  = ta.crossover( ta.sma(close, 14), ta.sma(close, 28))
bool shortcondition = ta.crossunder(ta.sma(close, 14), ta.sma(close, 28))

switch
    longCondition  => strategy.entry("Long iD", strategy.long)
    shortcondition => strategy.entry("short iD", strategy.short)


```

### Remarks

Explicitly mentioning the type in a variable declaration is optional, except when it is initialized with [na](https://pinerefsmall.tiiny.site//#var_na). Learn more about pine scriptA(r) types in the user Manual page on the [Type system](https://www.tradingview.com/pine-script-docs/en/v5/language/Type_system.html).

### See also

-   [var
    ](https://pinerefsmall.tiiny.site//#op_var)
-   [varip
    ](https://pinerefsmall.tiiny.site//#op_varip)
-   [int
    ](https://pinerefsmall.tiiny.site//#op_int)
-   [float
    ](https://pinerefsmall.tiiny.site//#op_float)
-   [color
    ](https://pinerefsmall.tiiny.site//#op_color)
-   [string
    ](https://pinerefsmall.tiiny.site//#op_string)
-   [true
    ](https://pinerefsmall.tiiny.site//#op_true)
-   [false
    ](https://pinerefsmall.tiiny.site//#op_false)

## # box

Keyword used to explicitly declare the "box" type of a variable or a parameter. box objects (or iDs) can be created with the [box.new](https://pinerefsmall.tiiny.site//#fun_box.new) function.

### Example


```s

//@version=5
indicator("Multi time period Chart", overlay = true)

timeframeinput = input.timeframe("1D")

type bar
    float o = open
    float h = high
    float l = low
    float c = close
    int   t = time

drawbox(bar b, right) =>
    bar s = bar.new()
    color boxcolor = b.c >= b.o ? color.green : color.red
    box.new(b.t, b.h, right, b.l, boxcolor, xloc = xloc.bar_time, bgcolor = color.new(boxcolor, 90))

updatebox(box boxid, bar b) =>
    color boxcolor = b.c >= b.o ? color.green : color.red
    box.set_border_color(boxid, boxcolor)
    box.set_bgcolor(boxid, color.new(boxcolor, 90))
    box.set_top(boxid, b.h)
    box.set_bottom(boxid, b.l)
    box.set_right(boxid, time)

secbar = request.security(syminfo.tickerid, timeframeinput, bar.new())

if not na(secbar)
    // To avoid a runtime error, only process data when an object exists.
    if not barstate.islast
        if timeframe.change(timeframeinput)
            // On historical bars, draw a new box in the past when the HTF closes.
            drawbox(secbar, time[1])
    else
        var box lastbox = na
        if na(lastbox) or timeframe.change(timeframeinput)
            // On the last bar, only draw a new current box the first time we get there or when HTF changes.
            lastbox := drawbox(secbar, time)
        else
            // On other chart updates, use setters to modify the current box.
            updatebox(lastbox, secbar)

```

### Remarks

box objects are always of "series" form.

### See also

-   [var
    ](https://pinerefsmall.tiiny.site//#op_var)
-   [line
    ](https://pinerefsmall.tiiny.site//#op_line)
-   [label
    ](https://pinerefsmall.tiiny.site//#op_label)
-   [table
    ](https://pinerefsmall.tiiny.site//#op_table)
-   [box.new
    ](https://pinerefsmall.tiiny.site//#fun_box.new)

## # chart.point

Keyword to explicitly declare the type of a variable or parameter as `chart.point`. scripts can produce `chart.point` instances using the [chart.point.from_time](https://pinerefsmall.tiiny.site//#fun_chart.point.from_time), [chart.point.from_index](https://pinerefsmall.tiiny.site//#fun_chart.point.from_index), and [chart.point.now](https://pinerefsmall.tiiny.site//#fun_chart.point.now) functions.

## Fields

index (series int) the x-coordinate of the point, expressed as a bar index value.

time (series float) the x-coordinate of the point, expressed as a unix time value.

price (series float) the y-coordinate of the point.

### See also

-   [polyline
    ](https://pinerefsmall.tiiny.site//#op_polyline)

## # color

Keyword used to explicitly declare the "color" type of a variable or a parameter.

### Example


```s

//@version=5
indicator("var keyword example")
var a = close
var b = 0.0
var c = 0.0
var green_bars_count = 0
if close > open
    var x = close
    b := x
    green_bars_count := green_bars_count + 1
    if green_bars_count >= 10
        var y = close
        c := y
plot(a)
plot(b)
plot(c)
the variable 'a' keeps the closing price of the first bar for each bar in the series.
the variable 'b' keeps the closing price of the first "green" bar in the series.
the variable 'c' keeps the closing price of the tenth "green" bar in the series.

```

#FF000080  // Red color (FF0000) with 50% transparency (80 which is half of FF).if barstate.islastconfirmedhistory    label.new(bar_index, high, text = "label", color = labelcolor, textcolor = textcolor)// When declaring variables with color literals, built-in constants(color.green) or functions (color.new(), color.rgb()), the "color" keyword for the type can be omitted.c = color.rgb(0,255,0,0)plot(close, color = c)

### Remarks

color literals have the following format: #RRGGbb or #RRGGbbaa. the letter pairs represent 00 to FF hexadecimal values (0 to 255 in decimal) where RR, GG and bb pairs are the values for the color's red, green and blue components. aa is an optional value for the color's transparency (or alpha component) where 00 is invisible and FF opaque. When no aa pair is supplied, FF is used. the hexadecimal letters can be upper or lower case.

Explicitly mentioning the type in a variable declaration is optional, except when it is initialized with [na](https://pinerefsmall.tiiny.site//#var_na). Learn more about pine scriptA(r) types in the user Manual page on the [Type system](https://www.tradingview.com/pine-script-docs/en/v5/language/Type_system.html).

### See also

-   [var
    ](https://pinerefsmall.tiiny.site//#op_var)
-   [varip
    ](https://pinerefsmall.tiiny.site//#op_varip)
-   [int
    ](https://pinerefsmall.tiiny.site//#op_int)
-   [float
    ](https://pinerefsmall.tiiny.site//#op_float)
-   [string
    ](https://pinerefsmall.tiiny.site//#op_string)
-   [color.rgb
    ](https://pinerefsmall.tiiny.site//#fun_color.rgb)
-   [color.new
    ](https://pinerefsmall.tiiny.site//#fun_color.new)

## # float

Keyword used to explicitly declare the "float" (floating point) type of a variable or a parameter.

### Example


```s

//@version=5
indicator("varip")
varip int v = -1
v := v + 1
plot(v)
With var, `v` would equal the value of the bar_index. On historical bars, where the script calculates only once per chart bar, the value of `v` is the same as with var. However, on realtime bars, the script will evaluate the expression on each new chart update, producing a different result.



```

### Remarks

Explicitly mentioning the type in a variable declaration is optional, except when it is initialized with [na](https://pinerefsmall.tiiny.site//#var_na). Learn more about pine scriptA(r) types in the user Manual page on the [Type system](https://www.tradingview.com/pine-script-docs/en/v5/language/Type_system.html).

### See also

-   [var
    ](https://pinerefsmall.tiiny.site//#op_var)
-   [varip
    ](https://pinerefsmall.tiiny.site//#op_varip)
-   [int
    ](https://pinerefsmall.tiiny.site//#op_int)
-   [bool
    ](https://pinerefsmall.tiiny.site//#op_bool)
-   [color
    ](https://pinerefsmall.tiiny.site//#op_color)
-   [string
    ](https://pinerefsmall.tiiny.site//#op_string)

## # int

Keyword used to explicitly declare the "int" (integer) type of a variable or a parameter.

### Example


```s

//@version=5
indicator("varip with types")
type bardata
    int index = -1
    varip int ticks = -1

var currbar = bardata.new()
currbar.index += 1
currbar.ticks += 1

// Will be equal to bar_index on all bars
plot(currbar.index)
// in real time, will increment per every tick on the chart
plot(currbar.ticks)
the same += operation applied to both the `index` and `ticks` fields results in different real-time values because `ticks` increases on every chart update, while `index` only does so once per bar. Note how the `currbar` object does not use the varip keyword. the `ticks` field of the object can increment on every tick, but the reference itself is defined once and then stays unchanged. if we were to declare `currbar` using varip, the behavior of `index` would remain unchanged because while the reference to the type instance would persist between chart updates, the `index` field of the object would not.


```

### Remarks

Explicitly mentioning the type in a variable declaration is optional, except when it is initialized with [na](https://pinerefsmall.tiiny.site//#var_na). Learn more about pine scriptA(r) types in the user Manual page on the [Type system](https://www.tradingview.com/pine-script-docs/en/v5/language/Type_system.html).

### See also

-   [var
    ](https://pinerefsmall.tiiny.site//#op_var)
-   [varip
    ](https://pinerefsmall.tiiny.site//#op_varip)
-   [float
    ](https://pinerefsmall.tiiny.site//#op_float)
-   [bool
    ](https://pinerefsmall.tiiny.site//#op_bool)
-   [color
    ](https://pinerefsmall.tiiny.site//#op_color)
-   [string
    ](https://pinerefsmall.tiiny.site//#op_string)

## # label

Keyword used to explicitly declare the "label" type of a variable or a parameter. label objects (or iDs) can be created with the [label.new](https://pinerefsmall.tiiny.site//#fun_label.new) function.

### Example


```s

//@version=5
indicator("while")
// this is a simple example of calculating a factorial using a while loop.
int i_n = input.int(10, "Factorial size", minval=0)
int counter   = i_n
int factorial = 1
while counter > 0
    factorial := factorial * counter
    counter   := counter - 1

plot(factorial)


```

### Remarks

label objects are always of "series" form.

### See also

-   [var
    ](https://pinerefsmall.tiiny.site//#op_var)
-   [line
    ](https://pinerefsmall.tiiny.site//#op_line)
-   [box
    ](https://pinerefsmall.tiiny.site//#op_box)
-   [label.new
    ](https://pinerefsmall.tiiny.site//#fun_label.new)

## # line

Keyword used to explicitly declare the "line" type of a variable or a parameter. line objects (or iDs) can be created with the [line.new](https://pinerefsmall.tiiny.site//#fun_line.new) function.

### Example


```s

//@version=5
indicator("array", overlay=true)
array<float> a = na
a := array.new<float>(1, close)
plot(array.get(a, 0))


```

### Remarks

line objects are always of "series" form.

### See also

-   [var
    ](https://pinerefsmall.tiiny.site//#op_var)
-   [label
    ](https://pinerefsmall.tiiny.site//#op_label)
-   [box
    ](https://pinerefsmall.tiiny.site//#op_box)
-   [line.new
    ](https://pinerefsmall.tiiny.site//#fun_line.new)

## # linefill

Keyword used to explicitly declare the "linefill" type of a variable or a parameter. linefill objects (or iDs) can be created with the [linefill.new](https://pinerefsmall.tiiny.site//#fun_linefill.new) function.

### Example


```s

//@version=5
indicator("bool")
bool b = true    // same as `b = true`
b := na
plot(b ? open : close)


```

### Remarks

linefill objects are always of "series" form.

### See also

-   [var
    ](https://pinerefsmall.tiiny.site//#op_var)
-   [line
    ](https://pinerefsmall.tiiny.site//#op_line)
-   [label
    ](https://pinerefsmall.tiiny.site//#op_label)
-   [table
    ](https://pinerefsmall.tiiny.site//#op_table)
-   [box
    ](https://pinerefsmall.tiiny.site//#op_box)
-   [linefill.new
    ](https://pinerefsmall.tiiny.site//#fun_linefill.new)

## # map

Keyword used to explicitly declare the "map" type of a variable or a parameter. map objects (or iDs) can be created with the [map.new<type,type>](https://pinerefsmall.tiiny.site//#fun_map.new%3Ctype,type%3E) function.

### Example


```s

//@version=5
indicator("box")
// empty `box1` box iD.
var box box1 = na
// `box` type is unnecessary because `box.new()` returns a "box" type.
var box2 = box.new(na, na, na, na)
box3 = box.new(time, open, time + 60 * 60 * 24, close, xloc=xloc.bar_time)


```

### Remarks

map objects are always of [series](https://www.tradingview.com/pine-script-docs/en/v5/language/Type_system.html#series) form.

### See also

> [map.new<type,type>
](https://pinerefsmall.tiiny.site//
#fun_map.new%3Ctype,type%3E)

## # matrix

Keyword used to explicitly declare the "matrix" type of a variable or a parameter. Matrix objects (or iDs) can be created with the [matrix.new<type>](https://pinerefsmall.tiiny.site//#fun_matrix.new%3Ctype%3E) function.

### Example


```s

//@version=5
indicator("color", overlay = true)

color textcolor = color.green
color labelcolor = #FF000080  // Red color (FF0000) with 50% transparency (80 which is half of FF).
if barstate.islastconfirmedhistory
    label.new(bar_index, high, text = "label", color = labelcolor, textcolor = textcolor)

// When declaring variables with color literals, built-in constants(color.green) or functions (color.new(), color.rgb()), the "color" keyword for the type can be omitted.
c = color.rgb(0,255,0,0)
plot(close, color = c)


```

### Remarks

Matrix objects are always of "series" form.

### See also

-   [var
    ](https://pinerefsmall.tiiny.site//#op_var)
-   [matrix.new<type>
    ](https://pinerefsmall.tiiny.site//#fun_matrix.new%3Ctype%3E)
-   [array
    ](https://pinerefsmall.tiiny.site//#op_array)

## # polyline

Keyword to explicitly declare the type of a variable or parameter as `polyline`. scripts can produce `polyline` instances using the [polyline.new](https://pinerefsmall.tiiny.site//#fun_polyline.new) function.

### See also

-   [chart.point
    ](https://pinerefsmall.tiiny.site//#op_chart.point)

## # series

**series** is a keyword that can be used in a library's exported functions to specify the type form required for a function's arguments. Explicit use of the `series` keyword is usually unnecessary because all arguments of exported functions are automatically converted to the "series" form by default.

### Syntax

```
export <functionName>([[series] <type>] <arg1>[ = <default_value>])
```

### Example


```s

//@version=5
indicator("float")
float f = 3.14    // same as `f = 3.14`
f := na
plot(f)


```

## # simple

**simple** is a keyword that can be used in a library's exported functions to specify the type form required for a function's arguments. by default, all arguments of exported functions are automatically converted into the "series" type form. in some cases, this would make arguments unusable with those of built-in functions that do not support the "series" form. For these cases, the `simple` keyword can be used instead.

### Syntax

```
export <functionName>([[simple] <type>] <arg1>[ = <default_value>])
```

### Example


```s

//@version=5
indicator("int")
int i = 14    // same as `i = 14`
i := na
plot(i)


```

## # string

Keyword used to explicitly declare the "string" type of a variable or a parameter.

### Example


```s

//@version=5
indicator("label")
// empty `label1` label iD.
var label label1 = na
// `label` type is unnecessary because `label.new()` returns "label" type.
var label2 = label.new(na, na, na)
if barstate.islastconfirmedhistory
    label3 = label.new(bar_index, high, text = "label3 text")


```

### Remarks

Explicitly mentioning the type in a variable declaration is optional, except when it is initialized with [na](https://pinerefsmall.tiiny.site//#var_na). Learn more about pine scriptA(r) types in the user Manual page on the [Type system](https://www.tradingview.com/pine-script-docs/en/v5/language/Type_system.html).

### See also

-   [var
    ](https://pinerefsmall.tiiny.site//#op_var)
-   [varip
    ](https://pinerefsmall.tiiny.site//#op_varip)
-   [int
    ](https://pinerefsmall.tiiny.site//#op_int)
-   [float
    ](https://pinerefsmall.tiiny.site//#op_float)
-   [bool
    ](https://pinerefsmall.tiiny.site//#op_bool)
-   [str.tostring
    ](https://pinerefsmall.tiiny.site//#fun_str.tostring)
-   [str.format
    ](https://pinerefsmall.tiiny.site//#fun_str.format)

## # table

Keyword used to explicitly declare the "table" type of a variable or a parameter. table objects (or iDs) can be created with the [table.new](https://pinerefsmall.tiiny.site//#fun_table.new) function.

### Example


```s

//@version=5
indicator("line")
// empty `line1` line iD.
var line line1 = na
// `line` type is unnecessary because `line.new()` returns "line" type.
var line2 = line.new(na, na, na, na)
line3 = line.new(bar_index - 1, high, bar_index, high, extend = extend.right)


```

### Remarks

table objects are always of "series" form.

### See also

-   [var
    ](https://pinerefsmall.tiiny.site//#op_var)
-   [line
    ](https://pinerefsmall.tiiny.site//#op_line)
-   [label
    ](https://pinerefsmall.tiiny.site//#op_label)
-   [box
    ](https://pinerefsmall.tiiny.site//#op_box)
-   [table.new
    ](https://pinerefsmall.tiiny.site//#fun_table.new)

Operators
---------

## # -

subtraction or unary minus. applicable to numerical expressions.

### Syntax

```
expr1 - expr2
```

### Returns

Returns integer or float value, or series of values:

binary `-` returns expr1 minus expr2.

unary `-` returns the negation of expr.

### Remarks

You may use arithmetic operators with numbers as well as with series variables. in case of usage with series the operators are applied elementwise.

## # -=

subtraction assignment. applicable to numerical expressions.

### Syntax

```
expr1 -= expr2
```

### Example


```s

//@version=5
indicator("linefill", overlay=true)
// empty `linefill1` line iD.
var linefill linefill1 = na
// `linefill` type is unnecessary because `linefill.new()` returns "linefill" type.
var linefill2 = linefill.new(na, na, na)

if barstate.islastconfirmedhistory
    line1 = line.new(bar_index - 10, high+1, bar_index, high+1, extend = extend.right)
    line2 = line.new(bar_index - 10, low+1, bar_index, low+1, extend = extend.right)
    linefill3 = linefill.new(line1, line2, color = color.new(color.green, 80))


```

### Returns

integer or float value, or series of values.

## # :=

Reassignment operator. it is used to assign a new value to a previously declared variable.

### Syntax

```
<var_name> := <new_value>
```

### Example


```s

//@version=5
indicator("map", overlay=true)
map<int, float> a = na
a := map.new<int, float>()
a.put(bar_index, close)
label.new(bar_index, a.get(bar_index), "Current close")


```

## # !=

Not equal to. applicable to expressions of any type.

### Syntax

```
expr1 != expr2
```

### Returns

boolean value, or series of boolean values.

## # ?:

Ternary conditional operator.

### Syntax

```
expr1 ? expr2 : expr3
```

### Example


```s

//@version=5
indicator("matrix example")

// Create `m1` matrix of `int` type.
matrix<int> m1 = matrix.new<int>(2, 3, 0)

// `matrix<int>` is unnecessary because the `matrix.new<int>()` function returns an `int` type matrix object.
m2 = matrix.new<int>(2, 3, 0)

// Display matrix using a label.
if barstate.islastconfirmedhistory
    label.new(bar_index, high, str.tostring(m2))


```

### Returns

expr2 if expr1 is evaluated to true, expr3 otherwise. Zero value (0 and also NaN, +infinity, -infinity) is considered to be false, any other value is true.

### Remarks

use [na](https://pinerefsmall.tiiny.site//#var_na) for 'else' branch if you do not need it.

You can combine two or more [?:](https://pinerefsmall.tiiny.site//#op_?:) operators to achieve the equivalent of a 'switch'-like statement (see examples above).

You may use arithmetic operators with numbers as well as with series variables. in case of usage with series the operators are applied elementwise.

### See also

-   [na
    ](https://pinerefsmall.tiiny.site//#var_na)

## # []

series subscript. provides access to previous values of series expr1. expr2 is the number of bars back, and must be numerical. Floats will be rounded down.

### Syntax

```
expr1[expr2]
```

### Example


```s

//@version=5
//@description library of debugging functions.
library("Debugging_library", overlay = true)
export smaCustom(series float source, series int length) =>
    ta.sma(source, length)

```

### Returns

a series of values.

### See also

-   [math.floor
    ](https://pinerefsmall.tiiny.site//#fun_math.floor)

## # *

Multiplication. applicable to numerical expressions.

### Syntax

```
expr1 * expr2
```

### Returns

integer or float value, or series of values.

## # *=

Multiplication assignment. applicable to numerical expressions.

### Syntax

```
expr1 *= expr2
```

### Example


```s

//@version=5
//@description library of debugging functions.
library("Debugging_library", overlay = true)
export emaWrong(float source, int length) =>
    // by default, both `source` and `length` will expect values of the `series` type form: `series float` for `source`, `series int` for `length`.
    // this function will not compile because `ema()` does not support a "series int" argument for `length`. a "simple int" is required.
    ta.ema(source, length)

export emaRight(float source, simple int length) =>
    // this function requires an argument of "simple int" type for its `length` parameter.
    ta.ema(source, length)

```

### Returns

integer or float value, or series of values.

## # /

division. applicable to numerical expressions.

### Syntax

```
expr1 / expr2
```

### Returns

integer or float value, or series of values.

## # /=

division assignment. applicable to numerical expressions.

### Syntax

```
expr1 /= expr2
```

### Example


```s

//@version=5
indicator("string")
string s = "Hello World!"    // same as `s = "Hello world!"`
// string s = na // same as ""
plot(na, title=s)


```

### Returns

integer or float value, or series of values.

## # %

Modulo (integer remainder). applicable to numerical expressions.

### Syntax

```
expr1 % expr2
```

### Returns

integer or float value, or series of values.

### Remarks

in pine scriptA(r), when the integer remainder is calculated, the quotient is truncated, i.e. rounded towards the lowest absolute value. the resulting value will have the same sign as the dividend.

Example: -1 % 9 = -1 - 9 * truncate(-1/9) = -1 - 9 * truncate(-0.111) = -1 - 9 * 0 = -1.

## # %=

Modulo assignment. applicable to numerical expressions.

### Syntax

```
expr1 %= expr2
```

### Example


```s

//@version=5
indicator("table")
// empty `table1` table iD.
var table table1 = na
// `table` type is unnecessary because `table.new()` returns "table" type.
var table2 = table.new(position.top_left, na, na)

if barstate.islastconfirmedhistory
    var table3 = table.new(position = position.top_right, columns = 1, rows = 1, bgcolor = color.yellow, border_width = 1)
    table.cell(table_id = table3, column = 0, row = 0, text = "table3 text")


```

### Returns

integer or float value, or series of values.

## # +

addition or unary plus. applicable to numerical expressions or strings.

### Syntax

```
expr1 + expr2
```

### Returns

binary `+` for strings returns concatenation of expr1 and expr2

For numbers returns integer or float value, or series of values:

binary `+` returns expr1 plus expr2.

unary `+` returns expr (does nothing added just for the symmetry with the unary - operator).

### Remarks

You may use arithmetic operators with numbers as well as with series variables. in case of usage with series the operators are applied elementwise.

## # +=

addition assignment. applicable to numerical expressions or strings.

### Syntax

```
expr1 += expr2
```

### Example


```s

//@version=5
indicator("-=")
// Equals to expr1 = expr1 - expr2.
a = 2
b = 3
a -= b
// Result: a = -1.
plot(a)


```

### Returns

For strings returns concatenation of expr1 and expr2. For numbers returns integer or float value, or series of values.

### Remarks

You may use arithmetic operators with numbers as well as with series variables. in case of usage with series the operators are applied elementwise.

## # <

Less than. applicable to numerical expressions.

### Syntax

```
expr1 < expr2
```

### Returns

boolean value, or series of boolean values.

## # <=

Less than or equal to. applicable to numerical expressions.

### Syntax

```
expr1 <= expr2
```

### Returns

boolean value, or series of boolean values.

## # ==

Equal to. applicable to expressions of any type.

### Syntax

```
expr1 == expr2
```

### Returns

boolean value, or series of boolean values.

## # =>

the '=>' operator is used in user-defined function declarations and in [switch](https://pinerefsmall.tiiny.site//#op_switch) statements.

the function declaration syntax is:

### Syntax

```
<identifier>([<parameter_name>[=<default_value>]], ...) =>
<local_block>
<function_result>
```

a <local_block> is zero or more pine scriptA(r) statements.

the <function_result> is a variable, an expression, or a tuple.

### Example


```s

//@version=5
indicator("My script")

myvar = 10

if close > open
    // Modifies the existing global scope `myvar` variable by changing its value from 10 to 20.
    myvar := 20
    // Creates a new `myvar` variable local to the `if` condition and unreachable from the global scope.
    // Does not affect the `myvar` declared in global scope.
    myvar = 30

plot(myvar)

```

### Remarks

You can learn more about user-defined functions in the user Manual's pages on [Declaring functions](https://www.tradingview.com/pine-script-docs/en/v5/language/user-defined_functions.html) and [libraries](https://www.tradingview.com/pine-script-docs/en/v5/concepts/libraries.html).

## # >

Greater than. applicable to numerical expressions.

### Syntax

```
expr1 > expr2
```

### Returns

boolean value, or series of boolean values.

## # >=

Greater than or equal to. applicable to numerical expressions.

### Syntax

```
expr1 >= expr2
```

### Returns

boolean value, or series of boolean values..
