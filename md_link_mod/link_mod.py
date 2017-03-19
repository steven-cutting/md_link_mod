__title__ = 'md_link_mod'
__author__ = 'Steven Cutting'
__author_email__ = 'steven.e.cutting@linux.com'
__created_on__ = '03/03/2017'
__copyright__ = "md_link_mod Copyright (C) 2017  Steven Cutting"
__doc__ = """
Only deals with Markdown formated links.
"""


import re
import toolz as tlz
import toolz.curried as ctlz

# Anything that isn't a square closing bracket
_name_regex = r"[^]]+"

# matches the url portion of the md link. Should work on [exp](/some/link/path)
_url_regex = r".+?(\\\))?[^)]?"

MARKUP_REGEX = r'\[({0})]\(\s*({1})\s*\)'.format(_name_regex, _url_regex)


# TODO (steven_c) Have it not match md image links: ![some image](http://some.com/image/link.jpg)

def rm_link_paren_esc(txt):
    return re.subn(r"([\\])([)])", r")", txt)[0]


def parse_links(txt):
    """
    Parses the contents of all Markdown links in txt.

    >>> parse_links("some text with [some](http://md.com/link)")
    [('some', 'http://md.com/link')]

    >>> parse_links("some text with [some](http://md.com/link_(bull_crap\\))")
    [('some', 'http://md.com/link_(bull_crap\\\)')]
    """
    return tlz.pipe(re.findall(MARKUP_REGEX, txt),
                    ctlz.map(ctlz.take(2)),
                    ctlz.map(tuple),
                    list)


def build_md_link(txt, link):
    """
    Uses txt and link to create a Markdown formated link.

    >>> build_md_link('some', 'http://md.com/link')
    '[some](http://md.com/link)'

    >>> build_md_link('some', 'http://md.com/link_(bull_crap\\)')
    '[some](http://md.com/link_(bull_crap\\\))'
    """
    return "[{0}]({1})".format(txt, link)


def build_html_link(txt, link, other_browser=True):
    """
    Uses txt and link to create an HTML link.

    >>> build_html_link("text", "link", False)
    '<a  href="link">text</a>'

    >>> build_html_link("text", "link")
    '<a target="_blank" href="link">text</a>'
    """
    if other_browser:
        target = 'target="_blank"'
    else:
        target = ''
    return """<a {target} href="{link}">{txt}</a>""".format(
        **{"link": rm_link_paren_esc(link), "txt": txt, "target": target})


def md_link_to_html(txt, other_browser=True):
    """
    In txt, change Markdown formated links to HTML.
    (Only links are touched)

    >>> md_link_to_html("derp ferp (f) [t](l).")
    'derp ferp (f) <a target="_blank" href="l">t</a>.'

    >>> md_link_to_html("derp ferp (f) [t](l).", False)
    'derp ferp (f) <a  href="l">t</a>.'
    """

    # Because it's unlikely that links are duplicated, don't worry about
    # duplicates. Also, md_link_to_html is idempotent. And, this is only intended
    # for small local jobs so it will be plenty fast.
    return tlz.pipe(txt,
                    parse_links,
                    ctlz.map(lambda tandl: {"html": build_html_link(tandl[0],
                                                                    tandl[1],
                                                                    other_browser),
                                            "md": build_md_link(tandl[0],
                                                                tandl[1])}),
                    lambda links: tlz.compose(*map(lambda l:
                                                   lambda text:
                                                   text.replace(l['md'],
                                                                l['html']),
                                                   links)),
                    lambda f: f(txt),
                    )
