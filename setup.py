"""
md_link_mod Copyright (C) 2017  Steven Cutting
"""


from setuptools import setup, find_packages

with open("README.md") as fp:
    THE_LONG_DESCRIPTION = fp.read()


setup(
    name="md_link_mod",
    version="0.1.0",
    license='GNU GPL v3+',
    description="For modifying markdown links in text.",
    long_description=THE_LONG_DESCRIPTION,
    classifiers=['Topic :: NLP',
                 'Topic :: text munging',
                 'Topic :: web',
                 'Intended Audience :: Developers',
                 'Operating System :: GNU Linux',
                 'Operating System :: OSX :: MacOS :: MacOS X',
                 'Development Status :: 3 - Alpha',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Pypy :: 2.5',
                 'Programming Language :: Pypy :: 3.5',
                 'License :: GNU GPL v3+',
                 'Status :: ' + "pre-alpha",
                 ],
    keywords='markdown',
    author='Steven Cutting',
    author_email='steven.e.cutting@linux.com',
    packages=find_packages(exclude=('bin', 'tests', 'docker',
                                    'data',)),
    scripts=['bin/mdlink2html'],
    install_requires=['toolz>=0.8.2',
                      'click>=6.7',
                      ],
    setup_requires=['pytest-runner>=2.11.1'],
    tests_require=['pytest>=3.0.6'],
    )
