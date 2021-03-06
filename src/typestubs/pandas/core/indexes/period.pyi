"""
This type stub file was generated by pyright.
"""

import pandas.core.indexes.base as ibase
from pandas.core.indexes.datetimes import Int64Index
from pandas.core.indexes.datetimelike import DatelikeOps, DatetimeIndexOpsMixin
from pandas._libs import period
from pandas.core.base import _shared_docs
from pandas.core.indexes.base import _index_shared_docs
from pandas.util._decorators import Appender, Substitution, cache_readonly, deprecate_kwarg
from typing import Any, Optional

_index_doc_kwargs = dict(ibase._index_doc_kwargs)
def _field_accessor(name, alias, docstring: Optional[Any] = ...):
    ...

def dt64arr_to_periodarr(data, freq, tz):
    ...

_DIFFERENT_FREQ_INDEX = period._DIFFERENT_FREQ_INDEX
def _period_index_cmp(opname, nat_result: bool = ...):
    """
    Wrap comparison operations to convert datetime-like to datetime64
    """
    ...

def _new_PeriodIndex(cls, **d):
    ...

class PeriodIndex(DatelikeOps, DatetimeIndexOpsMixin, Int64Index):
    """
    Immutable ndarray holding ordinal values indicating regular periods in
    time such as particular years, quarters, months, etc.

    Index keys are boxed to Period objects which carries the metadata (eg,
    frequency information).

    Parameters
    ----------
    data : array-like (1-dimensional), optional
        Optional period-like data to construct index with
    copy : bool
        Make a copy of input ndarray
    freq : string or period object, optional
        One of pandas period strings or corresponding objects
    start : starting value, period-like, optional
        If data is None, used as the start point in generating regular
        period data.
    periods : int, optional, > 0
        Number of periods to generate, if generating index. Takes precedence
        over end argument
    end : end value, period-like, optional
        If periods is none, generated index will extend to first conforming
        period on or just past end argument
    year : int, array, or Series, default None
    month : int, array, or Series, default None
    quarter : int, array, or Series, default None
    day : int, array, or Series, default None
    hour : int, array, or Series, default None
    minute : int, array, or Series, default None
    second : int, array, or Series, default None
    tz : object, default None
        Timezone for converting datetime64 data to Periods
    dtype : str or PeriodDtype, default None

    Examples
    --------
    >>> idx = PeriodIndex(year=year_arr, quarter=q_arr)

    >>> idx2 = PeriodIndex(start='2000', end='2010', freq='A')

    See Also
    ---------
    Index : The base pandas Index type
    Period : Represents a period of time
    DatetimeIndex : Index with datetime64 data
    TimedeltaIndex : Index of timedelta64 data
    """
    _box_scalars = ...
    _typ = ...
    _attributes = ...
    _other_ops = ...
    _bool_ops = ...
    _object_ops = ...
    _field_ops = ...
    _datetimelike_ops = ...
    _datetimelike_methods = ...
    _is_numeric_dtype = ...
    _infer_as_myclass = ...
    freq = ...
    __eq__ = ...
    __ne__ = ...
    __lt__ = ...
    __gt__ = ...
    __le__ = ...
    __ge__ = ...
    def __new__(cls, data: Optional[Any] = ..., ordinal: Optional[Any] = ..., freq: Optional[Any] = ..., start: Optional[Any] = ..., end: Optional[Any] = ..., periods: Optional[Any] = ..., copy: bool = ..., name: Optional[Any] = ..., tz: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs):
        ...
    
    @classmethod
    def _generate_range(cls, start, end, periods, freq, fields):
        ...
    
    @classmethod
    def _simple_new(cls, values, name: Optional[Any] = ..., freq: Optional[Any] = ..., **kwargs):
        """
        Values can be any type that can be coerced to Periods.
        Ordinals in an ndarray are fastpath-ed to `_from_ordinals`
        """
        ...
    
    @classmethod
    def _from_ordinals(cls, values, name: Optional[Any] = ..., freq: Optional[Any] = ..., **kwargs):
        """
        Values should be int ordinals
        `__new__` & `_simple_new` cooerce to ordinals and call this method
        """
        ...
    
    def _shallow_copy_with_infer(self, values: Optional[Any] = ..., **kwargs):
        """ we always want to return a PeriodIndex """
        ...
    
    def _shallow_copy(self, values: Optional[Any] = ..., freq: Optional[Any] = ..., **kwargs):
        ...
    
    def _coerce_scalar_to_index(self, item):
        """
        we need to coerce a scalar to a compat for our index type

        Parameters
        ----------
        item : scalar item to coerce
        """
        ...
    
    @Appender(_index_shared_docs['__contains__'])
    def __contains__(self, key):
        ...
    
    contains = ...
    @property
    def asi8(self):
        ...
    
    @cache_readonly
    def _int64index(self):
        ...
    
    @property
    def values(self):
        ...
    
    @property
    def _values(self):
        ...
    
    def __array__(self, dtype: Optional[Any] = ...):
        ...
    
    def __array_wrap__(self, result, context: Optional[Any] = ...):
        """
        Gets called after a ufunc. Needs additional handling as
        PeriodIndex stores internal data as int dtype

        Replace this to __numpy_ufunc__ in future version
        """
        ...
    
    @property
    def _box_func(self):
        ...
    
    def _to_embed(self, keep_tz: bool = ...):
        """
        return an array repr of this object, potentially casting to object
        """
        ...
    
    @property
    def _formatter_func(self):
        ...
    
    def asof_locs(self, where, mask):
        """
        where : array of timestamps
        mask : array of booleans where data is not NA

        """
        ...
    
    @Appender(_index_shared_docs['astype'])
    def astype(self, dtype, copy: bool = ..., how=...):
        ...
    
    @Substitution(klass='PeriodIndex')
    @Appender(_shared_docs['searchsorted'])
    @deprecate_kwarg(old_arg_name='key', new_arg_name='value')
    def searchsorted(self, value, side=..., sorter: Optional[Any] = ...):
        ...
    
    @property
    def is_all_dates(self):
        ...
    
    @property
    def is_full(self):
        """
        Returns True if there are any missing periods from start to end
        """
        ...
    
    def asfreq(self, freq: Optional[Any] = ..., how=...):
        """
        Convert the PeriodIndex to the specified frequency `freq`.

        Parameters
        ----------

        freq : str
            a frequency
        how : str {'E', 'S'}
            'E', 'END', or 'FINISH' for end,
            'S', 'START', or 'BEGIN' for start.
            Whether the elements should be aligned to the end
            or start within pa period. January 31st ('END') vs.
            Janury 1st ('START') for example.

        Returns
        -------

        new : PeriodIndex with the new frequency

        Examples
        --------
        >>> pidx = pd.period_range('2010-01-01', '2015-01-01', freq='A')
        >>> pidx
        <class 'pandas.core.indexes.period.PeriodIndex'>
        [2010, ..., 2015]
        Length: 6, Freq: A-DEC

        >>> pidx.asfreq('M')
        <class 'pandas.core.indexes.period.PeriodIndex'>
        [2010-12, ..., 2015-12]
        Length: 6, Freq: M

        >>> pidx.asfreq('M', how='S')
        <class 'pandas.core.indexes.period.PeriodIndex'>
        [2010-01, ..., 2015-01]
        Length: 6, Freq: M
        """
        ...
    
    def to_datetime(self, dayfirst: bool = ...):
        """
        .. deprecated:: 0.19.0
           Use :meth:`to_timestamp` instead.

        Cast to DatetimeIndex.
        """
        ...
    
    year = ...
    month = ...
    day = ...
    hour = ...
    minute = ...
    second = ...
    weekofyear = ...
    week = ...
    dayofweek = ...
    weekday = ...
    dayofyear = ...
    quarter = ...
    qyear = ...
    days_in_month = ...
    daysinmonth = ...
    @property
    def is_leap_year(self):
        """ Logical indicating if the date belongs to a leap year """
        ...
    
    @property
    def start_time(self):
        ...
    
    @property
    def end_time(self):
        ...
    
    def _mpl_repr(self):
        ...
    
    def to_timestamp(self, freq: Optional[Any] = ..., how=...):
        """
        Cast to DatetimeIndex

        Parameters
        ----------
        freq : string or DateOffset, default 'D' for week or longer, 'S'
               otherwise
            Target frequency
        how : {'s', 'e', 'start', 'end'}

        Returns
        -------
        DatetimeIndex
        """
        ...
    
    def _maybe_convert_timedelta(self, other):
        ...
    
    def _add_delta(self, other):
        ...
    
    def _sub_datelike(self, other):
        ...
    
    def _sub_period(self, other):
        ...
    
    def shift(self, n):
        """
        Specialized shift which produces an PeriodIndex

        Parameters
        ----------
        n : int
            Periods to shift by

        Returns
        -------
        shifted : PeriodIndex
        """
        ...
    
    @cache_readonly
    def dtype(self):
        ...
    
    @property
    def inferred_type(self):
        ...
    
    def get_value(self, series, key):
        """
        Fast lookup of value from 1-dimensional ndarray. Only use this if you
        know what you're doing
        """
        ...
    
    @Appender(_index_shared_docs['get_indexer'] % _index_doc_kwargs)
    def get_indexer(self, target, method: Optional[Any] = ..., limit: Optional[Any] = ..., tolerance: Optional[Any] = ...):
        ...
    
    def _get_unique_index(self, dropna: bool = ...):
        """
        wrap Index._get_unique_index to handle NaT
        """
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
        If label is a string or a datetime, cast it to Period.ordinal according
        to resolution.

        Parameters
        ----------
        label : object
        side : {'left', 'right'}
        kind : {'ix', 'loc', 'getitem'}

        Returns
        -------
        bound : Period or object

        Notes
        -----
        Value of `side` parameter should be validated in caller.

        """
        ...
    
    def _parsed_string_to_bounds(self, reso, parsed):
        ...
    
    def _get_string_slice(self, key):
        ...
    
    def _convert_tolerance(self, tolerance, target):
        ...
    
    def insert(self, loc, item):
        ...
    
    def join(self, other, how=..., level: Optional[Any] = ..., return_indexers: bool = ..., sort: bool = ...):
        """
        See Index.join
        """
        ...
    
    def _assert_can_do_setop(self, other):
        ...
    
    def _wrap_union_result(self, other, result):
        ...
    
    def _apply_meta(self, rawarr):
        ...
    
    def _format_native_types(self, na_rep=..., date_format: Optional[Any] = ..., **kwargs):
        ...
    
    def __setstate__(self, state):
        """Necessary for making this object picklable"""
        ...
    
    _unpickle_compat = ...
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

        Note
        ----
        Not currently implemented for PeriodIndex
        """
        ...
    
    def tz_localize(self, tz, infer_dst: bool = ...):
        """
        Localize tz-naive DatetimeIndex to given time zone (using
        pytz/dateutil), or remove timezone from tz-aware DatetimeIndex

        Parameters
        ----------
        tz : string, pytz.timezone, dateutil.tz.tzfile or None
            Time zone for time. Corresponding timestamps would be converted to
            time zone of the TimeSeries.
            None will remove timezone holding local time.
        infer_dst : boolean, default False
            Attempt to infer fall dst-transition hours based on order

        Returns
        -------
        localized : DatetimeIndex

        Note
        ----
        Not currently implemented for PeriodIndex
        """
        ...
    


def _get_ordinal_range(start, end, periods, freq, mult=...):
    ...

def _range_from_fields(year: Optional[Any] = ..., month: Optional[Any] = ..., quarter: Optional[Any] = ..., day: Optional[Any] = ..., hour: Optional[Any] = ..., minute: Optional[Any] = ..., second: Optional[Any] = ..., freq: Optional[Any] = ...):
    ...

def _make_field_arrays(*fields):
    ...

def pnow(freq: Optional[Any] = ...):
    ...

def period_range(start: Optional[Any] = ..., end: Optional[Any] = ..., periods: Optional[Any] = ..., freq=..., name: Optional[Any] = ...):
    """
    Return a fixed frequency PeriodIndex, with day (calendar) as the default
    frequency

    Parameters
    ----------
    start : string or period-like, default None
        Left bound for generating periods
    end : string or period-like, default None
        Right bound for generating periods
    periods : integer, default None
        Number of periods to generate
    freq : string or DateOffset, default 'D' (calendar daily)
        Frequency alias
    name : string, default None
        Name of the resulting PeriodIndex

    Notes
    -----
    Of the three parameters: ``start``, ``end``, and ``periods``, exactly two
    must be specified.

    To learn more about the frequency strings, please see `this link
    <http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases>`__.

    Returns
    -------
    prng : PeriodIndex

    Examples
    --------

    >>> pd.period_range(start='2017-01-01', end='2018-01-01', freq='M')
    PeriodIndex(['2017-01', '2017-02', '2017-03', '2017-04', '2017-05',
                 '2017-06', '2017-06', '2017-07', '2017-08', '2017-09',
                 '2017-10', '2017-11', '2017-12', '2018-01'],
                dtype='period[M]', freq='M')

    If ``start`` or ``end`` are ``Period`` objects, they will be used as anchor
    endpoints for a ``PeriodIndex`` with frequency matching that of the
    ``period_range`` constructor.

    >>> pd.period_range(start=pd.Period('2017Q1', freq='Q'),
    ...                 end=pd.Period('2017Q2', freq='Q'), freq='M')
    PeriodIndex(['2017-03', '2017-04', '2017-05', '2017-06'],
                dtype='period[M]', freq='M')
    """
    ...

