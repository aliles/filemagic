Background
----------

`libmagic <http://www.darwinsys.com/file/>`_ is the library that commonly
supports the *file* command on Unix system, other than Max OSX which has its
own implementation. The library handles the loading of *database* files that
describe the magic numbers used to identify various file types, as well as the
associated mime types. The library also handles character set detections.

Installation
------------

Before installing *filemagic*, the *libmagic* library will need to be
availabile.  To test this is the check for the presence of the *file* command
and/or the *libmagic* man page. ::

    $ which file
    $ man libmagic

On Mac OSX, Apple has implemented their own version of the file command.
However, *libmagic* can be installed using `homebrew
<https://github.com/mxcl/homebrew>`_ ::

    $ brew install libmagic

After *brew* finished installing, the test for the *libmagic* man page should
pass.

Now that the presence of *libmagic* has been confirmed, use `pip
<http://pypi.python.org/pypi/pip>`_ to install filemagic. ::

    $ pip install filemagic

The *magic* module should now be availabe from the Python shell. ::

    >>> import magic

The next section will describe how to use the *magic.Magic* class to identify
file types.

Usage
-----

The *magic* module uses `ctypes
<http://docs.python.org/dev/library/ctypes.html>` to wrap the primitives from
*libmagic* in the more user friendly *magic.Magic* class. This class handles
initialization, loading databases and the release of resources. ::

    >>> import magic

To ensure that resources are correctly released by *magic.Magic*, it's
necessary to either explicitly call *close* on instances, or use *with*
statement. ::

    >>> with magic.Magic as m:
    >>>     pass

*magic.Magic* supports context managers which ensures resources are correctly
released at the end of the *with* statements irrespective of any exceptions.

To identify a file from it's filename, use the *id_filename* method. ::

    >>> with magic.Magic as m:
    >>>     m.id_filename('setup.py')
    'Python script, ASCII text executable'

Similarily to identify a file from a *str* or *buffer* that has already been read, use the *id_filename* method. ::

    >>> with magic.Magic as m:
    >>>     m.desc_buffer('#!/usr/bin/python\n')
    'Python script, ASCII text executable'

To identify with mime type, rather than a textual description, pass the
*magic.MAGIC_MIME_TYPE* flag when creating the *magic.Magic* instance. ::

    >>> with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
    >>>     m.desc_file('setup.py')
    'text/x-python'

Similarily, *magic.MAGIC_MIME_ENCODING* can be passed to return the encoding
type. ::

    >>> with magic.Magic(flags=magic.MAGIC_MIME_ENCODING) as m:
    >>>     m.desc_file('setup.py')
    'us-ascii'

Unicode and Python3
-------------------

On both Python2 and Python3, *magic.Magic* will encode any unicode objects (the
default string type for Python3) to byte strings before being passed to
*libmagic*. On Python3, returned strings will be decoded to unicode using the
default encoding type. The user **should not** be concerned whether unicode or
bytes are passed to *magic.Magic* methods. However, the use **will** need to be
aware that return strings are always unicode on Python3 and byte strings on
Python2.
