__title__ = 'md_link_mod'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.e.cutting@linux.com'
__created_on__ = '03/03/2017'
__copyright__ = "md_link_mod Copyright (C) 2017  Steven Cutting"

import pytest

import md_link_mod.link_mod as mlm


EXMPLS = [
"[*Clojure Standard Library - Intro*](https://steven-cutting.github.io/notes/clojure-std-lib-intro)",
"[**`clojure.core/rand`**](http://clojuredocs.org/clojure.core/rand) returns a random floating point number between 0 and **n**. **n** defaults to 1. The floor (0) is inclusive, the ceiling (n)",
"[multiple-arity function](http://www.braveclojure.com/do-things/#Parameters_and_Arity) -- it can handle up to two parameters. It behaves differently based on the number of parameters [(arity overloading)](https://en.wikipedia.org/wiki/Function_overloading)",
"[^1]: For the most up to date version of the actual source code click on the source code link in this page for [range](http://clojuredocs.org/clojure.core/rand)",
"[`Math`](https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html)",
"[`random`](https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html#random--)",
"[Uniform Distribution](https://en.wikipedia.org/wiki/Uniform_distribution_(continuous\)) (UD). The below plot shows a histogram of a sample of 100,000 numbers (floats between 0.0 and 1.0) produced using `rand` (blue bars) and a perfect UD (black line). The plot does a decent job of showing how the random number generator only approximates a UD. If it produced a perfect UD then the bars of the histogram would all align at 1.0, and they would perfectly fit the area under the UD curve (black line)",
"[`rand` Histogram With Uniform Distribution](https://s3-us-west-2.amazonaws.com/steven-cutting-blog-assets/clojure-std-library/rand/daa5955e20dc-rand-hist-with-uniform-dist.png)",
"[Linear congruential generator](https://en.wikipedia.org/wiki/Linear_congruential_generator) and the Java docs for the class [`Random`](https://docs.oracle.com/javase/7/docs/api/java/util/Random.html)",
"[`generators/double` Histogram With Uniform Distribution](https://s3-us-west-2.amazonaws.com/steven-cutting-blog-assets/clojure-std-library/rand/23c26b71bb69-gens-double-hist-with-uniform-dist.png)",
"[License](/about#license)",
]

EXPCTD = [[("*Clojure Standard Library - Intro*",
            "https://steven-cutting.github.io/notes/clojure-std-lib-intro")],
          [("**`clojure.core/rand`**",
            "http://clojuredocs.org/clojure.core/rand")],
          [("multiple-arity function",
            "http://www.braveclojure.com/do-things/#Parameters_and_Arity"),
           ("(arity overloading)",
            "https://en.wikipedia.org/wiki/Function_overloading"),
           ],
          [("range",
            "http://clojuredocs.org/clojure.core/rand")],
          [("`Math`",
            "https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html")],
          [("`random`",
            "https://docs.oracle.com/javase/8/docs/api/java/lang/" +
            "Math.html#random--")],
          [("Uniform Distribution",
            "https://en.wikipedia.org/wiki/" +
            "Uniform_distribution_(continuous\\)")],
          [("`rand` Histogram With Uniform Distribution",
            "https://s3-us-west-2.amazonaws.com/steven-cutting-blog-assets/" +
            "clojure-std-library/rand/daa5955e20dc-rand-hist-with" +
            "-uniform-dist.png")],
          [("Linear congruential generator",
            "https://en.wikipedia.org/wiki/Linear_congruential_generator"),
           ("`Random`",
            "https://docs.oracle.com/javase/7/docs/api/java/util/Random.html"),
           ],
          [("`generators/double` Histogram With Uniform Distribution",
            "https://s3-us-west-2.amazonaws.com/steven-cutting-blog-assets/" +
            "clojure-std-library/rand/23c26b71bb69-gens-double-hist-" +
            "with-uniform-dist.png")],
          [("License", "/about#license")],
          ]


def rm_spaces(txt): return txt.replace(" ", "")


@pytest.mark.parametrize("txt,expected",
                         [("(derp\)", "(derp)"),
                          (r"https://en.wikipedia.org/wiki/Uniform_" +
                           r"distribution_(continuous\)",
                           r"https://en.wikipedia.org/wiki/Uniform_" +
                           r"distribution_(continuous)"),
                          ])
def test__rm_link_paren_esc(txt, expected):
    assert(mlm.rm_link_paren_esc(txt) == expected)


@pytest.mark.parametrize("txt,expected",
                         zip(EXMPLS, EXPCTD))
def test__parse_links(txt, expected):
    assert(mlm.parse_links(txt) == expected)


@pytest.mark.parametrize("txt,link,expected",
                         [("t", "l", "[t](l)"),
                          ])
def test__build_md_link(txt, link, expected):
    assert(mlm.build_md_link(txt, link) == expected)


@pytest.mark.parametrize("txt,link,other_browser,expected",
                         [("t", "l", True,
                           """<a target="_blank" href="l">t</a>"""),
                          ("t", "l", False,
                           """<a href="l">t</a>"""),
                          ])
def test__build_html_link(txt, link, other_browser, expected):
    assert(rm_spaces(mlm.build_html_link(txt, link, other_browser)) ==
           rm_spaces(expected))


@pytest.mark.parametrize("txt,other_browser,expected",
                         [("derp ferp (f) [t](l).", True,
                           """derp ferp (f) <a target="_blank" href="l">t</a>."""),
                          ("derp ferp (f) [t](l).", False,
                           """derp ferp (f) <a href="l">t</a>."""),
                          ("[derp](ferp) (f) [t](l).", False,
                           """<a href="ferp">derp</a> (f) <a href="l">t</a>."""),
                          ("[Uniform Distribution](https://en.wikipedia.org/wiki/Uniform_" +
                           "distribution_(continuous\)) (UD).",
                           False,
                           """<a href="https://en.wikipedia.org/wiki/Uniform_distribution_""" +
                           """(continuous)">Uniform Distribution</a> (UD)."""),
                          ])
def test__md_link_to_html(txt, other_browser, expected):
    assert(rm_spaces(mlm.md_link_to_html(txt, other_browser)) ==
           rm_spaces(expected))
