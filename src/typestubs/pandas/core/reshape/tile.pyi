"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""
Quantilization functions and related stuff
"""
def cut(x, bins, right: bool = ..., labels: Optional[Any] = ..., retbins: bool = ..., precision=..., include_lowest: bool = ...):
    """
    Return indices of half-open bins to which each value of `x` belongs.

    Parameters
    ----------
    x : array-like
        Input array to be binned. It has to be 1-dimensional.
    bins : int, sequence of scalars, or IntervalIndex
        If `bins` is an int, it defines the number of equal-width bins in the
        range of `x`. However, in this case, the range of `x` is extended
        by .1% on each side to include the min or max values of `x`. If
        `bins` is a sequence it defines the bin edges allowing for
        non-uniform bin width. No extension of the range of `x` is done in
        this case.
    right : bool, optional
        Indicates whether the bins include the rightmost edge or not. If
        right == True (the default), then the bins [1,2,3,4] indicate
        (1,2], (2,3], (3,4].
    labels : array or boolean, default None
        Used as labels for the resulting bins. Must be of the same length as
        the resulting bins. If False, return only integer indicators of the
        bins.
    retbins : bool, optional
        Whether to return the bins or not. Can be useful if bins is given
        as a scalar.
    precision : int, optional
        The precision at which to store and display the bins labels
    include_lowest : bool, optional
        Whether the first interval should be left-inclusive or not.

    Returns
    -------
    out : Categorical or Series or array of integers if labels is False
        The return type (Categorical or Series) depends on the input: a Series
        of type category if input is a Series else Categorical. Bins are
        represented as categories when categorical data is returned.
    bins : ndarray of floats
        Returned only if `retbins` is True.

    Notes
    -----
    The `cut` function can be useful for going from a continuous variable to
    a categorical variable. For example, `cut` could convert ages to groups
    of age ranges.

    Any NA values will be NA in the result.  Out of bounds values will be NA in
    the resulting Categorical object


    Examples
    --------
    >>> pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3, retbins=True)
    ... # doctest: +ELLIPSIS
    ([(0.19, 3.367], (0.19, 3.367], (0.19, 3.367], (3.367, 6.533], ...
    Categories (3, interval[float64]): [(0.19, 3.367] < (3.367, 6.533] ...

    >>> pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]),
    ...        3, labels=["good", "medium", "bad"])
    ... # doctest: +SKIP
    [good, good, good, medium, bad, good]
    Categories (3, object): [good < medium < bad]

    >>> pd.cut(np.ones(5), 4, labels=False)
    array([1, 1, 1, 1, 1])
    """
    ...

def qcut(x, q, labels: Optional[Any] = ..., retbins: bool = ..., precision=..., duplicates=...):
    """
    Quantile-based discretization function. Discretize variable into
    equal-sized buckets based on rank or based on sample quantiles. For example
    1000 values for 10 quantiles would produce a Categorical object indicating
    quantile membership for each data point.

    Parameters
    ----------
    x : 1d ndarray or Series
    q : integer or array of quantiles
        Number of quantiles. 10 for deciles, 4 for quartiles, etc. Alternately
        array of quantiles, e.g. [0, .25, .5, .75, 1.] for quartiles
    labels : array or boolean, default None
        Used as labels for the resulting bins. Must be of the same length as
        the resulting bins. If False, return only integer indicators of the
        bins.
    retbins : bool, optional
        Whether to return the (bins, labels) or not. Can be useful if bins
        is given as a scalar.
    precision : int, optional
        The precision at which to store and display the bins labels
    duplicates : {default 'raise', 'drop'}, optional
        If bin edges are not unique, raise ValueError or drop non-uniques.

        .. versionadded:: 0.20.0

    Returns
    -------
    out : Categorical or Series or array of integers if labels is False
        The return type (Categorical or Series) depends on the input: a Series
        of type category if input is a Series else Categorical. Bins are
        represented as categories when categorical data is returned.
    bins : ndarray of floats
        Returned only if `retbins` is True.

    Notes
    -----
    Out of bounds values will be NA in the resulting Categorical object

    Examples
    --------
    >>> pd.qcut(range(5), 4)
    ... # doctest: +ELLIPSIS
    [(-0.001, 1.0], (-0.001, 1.0], (1.0, 2.0], (2.0, 3.0], (3.0, 4.0]]
    Categories (4, interval[float64]): [(-0.001, 1.0] < (1.0, 2.0] ...

    >>> pd.qcut(range(5), 3, labels=["good", "medium", "bad"])
    ... # doctest: +SKIP
    [good, good, medium, bad, bad]
    Categories (3, object): [good < medium < bad]

    >>> pd.qcut(range(5), 4, labels=False)
    array([0, 0, 1, 2, 3])
    """
    ...

def _bins_to_cuts(x, bins, right: bool = ..., labels: Optional[Any] = ..., precision=..., include_lowest: bool = ..., dtype: Optional[Any] = ..., duplicates=...):
    ...

def _trim_zeros(x):
    ...

def _coerce_to_type(x):
    """
    if the passed data is of datetime/timedelta type,
    this method converts it to integer so that cut method can
    handle it
    """
    ...

def _convert_bin_to_numeric_type(bins, dtype):
    """
    if the passed bin is of datetime/timedelta type,
    this method converts it to integer

    Parameters
    ----------
    bins : list-liek of bins
    dtype : dtype of data

    Raises
    ------
    ValueError if bins are not of a compat dtype to dtype
    """
    ...

def _format_labels(bins, precision, right: bool = ..., include_lowest: bool = ..., dtype: Optional[Any] = ...):
    """ based on the dtype, return our labels """
    ...

def _preprocess_for_cut(x):
    """
    handles preprocessing for cut where we convert passed
    input to array, strip the index information and store it
    separately
    """
    ...

def _postprocess_for_cut(fac, bins, retbins, x_is_series, series_index, name):
    """
    handles post processing for the cut method where
    we combine the index information if the originally passed
    datatype was a series
    """
    ...

def _round_frac(x, precision):
    """
    Round the fractional part of the given number
    """
    ...

def _infer_precision(base_precision, bins):
    """Infer an appropriate precision for _round_frac
    """
    ...

