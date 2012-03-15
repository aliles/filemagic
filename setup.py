#!/usr/bin/env python
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup
import re

def load_version(filename='magic/version.py'):
    "Parse a __version__ number from a source file"
    with open(filename) as source:
        text = source.read()
        match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", text)
        if not match:
            msg = "Unable to find version number in {}".format(filename)
            raise RuntimeError(msg)
        version = match.group(1)
        return version

def load_rst(filename='docs/source/guide_content.rst'):
    "Purge refs directives from restructured text"
    with open(filename) as source:
        text = source.read()
        doc = re.sub(r':\w+:`~?([a-zA-Z._()]+)`', r'*\1*', text)
        return doc

setup(
    name="filemagic",
    version=load_version(),
    packages=['magic'],
    zip_safe=False,
    author="Aaron Iles",
    author_email="aaron.iles@gmail.com",
    url="http://github.com/aliles/filemagic",
    description="A Python API for libmagic, the library behind the Unix file command",
    long_description=load_rst(),
    license="ASL",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite = "tests"
)
