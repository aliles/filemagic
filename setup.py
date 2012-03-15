#!/usr/bin/env python
from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name="filemagic",
    version="0.2",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    author="Aaron Iles",
    author_email="aaron.iles@gmail.com",
    url="http://github.com/aliles/filemagic",
    download_url="http://github.com/aliles/filemagic/downloads",
    description="File type identification using libmagic",
    long_description=open('README.rst').read(),
    license="ASL",
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite = "tests"
)
