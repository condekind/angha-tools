"""
This type stub file was generated by pyright.
"""

from datetime import datetime
from pandas._libs import tslib
from typing import Any, Optional

def _guess_datetime_format_for_array(arr, **kwargs):
    ...

def to_datetime(arg, errors=..., dayfirst: bool = ..., yearfirst: bool = ..., utc: Optional[Any] = ..., box: bool = ..., format: Optional[Any] = ..., exact: bool = ..., unit: Optional[Any] = ..., infer_datetime_format: bool = ..., origin=...):
    """
    Convert argument to datetime.

    Parameters
    ----------
    arg : integer, float, string, datetime, list, tuple, 1-d array, Series

        .. versionadded: 0.18.1

           or DataFrame/dict-like

    errors : {'ignore', 'raise', 'coerce'}, default 'raise'

        - If 'raise', then invalid parsing will raise an exception
        - If 'coerce', then invalid parsing will be set as NaT
        - If 'ignore', then invalid parsing will return the input
    dayfirst : boolean, default False
        Specify a date parse order if `arg` is str or its list-likes.
        If True, parses dates with the day first, eg 10/11/12 is parsed as
        2012-11-10.
        Warning: dayfirst=True is not strict, but will prefer to parse
        with day first (this is a known bug, based on dateutil behavior).
    yearfirst : boolean, default False
        Specify a date parse order if `arg` is str or its list-likes.

        - If True parses dates with the year first, eg 10/11/12 is parsed as
          2010-11-12.
        - If both dayfirst and yearfirst are True, yearfirst is preceded (same
          as dateutil).

        Warning: yearfirst=True is not strict, but will prefer to parse
        with year first (this is a known bug, based on dateutil beahavior).

        .. versionadded: 0.16.1

    utc : boolean, default None
        Return UTC DatetimeIndex if True (converting any tz-aware
        datetime.datetime objects as well).
    box : boolean, default True

        - If True returns a DatetimeIndex
        - If False returns ndarray of values.
    format : string, default None
        strftime to parse time, eg "%d/%m/%Y", note that "%f" will parse
        all the way up to nanoseconds.
    exact : boolean, True by default

        - If True, require an exact format match.
        - If False, allow the format to match anywhere in the target string.

    unit : string, default 'ns'
        unit of the arg (D,s,ms,us,ns) denote the unit, which is an
        integer or float number. This will be based off the origin.
        Example, with unit='ms' and origin='unix' (the default), this
        would calculate the number of milliseconds to the unix epoch start.
    infer_datetime_format : boolean, default False
        If True and no `format` is given, attempt to infer the format of the
        datetime strings, and if it can be inferred, switch to a faster
        method of parsing them. In some cases this can increase the parsing
        speed by ~5-10x.
    origin : scalar, default is 'unix'
        Define the reference date. The numeric values would be parsed as number
        of units (defined by `unit`) since this reference date.

        - If 'unix' (or POSIX) time; origin is set to 1970-01-01.
        - If 'julian', unit must be 'D', and origin is set to beginning of
          Julian Calendar. Julian day number 0 is assigned to the day starting
          at noon on January 1, 4713 BC.
        - If Timestamp convertible, origin is set to Timestamp identified by
          origin.

        .. versionadded: 0.20.0

    Returns
    -------
    ret : datetime if parsing succeeded.
        Return type depends on input:

        - list-like: DatetimeIndex
        - Series: Series of datetime64 dtype
        - scalar: Timestamp

        In case when it is not possible to return designated types (e.g. when
        any element of input is before Timestamp.min or after Timestamp.max)
        return will have datetime.datetime type (or correspoding array/Series).

    Examples
    --------

    Assembling a datetime from multiple columns of a DataFrame. The keys can be
    common abbreviations like ['year', 'month', 'day', 'minute', 'second',
    'ms', 'us', 'ns']) or plurals of the same

    >>> df = pd.DataFrame({'year': [2015, 2016],
                           'month': [2, 3],
                           'day': [4, 5]})
    >>> pd.to_datetime(df)
    0   2015-02-04
    1   2016-03-05
    dtype: datetime64[ns]

    If a date does not meet the `timestamp limitations
    <http://pandas.pydata.org/pandas-docs/stable/timeseries.html
    #timeseries-timestamp-limits>`_, passing errors='ignore'
    will return the original input instead of raising any exception.

    Passing errors='coerce' will force an out-of-bounds date to NaT,
    in addition to forcing non-dates (or non-parseable dates) to NaT.

    >>> pd.to_datetime('13000101', format='%Y%m%d', errors='ignore')
    datetime.datetime(1300, 1, 1, 0, 0)
    >>> pd.to_datetime('13000101', format='%Y%m%d', errors='coerce')
    NaT

    Passing infer_datetime_format=True can often-times speedup a parsing
    if its not an ISO8601 format exactly, but in a regular format.

    >>> s = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000']*1000)

    >>> s.head()
    0    3/11/2000
    1    3/12/2000
    2    3/13/2000
    3    3/11/2000
    4    3/12/2000
    dtype: object

    >>> %timeit pd.to_datetime(s,infer_datetime_format=True)
    100 loops, best of 3: 10.4 ms per loop

    >>> %timeit pd.to_datetime(s,infer_datetime_format=False)
    1 loop, best of 3: 471 ms per loop

    Using a unix epoch time

    >>> pd.to_datetime(1490195805, unit='s')
    Timestamp('2017-03-22 15:16:45')
    >>> pd.to_datetime(1490195805433502912, unit='ns')
    Timestamp('2017-03-22 15:16:45.433502912')

    .. warning:: For float arg, precision rounding might happen. To prevent
        unexpected behavior use a fixed-width exact type.

    Using a non-unix epoch origin

    >>> pd.to_datetime([1, 2, 3], unit='D',
                       origin=pd.Timestamp('1960-01-01'))
    0    1960-01-02
    1    1960-01-03
    2    1960-01-04

    See also
    --------
    pandas.DataFrame.astype : Cast argument to a specified dtype.
    pandas.to_timedelta : Convert argument to timedelta.
    """
    ...

_unit_map = { 'year': 'year','years': 'year','month': 'month','months': 'month','day': 'day','days': 'day','hour': 'h','hours': 'h','minute': 'm','minutes': 'm','second': 's','seconds': 's','ms': 'ms','millisecond': 'ms','milliseconds': 'ms','us': 'us','microsecond': 'us','microseconds': 'us','ns': 'ns','nanosecond': 'ns','nanoseconds': 'ns' }
def _assemble_from_unit_mappings(arg, errors):
    """
    assemble the unit specifed fields from the arg (DataFrame)
    Return a Series for actual parsing

    Parameters
    ----------
    arg : DataFrame
    errors : {'ignore', 'raise', 'coerce'}, default 'raise'

        - If 'raise', then invalid parsing will raise an exception
        - If 'coerce', then invalid parsing will be set as NaT
        - If 'ignore', then invalid parsing will return the input

    Returns
    -------
    Series
    """
    ...

def _attempt_YYYYMMDD(arg, errors):
    """ try to parse the YYYYMMDD/%Y%m%d format, try to deal with NaT-like,
        arg is a passed in as an object dtype, but could really be ints/strings
        with nan-like/or floats (e.g. with nan)

    Parameters
    ----------
    arg : passed value
    errors : 'raise','ignore','coerce'
    """
    ...

normalize_date = tslib.normalize_date
_time_formats = ["%H:%M", "%H%M", "%I:%M%p", "%I%M%p", "%H:%M:%S", "%H%M%S", "%I:%M:%S%p", "%I%M%S%p"]
def _guess_time_format_for_array(arr):
    ...

def to_time(arg, format: Optional[Any] = ..., infer_time_format: bool = ..., errors=...):
    """
    Parse time strings to time objects using fixed strptime formats ("%H:%M",
    "%H%M", "%I:%M%p", "%I%M%p", "%H:%M:%S", "%H%M%S", "%I:%M:%S%p",
    "%I%M%S%p")

    Use infer_time_format if all the strings are in the same format to speed
    up conversion.

    Parameters
    ----------
    arg : string in time format, datetime.time, list, tuple, 1-d array,  Series
    format : str, default None
        Format used to convert arg into a time object.  If None, fixed formats
        are used.
    infer_time_format: bool, default False
        Infer the time format based on the first non-NaN element.  If all
        strings are in the same format, this will speed up conversion.
    errors : {'ignore', 'raise', 'coerce'}, default 'raise'
        - If 'raise', then invalid parsing will raise an exception
        - If 'coerce', then invalid parsing will be set as None
        - If 'ignore', then invalid parsing will return the input

    Returns
    -------
    datetime.time
    """
    ...

def format(dt):
    """Returns date in YYYYMMDD format."""
    ...

OLE_TIME_ZERO = datetime(1899, 12, 30, 0, 0, 0)
def ole2datetime(oledt):
    """function for converting excel date to normal date format"""
    ...

