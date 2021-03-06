"""
This type stub file was generated by pyright.
"""

import abc
from pandas.io.common import _NA_VALUES
from pandas.compat import add_metaclass
from pandas.util._decorators import Appender, deprecate_kwarg
from textwrap import fill
from typing import Any, Optional

"""
Module parse to/from Excel
"""
__all__ = ["read_excel", "ExcelWriter", "ExcelFile"]
_writer_extensions = ["xlsx", "xls", "xlsm"]
_writers = {  }
_read_excel_doc = """
Read an Excel table into a pandas DataFrame

Parameters
----------
io : string, path object (pathlib.Path or py._path.local.LocalPath),
    file-like object, pandas ExcelFile, or xlrd workbook.
    The string could be a URL. Valid URL schemes include http, ftp, s3,
    and file. For file URLs, a host is expected. For instance, a local
    file could be file://localhost/path/to/workbook.xlsx
sheet_name : string, int, mixed list of strings/ints, or None, default 0

    Strings are used for sheet names, Integers are used in zero-indexed
    sheet positions.

    Lists of strings/integers are used to request multiple sheets.

    Specify None to get all sheets.

    str|int -> DataFrame is returned.
    list|None -> Dict of DataFrames is returned, with keys representing
    sheets.

    Available Cases

    * Defaults to 0 -> 1st sheet as a DataFrame
    * 1 -> 2nd sheet as a DataFrame
    * "Sheet1" -> 1st sheet as a DataFrame
    * [0,1,"Sheet5"] -> 1st, 2nd & 5th sheet as a dictionary of DataFrames
    * None -> All sheets as a dictionary of DataFrames

sheetname : string, int, mixed list of strings/ints, or None, default 0
    .. deprecated:: 0.21.0
       Use `sheet_name` instead

header : int, list of ints, default 0
    Row (0-indexed) to use for the column labels of the parsed
    DataFrame. If a list of integers is passed those row positions will
    be combined into a ``MultiIndex``. Use None if there is no header.
skiprows : list-like
    Rows to skip at the beginning (0-indexed)
skip_footer : int, default 0
    Rows at the end to skip (0-indexed)
index_col : int, list of ints, default None
    Column (0-indexed) to use as the row labels of the DataFrame.
    Pass None if there is no such column.  If a list is passed,
    those columns will be combined into a ``MultiIndex``.  If a
    subset of data is selected with ``usecols``, index_col
    is based on the subset.
names : array-like, default None
    List of column names to use. If file contains no header row,
    then you should explicitly pass header=None
converters : dict, default None
    Dict of functions for converting values in certain columns. Keys can
    either be integers or column labels, values are functions that take one
    input argument, the Excel cell content, and return the transformed
    content.
dtype : Type name or dict of column -> type, default None
    Data type for data or columns. E.g. {'a': np.float64, 'b': np.int32}
    Use `object` to preserve data as stored in Excel and not interpret dtype.
    If converters are specified, they will be applied INSTEAD
    of dtype conversion.

    .. versionadded:: 0.20.0

true_values : list, default None
    Values to consider as True

    .. versionadded:: 0.19.0

false_values : list, default None
    Values to consider as False

    .. versionadded:: 0.19.0

parse_cols : int or list, default None
    .. deprecated:: 0.21.0
       Pass in `usecols` instead.

usecols : int or list, default None
    * If None then parse all columns,
    * If int then indicates last column to be parsed
    * If list of ints then indicates list of column numbers to be parsed
    * If string then indicates comma separated list of Excel column letters and
      column ranges (e.g. "A:E" or "A,C,E:F").  Ranges are inclusive of
      both sides.
squeeze : boolean, default False
    If the parsed data only contains one column then return a Series
na_values : scalar, str, list-like, or dict, default None
    Additional strings to recognize as NA/NaN. If dict passed, specific
    per-column NA values. By default the following values are interpreted
    as NaN: '""" + fill("', '".join(sorted(_NA_VALUES)), 70) + """'.
thousands : str, default None
    Thousands separator for parsing string columns to numeric.  Note that
    this parameter is only necessary for columns stored as TEXT in Excel,
    any numeric columns will automatically be parsed, regardless of display
    format.
keep_default_na : bool, default True
    If na_values are specified and keep_default_na is False the default NaN
    values are overridden, otherwise they're appended to.
verbose : boolean, default False
    Indicate number of NA values placed in non-numeric columns
engine: string, default None
    If io is not a buffer or path, this must be set to identify io.
    Acceptable values are None or xlrd
convert_float : boolean, default True
    convert integral floats to int (i.e., 1.0 --> 1). If False, all numeric
    data will be read in as floats: Excel stores all numbers as floats
    internally

Returns
-------
parsed : DataFrame or Dict of DataFrames
    DataFrame from the passed in Excel file.  See notes in sheet_name
    argument for more information on when a Dict of Dataframes is returned.
"""
def register_writer(klass):
    """Adds engine to the excel writer registry. You must use this method to
    integrate with ``to_excel``. Also adds config options for any new
    ``supported_extensions`` defined on the writer."""
    ...

def _get_default_writer(ext):
    ...

def get_writer(engine_name):
    ...

@Appender(_read_excel_doc)
@deprecate_kwarg("parse_cols", "usecols")
def read_excel(io, sheet_name=..., header=..., skiprows: Optional[Any] = ..., skip_footer=..., index_col: Optional[Any] = ..., names: Optional[Any] = ..., usecols: Optional[Any] = ..., parse_dates: bool = ..., date_parser: Optional[Any] = ..., na_values: Optional[Any] = ..., thousands: Optional[Any] = ..., convert_float: bool = ..., converters: Optional[Any] = ..., dtype: Optional[Any] = ..., true_values: Optional[Any] = ..., false_values: Optional[Any] = ..., engine: Optional[Any] = ..., squeeze: bool = ..., **kwds):
    ...

class ExcelFile(object):
    """
    Class for parsing tabular excel sheets into DataFrame objects.
    Uses xlrd. See read_excel for more documentation

    Parameters
    ----------
    io : string, path object (pathlib.Path or py._path.local.LocalPath),
        file-like object or xlrd workbook
        If a string or path object, expected to be a path to xls or xlsx file
    engine: string, default None
        If io is not a buffer or path, this must be set to identify io.
        Acceptable values are None or xlrd
    """
    def __init__(self, io, **kwds):
        self.io = ...
    
    def __fspath__(self):
        ...
    
    def parse(self, sheet_name=..., header=..., skiprows: Optional[Any] = ..., skip_footer=..., names: Optional[Any] = ..., index_col: Optional[Any] = ..., usecols: Optional[Any] = ..., parse_dates: bool = ..., date_parser: Optional[Any] = ..., na_values: Optional[Any] = ..., thousands: Optional[Any] = ..., convert_float: bool = ..., converters: Optional[Any] = ..., true_values: Optional[Any] = ..., false_values: Optional[Any] = ..., squeeze: bool = ..., **kwds):
        """
        Parse specified sheet(s) into a DataFrame

        Equivalent to read_excel(ExcelFile, ...)  See the read_excel
        docstring for more info on accepted parameters
        """
        ...
    
    def _should_parse(self, i, usecols):
        ...
    
    def _parse_excel(self, sheetname=..., header=..., skiprows: Optional[Any] = ..., names: Optional[Any] = ..., skip_footer=..., index_col: Optional[Any] = ..., usecols: Optional[Any] = ..., parse_dates: bool = ..., date_parser: Optional[Any] = ..., na_values: Optional[Any] = ..., thousands: Optional[Any] = ..., convert_float: bool = ..., true_values: Optional[Any] = ..., false_values: Optional[Any] = ..., verbose: bool = ..., dtype: Optional[Any] = ..., squeeze: bool = ..., **kwds):
        ...
    
    @property
    def sheet_names(self):
        ...
    
    def close(self):
        """close io if necessary"""
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    


def _validate_freeze_panes(freeze_panes):
    ...

def _trim_excel_header(row):
    ...

def _fill_mi_header(row, control_row):
    """Forward fills blank entries in row, but only inside the same parent index

    Used for creating headers in Multiindex.
    Parameters
    ----------
    row : list
        List of items in a single row.
    control_row : list of boolean
        Helps to determine if particular column is in same parent index as the
        previous value. Used to stop propagation of empty cells between
        different indexes.

    Returns
    ----------
    Returns changed row and control_row
    """
    ...

def _pop_header_name(row, index_col):
    """ (header, new_data) for header rows in MultiIndex parsing"""
    ...

def _conv_value(val):
    ...

@add_metaclass(abc.ABCMeta)
class ExcelWriter(object):
    """
    Class for writing DataFrame objects into excel sheets, default is to use
    xlwt for xls, openpyxl for xlsx.  See DataFrame.to_excel for typical usage.

    Parameters
    ----------
    path : string
        Path to xls or xlsx file.
    engine : string (optional)
        Engine to use for writing. If None, defaults to
        ``io.excel.<extension>.writer``.  NOTE: can only be passed as a keyword
        argument.
    date_format : string, default None
        Format string for dates written into Excel files (e.g. 'YYYY-MM-DD')
    datetime_format : string, default None
        Format string for datetime objects written into Excel files
        (e.g. 'YYYY-MM-DD HH:MM:SS')

    Notes
    -----
    For compatibility with CSV writers, ExcelWriter serializes lists
    and dicts to strings before writing.
    """
    def __new__(cls, path, engine: Optional[Any] = ..., **kwargs):
        ...
    
    book = ...
    curr_sheet = ...
    path = ...
    @abc.abstractproperty
    def supported_extensions(self):
        "extensions that writer engine supports"
        ...
    
    @abc.abstractproperty
    def engine(self):
        "name of engine"
        ...
    
    @abc.abstractmethod
    def write_cells(self, cells, sheet_name: Optional[Any] = ..., startrow=..., startcol=..., freeze_panes: Optional[Any] = ...):
        """
        Write given formated cells into Excel an excel sheet

        Parameters
        ----------
        cells : generator
            cell of formated data to save to Excel sheet
        sheet_name : string, default None
            Name of Excel sheet, if None, then use self.cur_sheet
        startrow: upper left cell row to dump data frame
        startcol: upper left cell column to dump data frame
        freeze_panes: integer tuple of length 2
            contains the bottom-most row and right-most column to freeze
        """
        ...
    
    @abc.abstractmethod
    def save(self):
        """
        Save workbook to disk.
        """
        ...
    
    def __init__(self, path, engine: Optional[Any] = ..., date_format: Optional[Any] = ..., datetime_format: Optional[Any] = ..., **engine_kwargs):
        self.path = ...
        self.sheets = ...
        self.cur_sheet = ...
    
    def __fspath__(self):
        ...
    
    def _get_sheet_name(self, sheet_name):
        ...
    
    @classmethod
    def check_extension(cls, ext):
        """checks that path's extension against the Writer's supported
        extensions.  If it isn't supported, raises UnsupportedFiletypeError."""
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_value, traceback):
        ...
    
    def close(self):
        """synonym for save, to make it more file-like"""
        ...
    


class _Openpyxl1Writer(ExcelWriter):
    engine = ...
    supported_extensions = ...
    openpyxl_majorver = ...
    def __init__(self, path, engine: Optional[Any] = ..., **engine_kwargs):
        self.book = ...
    
    def save(self):
        """
        Save workbook to disk.
        """
        ...
    
    def write_cells(self, cells, sheet_name: Optional[Any] = ..., startrow=..., startcol=..., freeze_panes: Optional[Any] = ...):
        ...
    
    @classmethod
    def _convert_to_style(cls, style_dict):
        """
        converts a style_dict to an openpyxl style object
        Parameters
        ----------
        style_dict: style dictionary to convert
        """
        ...
    


class _OpenpyxlWriter(_Openpyxl1Writer):
    engine = ...


class _Openpyxl20Writer(_Openpyxl1Writer):
    """
    Note: Support for OpenPyxl v2 is currently EXPERIMENTAL (GH7565).
    """
    engine = ...
    openpyxl_majorver = ...
    def write_cells(self, cells, sheet_name: Optional[Any] = ..., startrow=..., startcol=..., freeze_panes: Optional[Any] = ...):
        ...
    
    @classmethod
    def _convert_to_style_kwargs(cls, style_dict):
        """
        Convert a style_dict to a set of kwargs suitable for initializing
        or updating-on-copy an openpyxl v2 style object
        Parameters
        ----------
        style_dict : dict
            A dict with zero or more of the following keys (or their synonyms).
                'font'
                'fill'
                'border' ('borders')
                'alignment'
                'number_format'
                'protection'
        Returns
        -------
        style_kwargs : dict
            A dict with the same, normalized keys as ``style_dict`` but each
            value has been replaced with a native openpyxl style object of the
            appropriate class.
        """
        ...
    
    @classmethod
    def _convert_to_color(cls, color_spec):
        """
        Convert ``color_spec`` to an openpyxl v2 Color object
        Parameters
        ----------
        color_spec : str, dict
            A 32-bit ARGB hex string, or a dict with zero or more of the
            following keys.
                'rgb'
                'indexed'
                'auto'
                'theme'
                'tint'
                'index'
                'type'
        Returns
        -------
        color : openpyxl.styles.Color
        """
        ...
    
    @classmethod
    def _convert_to_font(cls, font_dict):
        """
        Convert ``font_dict`` to an openpyxl v2 Font object
        Parameters
        ----------
        font_dict : dict
            A dict with zero or more of the following keys (or their synonyms).
                'name'
                'size' ('sz')
                'bold' ('b')
                'italic' ('i')
                'underline' ('u')
                'strikethrough' ('strike')
                'color'
                'vertAlign' ('vertalign')
                'charset'
                'scheme'
                'family'
                'outline'
                'shadow'
                'condense'
        Returns
        -------
        font : openpyxl.styles.Font
        """
        ...
    
    @classmethod
    def _convert_to_stop(cls, stop_seq):
        """
        Convert ``stop_seq`` to a list of openpyxl v2 Color objects,
        suitable for initializing the ``GradientFill`` ``stop`` parameter.
        Parameters
        ----------
        stop_seq : iterable
            An iterable that yields objects suitable for consumption by
            ``_convert_to_color``.
        Returns
        -------
        stop : list of openpyxl.styles.Color
        """
        ...
    
    @classmethod
    def _convert_to_fill(cls, fill_dict):
        """
        Convert ``fill_dict`` to an openpyxl v2 Fill object
        Parameters
        ----------
        fill_dict : dict
            A dict with one or more of the following keys (or their synonyms),
                'fill_type' ('patternType', 'patterntype')
                'start_color' ('fgColor', 'fgcolor')
                'end_color' ('bgColor', 'bgcolor')
            or one or more of the following keys (or their synonyms).
                'type' ('fill_type')
                'degree'
                'left'
                'right'
                'top'
                'bottom'
                'stop'
        Returns
        -------
        fill : openpyxl.styles.Fill
        """
        ...
    
    @classmethod
    def _convert_to_side(cls, side_spec):
        """
        Convert ``side_spec`` to an openpyxl v2 Side object
        Parameters
        ----------
        side_spec : str, dict
            A string specifying the border style, or a dict with zero or more
            of the following keys (or their synonyms).
                'style' ('border_style')
                'color'
        Returns
        -------
        side : openpyxl.styles.Side
        """
        ...
    
    @classmethod
    def _convert_to_border(cls, border_dict):
        """
        Convert ``border_dict`` to an openpyxl v2 Border object
        Parameters
        ----------
        border_dict : dict
            A dict with zero or more of the following keys (or their synonyms).
                'left'
                'right'
                'top'
                'bottom'
                'diagonal'
                'diagonal_direction'
                'vertical'
                'horizontal'
                'diagonalUp' ('diagonalup')
                'diagonalDown' ('diagonaldown')
                'outline'
        Returns
        -------
        border : openpyxl.styles.Border
        """
        ...
    
    @classmethod
    def _convert_to_alignment(cls, alignment_dict):
        """
        Convert ``alignment_dict`` to an openpyxl v2 Alignment object
        Parameters
        ----------
        alignment_dict : dict
            A dict with zero or more of the following keys (or their synonyms).
                'horizontal'
                'vertical'
                'text_rotation'
                'wrap_text'
                'shrink_to_fit'
                'indent'
        Returns
        -------
        alignment : openpyxl.styles.Alignment
        """
        ...
    
    @classmethod
    def _convert_to_number_format(cls, number_format_dict):
        """
        Convert ``number_format_dict`` to an openpyxl v2.1.0 number format
        initializer.
        Parameters
        ----------
        number_format_dict : dict
            A dict with zero or more of the following keys.
                'format_code' : str
        Returns
        -------
        number_format : str
        """
        ...
    
    @classmethod
    def _convert_to_protection(cls, protection_dict):
        """
        Convert ``protection_dict`` to an openpyxl v2 Protection object.
        Parameters
        ----------
        protection_dict : dict
            A dict with zero or more of the following keys.
                'locked'
                'hidden'
        Returns
        -------
        """
        ...
    


class _Openpyxl22Writer(_Openpyxl20Writer):
    """
    Note: Support for OpenPyxl v2.2 is currently EXPERIMENTAL (GH7565).
    """
    engine = ...
    openpyxl_majorver = ...
    def write_cells(self, cells, sheet_name: Optional[Any] = ..., startrow=..., startcol=..., freeze_panes: Optional[Any] = ...):
        ...
    


class _XlwtWriter(ExcelWriter):
    engine = ...
    supported_extensions = ...
    def __init__(self, path, engine: Optional[Any] = ..., encoding: Optional[Any] = ..., **engine_kwargs):
        self.book = ...
        self.fm_datetime = ...
        self.fm_date = ...
    
    def save(self):
        """
        Save workbook to disk.
        """
        ...
    
    def write_cells(self, cells, sheet_name: Optional[Any] = ..., startrow=..., startcol=..., freeze_panes: Optional[Any] = ...):
        ...
    
    @classmethod
    def _style_to_xlwt(cls, item, firstlevel: bool = ..., field_sep=..., line_sep=...):
        """helper which recursively generate an xlwt easy style string
        for example:

            hstyle = {"font": {"bold": True},
            "border": {"top": "thin",
                    "right": "thin",
                    "bottom": "thin",
                    "left": "thin"},
            "align": {"horiz": "center"}}
            will be converted to
            font: bold on; \
                    border: top thin, right thin, bottom thin, left thin; \
                    align: horiz center;
        """
        ...
    
    @classmethod
    def _convert_to_style(cls, style_dict, num_format_str: Optional[Any] = ...):
        """
        converts a style_dict to an xlwt style object
        Parameters
        ----------
        style_dict: style dictionary to convert
        num_format_str: optional number format string
        """
        ...
    


class _XlsxWriter(ExcelWriter):
    engine = ...
    supported_extensions = ...
    def __init__(self, path, engine: Optional[Any] = ..., date_format: Optional[Any] = ..., datetime_format: Optional[Any] = ..., **engine_kwargs):
        self.book = ...
    
    def save(self):
        """
        Save workbook to disk.
        """
        ...
    
    def write_cells(self, cells, sheet_name: Optional[Any] = ..., startrow=..., startcol=..., freeze_panes: Optional[Any] = ...):
        ...
    
    def _convert_to_style(self, style_dict, num_format_str: Optional[Any] = ...):
        """
        converts a style_dict to an xlsxwriter format object
        Parameters
        ----------
        style_dict: style dictionary to convert
        num_format_str: optional number format string
        """
        ...
    


