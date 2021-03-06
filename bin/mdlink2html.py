#! /usr/bin/env python

import sys
import fnmatch
import os

import click
import toolz as tlz

from md_link_mod import md_link_to_html

"""
matches = []
for root, dirnames, filenames in os.walk('src'):
    for filename in fnmatch.filter(filenames, '*.c'):
        matches.append(os.path.join(root, filename))
"""


def spelunker_gen(rootdir):
    for dirname, subdirlist, filelist in os.walk(rootdir):
        for fname in filelist:
            yield os.path.join(dirname, fname)


def find_files(indir, match="*"):
    return tlz.concat(((os.path.join(r, ff) for ff in fnmatch.filter(f, indir))
                       for r, d, f in os.walk(indir)))


@click.command()
def cli():
    """
    Usage:
        cat doc.md | mdlink2html > new-doc.md

    This program is intended to be used on Markdown style documents.
    It is used to transform Markdown style links into HTML style links.

    It should be used as part of a Unix style pipe.
    """
    def output(txt):
        try:
            click.echo(md_link_to_html(txt))
        except Exception as e:
            click.echo("ERROR: mdlink2html: got exception {}".format(e.message),
                       err=True)

    # use [:-1] to remove the extra trailing newline that is added on for some reason.
    # TODO (steven_c) find out why this newline happens.
    [output(l[:-1]) for l in click.get_text_stream('stdin')]


if __name__ == "__main__":
    cli()
