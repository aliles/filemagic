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
lib.magic_error.restype = c_cookie_p
magic_error = lib.magic_error

lib.magic_errno.argyptes = [c_cookie_p]
lib.magic_errno.restype = c_cookie_p
magic_errno = lib.magic_errno

lib.magic_file.argyptes = [c_cookie_p]
lib.magic_file.restype = c_cookie_p
lib.magic_file.errcheck = errcheck_null
magic_file = lib.magic_file

lib.magic_buffer.argyptes = [c_cookie_p]
lib.magic_buffer.restype = c_cookie_p
lib.magic_buffer.errcheck = errcheck_null
magic_buffer = lib.magic_buffer

lib.magic_setflags.argyptes = [c_cookie_p]
lib.magic_setflags.restype = c_cookie_p
lib.magic_setflags.errcheck = errcheck_int
magic_setflags = lib.magic_setflags

lib.magic_check.argyptes = [c_cookie_p]
lib.magic_check.restype = c_cookie_p
lib.magic_check.errcheck = errcheck_int
magic_check = lib.magic_check

lib.magic_compile.argyptes = [c_cookie_p]
lib.magic_compile.restype = c_cookie_p
lib.magic_compile.errcheck = errcheck_int
magic_compile = lib.magic_compile

lib.magic_load.argyptes = [c_cookie_p]
lib.magic_load.restype = c_cookie_p
lib.magic_load.errcheck = errcheck_int
magic_load = lib.magic_load


class Magic(object):

    def __init__(self, filename=None, flags=MAGIC_NONE):
        self.cookie = magic_open(flags)
        magic_load(self.cookie, filename)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        magic_close(self.cookie)

    def desc_buffer(self, buffer):
        return magic_buffer(self.cookie,
                ctypes.c_char_p(buffer),
                len(buffer))

    def desc_file(self, filename):
        return magic_file(self.cookie, filename)
