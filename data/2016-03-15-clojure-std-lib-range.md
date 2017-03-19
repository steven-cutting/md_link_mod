---
title: range - Clojure Standard Library
updated: 2016-03-15 11:07
---

For a quick intro to this series of blog posts check out [*Clojure Standard Library - Intro*](/notes/clojure-std-lib-intro). It includes a lot of useful info, including notes about presentation of examples and more.

---

### This posts function:
<p style="font-size:4em; font-family:monospace; text-align:center;">range</p>


## Quick Overview

### Description

[**`clojure.core/range`**](http://clojuredocs.org/clojure.core/range) is a function that returns a [lazy sequence](http://clojure.org/reference/sequences) of numbers. The sequence is constructed using the parameters provided.


### Example

```clojure
(range 10)
; => (0 1 2 3 4 5 6 7 8 9)
```

Here I have passed `range` the integer `10`, and `range` returned a list of numbers 0 through 10.

## How To Use

### Parameters and Return Values

`range` has three parameters that all have default values. Each parameter accepts a number, which can be an integer or a float and can also be negative.

| Parameter | Default | Description |
| -- | -- | -: |
| **start** | 0 | The starting value - inclusive |
| **end** | infinity | The last value - exclusive |
| **step** | 1 | n<sub>1</sub> + step = n<sub>2</sub> |


#### Parameter Structure

`range` is a [multiple arity function](http://www.braveclojure.com/do-things/#Defining_Functions) -- it accepts a variable number of parameters, up to three. It behaves differently based on the number of parameters ([*arity overloading*](https://en.wikipedia.org/wiki/Function_overloading)).


+ `(range)`
    When given zero parameters, range returns an infinite [lazy sequence](http://clojure.org/reference/sequences) of every integer from 0 to infinity. The reason is that (as seen above) the default values for **start**, **end** and **step** are 0, infinity and 1.

    Ex: [^1]

```clojure
(take 10 (range))
; => (0 1 2 3 4 5 6 7 8 9)
(take 20 (range))
; => (0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19)
(take 30 (range))
; => (0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29)
```

+ `(range end)` 
    If only one number is given then it will be used as the **end** value. (start=0, step=1)
    
    Ex:

```clojure
(range 10)
; => (0 1 2 3 4 5 6 7 8 9)
(range 10.001)
; => (0 1 2 3 4 5 6 7 8 9 10)
```

+ `(range start end)`
    If two numbers are given then the first one will be used for **start** and the second for **end**. (step=1) If **start** is equal to **end**, `range` will return an empty list.
 
    Ex:

```clojure
(range 0 10)
; => (0 1 2 3 4 5 6 7 8 9)
(range 200 200)
; => ()
(range 0.5 10.5)
; => (0.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 9.5)
(range 0 -10)
; => ()
(range -15 -10)
; => (-15 -14 -13 -12 -11)
(range -15 0)
; => (-15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1)
(range -15.5 0)
; => (-15.5 -14.5 -13.5 -12.5 -11.5 -10.5 -9.5 -8.5 -7.5 -6.5 -5.5 -4.5 -3.5 -2.5 -1.5 -0.5)
```

+ `(range start end step)`
    When given three numbers, the first one is used for **start**, second for **end** and the third for **step**.
 
    Ex:

```clojure
(range 0 10 1)
; => (0 1 2 3 4 5 6 7 8 9)
(range 0 10 0.5)
; => (0 0.5 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0 6.5 7.0 7.5 8.0 8.5 9.0 9.5)
(range 0 -10 -1)
; => (0 -1 -2 -3 -4 -5 -6 -7 -8 -9)
```

<!--
## Example Use Cases

Consider adding this section later.
-->


[^1]: Checkout post on [`take`](/notes/take).
