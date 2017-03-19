---
title: random-sample - Clojure Standard Library
updated: 2017-02-01 20:05
---

For a quick intro to this series of blog posts check out <a target="_blank" href="https://steven-cutting.github.io/notes/clojure-std-lib-intro">*Clojure Standard Library - Intro*</a>. It includes a lot of useful info, including notes about presentation of examples and more.

---



### This posts function:


<p style="font-size:4em; font-family:monospace; text-align:center;">random-sample</p>



## Quick Overview


### Description


<a target="_blank" href="http://clojuredocs.org/clojure.core/random-sample">**`clojure.core/random-sample`**</a> is a function that can be used to take a random sample of a collection. It samples without replacement and considers each element within the collection independently.


### Examples

```clojure
(random-sample 0.5 [0 1 2 3 4 5 6 7 8 9 10])
; => (0 4 6)
(random-sample 0.5 (range 11))
; => (2 4 7 8 9)
(random-sample 1/10 (range 30))
; => (2 11 16 21)
```

*<b>Note:</b> With most of the examples, if you run them yourself, your output will likely be different. `random-sample` is <a target="_blank" href="https://en.wikipedia.org/wiki/Nondeterministic_algorithm">nondeterministic</a>.*



---


## How To Use


### Parameters and Return Values


`random-sample` is a <a target="_blank" href="http://www.braveclojure.com/do-things/#Parameters_and_Arity">multiple-arity function</a>, which means that it uses <a target="_blank" href="https://en.wikipedia.org/wiki/Function_overloading">*arity overloading*</a> in order to provide different behavior based on the number of arguments provided. `random-sample` accepts one or two arguments.

+ **One Argument:** `(random-sample prob)`

    Providing only `prob` (probability), returns a <a target="_blank" href="http://clojure.org/reference/transducers">transducer</a>; this is not the same as <a target="_blank" href="https://en.wikipedia.org/wiki/Partial_application">partial application</a> or <a target="_blank" href="https://en.wikipedia.org/wiki/Currying">currying</a>. `prob` can be any type of number (e.g. integer, float, ratio, etc.), or anything else that <a target="_blank" href="http://clojuredocs.org/clojure.core/%3C">`<`</a> can compare to a float. Note that only numbers between 0 and 1 make sense; providing 0 (or smaller) results in no items being selected and 1 (or greater) results in all items being selected.
    
    `random-sample` considers each item in the collection individually, so `prob` is the probability that any given item will be returned.

    Ex: 

```clojure
;; -- Transducer Examples --

;; Creat a transducer that selects items 50% of the time
;; and bind it to sample-about-half.
(def sample-about-half (random-sample 0.5))
; => #'user/sample-about-half

;; Use sample-about-half to sample items from a collection
;; of 20 integers.
(into [] sample-about-half (range 20))
; => [1 9 10 11 12 13 15 19] ;; Notice that only 8 items
                             ;; are selected from the
                             ;; population of 20 items.

;; Calculating the sums of random samples from a collection
;; of numbers 0 through 19.
(transduce sample-about-half + 0 (range 20))
; => 108
(transduce sample-about-half + 0 (range 20))
; => 67
```

+ **Two Arguments:** `(random-sample prob coll)`

    Providing both `prob` and a collection (`coll`), returns a <a target="_blank" href="http://clojure.org/reference/sequences">lazy sequence</a> of items randomly selected from `coll` without replacement. Each item in `coll` is 'considered' independently from the other items, to better understand this check out the break down of the source code in the **Expanded Description** section below.

    Ex:

```clojure
;; Randomly Selecting items from a collection of numbers 0
;; through 19, with prob = 0.5.
(random-sample 0.5 (range 20))
; => (0 4 6 7 8 11 15 17 18 19)
(random-sample 0.5 (range 20))
; => (0 6 8 9 11 12 14 17)  ;; Notice how both the items
                            ;; selected and the size of the
                            ;; sample are different even
                            ;; though the arguments are the
                            ;; same.

;; This is the same as supplying 0.5 for prob.
(random-sample 1/2 (range 20))
; => (0 3 5 8 10 11 14 16 17 18 19)

;; Out of 100,000 random samples, with prob set to 0.01,
;; from populations of 20 items about how many samples will
;; be non-empty. Refer to the footnote below for more info
;; on the functions used.
(count (filter not-empty
               (repeatedly 100000
                           #(random-sample 0.01 (range 20)))))
; => 18223
(count (filter not-empty
               (repeatedly 100000
                           #(random-sample 0.01 (range 20)))))
; => 18241
;; About 18.2% of the samples will be non-empty.

;; Ex: prob >= 1
(random-sample 1 (range 20))
; => (0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19)
(random-sample 20 (range 20))
; => (0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19)

;; Ex: prob <= 0
(random-sample 0 (range 20))
; => ()  ;; Returns an empty collection.
(random-sample -200 (range 20))
; => ()
(random-sample -0.5 (range 20))
; => ()
```
[^0]

[^0]: Check out posts on: <a target="_blank" href="/notes/clojure-std-lib-count">`count`</a>, <a target="_blank" href="/notes/clojure-std-lib-filter">`filter`</a>, <a target="_blank" href="/notes/clojure-std-lib-not-empty">`not-empty`</a>, <a target="_blank" href="/notes/clojure-std-lib-range">`range`</a> and <a target="_blank" href="/notes/clojure-std-lib-repeatedly">`repeatedly`</a>



---


## Expanded Description


### Examining Simplified Source Code

Below is a simplified version of the source code for `random-sample`. This simplified version is called `smpl-random-sample`. The main difference between the original and `smpl-random-sample`, is that I have changed it from being a multiple-arity function to a **two-arity funcion**. This means that it no longer accepts a variable number of arguments. It requires both `prob` and `coll` and it behaves identically to `random-sample` when both `prob` and `coll` are provided. I made this change in order reduce the number of concepts involved and to make it easier to understand. [^1]

[^1]: For the most up to date version of the actual source code click on the source code link in this page for <a target="_blank" href="http://clojuredocs.org/clojure.core/random-sample">random-sample</a>


```clojure
(defn smpl-random-sample                   ; Name
  "Simplified version of random-sample."   ; Doc String
  [prob coll]                              ; Parameters 
  (filter (fn [_] (< (rand) prob)) coll))  ; Function Body
```


#### Breaking It Down:

There are Two main parts to the body of this function, the  **Filter Expression** and the **Predicate function**.

```clojure
(filter                     ; Filter Expression
  (fn [_] (< (rand) prob))  ; Predicate Function
  coll)                     ; End of Filter Expression
```

##### **Predicate Function:** `(fn [_] (< (rand) prob))`

The predicate function used is an <a target="_blank" href="https://clojuredocs.org/clojure.core/fn">anonymous function</a> -- it's like any other function
    except that it has not been bound to a name.

Looking at the body of the predicate function you see the mechanism that is the heart of the `random-sample` function. `(< (rand) prob)`, this expression returns true when the random number, produced by <a target="_blank" href="/notes/clojure-std-lib-rand">`rand`</a>, is less than `prob` -- remember `prob` is the probability supplied to random-sample that represents the chance that any individual item will be selected. Because `rand` returns a number between 0 (inclusive) and 1 (exclusive), any number supplied for `prob` that is less than 0 is effectively 0 and any number greater than 1 is effectively 1.

Here is an example that should help to provide a better understanding of how the `(< (rand) prob)` expression works.:

```clojure
(def r (rand))           ; Bind a random float to the name "r".
; => #'user/r
r                        ; Check the value bound to "r". 
; => 0.6482491474337703
(def prob 0.5)           ; Bind the value 0.5 to the name "prob".
; => #'user/prob
(< r prob)               ; Test if "r" is smaller than "prob".
; => false
```

For more information about `rand` and how it affects which items are selected check out the section "More About `rand` And Randomness" below.


##### **Filter Expression:** `(filter predicate-function coll)`

The filter expression uses the function <a target="_blank" href="/notes/clojure-std-lib-filter">`filter`</a> which iterates over the collection `coll`, calling the predicate function on each item. When the predicate function returns 'true' the item is included in the output, if it returns 'false' the item is not included -- it is 'filtered' out.



### More About `rand` And Randomness

The <a target="_blank" href="https://en.wikipedia.org/wiki/Pseudorandomness">pseudorandom</a> number generator used by `rand` approximates a <a target="_blank" href="https://en.wikipedia.org/wiki/Uniform_distribution_(continuous)">Uniform Distribution</a> (UD) and `rand` only produces numbers between 0 and 1. [^3] With `rand` following a UD, each number between 0 and 1 has the same probability of being returned. As a result there is a 50% chance that a number produced by `rand` will be less than 0.5, because 50% of numbers that could be chosen are less than 0.5 and they are all equiprobable. The same is true for other values, e.g. 20% less than 0.2, 60% less than 0.6, etc..


[^3]: For even more information about `rand` check out my other post that covers it in more detail: <a target="_blank" href="/notes/clojure-std-lib-rand">rand - Clojure Standard Library</a>.


How does this effect the behavior of `random-sample`? Each item is considered independently so, this process can not make any guarantees as to the number of items that will ultimately be sampled form `col`. The only guarantee is that each item will have a probability of being chosen equal to `prob`.

Because the random numbers used are sampled from a UD, as the size of the population increases the distribution of the sample sizes (as a percentage of the population) produced will become increasingly normally distributed with a mean equal to `prob`.[^4] This behavior is clearly shown in the plots below.

[^4]: This process is described by the <a target="_blank" href="https://en.wikipedia.org/wiki/Central_limit_theorem">Central Limit Theorem</a>. 

The plots below show the distributions of samples sizes (as a percentage of the population) produced by `random-sample` with `prob` set to 0.1. All of the plots were produced using 100,000 samples but, each one shows samples taken from a different population size. The top plot shows samples taken from a population of 100, the middle a population of 500 and the bottom a population of 1,000. [^5]

[^5]: The data for the plots was produced using this code: <a target="_blank" href="https://s3-us-west-2.amazonaws.com/steven-cutting-blog-assets/clojure-std-library/random-sample/1d6a0341fdfc_mk_samples.html">code</a>

In the plots, the vertical bars show a histogram of the samples, the blue curve shows the probability density function estimated using <a target="_blank" href="https://en.wikipedia.org/wiki/Kernel_density_estimation">Kernel Density Estimation</a> and the black curve is a normal distribution used for comparison.

!<a target="_blank" href="https://s3-us-west-2.amazonaws.com/steven-cutting-blog-assets/clojure-std-library/random-sample/85b1d9edbdf9-random-sample-plots.png">Distributions Of Sample Sizes With 'prob' Set To 0.1</a>

What all of this ends up meaning is that, the larger the size of `col` (the population) the more likely it is that the resulting sample will be a percentage of `col` that is equal to `prob`. So the larger the collection is the more accurately you will be able to target a specific sample size. *<b>Note</b> that there are better methods for sampling large populations (e.g. <a target="_blank" href="https://en.wikipedia.org/wiki/Reservoir_sampling">Reservoir Sampling</a>) but, `random-sample` can still prove to be useful when the sample size does not need to be exact.*




---


## Example Use Case


A possible use case might be to use `random-sample` to create a random sample of an incoming stream of data of unknown size. This can be especially useful if you want to perform some kind of analysis of a live data stream and you can not handle all of the data at the rate it is steaming in -- you want to turn the fire hose into a plain garden hose. 

Ex:

```clojure
;; Create a stream of 1 million integers.
(def big-stream (range 1000000))  
; => #'user/big-stream

;; Create a sample of big-stream; each item has a
;; probability of being chosen equal to 0.1.
(def sample (random-sample 0.1 big-stream))  
; => #'user/sample

;; Filter the items in sample using some expensive
;; predicate, to find out which items fit some category.
(def fit-category (filter expensive-calculation sample))

;; Find out the percentage of items that fit in some
;; category.
(def percent-that-fit-category (/ (count fit-category)
                                  (count sample)))

;; The output of this can be used to estimate the percentage
;; of the population that would fit in some category.
```



---

Copyright (C) 2017 Steven Cutting - <a target="_blank" href="/about#license">License</a>
