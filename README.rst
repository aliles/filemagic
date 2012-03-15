=====
magic
=====

``magic`` is a Python module that wraps ``libmagic`` using ctypes to allow the
identification of files using magic numbers.

The ``Magic`` class manages ``libmagic`` for you. After construction use either
the ``id_filename`` for ``id_buffer`` methods to identify a file by filename, a
buffer of fie contents.

>>> import magic
>>> m = magic.Magic()
>>> m.desc_filename('README.rst')
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

Similarily, the encoding can be used as the textual descripton by pass
MAGIC_MIME_ENCODING.

>>> import magic
>>> m = magic.Magic()
>>> m = magic.Magic(flags=magic.MAGIC_MIME_ENCODING)
>>> m.desc_file('README.rst')
'us-ascii'
>>>

The low level ``libmagic`` API is also available from the ``magic.api`` module.
See libmagic(3) for details.
