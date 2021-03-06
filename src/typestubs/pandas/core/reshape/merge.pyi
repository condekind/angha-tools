"""
This type stub file was generated by pyright.
"""

import copy
from pandas.core.frame import _merge_doc
from pandas.core.dtypes.common import _ensure_float64, _ensure_int64, _ensure_object
from pandas.util._decorators import Appender, Substitution
from pandas._libs import join as libjoin
from typing import Any, Optional

"""
SQL-style merge routines
"""
@Substitution('\nleft : DataFrame')
@Appender(_merge_doc, indents=0)
def merge(left, right, how=..., on: Optional[Any] = ..., left_on: Optional[Any] = ..., right_on: Optional[Any] = ..., left_index: bool = ..., right_index: bool = ..., sort: bool = ..., suffixes=..., copy: bool = ..., indicator: bool = ..., validate: Optional[Any] = ...):
    ...

if __debug__:
    ...
def _groupby_and_merge(by, on, left, right, _merge_pieces, check_duplicates: bool = ...):
    """
    groupby & merge; we are always performing a left-by type operation

    Parameters
    ----------
    by: field to group
    on: duplicates field
    left: left frame
    right: right frame
    _merge_pieces: function for merging
    check_duplicates: boolean, default True
        should we check & clean duplicates
    """
    ...

def ordered_merge(left, right, on: Optional[Any] = ..., left_on: Optional[Any] = ..., right_on: Optional[Any] = ..., left_by: Optional[Any] = ..., right_by: Optional[Any] = ..., fill_method: Optional[Any] = ..., suffixes=...):
    ...

def merge_ordered(left, right, on: Optional[Any] = ..., left_on: Optional[Any] = ..., right_on: Optional[Any] = ..., left_by: Optional[Any] = ..., right_by: Optional[Any] = ..., fill_method: Optional[Any] = ..., suffixes=..., how=...):
    """Perform merge with optional filling/interpolation designed for ordered
    data like time series data. Optionally perform group-wise merge (see
    examples)

    Parameters
    ----------
    left : DataFrame
    right : DataFrame
    on : label or list
        Field names to join on. Must be found in both DataFrames.
    left_on : label or list, or array-like
        Field names to join on in left DataFrame. Can be a vector or list of
        vectors of the length of the DataFrame to use a particular vector as
        the join key instead of columns
    right_on : label or list, or array-like
        Field names to join on in right DataFrame or vector/list of vectors per
        left_on docs
    left_by : column name or list of column names
        Group left DataFrame by group columns and merge piece by piece with
        right DataFrame
    right_by : column name or list of column names
        Group right DataFrame by group columns and merge piece by piece with
        left DataFrame
    fill_method : {'ffill', None}, default None
        Interpolation method for data
    suffixes : 2-length sequence (tuple, list, ...)
        Suffix to apply to overlapping column names in the left and right
        side, respectively
    how : {'left', 'right', 'outer', 'inner'}, default 'outer'
        * left: use only keys from left frame (SQL: left outer join)
        * right: use only keys from right frame (SQL: right outer join)
        * outer: use union of keys from both frames (SQL: full outer join)
        * inner: use intersection of keys from both frames (SQL: inner join)

        .. versionadded:: 0.19.0

    Examples
    --------
    >>> A                      >>> B
          key  lvalue group        key  rvalue
    0   a       1     a        0     b       1
    1   c       2     a        1     c       2
    2   e       3     a        2     d       3
    3   a       1     b
    4   c       2     b
    5   e       3     b

    >>> ordered_merge(A, B, fill_method='ffill', left_by='group')
       key  lvalue group  rvalue
    0    a       1     a     NaN
    1    b       1     a       1
    2    c       2     a       2
    3    d       2     a       3
    4    e       3     a       3
    5    f       3     a       4
    6    a       1     b     NaN
    7    b       1     b       1
    8    c       2     b       2
    9    d       2     b       3
    10   e       3     b       3
    11   f       3     b       4

    Returns
    -------
    merged : DataFrame
        The output type will the be same as 'left', if it is a subclass
        of DataFrame.

    See also
    --------
    merge
    merge_asof

    """
    ...

def merge_asof(left, right, on: Optional[Any] = ..., left_on: Optional[Any] = ..., right_on: Optional[Any] = ..., left_index: bool = ..., right_index: bool = ..., by: Optional[Any] = ..., left_by: Optional[Any] = ..., right_by: Optional[Any] = ..., suffixes=..., tolerance: Optional[Any] = ..., allow_exact_matches: bool = ..., direction=...):
    """Perform an asof merge. This is similar to a left-join except that we
    match on nearest key rather than equal keys.

    Both DataFrames must be sorted by the key.

    For each row in the left DataFrame:

      - A "backward" search selects the last row in the right DataFrame whose
        'on' key is less than or equal to the left's key.

      - A "forward" search selects the first row in the right DataFrame whose
        'on' key is greater than or equal to the left's key.

      - A "nearest" search selects the row in the right DataFrame whose 'on'
        key is closest in absolute distance to the left's key.

    The default is "backward" and is compatible in versions below 0.20.0.
    The direction parameter was added in version 0.20.0 and introduces
    "forward" and "nearest".

    Optionally match on equivalent keys with 'by' before searching with 'on'.

    .. versionadded:: 0.19.0

    Parameters
    ----------
    left : DataFrame
    right : DataFrame
    on : label
        Field name to join on. Must be found in both DataFrames.
        The data MUST be ordered. Furthermore this must be a numeric column,
        such as datetimelike, integer, or float. On or left_on/right_on
        must be given.
    left_on : label
        Field name to join on in left DataFrame.
    right_on : label
        Field name to join on in right DataFrame.
    left_index : boolean
        Use the index of the left DataFrame as the join key.

        .. versionadded:: 0.19.2

    right_index : boolean
        Use the index of the right DataFrame as the join key.

        .. versionadded:: 0.19.2

    by : column name or list of column names
        Match on these columns before performing merge operation.
    left_by : column name
        Field names to match on in the left DataFrame.

        .. versionadded:: 0.19.2

    right_by : column name
        Field names to match on in the right DataFrame.

        .. versionadded:: 0.19.2

    suffixes : 2-length sequence (tuple, list, ...)
        Suffix to apply to overlapping column names in the left and right
        side, respectively.
    tolerance : integer or Timedelta, optional, default None
        Select asof tolerance within this range; must be compatible
        with the merge index.
    allow_exact_matches : boolean, default True

        - If True, allow matching with the same 'on' value
          (i.e. less-than-or-equal-to / greater-than-or-equal-to)
        - If False, don't match the same 'on' value
          (i.e., stricly less-than / strictly greater-than)

    direction : 'backward' (default), 'forward', or 'nearest'
        Whether to search for prior, subsequent, or closest matches.

        .. versionadded:: 0.20.0


    Returns
    -------
    merged : DataFrame

    Examples
    --------
    >>> left = pd.DataFrame({'a': [1, 5, 10], 'left_val': ['a', 'b', 'c']})
    >>> left
        a left_val
    0   1        a
    1   5        b
    2  10        c

    >>> right = pd.DataFrame({'a': [1, 2, 3, 6, 7],
    ...                       'right_val': [1, 2, 3, 6, 7]})
    >>> right
       a  right_val
    0  1          1
    1  2          2
    2  3          3
    3  6          6
    4  7          7

    >>> pd.merge_asof(left, right, on='a')
        a left_val  right_val
    0   1        a          1
    1   5        b          3
    2  10        c          7

    >>> pd.merge_asof(left, right, on='a', allow_exact_matches=False)
        a left_val  right_val
    0   1        a        NaN
    1   5        b        3.0
    2  10        c        7.0

    >>> pd.merge_asof(left, right, on='a', direction='forward')
        a left_val  right_val
    0   1        a        1.0
    1   5        b        6.0
    2  10        c        NaN

    >>> pd.merge_asof(left, right, on='a', direction='nearest')
        a left_val  right_val
    0   1        a          1
    1   5        b          6
    2  10        c          7

    We can use indexed DataFrames as well.

    >>> left = pd.DataFrame({'left_val': ['a', 'b', 'c']}, index=[1, 5, 10])
    >>> left
       left_val
    1         a
    5         b
    10        c

    >>> right = pd.DataFrame({'right_val': [1, 2, 3, 6, 7]},
    ...                      index=[1, 2, 3, 6, 7])
    >>> right
       right_val
    1          1
    2          2
    3          3
    6          6
    7          7

    >>> pd.merge_asof(left, right, left_index=True, right_index=True)
       left_val  right_val
    1         a          1
    5         b          3
    10        c          7

    Here is a real-world times-series example

    >>> quotes
                         time ticker     bid     ask
    0 2016-05-25 13:30:00.023   GOOG  720.50  720.93
    1 2016-05-25 13:30:00.023   MSFT   51.95   51.96
    2 2016-05-25 13:30:00.030   MSFT   51.97   51.98
    3 2016-05-25 13:30:00.041   MSFT   51.99   52.00
    4 2016-05-25 13:30:00.048   GOOG  720.50  720.93
    5 2016-05-25 13:30:00.049   AAPL   97.99   98.01
    6 2016-05-25 13:30:00.072   GOOG  720.50  720.88
    7 2016-05-25 13:30:00.075   MSFT   52.01   52.03

    >>> trades
                         time ticker   price  quantity
    0 2016-05-25 13:30:00.023   MSFT   51.95        75
    1 2016-05-25 13:30:00.038   MSFT   51.95       155
    2 2016-05-25 13:30:00.048   GOOG  720.77       100
    3 2016-05-25 13:30:00.048   GOOG  720.92       100
    4 2016-05-25 13:30:00.048   AAPL   98.00       100

    By default we are taking the asof of the quotes

    >>> pd.merge_asof(trades, quotes,
    ...                       on='time',
    ...                       by='ticker')
                         time ticker   price  quantity     bid     ask
    0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
    1 2016-05-25 13:30:00.038   MSFT   51.95       155   51.97   51.98
    2 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
    3 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93
    4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN

    We only asof within 2ms between the quote time and the trade time

    >>> pd.merge_asof(trades, quotes,
    ...                       on='time',
    ...                       by='ticker',
    ...                       tolerance=pd.Timedelta('2ms'))
                         time ticker   price  quantity     bid     ask
    0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
    1 2016-05-25 13:30:00.038   MSFT   51.95       155     NaN     NaN
    2 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
    3 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93
    4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN

    We only asof within 10ms between the quote time and the trade time
    and we exclude exact matches on time. However *prior* data will
    propagate forward

    >>> pd.merge_asof(trades, quotes,
    ...                       on='time',
    ...                       by='ticker',
    ...                       tolerance=pd.Timedelta('10ms'),
    ...                       allow_exact_matches=False)
                         time ticker   price  quantity     bid     ask
    0 2016-05-25 13:30:00.023   MSFT   51.95        75     NaN     NaN
    1 2016-05-25 13:30:00.038   MSFT   51.95       155   51.97   51.98
    2 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
    3 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93
    4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN

    See also
    --------
    merge
    merge_ordered

    """
    ...

class _MergeOperation(object):
    """
    Perform a database (SQL) merge operation between two DataFrame objects
    using either columns as keys or their row indexes
    """
    _merge_type = ...
    def __init__(self, left, right, how=..., on: Optional[Any] = ..., left_on: Optional[Any] = ..., right_on: Optional[Any] = ..., axis=..., left_index: bool = ..., right_index: bool = ..., sort: bool = ..., suffixes=..., copy: bool = ..., indicator: bool = ..., validate: Optional[Any] = ...):
        self.left = ...
        self.right = ...
        self.how = ...
        self.axis = ...
        self.on = ...
        self.left_on = ...
        self.right_on = ...
        self.copy = ...
        self.suffixes = ...
        self.sort = ...
        self.left_index = ...
        self.right_index = ...
        self.indicator = ...
    
    def get_result(self):
        ...
    
    def _indicator_pre_merge(self, left, right):
        ...
    
    def _indicator_post_merge(self, result):
        ...
    
    def _maybe_add_join_keys(self, result, left_indexer, right_indexer):
        ...
    
    def _get_join_indexers(self):
        """ return the join indexers """
        ...
    
    def _get_join_info(self):
        ...
    
    def _get_merge_keys(self):
        """
        Note: has side effects (copy/delete key columns)

        Parameters
        ----------
        left
        right
        on

        Returns
        -------
        left_keys, right_keys
        """
        ...
    
    def _maybe_coerce_merge_keys(self):
        ...
    
    def _validate_specification(self):
        ...
    
    def _validate(self, validate):
        ...
    


def _get_join_indexers(left_keys, right_keys, sort: bool = ..., how=..., **kwargs):
    """

    Parameters
    ----------
    left_keys: ndarray, Index, Series
    right_keys: ndarray, Index, Series
    sort: boolean, default False
    how: string {'inner', 'outer', 'left', 'right'}, default 'inner'

    Returns
    -------
    tuple of (left_indexer, right_indexer)
        indexers into the left_keys, right_keys

    """
    ...

class _OrderedMerge(_MergeOperation):
    _merge_type = ...
    def __init__(self, left, right, on: Optional[Any] = ..., left_on: Optional[Any] = ..., right_on: Optional[Any] = ..., left_index: bool = ..., right_index: bool = ..., axis=..., suffixes=..., copy: bool = ..., fill_method: Optional[Any] = ..., how=...):
        self.fill_method = ...
    
    def get_result(self):
        ...
    


def _asof_function(direction, on_type):
    ...

def _asof_by_function(direction, on_type, by_type):
    ...

_type_casters = { 'int64_t': _ensure_int64,'double': _ensure_float64,'object': _ensure_object }
_cython_types = { 'uint8': 'uint8_t','uint32': 'uint32_t','uint16': 'uint16_t','uint64': 'uint64_t','int8': 'int8_t','int32': 'int32_t','int16': 'int16_t','int64': 'int64_t','float16': 'error','float32': 'float','float64': 'double' }
def _get_cython_type(dtype):
    """ Given a dtype, return a C name like 'int64_t' or 'double' """
    ...

def _get_cython_type_upcast(dtype):
    """ Upcast a dtype to 'int64_t', 'double', or 'object' """
    ...

class _AsOfMerge(_OrderedMerge):
    _merge_type = ...
    def __init__(self, left, right, on: Optional[Any] = ..., left_on: Optional[Any] = ..., right_on: Optional[Any] = ..., left_index: bool = ..., right_index: bool = ..., by: Optional[Any] = ..., left_by: Optional[Any] = ..., right_by: Optional[Any] = ..., axis=..., suffixes=..., copy: bool = ..., fill_method: Optional[Any] = ..., how=..., tolerance: Optional[Any] = ..., allow_exact_matches: bool = ..., direction=...):
        self.by = ...
        self.left_by = ...
        self.right_by = ...
        self.tolerance = ...
        self.allow_exact_matches = ...
        self.direction = ...
    
    def _validate_specification(self):
        ...
    
    @property
    def _asof_key(self):
        """ This is our asof key, the 'on' """
        ...
    
    def _get_merge_keys(self):
        ...
    
    def _get_join_indexers(self):
        """ return the join indexers """
        ...
    


def _get_multiindex_indexer(join_keys, index, sort):
    ...

def _get_single_indexer(join_key, index, sort: bool = ...):
    ...

def _left_join_on_index(left_ax, right_ax, join_keys, sort: bool = ...):
    ...

def _right_outer_join(x, y, max_groups):
    ...

_join_functions = { 'inner': libjoin.inner_join,'left': libjoin.left_outer_join,'right': _right_outer_join,'outer': libjoin.full_outer_join }
def _factorize_keys(lk, rk, sort: bool = ...):
    ...

def _sort_labels(uniques, left, right):
    ...

def _get_join_keys(llab, rlab, shape, sort):
    ...

def _should_fill(lname, rname):
    ...

def _any(x):
    ...

