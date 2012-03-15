#!/usr/bin/env python
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup

setup(
    name="filemagic",
    version="1.0",
    packages=['magic'],
    zip_safe=False,
    author="Aaron Iles",
    author_email="aaron.iles@gmail.com",
    url="http://github.com/aliles/filemagic",
    description="A Python API for libmagic, the library behind the Unix file command",
    long_description=open('docs/source/guide.rst').read(),
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
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite = "tests"
)
