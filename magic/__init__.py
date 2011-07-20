"""File type identification using libmagic.

A ctypes Python wrapper for libmagic.

See libmagic(3) for low level details.
"""
import ctypes.util
import ctypes

libname = ctypes.util.find_library('magic')
if not libname:
    raise ImportError('Unable to find magic library')

try:
    lib = ctypes.CDLL(libname)
except Exception:
    raise ImportError('Loading {0} failed'.format(libname))

# magic.h constants
MAGIC_NONE              = 0x000000
MAGIC_DEBUG             = 0x000001
MAGIC_SYMLINK           = 0x000002
MAGIC_COMPRESS          = 0x000004
MAGIC_DEVICES           = 0x000008
MAGIC_MIME_TYPE         = 0x000010
MAGIC_CONTINUE          = 0x000020
MAGIC_CHECK             = 0x000040
MAGIC_PRESERVE_ATIME    = 0x000080
MAGIC_RAW               = 0x000100
MAGIC_ERROR             = 0x000200
MAGIC_MIME_ENCODING     = 0x000400
MAGIC_MIME              = MAGIC_MIME_TYPE | MAGIC_MIME_ENCODING
MAGIC_APPLE             = 0x000800

MAGIC_NO_CHECK_COMPRESS = 0x001000
MAGIC_NO_CHECK_TAR      = 0x002000
MAGIC_NO_CHECK_SOFT     = 0x004000
MAGIC_NO_CHECK_APPTYPE  = 0x008000
MAGIC_NO_CHECK_ELF      = 0x010000
MAGIC_NO_CHECK_TEXT     = 0x020000
MAGIC_NO_CHECK_CDF      = 0x040000
MAGIC_NO_CHECK_TOKENS   = 0x100000
MAGIC_NO_CHECK_ENCODING = 0x200000

MAGIC_NO_CHECK_BUILTIN  = 0x3fb000

MAGIC_NO_CHECK_ASCII    = MAGIC_NO_CHECK_TEXT

MAGIC_NO_CHECK_FORTRAN  = 0x000000
MAGIC_NO_CHECK_TROFF    = 0x000000


# magic_t type
class Cookie(ctypes.Structure):
    "Magic data structure"

c_cookie_p = ctypes.POINTER(Cookie)


# error handling
class MagicError(EnvironmentError):
    "Error occured inside libmagic"


def errcheck_int(result, func, arguments):
    "Raise an error if return integer is less than 0"
    if result < 0:
        cookie = arguments[0]
        errno = magic_errno(cookie)
        error = magic_error(cookie)
        raise MagicError(errno, error)
    return result


def errcheck_null(result, func, arguments):
    "Raise an error if the return pointer is NULL"
    if not result:
        errno = magic_errno(cookie)
        error = magic_error(cookie)
        raise MagicError(errno, error)
    return result

# dynamically load library
lib.magic_open.argtypes = [ctypes.c_int]
lib.magic_open.restype = c_cookie_p
lib.magic_open.err_check = errcheck_null
magic_open = lib.magic_open

lib.magic_close.argyptes = [c_cookie_p]
lib.magic_close.restype = None
magic_close = lib.magic_close

lib.magic_error.argyptes = [c_cookie_p]
lib.magic_error.restype = ctypes.c_char_p
magic_error = lib.magic_error

lib.magic_errno.argyptes = [c_cookie_p]
lib.magic_errno.restype = ctypes.c_int
magic_errno = lib.magic_errno

lib.magic_file.argyptes = [c_cookie_p, ctypes.c_char_p]
lib.magic_file.restype = ctypes.c_char_p
lib.magic_file.errcheck = errcheck_null
magic_file = lib.magic_file

lib.magic_buffer.argyptes = [c_cookie_p, ctypes.c_void_p, ctypes.c_size_t]
lib.magic_buffer.restype = ctypes.c_char_p
lib.magic_buffer.errcheck = errcheck_null
magic_buffer = lib.magic_buffer

lib.magic_setflags.argyptes = [c_cookie_p, ctypes.c_int]
lib.magic_setflags.restype = ctypes.c_int
lib.magic_setflags.errcheck = errcheck_int
magic_setflags = lib.magic_setflags

lib.magic_check.argyptes = [c_cookie_p, ctypes.c_char_p]
lib.magic_check.restype = ctypes.c_int
lib.magic_check.errcheck = errcheck_int
magic_check = lib.magic_check

lib.magic_compile.argyptes = [c_cookie_p, ctypes.c_char_p]
lib.magic_compile.restype = ctypes.c_int
lib.magic_compile.errcheck = errcheck_int
magic_compile = lib.magic_compile

lib.magic_load.argyptes = [c_cookie_p, ctypes.c_char_p]
lib.magic_load.restype = ctypes.c_int
lib.magic_load.errcheck = errcheck_int
magic_load = lib.magic_load


class Magic(object):
    """Identify and describe files using libmagic magic numbers.

    Manages the resources for libmagic. Provides two methods for identifying
    file contents.

     - desc_buffer identifies the contents of the buffer
     - desc_file identifies the contents of the named file

    To get mime types rather than textual descriptions, pass the flag
    MAGIC_MIME_TYPE to the contructor.
    """

    def __init__(self, filename=None, flags=MAGIC_NONE):
        """Open and initialise resources from libmagic.

        ``filename`` is a colon seperated list of magic database files to load.
        If None, the default database will be loaded. For details on the magic
        database file see magic(5).

        ``flags`` controls how libmagic should behave. See libmagic(3) for
        details of these flags.
        """
        self.cookie = magic_open(flags)
        magic_load(self.cookie, filename)

    def __enter__(self):
        "__enter__() -> self."
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        "__exit__(*excinfo) -> None.  Closes libmagic resources."
        self.close()

    def close(self):
        "Close any resources opened by libmagic"
        magic_close(self.cookie)

    def desc_buffer(self, buffer):
        "Return a textual description of the contents of buffer"
        return magic_buffer(self.cookie,
                ctypes.c_char_p(buffer),
                len(buffer))

    def desc_file(self, filename):
        "Return a textual description of of the contents of the file, fiename"
        return magic_file(self.cookie, filename)
