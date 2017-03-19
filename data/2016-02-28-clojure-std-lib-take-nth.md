---
title: take-nth - Clojure Standard Library
updated: 2016-02-29 16:18
---

For a quick intro to this series of blog posts check out [*Clojure Standard Library - Intro*](/notes/clojure-std-lib-intro). It includes a lot of useful info, including notes about presentation of examples and more.

---

### This posts function:
<p style="font-size:4em; font-family:monospace; text-align:center;">take-nth</p>


## Quick Overview

### Description

[**`clojure.core/take-nth`**](http://clojuredocs.org/clojure.core/take-nth) is a function that accepts a collection and returns every nth item in that collection.


### Example

In this example I am going to use `take-nth` to get every third number from a collection that contains numbers 0 up to 20 (exclusive). The collection of numbers will be generated using [`range`](/notes/clojure-std-lib-range) 

```clojure
(take-nth 3 (range 20))
; => (0 3 6 9 12 15 18)  ; Every third number from range(20).
```


## How To Use

### Parameters and Return Values

`take-nth` is a [multiple arity function](http://www.braveclojure.com/do-things/#Defining_Functions) and uses [*arity overloading*](https://en.wikipedia.org/wiki/Function_overloading) in order to provide different behavior based on the number of arguments you provide. `take-nth` takes one to two arguments.

+ `(take-nth n)`
    Providing only `n`, returns a stateful [transducer](http://clojure.org/reference/transducers).

+ `(take-nth n coll)`
    Providing both `n` and a collection (`coll`), returns a [lazy sequence](http://clojure.org/reference/sequences) that contains every nth item from `coll`.

***Note:*** *Non-positive integers and zero return an infinite lazy sequence of zeros.* [^1]

## Example Use Cases


One possible use might be to use take-nth to do a quick, naive downsample of a stream of data. If in the stream, items close together are likely to contain similar information or, if it is already random. 

Ex: [^2]

```clojure
(def random-stream (repeatedly #(rand-int 20)))  ; Created an infinite stream of random integers
; => #'user/random-stream
(def sample (take-nth 20 random-stream))  ; Created a sample of random-stream; contains every 20th integer.
; => #'user/sample
(take 10 sample)
; => (19 14 5 3 12 10 13 15 2 14)  ; The first ten items from sample.
```


[^1]: http://clojuredocs.org/clojure.core/take-nth#example-555dfc57e4b03e2132e7d169

[^2]: Checkout posts on [`repeatedly`](/notes/clojure-std-lib-repeatedly), [`rand-int`](/notes/clojure-std-lib-rand-int) and [`take`](/notes/clojure-std-lib-take).
