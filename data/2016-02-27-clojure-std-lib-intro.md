---
title: Intro - Clojure Standard Library
updated: 2016-02-27 15:08
---


## What and Why?


This is the intro post for a (maybe) long term series of posts I plan on doing about the [**Clojure Standard Library (CSL)**](http://clojure.org/api/cheatsheet). There will be a post for each function within the CSL.


The main reason I am doing this is that for a while I've wanted to start blogging, but each time I tried I would end up giving up because I kept picking topics that were large and complex. I hope that this approach, of writing a bunch of small and simple posts will help me to get in the habit of blogging and will help improve my ability to express complex ideas through writing. This should also help me to further learn Clojure.

Also, I hope my posts will be useful to someone else and they will help provide simple/unique examples of ways to use the functions in the CSL, or that they might be useful examples to others that are just starting out with their own blog.

## Extra Info

Throughout this series of posts I will keep updating this one with meta information that is relevant across all post.

### Running the Examples

If you do not want install Clojure just yet, you can try out the examples using [**Try Clojure**](http://www.tryclj.com/). It's an awesome little web app that allows you to try out Clojure using a repl in your browser. Being that these blog posts will be about functions from the CSL, all of these examples *should* work just fine in Try Clojure. I will, however, only be testing the examples using a local install of Clojure (using the [Leiningen repl](http://clojure.org/guides/getting_started)), so I do not guarantee that they will work with Try Clojure.

### Presentation Of Examples

**Comments:**
Anything within a code field that starts with a semicolon is a comment (is not code).
Ex:

```clojure
; This is a comment.
```

**Code Examples:**
The code will be presented in the same style as in [*Clojure for the Brave and True*](http://www.braveclojure.com/getting-started/).
Ex:

```clojure
(take-nth 3 (range 20))  ; This is the code.
; => (0 3 6 9 12 15 18)  ; This is the output.
```
