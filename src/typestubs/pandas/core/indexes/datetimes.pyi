"""
This type stub file was generated by pyright.
"""

from datetime import datetime, time
from pandas.core.base import _shared_docs
from pandas.core.indexes.base import _index_shared_docs
from pandas.core.indexes.numeric import Int64Index
from pandas.core.indexes.datetimelike import DatelikeOps, DatetimeIndexOpsMixin, TimelikeOps
from pandas.util._decorators import Appender, Substitution, cache_readonly, deprecate_kwarg
from pandas._libs import Timestamp
from typing import Any, Optional

def _field_accessor(name, field, docstring: Optional[Any] = ...):
    ...

def _dt_index_cmp(opname, nat_result: bool = ...):
    """
    Wrap comparison operations to convert datetime-like to datetime64
    """
    ...

def _ensure_datetime64(other):
    ...

_midnight = time(0, 0)
def _new_DatetimeIndex(cls, d):
    """ This is called upon unpickling, rather than the default which doesn't
    have arguments and breaks __new__ """
    ...

class DatetimeIndex(DatelikeOps, TimelikeOps, DatetimeIndexOpsMixin, Int64Index):
    """
    Immutable ndarray of datetime64 data, represented internally as int64, and
    which can be boxed to Timestamp objects that are subclasses of datetime and
    carry metadata such as frequency information.

    Parameters
    ----------
    data  : array-like (1-dimensional), optional
        Optional datetime-like data to construct index with
    copy  : bool
        Make a copy of input ndarray
    freq : string or pandas offset object, optional
        One of pandas date offset strings or corresponding objects
    start : starting value, datetime-like, optional
        If data is None, start is used as the start point in generating regular
        timestamp data.
    periods  : int, optional, > 0
        Number of periods to generate, if generating index. Takes precedence
        over end argument
    end   : end time, datetime-like, optional
        If periods is none, generated index will extend to first conforming
        time on or just past end argument
    closed : string or None, default None
        Make the interval closed with respect to the given frequency to
        the 'left', 'right', or both sides (None)
    tz : pytz.timezone or dateutil.tz.tzfile
    ambiguous : 'infer', bool-ndarray, 'NaT', default 'raise'
        - 'infer' will attempt to infer fall dst-transition hours based on
          order
        - bool-ndarray where True signifies a DST time, False signifies a
          non-DST time (note that this flag is only applicable for ambiguous
          times)
        - 'NaT' will return NaT where there are ambiguous times
        - 'raise' will raise an AmbiguousTimeError if there are ambiguous times
    infer_dst : boolean, default False
        .. deprecated:: 0.15.0
           Attempt to infer fall dst-transition hours based on order
    name : object
        Name to be stored in the index

    Notes
    -----
    To learn more about the frequency strings, please see `this link
    <http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases>`__.

    See Also
    ---------
    Index : The base pandas Index type
    TimedeltaIndex : Index of timedelta64 data
    PeriodIndex : Index of Period data
    """
    _typ = ...
    _join_precedence = ...
    def _join_i8_wrapper(joinf, **kwargs):
        ...
    
    _inner_indexer = ...
    _outer_indexer = ...
    _left_indexer = ...
    _left_indexer_unique = ...
    _arrmap = ...
    __eq__ = ...
    __ne__ = ...
    __lt__ = ...
    __gt__ = ...
    __le__ = ...
    __ge__ = ...
    _engine_type = ...
    tz = ...
    offset = ...
    _comparables = ...
    _attributes = ...
    _bool_ops = ...
    _object_ops = ...
    _field_ops = ...
    _other_ops = ...
    _datetimelike_ops = ...
    _datetimelike_methods = ...
    _is_numeric_dtype = ...
    _infer_as_myclass = ...
    @deprecate_kwarg(old_arg_name='infer_dst', new_arg_name='ambiguous', mapping={ True: 'infer',False: 'raise' })
    def __new__(cls, data: Optional[Any] = ..., freq: Optional[Any] = ..., start: Optional[Any] = ..., end: Optional[Any] = ..., periods: Optional[Any] = ..., copy: bool = ..., name: Optional[Any] = ..., tz: Optional[Any] = ..., verify_integrity: bool = ..., normalize: bool = ..., closed: Optional[Any] = ..., ambiguous=..., dtype: Optional[Any] = ..., **kwargs):
        ...
    
    @classmethod
    def _generate(cls, start, end, periods, name, offset, tz: Optional[Any] = ..., normalize: bool = ..., ambiguous=..., closed: Optional[Any] = ...):
        ...
    
    @property
    def _box_func(self):
        ...
    
    def _convert_for_op(self, value):
        """ Convert value to be insertable to ndarray """
        ...
    
    def _local_timestamps(self):
        ...
    
    @classmethod
    def _simple_new(cls, values, name: Optional[Any] = ..., freq: Optional[Any] = ..., tz: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs):
        """
        we require the we have a dtype compat for the values
        if we are passed a non-dtype compat, then coerce using the constructor
        """
        ...
    
    @property
    def tzinfo(self):
        """
        Alias for tz attribute
        """
        ...
    
    @cache_readonly
    def _timezone(self):
        """ Comparable timezone both for pytz / dateutil"""
        ...
    
    def _has_same_tz(self, other):
        ...
    
    @classmethod
    def _cached_range(cls, start: Optional[Any] = ..., end: Optional[Any] = ..., periods: Optional[Any] = ..., offset: Optional[Any] = ..., name: Optional[Any] = ...):
        ...
    
    def _mpl_repr(self):
        ...
    
    @cache_readonly
    def _is_dates_only(self):
        ...
    
    @property
    def _formatter_func(self):
        ...
    
    def __reduce__(self):
        ...
    
    def __setstate__(self, state):
        """Necessary for making this object picklable"""
        ...
    
    _unpickle_compat = ...
    def _add_datelike(self, other):
        ...
    
    def _sub_datelike(self, other):
        ...
    
    def _sub_datelike_dti(self, other):
        """subtraction of two DatetimeIndexes"""
        ...
    
    def _maybe_update_attributes(self, attrs):
        """ Update Index attributes (e.g. freq) depending on op """
        ...
    
    def _add_delta(self, delta):
        ...
    
    def _add_offset(self, offset):
        ...
    
    def _format_native_types(self, na_rep=..., date_format: Optional[Any] = ..., **kwargs):
        ...
    
    def to_datetime(self, dayfirst: bool = ...):
        ...
    
    @Appender(_index_shared_docs['astype'])
    def astype(self, dtype, copy: bool = ...):
        ...
    
    def _get_time_micros(self):
        ...
    
    def to_series(self, keep_tz: bool = ...):
        """
        Create a Series with both index and values equal to the index keys
        useful with map for returning an indexer based on an index

        Parameters
        ----------
        keep_tz : optional, defaults False.
            return the data keeping the timezone.

            If keep_tz is True:

              If the timezone is not set, the resulting
              Series will have a datetime64[ns] dtype.

              Otherwise the Series will have an datetime64[ns, tz] dtype; the
              tz will be preserved.

            If keep_tz is False:

              Series will have a datetime64[ns] dtype. TZ aware
              objects will have the tz removed.

        Returns
        -------
        Series
        """
        ...
    
    def _to_embed(self, keep_tz: bool = ...):
        """
        return an array repr of this object, potentially casting to object

        This is for internal compat
        """
        ...
    
    def to_pydatetime(self):
        """
        Return DatetimeIndex as object ndarray of datetime.datetime objects

        Returns
        -------
        datetimes : ndarray
        """
        ...
    
    def to_period(self, freq: Optional[Any] = ...):
        """
        Cast to PeriodIndex at a particular frequency
        """
        ...
    
    def snap(self, freq=...):
        """
        Snap time stamps to nearest occurring frequency

        """
        ...
    
    def union(self, other):
        """
        Specialized union for DatetimeIndex objects. If combine
        overlapping ranges with the same DateOffset, will be much
        faster than Index.union

        Parameters
        ----------
        other : DatetimeIndex or array-like

        Returns
        -------
        y : Index or DatetimeIndex
        """
        ...
    
    def to_perioddelta(self, freq):
        """
        Calcuates TimedeltaIndex of difference between index
        values and index converted to PeriodIndex at specified
        freq.  Used for vectorized offsets

        .. versionadded:: 0.17.0

        Parameters
        ----------
        freq : Period frequency

        Returns
        -------
        y : TimedeltaIndex
        """
        ...
    
    def union_many(self, others):
        """
        A bit of a hack to accelerate unioning a collection of indexes
        """
        ...
    
    def join(self, other, how=..., level: Optional[Any] = ..., return_indexers: bool = ..., sort: bool = ...):
        """
        See Index.join
        """
        ...
    
    def _maybe_utc_convert(self, other):
        ...
    
    def _wrap_joined_index(self, joined, other):
        ...
    
    def _can_fast_union(self, other):
        ...
    
    def _fast_union(self, other):
        ...
    
    def __iter__(self):
        """
        Return an iterator over the boxed values

        Returns
        -------
        Timestamps : ndarray
        """
        ...
    
    def _wrap_union_result(self, other, result):
        ...
    
    def intersection(self, other):
        """
        Specialized intersection for DatetimeIndex objects. May be much faster
        than Index.intersection

        Parameters
        ----------
        other : DatetimeIndex or array-like

        Returns
        -------
        y : Index or DatetimeIndex
        """
        ...
    
    def _parsed_string_to_bounds(self, reso, parsed):
        """
        Calculate datetime bounds for parsed time string and its resolution.

        Parameters
        ----------
        reso : Resolution
            Resolution provided by parsed string.
        parsed : datetime
            Datetime from parsed string.

        Returns
        -------
        lower, upper: pd.Timestamp

        """
        ...
    
    def _partial_date_slice(self, reso, parsed, use_lhs: bool = ..., use_rhs: bool = ...):
        ...
    
    def _maybe_promote(self, other):
        ...
    
    def get_value(self, series, key):
        """
        Fast lookup of value from 1-dimensional ndarray. Only use this if you
        know what you're doing
        """
        ...
    
    def get_value_maybe_box(self, series, key):
        ...
    
    def get_loc(self, key, method: Optional[Any] = ..., tolerance: Optional[Any] = ...):
        """
        Get integer location for requested label

        Returns
        -------
        loc : int
        """
        ...
    
    def _maybe_cast_slice_bound(self, label, side, kind):
        """
        If label is a string, cast it to datetime according to resolution.

        Parameters
        ----------
        label : object
        side : {'left', 'right'}
        kind : {'ix', 'loc', 'getitem'}

        Returns
        -------
        label :  object

        Notes
        -----
        Value of `side` parameter should be validated in caller.

        """
        ...
    
    def _get_string_slice(self, key, use_lhs: bool = ..., use_rhs: bool = ...):
        ...
    
    def slice_indexer(self, start: Optional[Any] = ..., end: Optional[Any] = ..., step: Optional[Any] = ..., kind: Optional[Any] = ...):
        """
        Return indexer for specified label slice.
        Index.slice_indexer, customized to handle time slicing.

        In addition to functionality provided by Index.slice_indexer, does the
        following:

        - if both `start` and `end` are instances of `datetime.time`, it
          invokes `indexer_between_time`
        - if `start` and `end` are both either string or None perform
          value-based selection in non-monotonic cases.

        """
        ...
    
    def _get_freq(self):
        ...
    
    def _set_freq(self, value):
        self.offset = ...
    
    freq = ...
    year = ...
    month = ...
    day = ...
    hour = ...
    minute = ...
    second = ...
    microsecond = ...
    nanosecond = ...
    weekofyear = ...
    week = ...
    dayofweek = ...
    weekday = ...
    weekday_name = ...
    dayofyear = ...
    quarter = ...
    days_in_month = ...
    daysinmonth = ...
    is_month_start = ...
    is_month_end = ...
    is_quarter_start = ...
    is_quarter_end = ...
    is_year_start = ...
    is_year_end = ...
    is_leap_year = ...
    @property
    def time(self):
        """
        Returns numpy array of datetime.time. The time part of the Timestamps.
        """
        ...
    
    @property
    def date(self):
        """
        Returns numpy array of python datetime.date objects (namely, the date
        part of Timestamps without timezone information).
        """
        ...
    
    def normalize(self):
        """
        Return DatetimeIndex with times to midnight. Length is unaltered

        Returns
        -------
        normalized : DatetimeIndex
        """
        ...
    
    @Substitution(klass='DatetimeIndex')
    @Appender(_shared_docs['searchsorted'])
    @deprecate_kwarg(old_arg_name='key', new_arg_name='value')
    def searchsorted(self, value, side=..., sorter: Optional[Any] = ...):
        ...
    
    def is_type_compatible(self, typ):
        ...
    
    @property
    def inferred_type(self):
        ...
    
    @cache_readonly
    def dtype(self):
        ...
    
    @property
    def is_all_dates(self):
        ...
    
    @cache_readonly
    def is_normalized(self):
        """
        Returns True if all of the dates are at midnight ("no time")
        """
        ...
    
    @cache_readonly
    def _resolution(self):
        ...
    
    def insert(self, loc, item):
        """
        Make new Index inserting new item at location

        Parameters
        ----------
        loc : int
        item : object
            if not either a Python datetime or a numpy integer-like, returned
            Index dtype will be object rather than datetime.

        Returns
        -------
        new_index : Index
        """
        ...
    
    def delete(self, loc):
        """
        Make a new DatetimeIndex with passed location(s) deleted.

        Parameters
        ----------
        loc: int, slice or array of ints
            Indicate which sub-arrays to remove.

        Returns
        -------
        new_index : DatetimeIndex
        """
        ...
    
    def tz_convert(self, tz):
        """
        Convert tz-aware DatetimeIndex from one time zone to another (using
        pytz/dateutil)

        Parameters
        ----------
        tz : string, pytz.timezone, dateutil.tz.tzfile or None
            Time zone for time. Corresponding timestamps would be converted to
            time zone of the TimeSeries.
            None will remove timezone holding UTC time.

        Returns
        -------
        normalized : DatetimeIndex

        Raises
        ------
        TypeError
            If DatetimeIndex is tz-naive.
        """
        ...
    
    @deprecate_kwarg(old_arg_name='infer_dst', new_arg_name='ambiguous', mapping={ True: 'infer',False: 'raise' })
    def tz_localize(self, tz, ambiguous=..., errors=...):
        """
        Localize tz-naive DatetimeIndex to given time zone (using
        pytz/dateutil), or remove timezone from tz-aware DatetimeIndex

        Parameters
        ----------
        tz : string, pytz.timezone, dateutil.tz.tzfile or None
            Time zone for time. Corresponding timestamps would be converted to
            time zone of the TimeSeries.
            None will remove timezone holding local time.
        ambiguous : 'infer', bool-ndarray, 'NaT', default 'raise'
            - 'infer' will attempt to infer fall dst-transition hours based on
              order
            - bool-ndarray where True signifies a DST time, False signifies a
              non-DST time (note that this flag is only applicable for
              ambiguous times)
            - 'NaT' will return NaT where there are ambiguous times
            - 'raise' will raise an AmbiguousTimeError if there are ambiguous
              times
        errors : 'raise', 'coerce', default 'raise'
            - 'raise' will raise a NonExistentTimeError if a timestamp is not
               valid in the specified timezone (e.g. due to a transition from
               or to DST time)
            - 'coerce' will return NaT if the timestamp can not be converted
              into the specified timezone

            .. versionadded:: 0.19.0

        infer_dst : boolean, default False
            .. deprecated:: 0.15.0
               Attempt to infer fall dst-transition hours based on order

        Returns
        -------
        localized : DatetimeIndex

        Raises
        ------
        TypeError
            If the DatetimeIndex is tz-aware and tz is not None.
        """
        ...
    
    def indexer_at_time(self, time, asof: bool = ...):
        """
        Select values at particular time of day (e.g. 9:30AM)

        Parameters
        ----------
        time : datetime.time or string

        Returns
        -------
        values_at_time : TimeSeries
        """
        ...
    
    def indexer_between_time(self, start_time, end_time, include_start: bool = ..., include_end: bool = ...):
        """
        Select values between particular times of day (e.g., 9:00-9:30AM).

        Return values of the index between two times.  If start_time or
        end_time are strings then tseries.tools.to_time is used to convert to
        a time object.

        Parameters
        ----------
        start_time, end_time : datetime.time, str
            datetime.time or string in appropriate format ("%H:%M", "%H%M",
            "%I:%M%p", "%I%M%p", "%H:%M:%S", "%H%M%S", "%I:%M:%S%p",
            "%I%M%S%p")
        include_start : boolean, default True
        include_end : boolean, default True

        Returns
        -------
        values_between_time : TimeSeries
        """
        ...
    
    def to_julian_date(self):
        """
        Convert DatetimeIndex to Float64Index of Julian Dates.
        0 Julian date is noon January 1, 4713 BC.
        http://en.wikipedia.org/wiki/Julian_day
        """
        ...
    


def _generate_regular_range(start, end, periods, offset):
    ...

def date_range(start: Optional[Any] = ..., end: Optional[Any] = ..., periods: Optional[Any] = ..., freq=..., tz: Optional[Any] = ..., normalize: bool = ..., name: Optional[Any] = ..., closed: Optional[Any] = ..., **kwargs):
    """
    Return a fixed frequency DatetimeIndex, with day (calendar) as the default
    frequency

    Parameters
    ----------
    start : string or datetime-like, default None
        Left bound for generating dates
    end : string or datetime-like, default None
        Right bound for generating dates
    periods : integer, default None
        Number of periods to generate
    freq : string or DateOffset, default 'D' (calendar daily)
        Frequency strings can have multiples, e.g. '5H'
    tz : string, default None
        Time zone name for returning localized DatetimeIndex, for example
        Asia/Hong_Kong
    normalize : bool, default False
        Normalize start/end dates to midnight before generating date range
    name : string, default None
        Name of the resulting DatetimeIndex
    closed : string, default None
        Make the interval closed with respect to the given frequency to
        the 'left', 'right', or both sides (None)

    Notes
    -----
    Of the three parameters: ``start``, ``end``, and ``periods``, exactly two
    must be specified.

    To learn more about the frequency strings, please see `this link
    <http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases>`__.

    Returns
    -------
    rng : DatetimeIndex
    """
    ...

def bdate_range(start: Optional[Any] = ..., end: Optional[Any] = ..., periods: Optional[Any] = ..., freq=..., tz: Optional[Any] = ..., normalize: bool = ..., name: Optional[Any] = ..., weekmask: Optional[Any] = ..., holidays: Optional[Any] = ..., closed: Optional[Any] = ..., **kwargs):
    """
    Return a fixed frequency DatetimeIndex, with business day as the default
    frequency

    Parameters
    ----------
    start : string or datetime-like, default None
        Left bound for generating dates
    end : string or datetime-like, default None
        Right bound for generating dates
    periods : integer, default None
        Number of periods to generate
    freq : string or DateOffset, default 'B' (business daily)
        Frequency strings can have multiples, e.g. '5H'
    tz : string or None
        Time zone name for returning localized DatetimeIndex, for example
        Asia/Beijing
    normalize : bool, default False
        Normalize start/end dates to midnight before generating date range
    name : string, default None
        Name of the resulting DatetimeIndex
    weekmask : string or None, default None
        Weekmask of valid business days, passed to ``numpy.busdaycalendar``,
        only used when custom frequency strings are passed.  The default
        value None is equivalent to 'Mon Tue Wed Thu Fri'

        .. versionadded:: 0.21.0

    holidays : list-like or None, default None
        Dates to exclude from the set of valid business days, passed to
        ``numpy.busdaycalendar``, only used when custom frequency strings
        are passed

        .. versionadded:: 0.21.0

    closed : string, default None
        Make the interval closed with respect to the given frequency to
        the 'left', 'right', or both sides (None)

    Notes
    -----
    Of the three parameters: ``start``, ``end``, and ``periods``, exactly two
    must be specified.

    To learn more about the frequency strings, please see `this link
    <http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases>`__.

    Returns
    -------
    rng : DatetimeIndex
    """
    ...

def cdate_range(start: Optional[Any] = ..., end: Optional[Any] = ..., periods: Optional[Any] = ..., freq=..., tz: Optional[Any] = ..., normalize: bool = ..., name: Optional[Any] = ..., closed: Optional[Any] = ..., **kwargs):
    """
    Return a fixed frequency DatetimeIndex, with CustomBusinessDay as the
    default frequency

    .. deprecated:: 0.21.0

    Parameters
    ----------
    start : string or datetime-like, default None
        Left bound for generating dates
    end : string or datetime-like, default None
        Right bound for generating dates
    periods : integer, default None
        Number of periods to generate
    freq : string or DateOffset, default 'C' (CustomBusinessDay)
        Frequency strings can have multiples, e.g. '5H'
    tz : string, default None
        Time zone name for returning localized DatetimeIndex, for example
        Asia/Beijing
    normalize : bool, default False
        Normalize start/end dates to midnight before generating date range
    name : string, default None
        Name of the resulting DatetimeIndex
    weekmask : string, Default 'Mon Tue Wed Thu Fri'
        weekmask of valid business days, passed to ``numpy.busdaycalendar``
    holidays : list
        list/array of dates to exclude from the set of valid business days,
        passed to ``numpy.busdaycalendar``
    closed : string, default None
        Make the interval closed with respect to the given frequency to
        the 'left', 'right', or both sides (None)

    Notes
    -----
    Of the three parameters: ``start``, ``end``, and ``periods``, exactly two
    must be specified.

    To learn more about the frequency strings, please see `this link
    <http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases>`__.

    Returns
    -------
    rng : DatetimeIndex
    """
    ...

def _to_m8(key, tz: Optional[Any] = ...):
    """
    Timestamp-like => dt64
    """
    ...

_CACHE_START = Timestamp(datetime(1950, 1, 1))
_CACHE_END = Timestamp(datetime(2030, 1, 1))
_daterange_cache = {  }
def _naive_in_cache_range(start, end):
    ...

def _in_range(start, end, rng_start, rng_end):
    ...

def _use_cached_range(offset, _normalized, start, end):
    ...

def _time_to_micros(time):
    ...

