"""
This type stub file was generated by pyright.
"""

import csv
from textwrap import fill
from pandas.compat import u
from pandas.io.common import BaseIterator, _NA_VALUES
from pandas.util._decorators import Appender
from typing import Any, Optional

"""
Module contains tools for processing files into DataFrames or other objects
"""
_BOM = u('\ufeff')
_parser_params = """Also supports optionally iterating or breaking of the file
into chunks.

Additional help can be found in the `online docs for IO Tools
<http://pandas.pydata.org/pandas-docs/stable/io.html>`_.

Parameters
----------
filepath_or_buffer : str, pathlib.Path, py._path.local.LocalPath or any \
object with a read() method (such as a file handle or StringIO)
    The string could be a URL. Valid URL schemes include http, ftp, s3, and
    file. For file URLs, a host is expected. For instance, a local file could
    be file ://localhost/path/to/table.csv
%s
delim_whitespace : boolean, default False
    Specifies whether or not whitespace (e.g. ``' '`` or ``'\t'``) will be
    used as the sep. Equivalent to setting ``sep='\s+'``. If this option
    is set to True, nothing should be passed in for the ``delimiter``
    parameter.

    .. versionadded:: 0.18.1 support for the Python parser.

header : int or list of ints, default 'infer'
    Row number(s) to use as the column names, and the start of the
    data.  Default behavior is to infer the column names: if no names
    are passed the behavior is identical to ``header=0`` and column
    names are inferred from the first line of the file, if column
    names are passed explicitly then the behavior is identical to
    ``header=None``. Explicitly pass ``header=0`` to be able to
    replace existing names. The header can be a list of integers that
    specify row locations for a multi-index on the columns
    e.g. [0,1,3]. Intervening rows that are not specified will be
    skipped (e.g. 2 in this example is skipped). Note that this
    parameter ignores commented lines and empty lines if
    ``skip_blank_lines=True``, so header=0 denotes the first line of
    data rather than the first line of the file.
names : array-like, default None
    List of column names to use. If file contains no header row, then you
    should explicitly pass header=None. Duplicates in this list will cause
    a ``UserWarning`` to be issued.
index_col : int or sequence or False, default None
    Column to use as the row labels of the DataFrame. If a sequence is given, a
    MultiIndex is used. If you have a malformed file with delimiters at the end
    of each line, you might consider index_col=False to force pandas to _not_
    use the first column as the index (row names)
usecols : array-like or callable, default None
    Return a subset of the columns. If array-like, all elements must either
    be positional (i.e. integer indices into the document columns) or strings
    that correspond to column names provided either by the user in `names` or
    inferred from the document header row(s). For example, a valid array-like
    `usecols` parameter would be [0, 1, 2] or ['foo', 'bar', 'baz'].

    If callable, the callable function will be evaluated against the column
    names, returning names where the callable function evaluates to True. An
    example of a valid callable argument would be ``lambda x: x.upper() in
    ['AAA', 'BBB', 'DDD']``. Using this parameter results in much faster
    parsing time and lower memory usage.
as_recarray : boolean, default False
    .. deprecated:: 0.19.0
       Please call `pd.read_csv(...).to_records()` instead.

    Return a NumPy recarray instead of a DataFrame after parsing the data.
    If set to True, this option takes precedence over the `squeeze` parameter.
    In addition, as row indices are not available in such a format, the
    `index_col` parameter will be ignored.
squeeze : boolean, default False
    If the parsed data only contains one column then return a Series
prefix : str, default None
    Prefix to add to column numbers when no header, e.g. 'X' for X0, X1, ...
mangle_dupe_cols : boolean, default True
    Duplicate columns will be specified as 'X.0'...'X.N', rather than
    'X'...'X'. Passing in False will cause data to be overwritten if there
    are duplicate names in the columns.
dtype : Type name or dict of column -> type, default None
    Data type for data or columns. E.g. {'a': np.float64, 'b': np.int32}
    Use `str` or `object` to preserve and not interpret dtype.
    If converters are specified, they will be applied INSTEAD
    of dtype conversion.
%s
converters : dict, default None
    Dict of functions for converting values in certain columns. Keys can either
    be integers or column labels
true_values : list, default None
    Values to consider as True
false_values : list, default None
    Values to consider as False
skipinitialspace : boolean, default False
    Skip spaces after delimiter.
skiprows : list-like or integer or callable, default None
    Line numbers to skip (0-indexed) or number of lines to skip (int)
    at the start of the file.

    If callable, the callable function will be evaluated against the row
    indices, returning True if the row should be skipped and False otherwise.
    An example of a valid callable argument would be ``lambda x: x in [0, 2]``.
skipfooter : int, default 0
    Number of lines at bottom of file to skip (Unsupported with engine='c')
skip_footer : int, default 0
    .. deprecated:: 0.19.0
       Use the `skipfooter` parameter instead, as they are identical
nrows : int, default None
    Number of rows of file to read. Useful for reading pieces of large files
na_values : scalar, str, list-like, or dict, default None
    Additional strings to recognize as NA/NaN. If dict passed, specific
    per-column NA values.  By default the following values are interpreted as
    NaN: '""" + fill("', '".join(sorted(_NA_VALUES)), 70, subsequent_indent="    ") + """'.
keep_default_na : bool, default True
    If na_values are specified and keep_default_na is False the default NaN
    values are overridden, otherwise they're appended to.
na_filter : boolean, default True
    Detect missing value markers (empty strings and the value of na_values). In
    data without any NAs, passing na_filter=False can improve the performance
    of reading a large file
verbose : boolean, default False
    Indicate number of NA values placed in non-numeric columns
skip_blank_lines : boolean, default True
    If True, skip over blank lines rather than interpreting as NaN values
parse_dates : boolean or list of ints or names or list of lists or dict, \
default False

    * boolean. If True -> try parsing the index.
    * list of ints or names. e.g. If [1, 2, 3] -> try parsing columns 1, 2, 3
      each as a separate date column.
    * list of lists. e.g.  If [[1, 3]] -> combine columns 1 and 3 and parse as
      a single date column.
    * dict, e.g. {'foo' : [1, 3]} -> parse columns 1, 3 as date and call result
      'foo'

    If a column or index contains an unparseable date, the entire column or
    index will be returned unaltered as an object data type. For non-standard
    datetime parsing, use ``pd.to_datetime`` after ``pd.read_csv``

    Note: A fast-path exists for iso8601-formatted dates.
infer_datetime_format : boolean, default False
    If True and `parse_dates` is enabled, pandas will attempt to infer the
    format of the datetime strings in the columns, and if it can be inferred,
    switch to a faster method of parsing them. In some cases this can increase
    the parsing speed by 5-10x.
keep_date_col : boolean, default False
    If True and `parse_dates` specifies combining multiple columns then
    keep the original columns.
date_parser : function, default None
    Function to use for converting a sequence of string columns to an array of
    datetime instances. The default uses ``dateutil.parser.parser`` to do the
    conversion. Pandas will try to call `date_parser` in three different ways,
    advancing to the next if an exception occurs: 1) Pass one or more arrays
    (as defined by `parse_dates`) as arguments; 2) concatenate (row-wise) the
    string values from the columns defined by `parse_dates` into a single array
    and pass that; and 3) call `date_parser` once for each row using one or
    more strings (corresponding to the columns defined by `parse_dates`) as
    arguments.
dayfirst : boolean, default False
    DD/MM format dates, international and European format
iterator : boolean, default False
    Return TextFileReader object for iteration or getting chunks with
    ``get_chunk()``.
chunksize : int, default None
    Return TextFileReader object for iteration.
    See the `IO Tools docs
    <http://pandas.pydata.org/pandas-docs/stable/io.html#io-chunking>`_
    for more information on ``iterator`` and ``chunksize``.
compression : {'infer', 'gzip', 'bz2', 'zip', 'xz', None}, default 'infer'
    For on-the-fly decompression of on-disk data. If 'infer' and
    `filepath_or_buffer` is path-like, then detect compression from the
    following extensions: '.gz', '.bz2', '.zip', or '.xz' (otherwise no
    decompression). If using 'zip', the ZIP file must contain only one data
    file to be read in. Set to None for no decompression.

    .. versionadded:: 0.18.1 support for 'zip' and 'xz' compression.

thousands : str, default None
    Thousands separator
decimal : str, default '.'
    Character to recognize as decimal point (e.g. use ',' for European data).
float_precision : string, default None
    Specifies which converter the C engine should use for floating-point
    values. The options are `None` for the ordinary converter,
    `high` for the high-precision converter, and `round_trip` for the
    round-trip converter.
lineterminator : str (length 1), default None
    Character to break file into lines. Only valid with C parser.
quotechar : str (length 1), optional
    The character used to denote the start and end of a quoted item. Quoted
    items can include the delimiter and it will be ignored.
quoting : int or csv.QUOTE_* instance, default 0
    Control field quoting behavior per ``csv.QUOTE_*`` constants. Use one of
    QUOTE_MINIMAL (0), QUOTE_ALL (1), QUOTE_NONNUMERIC (2) or QUOTE_NONE (3).
doublequote : boolean, default ``True``
   When quotechar is specified and quoting is not ``QUOTE_NONE``, indicate
   whether or not to interpret two consecutive quotechar elements INSIDE a
   field as a single ``quotechar`` element.
escapechar : str (length 1), default None
    One-character string used to escape delimiter when quoting is QUOTE_NONE.
comment : str, default None
    Indicates remainder of line should not be parsed. If found at the beginning
    of a line, the line will be ignored altogether. This parameter must be a
    single character. Like empty lines (as long as ``skip_blank_lines=True``),
    fully commented lines are ignored by the parameter `header` but not by
    `skiprows`. For example, if comment='#', parsing '#empty\\na,b,c\\n1,2,3'
    with `header=0` will result in 'a,b,c' being
    treated as the header.
encoding : str, default None
    Encoding to use for UTF when reading/writing (ex. 'utf-8'). `List of Python
    standard encodings
    <https://docs.python.org/3/library/codecs.html#standard-encodings>`_
dialect : str or csv.Dialect instance, default None
    If provided, this parameter will override values (default or not) for the
    following parameters: `delimiter`, `doublequote`, `escapechar`,
    `skipinitialspace`, `quotechar`, and `quoting`. If it is necessary to
    override values, a ParserWarning will be issued. See csv.Dialect
    documentation for more details.
tupleize_cols : boolean, default False
    .. deprecated:: 0.21.0
       This argument will be removed and will always convert to MultiIndex

    Leave a list of tuples on columns as is (default is to convert to
    a MultiIndex on the columns)
error_bad_lines : boolean, default True
    Lines with too many fields (e.g. a csv line with too many commas) will by
    default cause an exception to be raised, and no DataFrame will be returned.
    If False, then these "bad lines" will dropped from the DataFrame that is
    returned.
warn_bad_lines : boolean, default True
    If error_bad_lines is False, and warn_bad_lines is True, a warning for each
    "bad line" will be output.
low_memory : boolean, default True
    Internally process the file in chunks, resulting in lower memory use
    while parsing, but possibly mixed type inference.  To ensure no mixed
    types either set False, or specify the type with the `dtype` parameter.
    Note that the entire file is read into a single DataFrame regardless,
    use the `chunksize` or `iterator` parameter to return the data in chunks.
    (Only valid with C parser)
buffer_lines : int, default None
    .. deprecated:: 0.19.0
       This argument is not respected by the parser
compact_ints : boolean, default False
    .. deprecated:: 0.19.0
       Argument moved to ``pd.to_numeric``

    If compact_ints is True, then for any column that is of integer dtype,
    the parser will attempt to cast it as the smallest integer dtype possible,
    either signed or unsigned depending on the specification from the
    `use_unsigned` parameter.
use_unsigned : boolean, default False
    .. deprecated:: 0.19.0
       Argument moved to ``pd.to_numeric``

    If integer columns are being compacted (i.e. `compact_ints=True`), specify
    whether the column should be compacted to the smallest signed or unsigned
    integer dtype.
memory_map : boolean, default False
    If a filepath is provided for `filepath_or_buffer`, map the file object
    directly onto memory and access the data directly from there. Using this
    option can improve performance because there is no longer any I/O overhead.

Returns
-------
result : DataFrame or TextParser
"""
_engine_doc = """engine : {'c', 'python'}, optional
    Parser engine to use. The C engine is faster while the python engine is
    currently more feature-complete."""
_sep_doc = r"""sep : str, default {default}
    Delimiter to use. If sep is None, the C engine cannot automatically detect
    the separator, but the Python parsing engine can, meaning the latter will
    be used and automatically detect the separator by Python's builtin sniffer
    tool, ``csv.Sniffer``. In addition, separators longer than 1 character and
    different from ``'\s+'`` will be interpreted as regular expressions and
    will also force the use of the Python parsing engine. Note that regex
    delimiters are prone to ignoring quoted data. Regex example: ``'\r\t'``
delimiter : str, default ``None``
    Alternative argument name for sep."""
_read_csv_doc = """
Read CSV (comma-separated) file into DataFrame

%s
""" % _parser_params % (_sep_doc.format(default="','"), _engine_doc)
_read_table_doc = """
Read general delimited file into DataFrame

%s
""" % _parser_params % (_sep_doc.format(default="\\t (tab-stop)"), _engine_doc)
_fwf_widths = """\
colspecs : list of pairs (int, int) or 'infer'. optional
    A list of pairs (tuples) giving the extents of the fixed-width
    fields of each line as half-open intervals (i.e.,  [from, to[ ).
    String value 'infer' can be used to instruct the parser to try
    detecting the column specifications from the first 100 rows of
    the data which are not being skipped via skiprows (default='infer').
widths : list of ints. optional
    A list of field widths which can be used instead of 'colspecs' if
    the intervals are contiguous.
delimiter : str, default ``'\t' + ' '``
    Characters to consider as filler characters in the fixed-width file.
    Can be used to specify the filler character of the fields
    if it is not spaces (e.g., '~').
"""
_read_fwf_doc = """
Read a table of fixed-width formatted lines into DataFrame

%s
""" % _parser_params % (_fwf_widths, '')
def _validate_integer(name, val, min_val=...):
    """
    Checks whether the 'name' parameter for parsing is either
    an integer OR float that can SAFELY be cast to an integer
    without losing accuracy. Raises a ValueError if that is
    not the case.

    Parameters
    ----------
    name : string
        Parameter name (used for error reporting)
    val : int or float
        The value to check
    min_val : int
        Minimum allowed value (val < min_val will result in a ValueError)
    """
    ...

def _validate_names(names):
    """
    Check if the `names` parameter contains duplicates.

    If duplicates are found, we issue a warning before returning.

    Parameters
    ----------
    names : array-like or None
        An array containing a list of the names used for the output DataFrame.

    Returns
    -------
    names : array-like or None
        The original `names` parameter.
    """
    ...

def _read(filepath_or_buffer, kwds):
    """Generic reader of line files."""
    ...

_parser_defaults = { 'delimiter': None,'doublequote': True,'escapechar': None,'quotechar': '"','quoting': csv.QUOTE_MINIMAL,'skipinitialspace': False,'lineterminator': None,'header': 'infer','index_col': None,'names': None,'prefix': None,'skiprows': None,'na_values': None,'true_values': None,'false_values': None,'converters': None,'dtype': None,'skipfooter': 0,'keep_default_na': True,'thousands': None,'comment': None,'decimal': b'.','parse_dates': False,'keep_date_col': False,'dayfirst': False,'date_parser': None,'usecols': None,'nrows': None,'chunksize': None,'verbose': False,'encoding': None,'squeeze': False,'compression': None,'mangle_dupe_cols': True,'tupleize_cols': False,'infer_datetime_format': False,'skip_blank_lines': True }
_c_parser_defaults = { 'delim_whitespace': False,'as_recarray': False,'na_filter': True,'compact_ints': False,'use_unsigned': False,'low_memory': True,'memory_map': False,'buffer_lines': None,'error_bad_lines': True,'warn_bad_lines': True,'tupleize_cols': False,'float_precision': None }
_fwf_defaults = { 'colspecs': 'infer','widths': None }
_c_unsupported = 'skipfooter'
_python_unsupported = 'low_memory', 'buffer_lines', 'float_precision'
_deprecated_defaults = { 'as_recarray': None,'buffer_lines': None,'compact_ints': None,'use_unsigned': None,'tupleize_cols': None }
_deprecated_args = 'as_recarray', 'buffer_lines', 'compact_ints', 'use_unsigned', 'tupleize_cols'
def _make_parser_function(name, sep=...):
    ...

read_csv = _make_parser_function('read_csv', sep=',')
read_csv = Appender(_read_csv_doc)(read_csv)
read_table = _make_parser_function('read_table', sep='\t')
read_table = Appender(_read_table_doc)(read_table)
@Appender(_read_fwf_doc)
def read_fwf(filepath_or_buffer, colspecs=..., widths: Optional[Any] = ..., **kwds):
    ...

class TextFileReader(BaseIterator):
    """

    Passed dialect overrides any of the related parser options

    """
    def __init__(self, f, engine: Optional[Any] = ..., **kwds):
        self.f = ...
        self.orig_options = ...
        self.engine = ...
        self.chunksize = ...
        self.nrows = ...
        self.squeeze = ...
        self.engine = ...
    
    def close(self):
        ...
    
    def _get_options_with_defaults(self, engine):
        ...
    
    def _check_file_or_buffer(self, f, engine):
        ...
    
    def _clean_options(self, options, engine):
        ...
    
    def __next__(self):
        ...
    
    def _make_engine(self, engine=...):
        ...
    
    def _failover_to_python(self):
        ...
    
    def read(self, nrows: Optional[Any] = ...):
        ...
    
    def _create_index(self, ret):
        ...
    
    def get_chunk(self, size: Optional[Any] = ...):
        ...
    


def _is_index_col(col):
    ...

def _evaluate_usecols(usecols, names):
    """
    Check whether or not the 'usecols' parameter
    is a callable.  If so, enumerates the 'names'
    parameter and returns a set of indices for
    each entry in 'names' that evaluates to True.
    If not a callable, returns 'usecols'.
    """
    ...

def _validate_skipfooter_arg(skipfooter):
    """
    Validate the 'skipfooter' parameter.

    Checks whether 'skipfooter' is a non-negative integer.
    Raises a ValueError if that is not the case.

    Parameters
    ----------
    skipfooter : non-negative integer
        The number of rows to skip at the end of the file.

    Returns
    -------
    validated_skipfooter : non-negative integer
        The original input if the validation succeeds.

    Raises
    ------
    ValueError : 'skipfooter' was not a non-negative integer.
    """
    ...

def _validate_usecols_arg(usecols):
    """
    Validate the 'usecols' parameter.

    Checks whether or not the 'usecols' parameter contains all integers
    (column selection by index), strings (column by name) or is a callable.
    Raises a ValueError if that is not the case.

    Parameters
    ----------
    usecols : array-like, callable, or None
        List of columns to use when parsing or a callable that can be used
        to filter a list of table columns.

    Returns
    -------
    usecols_tuple : tuple
        A tuple of (verified_usecols, usecols_dtype).

        'verified_usecols' is either a set if an array-like is passed in or
        'usecols' if a callable or None is passed in.

        'usecols_dtype` is the inferred dtype of 'usecols' if an array-like
        is passed in or None if a callable or None is passed in.
    """
    ...

def _validate_parse_dates_arg(parse_dates):
    """
    Check whether or not the 'parse_dates' parameter
    is a non-boolean scalar. Raises a ValueError if
    that is the case.
    """
    ...

class ParserBase(object):
    def __init__(self, kwds):
        self.names = ...
        self.orig_names = ...
        self.prefix = ...
        self.index_col = ...
        self.index_names = ...
        self.col_names = ...
        self.parse_dates = ...
        self.date_parser = ...
        self.dayfirst = ...
        self.keep_date_col = ...
        self.na_values = ...
        self.na_fvalues = ...
        self.na_filter = ...
        self.true_values = ...
        self.false_values = ...
        self.as_recarray = ...
        self.tupleize_cols = ...
        self.mangle_dupe_cols = ...
        self.infer_datetime_format = ...
        self.header = ...
        self.handles = ...
    
    def close(self):
        ...
    
    @property
    def _has_complex_date_col(self):
        ...
    
    def _should_parse_dates(self, i):
        ...
    
    def _extract_multi_indexer_columns(self, header, index_names, col_names, passed_names: bool = ...):
        """ extract and return the names, index_names, col_names
            header is a list-of-lists returned from the parsers """
        ...
    
    def _maybe_dedup_names(self, names):
        ...
    
    def _maybe_make_multi_index_columns(self, columns, col_names: Optional[Any] = ...):
        ...
    
    def _make_index(self, data, alldata, columns, indexnamerow: bool = ...):
        ...
    
    _implicit_index = ...
    def _get_simple_index(self, data, columns):
        ...
    
    def _get_complex_date_index(self, data, col_names):
        ...
    
    def _agg_index(self, index, try_parse_dates: bool = ...):
        ...
    
    def _convert_to_ndarrays(self, dct, na_values, na_fvalues, verbose: bool = ..., converters: Optional[Any] = ..., dtypes: Optional[Any] = ...):
        ...
    
    def _infer_types(self, values, na_values, try_num_bool: bool = ...):
        """
        Infer types of values, possibly casting

        Parameters
        ----------
        values : ndarray
        na_values : set
        try_num_bool : bool, default try
           try to cast values to numeric (first preference) or boolean

        Returns:
        --------
        converted : ndarray
        na_count : int
        """
        ...
    
    def _cast_types(self, values, cast_type, column):
        """
        Cast values to specified type

        Parameters
        ----------
        values : ndarray
        cast_type : string or np.dtype
           dtype to cast values to
        column : string
            column name - used only for error reporting

        Returns
        -------
        converted : ndarray
        """
        ...
    
    def _do_date_conversions(self, names, data):
        ...
    


class CParserWrapper(ParserBase):
    """

    """
    def __init__(self, src, **kwds):
        self.kwds = ...
        self.orig_names = ...
        self.orig_names = ...
    
    def close(self):
        ...
    
    def _set_noconvert_columns(self):
        """
        Set the columns that should not undergo dtype conversions.

        Currently, any column that is involved with date parsing will not
        undergo such conversions.
        """
        ...
    
    def set_error_bad_lines(self, status):
        ...
    
    def read(self, nrows: Optional[Any] = ...):
        ...
    
    def _filter_usecols(self, names):
        ...
    
    def _get_index_names(self):
        ...
    
    def _maybe_parse_dates(self, values, index, try_parse_dates: bool = ...):
        ...
    


def TextParser(*args, **kwds):
    """
    Converts lists of lists/tuples into DataFrames with proper type inference
    and optional (e.g. string to datetime) conversion. Also enables iterating
    lazily over chunks of large files

    Parameters
    ----------
    data : file-like object or list
    delimiter : separator character to use
    dialect : str or csv.Dialect instance, default None
        Ignored if delimiter is longer than 1 character
    names : sequence, default
    header : int, default 0
        Row to use to parse column labels. Defaults to the first row. Prior
        rows will be discarded
    index_col : int or list, default None
        Column or columns to use as the (possibly hierarchical) index
    has_index_names: boolean, default False
        True if the cols defined in index_col have an index name and are
        not in the header
    na_values : scalar, str, list-like, or dict, default None
        Additional strings to recognize as NA/NaN.
    keep_default_na : bool, default True
    thousands : str, default None
        Thousands separator
    comment : str, default None
        Comment out remainder of line
    parse_dates : boolean, default False
    keep_date_col : boolean, default False
    date_parser : function, default None
    skiprows : list of integers
        Row numbers to skip
    skipfooter : int
        Number of line at bottom of file to skip
    converters : dict, default None
        Dict of functions for converting values in certain columns. Keys can
        either be integers or column labels, values are functions that take one
        input argument, the cell (not column) content, and return the
        transformed content.
    encoding : string, default None
        Encoding to use for UTF when reading/writing (ex. 'utf-8')
    squeeze : boolean, default False
        returns Series if only one column
    infer_datetime_format: boolean, default False
        If True and `parse_dates` is True for a column, try to infer the
        datetime format based on the first datetime string. If the format
        can be inferred, there often will be a large parsing speed-up.
    float_precision : string, default None
        Specifies which converter the C engine should use for floating-point
        values. The options are None for the ordinary converter,
        'high' for the high-precision converter, and 'round_trip' for the
        round-trip converter.
    """
    ...

def count_empty_vals(vals):
    ...

class PythonParser(ParserBase):
    def __init__(self, f, **kwds):
        """
        Workhorse function for processing nested list into DataFrame

        Should be replaced by np.genfromtxt eventually?
        """
        self.data = ...
        self.buf = ...
        self.pos = ...
        self.line_pos = ...
        self.encoding = ...
        self.compression = ...
        self.memory_map = ...
        self.skiprows = ...
        self.skipfooter = ...
        self.delimiter = ...
        self.quotechar = ...
        self.escapechar = ...
        self.doublequote = ...
        self.skipinitialspace = ...
        self.lineterminator = ...
        self.quoting = ...
        self.skip_blank_lines = ...
        self.warn_bad_lines = ...
        self.error_bad_lines = ...
        self.names_passed = ...
        self.has_index_names = ...
        self.verbose = ...
        self.converters = ...
        self.dtype = ...
        self.compact_ints = ...
        self.use_unsigned = ...
        self.thousands = ...
        self.decimal = ...
        self.comment = ...
        self.orig_names = ...
    
    def _set_no_thousands_columns(self):
        ...
    
    def _make_reader(self, f):
        self.data = ...
    
    def read(self, rows: Optional[Any] = ...):
        ...
    
    def _exclude_implicit_index(self, alldata):
        ...
    
    def get_chunk(self, size: Optional[Any] = ...):
        ...
    
    def _convert_data(self, data):
        ...
    
    def _to_recarray(self, data, columns):
        ...
    
    def _infer_columns(self):
        ...
    
    def _handle_usecols(self, columns, usecols_key):
        """
        Sets self._col_indices

        usecols_key is used if there are string usecols.
        """
        ...
    
    def _buffered_line(self):
        """
        Return a line from buffer, filling buffer if required.
        """
        ...
    
    def _check_for_bom(self, first_row):
        """
        Checks whether the file begins with the BOM character.
        If it does, remove it. In addition, if there is quoting
        in the field subsequent to the BOM, remove it as well
        because it technically takes place at the beginning of
        the name, not the middle of it.
        """
        ...
    
    def _is_line_empty(self, line):
        """
        Check if a line is empty or not.

        Parameters
        ----------
        line : str, array-like
            The line of data to check.

        Returns
        -------
        boolean : Whether or not the line is empty.
        """
        ...
    
    def _next_line(self):
        ...
    
    def _alert_malformed(self, msg, row_num):
        """
        Alert a user about a malformed row.

        If `self.error_bad_lines` is True, the alert will be `ParserError`.
        If `self.warn_bad_lines` is True, the alert will be printed out.

        Parameters
        ----------
        msg : The error message to display.
        row_num : The row number where the parsing error occurred.
                  Because this row number is displayed, we 1-index,
                  even though we 0-index internally.
        """
        ...
    
    def _next_iter_line(self, row_num):
        """
        Wrapper around iterating through `self.data` (CSV source).

        When a CSV error is raised, we check for specific
        error messages that allow us to customize the
        error message displayed to the user.

        Parameters
        ----------
        row_num : The row number of the line being parsed.
        """
        ...
    
    def _check_comments(self, lines):
        ...
    
    def _remove_empty_lines(self, lines):
        """
        Iterate through the lines and remove any that are
        either empty or contain only one whitespace value

        Parameters
        ----------
        lines : array-like
            The array of lines that we are to filter.

        Returns
        -------
        filtered_lines : array-like
            The same array of lines with the "empty" ones removed.
        """
        ...
    
    def _check_thousands(self, lines):
        ...
    
    def _search_replace_num_columns(self, lines, search, replace):
        ...
    
    def _check_decimal(self, lines):
        ...
    
    def _clear_buffer(self):
        self.buf = ...
    
    _implicit_index = ...
    def _get_index_name(self, columns):
        """
        Try several cases to get lines:

        0) There are headers on row 0 and row 1 and their
        total summed lengths equals the length of the next line.
        Treat row 0 as columns and row 1 as indices
        1) Look for implicit index: there are more columns
        on row 1 than row 0. If this is true, assume that row
        1 lists index columns and row 0 lists normal columns.
        2) Get index from the columns if it was listed.
        """
        ...
    
    def _rows_to_cols(self, content):
        ...
    
    def _get_lines(self, rows: Optional[Any] = ...):
        ...
    


def _make_date_converter(date_parser: Optional[Any] = ..., dayfirst: bool = ..., infer_datetime_format: bool = ...):
    ...

def _process_date_conversion(data_dict, converter, parse_spec, index_col, index_names, columns, keep_date_col: bool = ...):
    ...

def _try_convert_dates(parser, colspec, data_dict, columns):
    ...

def _clean_na_values(na_values, keep_default_na: bool = ...):
    ...

def _clean_index_names(columns, index_col):
    ...

def _get_empty_meta(columns, index_col, index_names, dtype: Optional[Any] = ...):
    ...

def _floatify_na_values(na_values):
    ...

def _stringify_na_values(na_values):
    """ return a stringified and numeric for these values """
    ...

def _get_na_values(col, na_values, na_fvalues):
    ...

def _get_col_names(colspec, columns):
    ...

def _concat_date_cols(date_cols):
    ...

class FixedWidthReader(BaseIterator):
    """
    A reader of fixed-width lines.
    """
    def __init__(self, f, colspecs, delimiter, comment, skiprows: Optional[Any] = ...):
        self.f = ...
        self.buffer = ...
        self.delimiter = ...
        self.comment = ...
    
    def get_rows(self, n, skiprows: Optional[Any] = ...):
        """
        Read rows from self.f, skipping as specified.

        We distinguish buffer_rows (the first <= n lines)
        from the rows returned to detect_colspecs because
        it's simpler to leave the other locations with
        skiprows logic alone than to modify them to deal
        with the fact we skipped some rows here as well.

        Parameters
        ----------
        n : int
            Number of rows to read from self.f, not counting
            rows that are skipped.
        skiprows: set, optional
            Indices of rows to skip.

        Returns
        -------
        detect_rows : list of str
            A list containing the rows to read.

        """
        self.buffer = ...
    
    def detect_colspecs(self, n=..., skiprows: Optional[Any] = ...):
        ...
    
    def __next__(self):
        ...
    


class FixedWidthFieldParser(PythonParser):
    """
    Specialization that Converts fixed-width fields into DataFrames.
    See PythonParser for details.
    """
    def __init__(self, f, **kwds):
        self.colspecs = ...
    
    def _make_reader(self, f):
        self.data = ...
    


