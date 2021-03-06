"""
This type stub file was generated by pyright.
"""

from pandas.core.base import GroupByMixin, PandasObject, SelectionMixin
from pandas.util._decorators import Appender, Substitution, cache_readonly
from pandas.core.generic import _shared_docs
from typing import Any, Optional

"""

provide a generic structure to support window functions,
similar to how we have a Groupby object


"""
_shared_docs = dict(**_shared_docs)
_doc_template = """

Returns
-------
same type as input

See also
--------
pandas.Series.%(name)s
pandas.DataFrame.%(name)s
"""
class _Window(PandasObject, SelectionMixin):
    _attributes = ...
    exclusions = ...
    def __init__(self, obj, window: Optional[Any] = ..., min_periods: Optional[Any] = ..., freq: Optional[Any] = ..., center: bool = ..., win_type: Optional[Any] = ..., axis=..., on: Optional[Any] = ..., closed: Optional[Any] = ..., **kwargs):
        self.blocks = ...
        self.obj = ...
        self.on = ...
        self.closed = ...
        self.window = ...
        self.min_periods = ...
        self.freq = ...
        self.center = ...
        self.win_type = ...
        self.win_freq = ...
        self.axis = ...
    
    @property
    def _constructor(self):
        ...
    
    @property
    def is_datetimelike(self):
        ...
    
    @property
    def _on(self):
        ...
    
    @property
    def is_freq_type(self):
        ...
    
    def validate(self):
        ...
    
    def _convert_freq(self, how: Optional[Any] = ...):
        """ resample according to the how, return a new object """
        ...
    
    def _create_blocks(self, how):
        """ split data into blocks & return conformed data """
        ...
    
    def _gotitem(self, key, ndim, subset: Optional[Any] = ...):
        """
        sub-classes to define
        return a sliced object

        Parameters
        ----------
        key : string / list of selections
        ndim : 1,2
            requested ndim of result
        subset : object, default None
            subset to act on
        """
        ...
    
    def __getattr__(self, attr):
        ...
    
    def _dir_additions(self):
        ...
    
    def _get_window(self, other: Optional[Any] = ...):
        ...
    
    @property
    def _window_type(self):
        ...
    
    def __unicode__(self):
        """ provide a nice str repr of our rolling object """
        ...
    
    def _get_index(self, index: Optional[Any] = ...):
        """
        Return index as ndarrays

        Returns
        -------
        tuple of (index, index_as_ndarray)
        """
        ...
    
    def _prep_values(self, values: Optional[Any] = ..., kill_inf: bool = ..., how: Optional[Any] = ...):
        ...
    
    def _wrap_result(self, result, block: Optional[Any] = ..., obj: Optional[Any] = ...):
        """ wrap a single result """
        ...
    
    def _wrap_results(self, results, blocks, obj):
        """
        wrap the results

        Paramters
        ---------
        results : list of ndarrays
        blocks : list of blocks
        obj : conformed data (may be resampled)
        """
        ...
    
    def _center_window(self, result, window):
        """ center the result in the window """
        ...
    
    def aggregate(self, arg, *args, **kwargs):
        ...
    
    agg = ...


class Window(_Window):
    """
    Provides rolling window calculations.

    .. versionadded:: 0.18.0

    Parameters
    ----------
    window : int, or offset
        Size of the moving window. This is the number of observations used for
        calculating the statistic. Each window will be a fixed size.

        If its an offset then this will be the time period of each window. Each
        window will be a variable sized based on the observations included in
        the time-period. This is only valid for datetimelike indexes. This is
        new in 0.19.0
    min_periods : int, default None
        Minimum number of observations in window required to have a value
        (otherwise result is NA). For a window that is specified by an offset,
        this will default to 1.
    freq : string or DateOffset object, optional (default None)
        .. deprecated:: 0.18.0
           Frequency to conform the data to before computing the statistic.
           Specified as a frequency string or DateOffset object.
    center : boolean, default False
        Set the labels at the center of the window.
    win_type : string, default None
        Provide a window type. See the notes below.
    on : string, optional
        For a DataFrame, column on which to calculate
        the rolling window, rather than the index
    closed : string, default None
        Make the interval closed on the 'right', 'left', 'both' or
        'neither' endpoints.
        For offset-based windows, it defaults to 'right'.
        For fixed windows, defaults to 'both'. Remaining cases not implemented
        for fixed windows.

        .. versionadded:: 0.20.0

    axis : int or string, default 0

    Returns
    -------
    a Window or Rolling sub-classed for the particular operation

    Examples
    --------

    >>> df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]})
    >>> df
         B
    0  0.0
    1  1.0
    2  2.0
    3  NaN
    4  4.0

    Rolling sum with a window length of 2, using the 'triang'
    window type.

    >>> df.rolling(2, win_type='triang').sum()
         B
    0  NaN
    1  1.0
    2  2.5
    3  NaN
    4  NaN

    Rolling sum with a window length of 2, min_periods defaults
    to the window length.

    >>> df.rolling(2).sum()
         B
    0  NaN
    1  1.0
    2  3.0
    3  NaN
    4  NaN

    Same as above, but explicity set the min_periods

    >>> df.rolling(2, min_periods=1).sum()
         B
    0  0.0
    1  1.0
    2  3.0
    3  2.0
    4  4.0

    A ragged (meaning not-a-regular frequency), time-indexed DataFrame

    >>> df = pd.DataFrame({'B': [0, 1, 2, np.nan, 4]},
    ....:                 index = [pd.Timestamp('20130101 09:00:00'),
    ....:                          pd.Timestamp('20130101 09:00:02'),
    ....:                          pd.Timestamp('20130101 09:00:03'),
    ....:                          pd.Timestamp('20130101 09:00:05'),
    ....:                          pd.Timestamp('20130101 09:00:06')])

    >>> df
                           B
    2013-01-01 09:00:00  0.0
    2013-01-01 09:00:02  1.0
    2013-01-01 09:00:03  2.0
    2013-01-01 09:00:05  NaN
    2013-01-01 09:00:06  4.0


    Contrasting to an integer rolling window, this will roll a variable
    length window corresponding to the time period.
    The default for min_periods is 1.

    >>> df.rolling('2s').sum()
                           B
    2013-01-01 09:00:00  0.0
    2013-01-01 09:00:02  1.0
    2013-01-01 09:00:03  3.0
    2013-01-01 09:00:05  NaN
    2013-01-01 09:00:06  4.0

    Notes
    -----
    By default, the result is set to the right edge of the window. This can be
    changed to the center of the window by setting ``center=True``.

    The `freq` keyword is used to conform time series data to a specified
    frequency by resampling the data. This is done with the default parameters
    of :meth:`~pandas.Series.resample` (i.e. using the `mean`).

    To learn more about the offsets & frequency strings, please see `this link
    <http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases>`__.

    The recognized win_types are:

    * ``boxcar``
    * ``triang``
    * ``blackman``
    * ``hamming``
    * ``bartlett``
    * ``parzen``
    * ``bohman``
    * ``blackmanharris``
    * ``nuttall``
    * ``barthann``
    * ``kaiser`` (needs beta)
    * ``gaussian`` (needs std)
    * ``general_gaussian`` (needs power, width)
    * ``slepian`` (needs width).

    If ``win_type=None`` all points are evenly weighted. To learn more about
    different window types see `scipy.signal window functions
    <https://docs.scipy.org/doc/scipy/reference/signal.html#window-functions>`__.
    """
    def validate(self):
        ...
    
    def _prep_window(self, **kwargs):
        """
        provide validation for our window type, return the window
        we have already been validated
        """
        ...
    
    def _apply_window(self, mean: bool = ..., how: Optional[Any] = ..., **kwargs):
        """
        Applies a moving window of type ``window_type`` on the data.

        Parameters
        ----------
        mean : boolean, default True
            If True computes weighted mean, else weighted sum
        how : string, default to None
            .. deprecated:: 0.18.0
               how to resample

        Returns
        -------
        y : type of input argument

        """
        ...
    
    _agg_doc = ...
    @Appender(_agg_doc)
    @Appender(_shared_docs['aggregate'] % dict(versionadded='', klass='Series/DataFrame'))
    def aggregate(self, arg, *args, **kwargs):
        ...
    
    agg = ...
    @Substitution(name='window')
    @Appender(_doc_template)
    @Appender(_shared_docs['sum'])
    def sum(self, *args, **kwargs):
        ...
    
    @Substitution(name='window')
    @Appender(_doc_template)
    @Appender(_shared_docs['mean'])
    def mean(self, *args, **kwargs):
        ...
    


class _GroupByMixin(GroupByMixin):
    """ provide the groupby facilities """
    def __init__(self, obj, *args, **kwargs):
        ...
    
    count = ...
    corr = ...
    cov = ...
    def _apply(self, func, name, window: Optional[Any] = ..., center: Optional[Any] = ..., check_minp: Optional[Any] = ..., how: Optional[Any] = ..., **kwargs):
        """
        dispatch to apply; we are stripping all of the _apply kwargs and
        performing the original function call on the grouped object
        """
        ...
    


class _Rolling(_Window):
    @property
    def _constructor(self):
        ...
    
    def _apply(self, func, name: Optional[Any] = ..., window: Optional[Any] = ..., center: Optional[Any] = ..., check_minp: Optional[Any] = ..., how: Optional[Any] = ..., **kwargs):
        """
        Rolling statistical measure using supplied function. Designed to be
        used with passed-in Cython array-based functions.

        Parameters
        ----------
        func : string/callable to apply
        name : string, optional
           name of this function
        window : int/array, default to _get_window()
        center : boolean, default to self.center
        check_minp : function, default to _use_window
        how : string, default to None
            .. deprecated:: 0.18.0
               how to resample

        Returns
        -------
        y : type of input
        """
        ...
    


class _Rolling_and_Expanding(_Rolling):
    def count(self):
        ...
    
    def apply(self, func, args=..., kwargs=...):
        ...
    
    def sum(self, *args, **kwargs):
        ...
    
    def max(self, how: Optional[Any] = ..., *args, **kwargs):
        ...
    
    def min(self, how: Optional[Any] = ..., *args, **kwargs):
        ...
    
    def mean(self, *args, **kwargs):
        ...
    
    def median(self, how: Optional[Any] = ..., **kwargs):
        ...
    
    def std(self, ddof=..., *args, **kwargs):
        ...
    
    def var(self, ddof=..., *args, **kwargs):
        ...
    
    def skew(self, **kwargs):
        ...
    
    def kurt(self, **kwargs):
        ...
    
    def quantile(self, quantile, **kwargs):
        ...
    
    def cov(self, other: Optional[Any] = ..., pairwise: Optional[Any] = ..., ddof=..., **kwargs):
        ...
    
    def corr(self, other: Optional[Any] = ..., pairwise: Optional[Any] = ..., **kwargs):
        ...
    


class Rolling(_Rolling_and_Expanding):
    @cache_readonly
    def is_datetimelike(self):
        ...
    
    @cache_readonly
    def _on(self):
        ...
    
    def validate(self):
        ...
    
    def _validate_monotonic(self):
        """ validate on is monotonic """
        ...
    
    def _validate_freq(self):
        """ validate & return our freq """
        ...
    
    _agg_doc = ...
    @Appender(_agg_doc)
    @Appender(_shared_docs['aggregate'] % dict(versionadded='', klass='Series/DataFrame'))
    def aggregate(self, arg, *args, **kwargs):
        ...
    
    agg = ...
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['count'])
    def count(self):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['apply'])
    def apply(self, func, args=..., kwargs=...):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['sum'])
    def sum(self, *args, **kwargs):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['max'])
    def max(self, *args, **kwargs):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['min'])
    def min(self, *args, **kwargs):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['mean'])
    def mean(self, *args, **kwargs):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['median'])
    def median(self, **kwargs):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['std'])
    def std(self, ddof=..., *args, **kwargs):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['var'])
    def var(self, ddof=..., *args, **kwargs):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['skew'])
    def skew(self, **kwargs):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['kurt'])
    def kurt(self, **kwargs):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['quantile'])
    def quantile(self, quantile, **kwargs):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['cov'])
    def cov(self, other: Optional[Any] = ..., pairwise: Optional[Any] = ..., ddof=..., **kwargs):
        ...
    
    @Substitution(name='rolling')
    @Appender(_doc_template)
    @Appender(_shared_docs['corr'])
    def corr(self, other: Optional[Any] = ..., pairwise: Optional[Any] = ..., **kwargs):
        ...
    


class RollingGroupby(_GroupByMixin, Rolling):
    """
    Provides a rolling groupby implementation

    .. versionadded:: 0.18.1

    """
    @property
    def _constructor(self):
        ...
    
    def _gotitem(self, key, ndim, subset: Optional[Any] = ...):
        ...
    
    def _validate_monotonic(self):
        """
        validate that on is monotonic;
        we don't care for groupby.rolling
        because we have already validated at a higher
        level
        """
        ...
    


class Expanding(_Rolling_and_Expanding):
    """
    Provides expanding transformations.

    .. versionadded:: 0.18.0

    Parameters
    ----------
    min_periods : int, default None
        Minimum number of observations in window required to have a value
        (otherwise result is NA).
    freq : string or DateOffset object, optional (default None)
        .. deprecated:: 0.18.0
           Frequency to conform the data to before computing the statistic.
           Specified as a frequency string or DateOffset object.
    center : boolean, default False
        Set the labels at the center of the window.
    axis : int or string, default 0

    Returns
    -------
    a Window sub-classed for the particular operation

    Examples
    --------

    >>> df = DataFrame({'B': [0, 1, 2, np.nan, 4]})
         B
    0  0.0
    1  1.0
    2  2.0
    3  NaN
    4  4.0

    >>> df.expanding(2).sum()
         B
    0  NaN
    1  1.0
    2  3.0
    3  3.0
    4  7.0

    Notes
    -----
    By default, the result is set to the right edge of the window. This can be
    changed to the center of the window by setting ``center=True``.

    The `freq` keyword is used to conform time series data to a specified
    frequency by resampling the data. This is done with the default parameters
    of :meth:`~pandas.Series.resample` (i.e. using the `mean`).
    """
    _attributes = ...
    def __init__(self, obj, min_periods=..., freq: Optional[Any] = ..., center: bool = ..., axis=..., **kwargs):
        ...
    
    @property
    def _constructor(self):
        ...
    
    def _get_window(self, other: Optional[Any] = ...):
        ...
    
    _agg_doc = ...
    @Appender(_agg_doc)
    @Appender(_shared_docs['aggregate'] % dict(versionadded='', klass='Series/DataFrame'))
    def aggregate(self, arg, *args, **kwargs):
        ...
    
    agg = ...
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['count'])
    def count(self, **kwargs):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['apply'])
    def apply(self, func, args=..., kwargs=...):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['sum'])
    def sum(self, *args, **kwargs):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['max'])
    def max(self, *args, **kwargs):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['min'])
    def min(self, *args, **kwargs):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['mean'])
    def mean(self, *args, **kwargs):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['median'])
    def median(self, **kwargs):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['std'])
    def std(self, ddof=..., *args, **kwargs):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['var'])
    def var(self, ddof=..., *args, **kwargs):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['skew'])
    def skew(self, **kwargs):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['kurt'])
    def kurt(self, **kwargs):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['quantile'])
    def quantile(self, quantile, **kwargs):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['cov'])
    def cov(self, other: Optional[Any] = ..., pairwise: Optional[Any] = ..., ddof=..., **kwargs):
        ...
    
    @Substitution(name='expanding')
    @Appender(_doc_template)
    @Appender(_shared_docs['corr'])
    def corr(self, other: Optional[Any] = ..., pairwise: Optional[Any] = ..., **kwargs):
        ...
    


class ExpandingGroupby(_GroupByMixin, Expanding):
    """
    Provides a expanding groupby implementation

    .. versionadded:: 0.18.1

    """
    @property
    def _constructor(self):
        ...
    


_bias_template = """

Parameters
----------
bias : boolean, default False
    Use a standard estimation bias correction
"""
_pairwise_template = """

Parameters
----------
other : Series, DataFrame, or ndarray, optional
    if not supplied then will default to self and produce pairwise output
pairwise : bool, default None
    If False then only matching columns between self and other will be used and
    the output will be a DataFrame.
    If True then all pairwise combinations will be calculated and the output
    will be a MultiIndex DataFrame in the case of DataFrame inputs.
    In the case of missing elements, only complete pairwise observations will
    be used.
bias : boolean, default False
   Use a standard estimation bias correction
"""
class EWM(_Rolling):
    r"""
    Provides exponential weighted functions

    .. versionadded:: 0.18.0

    Parameters
    ----------
    com : float, optional
        Specify decay in terms of center of mass,
        :math:`\alpha = 1 / (1 + com),\text{ for } com \geq 0`
    span : float, optional
        Specify decay in terms of span,
        :math:`\alpha = 2 / (span + 1),\text{ for } span \geq 1`
    halflife : float, optional
        Specify decay in terms of half-life,
        :math:`\alpha = 1 - exp(log(0.5) / halflife),\text{ for } halflife > 0`
    alpha : float, optional
        Specify smoothing factor :math:`\alpha` directly,
        :math:`0 < \alpha \leq 1`

        .. versionadded:: 0.18.0

    min_periods : int, default 0
        Minimum number of observations in window required to have a value
        (otherwise result is NA).
    freq : None or string alias / date offset object, default=None
        .. deprecated:: 0.18.0
           Frequency to conform to before computing statistic
    adjust : boolean, default True
        Divide by decaying adjustment factor in beginning periods to account
        for imbalance in relative weightings (viewing EWMA as a moving average)
    ignore_na : boolean, default False
        Ignore missing values when calculating weights;
        specify True to reproduce pre-0.15.0 behavior

    Returns
    -------
    a Window sub-classed for the particular operation

    Examples
    --------

    >>> df = DataFrame({'B': [0, 1, 2, np.nan, 4]})
         B
    0  0.0
    1  1.0
    2  2.0
    3  NaN
    4  4.0

    >>> df.ewm(com=0.5).mean()
              B
    0  0.000000
    1  0.750000
    2  1.615385
    3  1.615385
    4  3.670213

    Notes
    -----
    Exactly one of center of mass, span, half-life, and alpha must be provided.
    Allowed values and relationship between the parameters are specified in the
    parameter descriptions above; see the link at the end of this section for
    a detailed explanation.

    The `freq` keyword is used to conform time series data to a specified
    frequency by resampling the data. This is done with the default parameters
    of :meth:`~pandas.Series.resample` (i.e. using the `mean`).

    When adjust is True (default), weighted averages are calculated using
    weights (1-alpha)**(n-1), (1-alpha)**(n-2), ..., 1-alpha, 1.

    When adjust is False, weighted averages are calculated recursively as:
       weighted_average[0] = arg[0];
       weighted_average[i] = (1-alpha)*weighted_average[i-1] + alpha*arg[i].

    When ignore_na is False (default), weights are based on absolute positions.
    For example, the weights of x and y used in calculating the final weighted
    average of [x, None, y] are (1-alpha)**2 and 1 (if adjust is True), and
    (1-alpha)**2 and alpha (if adjust is False).

    When ignore_na is True (reproducing pre-0.15.0 behavior), weights are based
    on relative positions. For example, the weights of x and y used in
    calculating the final weighted average of [x, None, y] are 1-alpha and 1
    (if adjust is True), and 1-alpha and alpha (if adjust is False).

    More details can be found at
    http://pandas.pydata.org/pandas-docs/stable/computation.html#exponentially-weighted-windows
    """
    _attributes = ...
    def __init__(self, obj, com: Optional[Any] = ..., span: Optional[Any] = ..., halflife: Optional[Any] = ..., alpha: Optional[Any] = ..., min_periods=..., freq: Optional[Any] = ..., adjust: bool = ..., ignore_na: bool = ..., axis=...):
        self.obj = ...
        self.com = ...
        self.min_periods = ...
        self.freq = ...
        self.adjust = ...
        self.ignore_na = ...
        self.axis = ...
        self.on = ...
    
    @property
    def _constructor(self):
        ...
    
    _agg_doc = ...
    @Appender(_agg_doc)
    @Appender(_shared_docs['aggregate'] % dict(versionadded='', klass='Series/DataFrame'))
    def aggregate(self, arg, *args, **kwargs):
        ...
    
    agg = ...
    def _apply(self, func, how: Optional[Any] = ..., **kwargs):
        """Rolling statistical measure using supplied function. Designed to be
        used with passed-in Cython array-based functions.

        Parameters
        ----------
        func : string/callable to apply
        how : string, default to None
            .. deprecated:: 0.18.0
               how to resample

        Returns
        -------
        y : type of input argument

        """
        ...
    
    @Substitution(name='ewm')
    @Appender(_doc_template)
    def mean(self, *args, **kwargs):
        """exponential weighted moving average"""
        ...
    
    @Substitution(name='ewm')
    @Appender(_doc_template)
    @Appender(_bias_template)
    def std(self, bias: bool = ..., *args, **kwargs):
        """exponential weighted moving stddev"""
        ...
    
    vol = ...
    @Substitution(name='ewm')
    @Appender(_doc_template)
    @Appender(_bias_template)
    def var(self, bias: bool = ..., *args, **kwargs):
        """exponential weighted moving variance"""
        ...
    
    @Substitution(name='ewm')
    @Appender(_doc_template)
    @Appender(_pairwise_template)
    def cov(self, other: Optional[Any] = ..., pairwise: Optional[Any] = ..., bias: bool = ..., **kwargs):
        """exponential weighted sample covariance"""
        ...
    
    @Substitution(name='ewm')
    @Appender(_doc_template)
    @Appender(_pairwise_template)
    def corr(self, other: Optional[Any] = ..., pairwise: Optional[Any] = ..., **kwargs):
        """exponential weighted sample correlation"""
        ...
    


def _flex_binary_moment(arg1, arg2, f, pairwise: bool = ...):
    ...

def _get_center_of_mass(com, span, halflife, alpha):
    ...

def _offset(window, center):
    ...

def _require_min_periods(p):
    ...

def _use_window(minp, window):
    ...

def _zsqrt(x):
    ...

def _prep_binary(arg1, arg2):
    ...

def rolling(obj, win_type: Optional[Any] = ..., **kwds):
    ...

def expanding(obj, **kwds):
    ...

def ewm(obj, **kwds):
    ...

