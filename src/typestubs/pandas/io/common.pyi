"""
This type stub file was generated by pyright.
"""

import mmap
from contextlib import contextmanager
from pandas import compat
from pandas.errors import ParserError
from urllib.request import urlopen
from urllib.parse import uses_netloc, uses_params, uses_relative
from urllib2 import urlopen as _urlopen
from urlparse import uses_netloc, uses_params, uses_relative
from typing import Any, Optional

"""Common IO api utilities"""
CParserError = ParserError
_NA_VALUES = set(['-1.#IND', '1.#QNAN', '1.#IND', '-1.#QNAN', '#N/A N/A', '#N/A', 'N/A', 'n/a', 'NA', '#NA', 'NULL', 'null', 'NaN', '-NaN', 'nan', '-nan', ''])
if compat.PY3:
    _urlopen = urlopen
else:
    @contextmanager
    def urlopen(*args, **kwargs):
        ...
    
_VALID_URLS = set(uses_relative + uses_netloc + uses_params)
class BaseIterator(object):
    """Subclass this and provide a "__next__()" method to obtain an iterator.
    Useful only when the object being iterated is non-reusable (e.g. OK for a
    parser, not for an in-memory table, yes for its iterator)."""
    def __iter__(self):
        ...
    
    def __next__(self):
        ...
    


if not compat.PY3:
    ...
def _is_url(url):
    """Check to see if a URL has a valid protocol.

    Parameters
    ----------
    url : str or unicode

    Returns
    -------
    isurl : bool
        If `url` has a valid protocol return True otherwise False.
    """
    ...

def _is_s3_url(url):
    """Check for an s3, s3n, or s3a url"""
    ...

def _expand_user(filepath_or_buffer):
    """Return the argument with an initial component of ~ or ~user
       replaced by that user's home directory.

    Parameters
    ----------
    filepath_or_buffer : object to be converted if possible

    Returns
    -------
    expanded_filepath_or_buffer : an expanded filepath or the
                                  input if not expandable
    """
    ...

def _validate_header_arg(header):
    ...

def _stringify_path(filepath_or_buffer):
    """Attempt to convert a path-like object to a string.

    Parameters
    ----------
    filepath_or_buffer : object to be converted

    Returns
    -------
    str_filepath_or_buffer : maybe a string version of the object

    Notes
    -----
    Objects supporting the fspath protocol (python 3.6+) are coerced
    according to its __fspath__ method.

    For backwards compatibility with older pythons, pathlib.Path and
    py.path objects are specially coerced.

    Any other object is passed through unchanged, which includes bytes,
    strings, buffers, or anything else that's not even path-like.
    """
    ...

def get_filepath_or_buffer(filepath_or_buffer, encoding: Optional[Any] = ..., compression: Optional[Any] = ...):
    """
    If the filepath_or_buffer is a url, translate and return the buffer.
    Otherwise passthrough.

    Parameters
    ----------
    filepath_or_buffer : a url, filepath (str, py.path.local or pathlib.Path),
                         or buffer
    encoding : the encoding to use to decode py3 bytes, default is 'utf-8'

    Returns
    -------
    a filepath_or_buffer, the encoding, the compression
    """
    ...

def file_path_to_url(path):
    """
    converts an absolute native path to a FILE URL.

    Parameters
    ----------
    path : a path in native format

    Returns
    -------
    a valid FILE URL
    """
    ...

_compression_to_extension = { 'gzip': '.gz','bz2': '.bz2','zip': '.zip','xz': '.xz' }
def _infer_compression(filepath_or_buffer, compression):
    """
    Get the compression method for filepath_or_buffer. If compression='infer',
    the inferred compression method is returned. Otherwise, the input
    compression method is returned unchanged, unless it's invalid, in which
    case an error is raised.

    Parameters
    ----------
    filepath_or_buf :
        a path (str) or buffer
    compression : str or None
        the compression method including None for no compression and 'infer'

    Returns
    -------
    string or None :
        compression method

    Raises
    ------
    ValueError on invalid compression specified
    """
    ...

def _get_handle(path_or_buf, mode, encoding: Optional[Any] = ..., compression: Optional[Any] = ..., memory_map: bool = ..., is_text: bool = ...):
    """
    Get file handle for given path/buffer and mode.

    Parameters
    ----------
    path_or_buf :
        a path (str) or buffer
    mode : str
        mode to open path_or_buf with
    encoding : str or None
    compression : str or None
        Supported compression protocols are gzip, bz2, zip, and xz
    memory_map : boolean, default False
        See parsers._parser_params for more information.
    is_text : boolean, default True
        whether file/buffer is in text format (csv, json, etc.), or in binary
        mode (pickle, etc.)
    Returns
    -------
    f : file-like
        A file-like object
    handles : list of file-like objects
        A list of file-like object that were openned in this function.
    """
    ...

class MMapWrapper(BaseIterator):
    """
    Wrapper for the Python's mmap class so that it can be properly read in
    by Python's csv.reader class.

    Parameters
    ----------
    f : file object
        File object to be mapped onto memory. Must support the 'fileno'
        method or have an equivalent attribute

    """
    def __init__(self, f):
        self.mmap = ...
    
    def __getattr__(self, name):
        ...
    
    def __iter__(self):
        ...
    
    def __next__(self):
        ...
    


if not compat.PY3:
    ...
class UTF8Recoder(BaseIterator):
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = ...
    
    def read(self, bytes=...):
        ...
    
    def readline(self):
        ...
    
    def next(self):
        ...
    


if compat.PY3:
    def UnicodeReader(f, dialect=..., encoding=..., **kwds):
        ...
    
    def UnicodeWriter(f, dialect=..., encoding=..., **kwds):
        ...
    
else:
    class UnicodeReader(BaseIterator):
        """
        A CSV reader which will iterate over lines in the CSV file "f",
        which is encoded in the given encoding.

        On Python 3, this is replaced (below) by csv.reader, which handles
        unicode.
        """
        def __init__(self, f, dialect=..., encoding=..., **kwds):
            self.reader = ...
        
        def __next__(self):
            ...
        
    
    
    class UnicodeWriter:
        """
        A CSV writer which will write rows to CSV file "f",
        which is encoded in the given encoding.
        """
        def __init__(self, f, dialect=..., encoding=..., **kwds):
            self.queue = ...
            self.writer = ...
            self.stream = ...
            self.encoder = ...
            self.quoting = ...
        
        def writerow(self, row):
            ...
        
        def writerows(self, rows):
            ...
        
    
    
