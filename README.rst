filemagic
---------

*filemagic* is a ctypes wrapper for `libmagic
<http://www.darwinsys.com/file/>`_, the library that supports the *file*
command on most Unix systems. The package provides a simple Python API for
identifying files using the extensive database of magic strings that ships with
*libmagic*.

* Documentation for *filemagic* is hosted on `Read the Docs
  <http://filemagic.readthedocs.org>`_.
* Packages are hosted by the `Python Package Index
  <http://pypi.python.org/pypi/filemagic>`_.

*filemagic* supports both Python2 and Python3, as well as CPython and PyPy.

Example
-------

Below is a short snippet of code showing how to use *filemagic* to identifying
this README file. ::

    >>> import magic
    >>> with magic.Magic() as m:
    ...     m.id_filename('setup.py')
    ...
    'ASCII text'

It is recommended that *magic.Magic* be used with a context manager (the *with*
statement) to avoid leaking resources from *libmagic* when instances go out of
scope. Otherwise the *close()* method must be called explicitly.

Further Reading
---------------

Refer to the `filemagic documenation <http://filemagic.readthedocs.org>`_ for
further references.
