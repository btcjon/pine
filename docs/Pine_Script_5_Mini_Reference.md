
# Pine Mini-Reference for more information

## Pine Script™ Operators

> The following operators are available.

| Operator | Description                                                 |
| -------- | ----------------------------------------------------------- |
| +        | Adds two operands                                           |
| -        | Subtracts the second operand from the first                 |
| \*       | Multiplies both operands                                    |
| /        | Divides first operand by second                             |
| %        | Modulus Operator and remainder of after an integer division |

## Pine Script Comparison Operaors

| Operator | Checks for                                                                 |
| -------- | -------------------------------------------------------------------------- |
| ==       | if values are equal then condition becomes true.                           |
| !=       | if values are not equal then condition becomes true.                       |
| >        | leftis greater than right, if yes then condition becomes true.             |
| <        | leftis less than right, if yes then condition becomes true.                |
| >=       | leftis greater than or equal to right, if yes then condition becomes true. |
| <=       | leftis less than or equal to right, if yes                                 |

## Pine Script Logical Operaors

| Operator | edsc             |
| -------- | ---------------- |
| and      | logical and      |
| or       | logical or       |
| not      | logical not      |
| ?:       | ternary operator |

## Pine Script Assignment Operaors

| Operator | Description               |
| -------- | ------------------------- |
| =        | assignment                |
| :=       | re-assignment             |
| +=       | addition assignment       |
| -=       | subtraction assignment    |
| \ \*=    | multiplication assignment |
| /=       | division assignment       |
| %=       | modulo assignment         |

# Pine Script™ Keywords

The following keywords are reserved in Pine Script™ and cannot be used as variable names.

| Keyword | Description                                  |
| ------- | -------------------------------------------- |
| import  | Imports a function                           |
| export  | Exports a function                           |
| method  | Creates a method                             |
| type    | Creates a user defined type statement        |
| matrix  | namespace, see matrix                        |
| var     | Creates a variable                           |
| varip   | Creates a variable with intrabar persistence |

## Reserved Keywords

`Catch` ,`Class` ,`Do` ,`Ellipse` ,`In` ,`Is` ,`Polygon` ,`Range` ,`Return` ,`Struct` ,`Text` ,`Throw` ,`Try`

# storage methods (using string as type for example purposes)

| Storage Method | Description                              |
| -------------- | ---------------------------------------- |
| matrix<string> | Matrix are row and column structures     |
| array<string>  | Arrays are single dimensional structures |
| string[]       | Array legacy or declaration shorthand    |
| string         | type name is plain for single item       |

## Pine Script™ Built-in Types

Thesse 10 types are built-in for variables, and can appear in storage types

| Types    | Description                                                                       |
| -------- | --------------------------------------------------------------------------------- |
| string   | String of characters                                                              |
| int      | Integer (whole number)                                                            |
| float    | Float (number with decimal and optional _[Ee]_                                    |
| bool     | Boolean (true/false)                                                              |
| color    | 3 options (color.name, #RRGGBBTT, rgba(r, g, b, a))                               |
| line     | line object (line.new(x1, y1, x2, y2, xloc, extend, style, width, color))         |
| linefill | line fill object (linefill.new(l1, l1, coor))                                     |
| box      | box object (box.new(left, top, right, bottom, .. etc.. )                          |
| label    | label object (label.new(x, y, string, xloc, yloc, style, color, .. etc.. )        |
| table    | table object (table.new(position, columns, rows, bgcolor, bordercolor, .. etc.. ) |

## Pine Script™ User-defined Types

The following types are available for user-defined types.
A type can be defined with the type keyword.
A type is similar to a class in object-oriented languages,
but methods are declared afterwards and externally

| Type           | Description                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------- |
| type <name>    | Create a user-defined type with name                                                           |
| <name> .new()  | Create a new user-defined type object                                                          |
| <name>.<field> | calls the stored field item of the type either to reassign, or as an expression's return value |

# Pine Script™ Variables and Constants

Pine Script™ is a loosely typed language. This means that
you do not need to specify the type of data a variable
refers to on asignment unless it is 'na'.
The data type is automatically assigned when
the variable is assigned a value.
It is NOT possible to change the data type after.

> Example

```s
a = 1                         // a is  a int
b = 1.2                       // b is  a float
c = "1.2"                     // c is  a string
d = true                      // d is  a bool
e = color.new(color.red, 50)  // e is  a color
```

> Example

```s
// type inference
// declare a variable without an initial value
// the variable type will be 'na' until it is assigned a value
var int a = na
// assign a value to the na int
a := 1
// variable type is now a value

```

# BUILT INS

## Pine Script Indicator functions and variables

| Function/Var           | Description                                        |
| ---------------------- | -------------------------------------------------- |
| ta.accdist             | Returns the accumulation/distribution line.        |
| ta.alma()              | Returns the Arnaud Legoux Moving Average.          |
| ta.atr()               | ATR Returns the Average True Range indicator.      |
| ta.bb()                | Returns the Bollinger Bands.                       |
| ta.bbw()               | Returns the Bollinger Width indicator.             |
| ta.cci()               | Returns the Commodity Channel index.               |
| ta.cmo()               | Returns the Chande Momentum Oscillator.            |
| ta.cog()               | Returns the Center of Gravity indicator.           |
| ta.dmi()               | Returns the Directional Movement indicator.        |
| ta.ema()               | Returns the Exponential Moving Average.            |
| ta.hma()               | Returns the Hull Moving Average.                   |
| ta.iii                 | Returns the Intraday Intensity Index indicator.    |
| ta.kc()                | Returns the Keltner Channels.                      |
| ta.kcw()               | Returns the Keltner Channels width.                |
| ta.linreg()            | Returns the Linear Regression Overlay.             |
| ta.macd()              | Returns the Moving Average Convergence/Divergence. |
| ta.mfi()               | Returns the Money Flow Index.                      |
| ta.mom()               | Returns the Momentum indicator.                    |
| ta.nvi                 | Returns the Negative Volume Index.                 |
| ta.obv                 | Returns the On-Balance Volume indicator.           |
| ta.pvi                 | Returns the Positive Volume Index.                 |
| ta.pvt                 | Returns the Price Volume Trend indicator.          |
| ta.rma()               | Returns the Roughness Moving Average.              |
| ta.roc()               | Returns the Rate of Change indicator.              |
| ta.rsi(source, length) | Returns the Relative Strength Index.               |
| ta.sar()               | Returns the Parabolic Stop and Reverse.            |
| ta.sma()               | Returns the Simple Moving Average.                 |
| ta.stoch()             | Returns the Stochastic oscillator.                 |
| ta.supertrend()        | Returns the Supertrend indicator.                  |
| ta.swma(source)        | Returns the Smoothed Weighted Moving Average.      |
| ta.tr                  | Returns the True Range.                            |
| ta.tsi()               | Returns the True Strength Index.                   |
| ta.vwap                | Returns the Volume Weighted Average Price.         |
| ta.vwma()              | Returns the Volume Weighted Moving Average.        |
| ta.wad                 | Returns the Williams Accumulation/Distribution.    |
| ta.wma()               | Returns the Weighted Moving Average.               |
| ta.wpr()               | Returns the Williams %R indicator.                 |
| ta.wvad                | Returns the Volume Accumulation/Distribution.      |

## Pine Script Supporting functions

| Function                                 | Description                                                                                  |
| ---------------------------------------- | -------------------------------------------------------------------------------------------- |
| ta.barsince()                            | Returns the number of bars since a condition has been true.                                  |
| ta.change()                              | Returns the percent change of a bar compared to the previous bar.                            |
| ta.correlation(source1, source2, length) | Returns the Pearson’s correlation coefficient between two prices.                            |
| ta.cross(source1, source2)               | Returns true if source1 crossed source2 from downward to upward.                             |
| ta.crossover(source1, source2)           | Returns true if source1 crossed source2 from downward to upward.                             |
| ta.crossunder(source1, source2)          | Returns true if source1 crossed source2 from upward to downward.                             |
| ta.cum(source)                           | Returns the cumulative sum of a source.                                                      |
| ta.dev()                                 | Returns the standard deviation of a source.                                                  |
| ta.falling()                             | Returns true if the current bar’s close price is lower than the previous bar’s close price.  |
| ta.highest()                             | Returns the highest value from the source.                                                   |
| ta.highestbars()                         | Returns the highest value from the source within n bars.                                     |
| ta.lowest()                              | Returns the lowest value from the source.                                                    |
| ta.lowestbars()                          | Returns the lowest value from the source within n bars.                                      |
| ta.median()                              | Returns the median given the source data.                                                    |
| ta.mode()                                | Returns the mode given the source data.                                                      |
| ta.percentile_linear_interpolation()     | Returns the percentile of the data using linear interpolation.                               |
| ta.percentile_nearest_rank()             | Returns the percentile of the data using the nea                                             |
| ta.percentrank(n)                        | Returns the percentile rank based on the source within n bars.                               |
| ta.pivothigh()                           | Returns the highest high/low that preceded the current bar.                                  |
| ta.pivotlow()                            | Returns the lowest high/low that preceded the current bar.                                   |
| ta.range()                               | Returns the high to low range of the source.                                                 |
| ta.rising()                              | Returns true if the current bar’s close price is higher than the previous bar’s close price. |
| ta.stdev()                               | Returns the standard deviation of the source.                                                |
| ta.valuewhen()                           | Returns the source’s last value when a condition of a given length was true.                 |
| ta.variance()                            | Returns the variance for a given source                                                      |

## Pine Script “math” namespace for math-related functions and variables

| Function                      | Description                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------- |
| math.abs(number)              | Returns the absolute value of the number.                                               |
| math.acos(number)             | Returns the arc cosine of the number.                                                   |
| math.asin(number)             | Returns the arc sine of the number.                                                     |
| math.atan(number)             | Returns the arc tangent of the number.                                                  |
| math.avg()                    | Returns the average of the numbers.                                                     |
| math.ceil(number)             | Returns the ceiling of the number.                                                      |
| math.cos(angle)               | Returns the cosine of an angle.                                                         |
| math.exp(number)              | Returns the exponential of the number.                                                  |
| math.floor(number)            | Returns the floor of the number.                                                        |
| math.log(number)              | Returns the natural logarithm of a number.                                              |
| math.log10(number)            | Returns the base-10 logarithm of a number.                                              |
| math.max()                    | Returns the maximum of the numbers.                                                     |
| math.min()                    | Returns the minimum of the numbers.                                                     |
| math.pow()                    | Returns the value of the first number raised to the power of the second number.         |
| math.random()                 | Returns a random number between 0 and 1.                                                |
| math.round(number, precision) | Rounds the number to a given number of decimal places.                                  |
| math.round_to_mintick(number) | Rounds the number to the smallest increment allowed by the broker                       |
| math.sign(number)             | Returns a 1 for a postive number and a -1 for a negative number, or 0 for a zero number |
| math.sin(angle)               | Returns the sine of an angle.                                                           |
| math.sqrt(number)             | Returns the square root of a number.                                                    |
| math.sum()                    | Returns the sum of the numbers.                                                         |
| math.tan(angle)               | Returns the tangent of an angle.                                                        |
| math.todegrees()              | Converts an angle from radians to degrees.                                              |
| math.toradians()              | Converts an angle from degrees to radians.                                              |

## Pine Script “request” namespace for functions that request external data

| Function                                  | Description                                                                                |
| ----------------------------------------- | ------------------------------------------------------------------------------------------ |
| request.financial()                       | Requests financial data such as P/E ratio and market capitalization from an online source. |
| request.quandl()                          | Requests a dataset stored online using Quandl.                                             |
| request.security(<...>, timeframe, <...>) | Requests a certain security to be plotted on the chart.                                    |
| request.splits()                          | Requests stock splits data from an online source.                                          |
| request.dividends()                       | Requests dividend information from an online source.                                       |
| request.earnings()                        | Requests earnings data from an online source.                                              |

## Pine Script “ticker” namespace for functions that help create tickers

| Function             | Description                     |
| -------------------- | ------------------------------- |
| ticker.heikinashi()  | Creates a Heikin-Ashi ticker.   |
| ticker.kagi()        | Creates a Kagi chart.           |
| ticker.linebreak()   | Creates a Line Break chart.     |
| ticker.pointfigure() | Creates a Point & Figure chart. |
| ticker.renko()       | Creates a Renko chart.          |
| ticker.new()         | Creates a new ticker.           |

## Pine Script™ Arrays

Arrays allow you to store multiple values in a single variable. Each value in the array is identified by a unique index number. The first element in an array is always 0, the second element is 1, and so on.

| Function                                 | Description                                                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| array.abs ()                             | Returns the absolute value of each element in the array.                                                      |
| array.avg ()                             | Returns the average of the array elements.                                                                    |
| array.binary_search ()                   | Searches for a value in a sorted array and returns the index of the element that matches the value.           |
| array.binary_search_leftmost ()          | Searches for a value in a sorted array and returns the index of the leftmost element that matches the value.  |
| array.binary_search_rightmost ()         | Searches for a value in a sorted array and returns the index of the rightmost element that matches the value. |
| array.clear ()                           | Removes all elements from the array.                                                                          |
| array.concat ()                          | Concatenates two arrays.                                                                                      |
| array.copy ()                            | Copies the array.                                                                                             |
| array.covariance ()                      | Returns the covariance of the array elements.                                                                 |
| array.every ()                           | Tests whether all elements in the array pass the provided test function.                                      |
| array.fill ()                            | Fills the array with a value.                                                                                 |
| array.first ()                           | Returns the first element in the array.                                                                       |
| array.from ()                            | Creates an array from a list of values.                                                                       |
| array.get ()                             | Returns the element at the specified index.                                                                   |
| array.includes ()                        | Returns true if the array contains the specified value.                                                       |
| array.indexof ()                         | Returns the index of the first occurrence of a value in the array.                                            |
| array.insert ()                          | Inserts a new element at the specified index.                                                                 |
| array.join ()                            | Joins all elements of an array into a string.                                                                 |
| array.last ()                            | Returns the last element in the array.                                                                        |
| array.lastindexof ()                     | Returns the index of the last occurrence of a value in the array.                                             |
| array.max ()                             | Returns the maximum value in the array.                                                                       |
| array.median ()                          | Returns the median of the array elements.                                                                     |
| array.min ()                             | Returns the minimum value in the array.                                                                       |
| array.mode ()                            | Returns the mode of the array elements.                                                                       |
| array.new\<bool\>()                      | Creates a new array of booleans.                                                                              |
| array.new\<box\>()                       | Creates a new array of boxes.                                                                                 |
| array.new\<color\>()                     | Creates a new array of colors.                                                                                |
| array.new\<float\>()                     | Creates a new array of floats.                                                                                |
| array.new\<int\>()                       | Creates a new array of integers.                                                                              |
| array.new\<label\>()                     | Creates a new array of labels.                                                                                |
| array.new\<line\>()                      | Creates a new array of lines.                                                                                 |
| array.new\<linefill\>()                  | Creates a new array of linefills.                                                                             |
| array.new\<string\>()                    | Creates a new array of strings.                                                                               |
| array.new\<table\>()                     | Creates a new array of tables.                                                                                |
| array.new\<type\>()                      | Creates a new array of the specified type.                                                                    |
| array.percentile_linear_interpolation () | Returns the value at the given percentile using linear interpolation.                                         |
| array.percentile_nearest_rank ()         | Returns the value at the given percentile using the nearest rank method.                                      |
| array.percentrank ()                     | Returns the percentile rank of a value in the array.                                                          |
| array.pop ()                             | Removes the last element from the array and returns it.                                                       |
| array.push ()                            | Adds one or more elements to the end of the array and returns the new length of the array.                    |
| array.range ()                           | Creates a new array with a range of numbers.                                                                  |
| array.remove ()                          | Removes the element at the specified index from the array.                                                    |
| array.reverse ()                         | Reverses the order of the elements in the array.                                                              |
| array.set ()                             | Sets the element at the specified index.                                                                      |
| array.shift ()                           | Removes the first element from the array and returns it.                                                      |
| array.size ()                            | Returns the number of elements in the array.                                                                  |
| array.slice ()                           | Returns a section of the array.                                                                               |
| array.some ()                            | Tests whether at least one element in the array is true if bool, or if any value exists otherwise             |
| array.sort ()                            | Sorts the elements of an array in place.                                                                      |
| array.sort ()                            | Sorts the elements of the array.                                                                              |
| array.sort_indices ()                    | Returns a new array containing the indices of the original array's elements in sorted order.                  |
| array.splice ()                          | Adds and/or removes elements from the array.                                                                  |
| array.standardize ()                     | Standardizes the array elements by subtracting the mean and dividing by the standard deviation.               |
| array.stdev ()                           | Returns the standard deviation of the array elements.                                                         |
| array.sum ()                             | Returns the sum of the array elements.                                                                        |
| array.unshift ()                         | Adds one or more elements to the beginning of the array and returns the new length of the array.              |
| array.variance ()                        | Returns the variance of the array elements.                                                                   |

## Pine Script™ Colors

The following functions are available for colors.

| Function  | Description                                    |
| --------- | ---------------------------------------------- |
| color.a   | Returns the alpha component of the color.      |
| color.b   | Returns the blue component of the color.       |
| color.g   | Returns the green component of the color.      |
| color.r   | Returns the red component of the color.        |
| color.rgb | Returns a color from red, green, blue , transp |

## Pine Script™ Matrices

The following functions are available for matrices as functions and methods

| Function                | Description                                    |
| ----------------------- | ---------------------------------------------- |
| matrix.add_col          | Adds a column to a matrix                      |
| matrix.add_row          | Adds a row to a matrix                         |
| matrix.avg              | Returns the average of a matrix                |
| matrix.col              | Returns a column from a matrix                 |
| matrix.columns          | Returns the number of columns in a matrix      |
| matrix.concat           | Concatenates two matrices                      |
| matrix.copy             | Copies a matrix                                |
| matrix.det              | Returns the determinant of a matrix            |
| matrix.diff             | Returns the difference of a matrix             |
| matrix.eigenvalues      | Returns the eigenvalues of a matrix            |
| matrix.eigenvectors     | Returns the eigenvectors of a matrix           |
| matrix.elements_count   | Returns the number of elements in a matrix     |
| matrix.fill             | Fills a matrix with a value                    |
| matrix.get              | Returns the value of a matrix element          |
| matrix.inv              | Returns the inverse of a matrix                |
| matrix.is_antidiagonal  | Returns true if a matrix is antidiagonal       |
| matrix.is_antisymmetric | Returns true if a matrix is antisymmetric      |
| matrix.is_binary        | Returns true if a matrix is binary             |
| matrix.is_diagonal      | Returns true if a matrix is diagonal           |
| matrix.is_identity      | Returns true if a matrix is identity           |
| matrix.is_square        | Returns true if a matrix is square             |
| matrix.is_stochastic    | Returns true if a matrix is stochastic         |
| matrix.is_symmetric     | Returns true if a matrix is symmetric          |
| matrix.is_triangular    | Returns true if a matrix is triangular         |
| matrix.is_zero          | Returns true if a matrix is zero               |
| matrix.kron             | Returns the Kronecker product of two matrices  |
| matrix.max              | Returns the maximum value of a matrix          |
| matrix.median           | Returns the median of a matrix                 |
| matrix.min              | Returns the minimum value of a matrix          |
| matrix.mode             | Returns the mode of a matrix                   |
| matrix.mult             | Returns the product of two matrices            |
| matrix.new<type>        | Creates a new matrix                           |
| matrix.pinv             | Returns the pseudoinverse of a matrix          |
| matrix.pow              | Returns the power of a matrix                  |
| matrix.rank             | Returns the rank of a matrix                   |
| matrix.remove_col       | Removes a column from a matrix                 |
| matrix.remove_row       | Removes a row from a matrix                    |
| matrix.reshape          | Reshapes a matrix                              |
| matrix.reverse          | Reverses the order of the elements in a matrix |
| matrix.row              | Returns a row from a matrix                    |
| matrix.rows             | Returns the number of rows in a matrix         |
| matrix.set              | Sets the value of a matrix element             |
| matrix.sort             | Sorts the elements of a matrix                 |
| matrix.submatrix        | Returns a submatrix from a matrix              |
| matrix.sum              | Returns the sum of a matrix                    |
| matrix.swap_columns     | Swaps two columns in a matrix                  |
| matrix.swap_rows        | Swaps two rows in a matrix                     |
| matrix.trace            | Returns the trace of a matrix                  |
| matrix.transpose        | Returns the transpose of a matrix              |

## Python String Functions

The following functions are available for strings in Python.

| Function        | Description                                                                              |
| --------------- | ---------------------------------------------------------------------------------------- |
| str.contains    | Returns whether the string contains the specified substring.                             |
| str.endswith    | Returns whether the string ends with the specified substring.                            |
| str.format      | Formats the string by replacing specified placeholders with values.                      |
| str.format_time | Formats the string to represent a specified time.                                        |
| str.length      | Returns the length of the string.                                                        |
| str.lower       | Returns the string converted to lowercase.                                               |
| str.match       | Matches the string against a specified regular expression.                               |
| str.pos         | Returns the position of the first occurrence of a specified substring within the string. |
| str.replace     | Replaces occurrences of a specified value or pattern in the string with a new value.     |
| str.replace_all | Replaces all occurrences of a specified value or pattern in the string with a new value. |
| str.split       | Splits the string into a list of substrings based on a specified delimiter.              |
| str.startswith  | Returns whether the string starts with the specified substring.                          |
| str.substring   | Extracts a substring from the string based on specified start and end indices.           |
| str.tonumber    | Converts the string to a numerical value, if possible.                                   |
| str.tostring    | Converts the value to a string representation.                                           |
| str.upper       | Returns the string converted to uppercase.                                               |

## Pine Script™ Time

The following functions are available for time.

| Function         | Description                                        |
| ---------------- | -------------------------------------------------- |
| time.dayofmonth  | Returns the day of the month.                      |
| time.dayofweek   | Returns the day of the week.                       |
| time.dayofyear   | Returns the day of the year.                       |
| time.hour        | Returns the hour.                                  |
| time.isdst       | Returns whether daylight saving time is in effect. |
| time.millisecond | Returns the millisecond.                           |
| time.minute      | Returns the minute.                                |
| time.month       | Returns the month.                                 |
| time.second      | Returns the second.                                |
| time.timezone    | Returns the time zone.                             |
| time.tzoffset    | Returns the time zone offset.                      |
| time.year        | Returns the year.                                  |

# notes about pine script:

## Storage methods:

> Storage methods are methods that are used in type declarations.

> TYPE is a built in type, or a user defined type,
> identifier format is a letter or underscore followed by any number of letters, numbers, and underscores.

> the type might have a class name prefix, which is a letter or underscore followed by any number of letters, numbers, and underscores, followed by a '.'

### storage methods can be:

    TYPE
    TYPE []
    matrix<TYPE>
    array<TYPE>

## UDT - User defined types:

> The User Defined Types (UDTs) are the types that are defined in the source code, and are used in the function declarations.

    a UDT FIELD is a name, which is a letter or underscore followed by any number of letters, numbers, and underscores,

### A UDT is a User Defined Type that consists of:

- OPTIONAL annotations:

  - @type tag = description of the UDT
  - @field tag = name of field, description of a contained field

- Type declaration:

  - "export" keyword is optional (only for Library Scripts, no in strategy or indicator scripts)
  - "type" keyword is required
  - name of the UDT bbeing created

- Fields

  - fields of the UDT, each field is a storage method followed by a field name, and optional default value on [ string, boolean, int, float, color ] types.

  - each field consists of:

    - an indent exactly 1 level deep.
    - a storage declaration (see above, "Storage methods")
    - a field name, which cannor start with a number and can only contain letters, numbers, and underscores
    - `OPTIONAL` :
      - default value, which is "=" followed by a value of the type of the field

## FUNCTION declaration consists of:

- OPTIONAL annotations:

  - @function tag = description of the function
  - @param tag = name of parameer, optional storage method, description of a parameter
  - @return tag = description of the return value

- function declaration:

  - "export" keyword is optional on Library scripts, not Indicator or strategy.
  - "method" keyword is optional second keyword
  - NAME is a letter or underscore followed by any number of letters, numbers, and underscores
  - '(' PARAMS ')'

    - PARAMS is a comma separated list of PARAMS, and may be multiline where lines have an offset of 2 spaces
      - optional "series" or "simple"
      - optional storage method
      - NAME of parameter
      - optional default value, which is "=" followed by a value of the type of the field
        - DEFAULT only allowed if TYPE is specified
        - DEFAULT not permitted for array, matrix, or UDT type
        - PARAMS with default values must be at the end of the list

  - '=>'

    - denotes start of code

  - SINGLE_LINE_RETURN or NEW_LINE + INDENTED_BLOCK

    - SINGLE_LINE_RETURN is a single line of code
    - NEW_LINE + INDENTED_BLOCK is a block of code statements

## Annotations:

- Script:

  - for the script "library" declaration, the annotation is linked to the script itself.
  - it is also useful on "indicator" and "strategy" declarations, but not required.
  - the tag is "@description" for the script description
  - the tag is "@version=" for the pinescript version and mandatory

        Exaample:
        `@description this is a script`

- UDT (user defined type):
  for a udt (user defined type) declaration, the tag is "@type" and conttent is a description of the type.
  for udt fields, the tag is "@field" and the content is:

  - (req) name of the field
  - (opt) storage type of the field
  - (opt) a description of the field.

        Exaample:
        `@field myfield int this is my field`

- Function:

  - for function declaration, the tag is "@function" and the content is a description of the function. for any other function annotators, it is required

        Exaample:
        `@function this is my function`

  - for function parameters, the tag is "@param" and the content is a description of the parameter.

    - (req) name of the parameter
    - (opt) storage type of the parameter
    - (opt) a default value for the parameter.
    - (opt) a description of the parameter.

      Example:
      `@param myparam string  this is my parameter`
      `@param myparam matrix<lib.type> this is my parameter`

  - for function return values, the tag is "@returns" and the content is a description of the return value. - (opt) storage type of the return value - (opt) a description of the return value.

        Example:
        `@returns int this is my return value`

- variable declarations (optional)

  - for variable declarations, the tag is "@variable" and the content is a description of the variable.

        - (req) name of the variable
        - (opt) storage type of the variable
        - (opt) a description of the variable.

        Example:
        `@variable myvar int this is my variable`
        `@variable myvar matrix<implib.udtimp> this is my variable`
        `@variable myvar array<int> this is my variable`

# Statements:

Statements are commands that are used to execute actions or to assign values to variables.

- Assignment statement:

  - assigns a value to a variable
  - consists of a variable name, an assignment operator, and a value
  - the value can be a literal, a variable, or an expression

- Control statement:

  - used to control the flow of the program
  - consists of a keyword, followed by a condition, and a block of code

- Function call statement:

  - calls a function
  - consists of a function name, followed by a list of arguments

- the regex Pattern to capture a statement:

# summary of the declaration rules:

    User defined types:
        - a UDT must have a name
        - a UDT must have at least one field
        - a UDT field must have a name
        - a UDT field must have a type
        - a UDT field name cannot start with a number
        - a UDT field name can only contain letters, numbers, and underscores
        - a UDT field type can only be a TYPE or a TYPE[] or matrix<TYPE> or array<TYPE>
        - a UDT field name cannot be a storage type
        - a UDT field type can be the UDT itself in any of the above forms
        - a UDT field doed not require a default value
        - a UDT field with a UDT type  can not have a default value
        - a UDT definition ends after the fields when a newline begins with a character hat is no a commentt or whitespac

    user defined functions
        - a FUNCION must have a name
        - a FUNCTION may be a method
        - a FUNCTION wiht method must have the TYPE specified for fisrt parameter
        - a FUNCTION must have at least one parameter
        - a FUNCTION parameter must have a name
        - a FUNCTION parameter must have a type
        - a FUNCTION parameter name cannot start with a number
        - a FUNCTION parameter name can only contain letters, numbers, and underscores
        - a FUNCTION parameter type can only be a TYPE or a TYPE[] or matrix<TYPE> or array<TYPE>
        - a FUNCTION parameter name cannot be a storage type
        - a FUNCTION parameter type can be the UDT itself in any of the above forms
        - a FUNCTION parameter doed not require a default value
        - a FUNCTION parameter with a UDT type  can not have a default value
        - a FUNCTION definition ends after the return value when a newline begins with a character hat is no a commentt or whitespac

    annotations
        - annotations must start a line by themselves
        - annotations must start with '//' and a '@' character
        - annotations must be followed by a tag, which is a specified comment from the list here:
            - @description  - script description before  the "library" or "indicator" or "strategy"  script declaration witth a '('  and string  title first arg
            - @type     - description a UDT definition
            - @field    - description of a field in a UDT definition
            - @function - description of a function
            - @param    - description of a parameter
            - @return   - description of a return value
        - annotations of fields and parameters must be followed by the name, then description
        - annotations description is any text following until code on a new line or the next annotation.
        - annotations may include markdown formatting  on several lines, each starting with '//' after the @tag line

    comments
        - comments start with twwo slashes : '//'
        - comments may start a line or follow anything else
        - comments run from slash to line end, and end a line

    storage types

        - storage types can be:
            - TYPE
            - TYPE[]
            - matrix<TYPE>
            - array<TYPE>

        - storage types can not be:
            - TYPE[] []
            - matrix<TYPE> []
            - array<TYPE`enter code here`> []
            - matrix<TYPE> matrix<TYPE>
            - array<TYPE> matrix<TYPE>
            - matrix<TYPE> array<TYPE>
            - array<TYPE> array<TYPE>

    default values
        - values can be:
            - a number
            - a string
            - a boolean
            - na
            - a system variable
        - values cannot be:
            - a list of values
            - a function
            - a UDT
