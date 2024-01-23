-   [Introduction](https://www.tradingview.com/pine-script-docs/en/v5/language/User-defined_functions.html#introduction)
-   [Single-line functions](https://www.tradingview.com/pine-script-docs/en/v5/language/User-defined_functions.html#single-line-functions)
-   [Multi-line functions](https://www.tradingview.com/pine-script-docs/en/v5/language/User-defined_functions.html#multi-line-functions)
-   [Scopes in the script](https://www.tradingview.com/pine-script-docs/en/v5/language/User-defined_functions.html#scopes-in-the-script)
-   [Functions that return multiple results](https://www.tradingview.com/pine-script-docs/en/v5/language/User-defined_functions.html#functions-that-return-multiple-results)
-   [Limitations](https://www.tradingview.com/pine-script-docs/en/v5/language/User-defined_functions.html#limitations)

## [Introduction](https://www.tradingview.com/pine-script-docs/en/v5/language/User-defined_functions.html#id1)

User-defined functions are functions that you write, as opposed to the built-in functions in Pine Script™. They are useful to define calculations that you must do repetitevely, or that you want to isolate from your script’s main section of calculations. Think of user-defined functions as a way to extend the capabilities of Pine Script™, when no built-in function will do what you need.

You can write your functions in two ways:

-   In a single line, when they are simple, or
-   On multiple lines

Functions can be located in two places:

-   If a function is only used in one script, you can include it in the script where it is used. See our [Style guide](https://www.tradingview.com/pine-script-docs/en/v5/writing/Style_guide.html#pagestyleguide-functiondeclarations) for recommendations on where to place functions in your script.
-   You can create a Pine Script™ [library](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Libraries.html#pagelibraries) to include your functions, which makes them reusable in other scripts without having to copy their code. Distinct requirements exist for library functions. They are explained in the page on [libraries](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Libraries.html#pagelibraries).

Whether they use one line or multiple lines, user-defined functions have the following characteristics:

-   They cannot be embedded. All functions are defined in the script’s global scope.
-   They do not support recursion. It is **not allowed** for a function to call itself from within its own code.
-   The type of the value returned by a function is determined automatically and depends on the type of arguments used in each particular function call.
-   A function’s returned value is that of the last value in the function’s body.
-   Each instance of a function call in a script maintains its own, independent history.

## [Single-line functions](https://www.tradingview.com/pine-script-docs/en/v5/language/User-defined_functions.html#id2)

Simple functions can often be written in one line. This is the formal definition of single-line functions:

```
<span><span>&lt;</span><span>function_declaration</span><span>&gt;</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>&lt;</span><span>identifier</span><span>&gt;</span><span>(</span><span>&lt;</span><span>parameter_list</span><span>&gt;</span><span>)</span><span>&nbsp;</span><span>=&gt;</span><span>&nbsp;</span><span>&lt;</span><span>return_value</span><span>&gt;</span></span><br><span><span></span></span><br><span><span>&lt;</span><span>parameter_list</span><span>&gt;</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;{</span><span>&lt;</span><span>parameter_definition</span><span>&gt;</span><span>{</span><span>,</span><span>&nbsp;</span><span>&lt;</span><span>parameter_definition</span><span>&gt;</span><span>}}</span></span><br><span><span></span></span><br><span><span>&lt;</span><span>parameter_definition</span><span>&gt;</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>[</span><span>&lt;</span><span>identifier</span><span>&gt;</span><span>&nbsp;</span><span>=</span><span>&nbsp;</span><span>&lt;</span><span>default_value</span><span>&gt;</span><span>]</span></span><br><span><span></span></span><br><span><span>&lt;</span><span>return_value</span><span>&gt;</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>&lt;</span><span>statement</span><span>&gt;</span><span>&nbsp;</span><span>|</span><span>&nbsp;</span><span>&lt;</span><span>expression</span><span>&gt;</span><span>&nbsp;</span><span>|</span><span>&nbsp;</span><span>&lt;</span><span>tuple</span><span>&gt;</span></span><br><span><span></span></span><br>
```

Here is an example:

After the function `f()` has been declared, it’s possible to call it using different types of arguments:

```
<span><span>a</span><span>&nbsp;</span><span>=</span><span>&nbsp;</span><span>f</span><span>(</span><span>open</span><span>,</span><span>&nbsp;</span><span>close</span><span>)</span></span><br><span><span>b</span><span>&nbsp;</span><span>=</span><span>&nbsp;</span><span>f</span><span>(</span><span>2</span><span>,</span><span>&nbsp;</span><span>2</span><span>)</span></span><br><span><span>c</span><span>&nbsp;</span><span>=</span><span>&nbsp;</span><span>f</span><span>(</span><span>open</span><span>,</span><span>&nbsp;</span><span>2</span><span>)</span></span><br><span><span></span></span><br>
```

In the example above, the type of variable `a` is _series_ because the arguments are both _series_. The type of variable `b` is _integer_ because arguments are both _literal integers_. The type of variable `c` is _series_ because the addition of a _series_ and _literal integer_ produces a _series_ result.

## [Multi-line functions](https://www.tradingview.com/pine-script-docs/en/v5/language/User-defined_functions.html#id3)

Pine Script™ also supports multi-line functions with the following syntax:

```
<span><span>&lt;</span><span>identifier</span><span>&gt;</span><span>(</span><span>&lt;</span><span>parameter_list</span><span>&gt;</span><span>)</span><span>&nbsp;</span><span>=&gt;</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>&lt;</span><span>local_block</span><span>&gt;</span></span><br><span><span></span></span><br><span><span>&lt;</span><span>identifier</span><span>&gt;</span><span>(</span><span>&lt;</span><span>list</span><span>&nbsp;</span><span>of</span><span>&nbsp;</span><span>parameters</span><span>&gt;</span><span>)</span><span>&nbsp;</span><span>=&gt;</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>&lt;</span><span>variable</span><span>&nbsp;</span><span>declaration</span><span>&gt;</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;...</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>&lt;</span><span>variable</span><span>&nbsp;</span><span>declaration</span><span>&nbsp;</span><span>or</span><span>&nbsp;</span><span>expression</span><span>&gt;</span></span><br><span><span></span></span><br>
```

where:

```
<span><span>&lt;</span><span>parameter_list</span><span>&gt;</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;{</span><span>&lt;</span><span>parameter_definition</span><span>&gt;</span><span>{</span><span>,</span><span>&nbsp;</span><span>&lt;</span><span>parameter_definition</span><span>&gt;</span><span>}}</span></span><br><span><span></span></span><br><span><span>&lt;</span><span>parameter_definition</span><span>&gt;</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>[</span><span>&lt;</span><span>identifier</span><span>&gt;</span><span>&nbsp;</span><span>=</span><span>&nbsp;</span><span>&lt;</span><span>default_value</span><span>&gt;</span><span>]</span></span><br><span><span></span></span><br>
```

The body of a multi-line function consists of several statements. Each statement is placed on a separate line and must be preceded by 1 indentation (4 spaces or 1 tab). The indentation before the statement indicates that it is a part of the body of the function and not part of the script’s global scope. After the function’s code, the first statement without an indent indicates the body of the function has ended.

Either an expression or a declared variable should be the last statement of the function’s body. The result of this expression (or variable) will be the result of the function’s call. For example:

```
<span><span>geom_average</span><span>(</span><span>x</span><span>,</span><span>&nbsp;</span><span>y</span><span>)</span><span>&nbsp;</span><span>=&gt;</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>a</span><span>&nbsp;</span><span>=</span><span>&nbsp;</span><span>x</span><span>*</span><span>x</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>b</span><span>&nbsp;</span><span>=</span><span>&nbsp;</span><span>y</span><span>*</span><span>y</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>math.sqrt</span><span>(</span><span>a</span><span>&nbsp;</span><span>+</span><span>&nbsp;</span><span>b</span><span>)</span></span><br><span><span></span></span><br>
```

The function `geom_average` has two arguments and creates two variables in the body: `a` and `b`. The last statement calls the function `math.sqrt` (an extraction of the square root). The `geom_average` call will return the value of the last expression: `(math.sqrt(a + b))`.

## [Scopes in the script](https://www.tradingview.com/pine-script-docs/en/v5/language/User-defined_functions.html#id4)

Variables declared outside the body of a function or of other local blocks belong to the _global_ scope. User-declared and built-in functions, as well as built-in variables also belong to the global scope.

Each function has its own _local_ scope. All the variables declared within the function, as well as the function’s arguments, belong to the scope of that function, meaning that it is impossible to reference them from outside — e.g., from the global scope or the local scope of another function.

On the other hand, since it is possible to refer to any variable or function declared in the global scope from the scope of a function (except for self-referencing recursive calls), one can say that the local scope is embedded into the global scope.

In Pine Script™, nested functions are not allowed, i.e., one cannot declare a function inside another one. All user functions are declared in the global scope. Local scopes cannot intersect with each other.

## [Functions that return multiple results](https://www.tradingview.com/pine-script-docs/en/v5/language/User-defined_functions.html#id5)

In most cases a function returns only one result, but it is possible to return a list of results (a _tuple_\-like result):

```
<span><span>fun</span><span>(</span><span>x</span><span>,</span><span>&nbsp;</span><span>y</span><span>)</span><span>&nbsp;</span><span>=&gt;</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>a</span><span>&nbsp;</span><span>=</span><span>&nbsp;</span><span>x</span><span>+</span><span>y</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>b</span><span>&nbsp;</span><span>=</span><span>&nbsp;</span><span>x</span><span>-</span><span>y</span></span><br><span><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span>[</span><span>a</span><span>,</span><span>&nbsp;</span><span>b</span><span>]</span></span><br><span><span></span></span><br>
```

Special syntax is required for calling such functions:

```
<span><span>[</span><span>res0</span><span>,</span><span>&nbsp;</span><span>res1</span><span>]</span><span>&nbsp;</span><span>=</span><span>&nbsp;</span><span>fun</span><span>(</span><span>open</span><span>,</span><span>&nbsp;</span><span>close</span><span>)</span></span><br><span><span>plot</span><span>(</span><span>res0</span><span>)</span></span><br><span><span>plot</span><span>(</span><span>res1</span><span>)</span></span><br><span><span></span></span><br>
```

## [Limitations](https://www.tradingview.com/pine-script-docs/en/v5/language/User-defined_functions.html#id6)

User-defined functions can use any of the Pine Script™ built-ins, except: [barcolor()](https://www.tradingview.com/pine-script-reference/v5/#fun_barcolor), [fill()](https://www.tradingview.com/pine-script-reference/v5/#fun_fill), [hline()](https://www.tradingview.com/pine-script-reference/v5/#fun_hline), [indicator()](https://www.tradingview.com/pine-script-reference/v5/#fun_indicator), [library()](https://www.tradingview.com/pine-script-reference/v5/#fun_library), [plot()](https://www.tradingview.com/pine-script-reference/v5/#fun_plot), [plotbar()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotbar), [plotcandle()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotcandle), [plotchar()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotchar), [plotshape()](https://www.tradingview.com/pine-script-reference/v5/#fun_plotshape) and [strategy()](https://www.tradingview.com/pine-script-reference/v5/#fun_strategy).

[

![../_images/TradingView_Logo_Block.svg](https://www.tradingview.com/pine-script-docs/en/v5/_images/TradingView_Logo_Block.svg)

](https://www.tradingview.com/)