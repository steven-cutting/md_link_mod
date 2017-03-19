---
title: rand-int - Clojure Standard Library
updated: 2016-03-07 16:28
---

For a quick intro to this series of blog posts check out [*Clojure Standard Library - Intro*](/notes/clojure-std-lib-intro). It includes a lot of useful info, including notes about presentation of examples and more.

---

### This posts function:
<p style="font-size:4em; font-family:monospace; text-align:center;">rand-int</p>


## Quick Overview

### Description

[**`clojure.core/rand-int`**](http://clojuredocs.org/clojure.core/rand-int) returns a random integer between 0 and **n** (exclusive).


### Example

```clojure
(rand-int 10)
; => 2
(rand-int 30)
; => 26
```

## How To Use

### Parameters and Return Values

`rand-int` is a [1-arity function](http://www.braveclojure.com/do-things/#Defining_Functions) -- it accepts only one parameter that has no default value (it is mandatory).

`(rand-int n)` - **n** is the max value (exclusive) and can be any number (e.g. integer, ratio, float).

Ex:

```clojure
(rand-int 5000)
; => 3648
(rand-int 10.5)
; => 6
(rand-int 10/3)
; => 2
(rand-int 100/3)
; => 30
```
