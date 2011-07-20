=====
magic
=====

A Python module that wraps ``libmagic`` using ctypes to allow the identification of
files using magic numbers.

The ``Magic`` class manages ``libmagic`` for you. After construction use either
the ``desc_file`` for ``desc_buffer`` methods to identify a file by filename, a
buffer of fie contents.

>>> import magic
>>> m = magic.Magic()
>>> m.desc_file('README.rst')
'ASCII English text'
>>> m.desc_buffer('#!/usr/bin/python\n')
'a /usr/bin/python script, ASCII text executable'
>>>

To get a mime type, rather than a textual description, pass the MAGIC_MIME_TYPE
flag to the contructor.

>>> import magic
>>> m = magic.Magic()
>>> m = magic.Magic(flags=magic.MAGIC_MIME_TYPE)
>>> m.desc_file('README.rst')
'text/plain'
>>>

The low level ``libmagic`` API is also available. See libmagic(3) for details.
