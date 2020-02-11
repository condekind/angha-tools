"""
This type stub file was generated by pyright.
"""

import pandas.core.base as base
import pandas.core.indexes.base as ibase
from pandas.util._decorators import Appender, cache_readonly, deprecate_kwarg
from pandas.core.indexes.base import Index, _index_shared_docs
from typing import Any, Optional

_index_doc_kwargs = dict(ibase._index_doc_kwargs)
class MultiIndex(Index):
    """
    A multi-level, or hierarchical, index object for pandas objects

    Parameters
    ----------
    levels : sequence of arrays
        The unique labels for each level
    labels : sequence of arrays
        Integers for each level designating which label at each location
    sortorder : optional int
        Level of sortedness (must be lexicographically sorted by that
        level)
    names : optional sequence of objects
        Names for each of the index levels. (name is accepted for compat)
    copy : boolean, default False
        Copy the meta-data
    verify_integrity : boolean, default True
        Check that the levels/labels are consistent and valid

    Examples
    ---------
    A new ``MultiIndex`` is typically constructed using one of the helper
    methods :meth:`MultiIndex.from_arrays`, :meth:`MultiIndex.from_product`
    and :meth:`MultiIndex.from_tuples`. For example (using ``.from_arrays``):

    >>> arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
    >>> pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))
    MultiIndex(levels=[[1, 2], ['blue', 'red']],
           labels=[[0, 0, 1, 1], [1, 0, 1, 0]],
           names=['number', 'color'])

    See further examples for how to construct a MultiIndex in the doc strings
    of the mentioned helper methods.

    Notes
    -----
    See the `user guide
    <http://pandas.pydata.org/pandas-docs/stable/advanced.html>`_ for more.

    See Also
    --------
    MultiIndex.from_arrays  : Convert list of arrays to MultiIndex
    MultiIndex.from_product : Create a MultiIndex from the cartesian product
                              of iterables
    MultiIndex.from_tuples  : Convert list of tuples to a MultiIndex
    Index : The base pandas Index type
    """
    _typ = ...
    _names = ...
    _levels = ...
    _labels = ...
    _comparables = ...
    rename = ...
    def __new__(cls, levels: Optional[Any] = ..., labels: Optional[Any] = ..., sortorder: Optional[Any] = ..., names: Optional[Any] = ..., copy: bool = ..., verify_integrity: bool = ..., _set_identity: bool = ..., name: Optional[Any] = ..., **kwargs):
        ...
    
    def _verify_integrity(self, labels: Optional[Any] = ..., levels: Optional[Any] = ...):
        """

        Parameters
        ----------
        labels : optional list
            Labels to check for validity. Defaults to current labels.
        levels : optional list
            Levels to check for validity. Defaults to current levels.

        Raises
        ------
        ValueError
            * if length of levels and labels don't match or any label would
            exceed level bounds
        """
        ...
    
    def _get_levels(self):
        ...
    
    def _set_levels(self, levels, level: Optional[Any] = ..., copy: bool = ..., validate: bool = ..., verify_integrity: bool = ...):
        ...
    
    def set_levels(self, levels, level: Optional[Any] = ..., inplace: bool = ..., verify_integrity: bool = ...):
        """
        Set new levels on MultiIndex. Defaults to returning
        new index.

        Parameters
        ----------
        levels : sequence or list of sequence
            new level(s) to apply
        level : int, level name, or sequence of int/level names (default None)
            level(s) to set (None for all levels)
        inplace : bool
            if True, mutates in place
        verify_integrity : bool (default True)
            if True, checks that levels and labels are compatible

        Returns
        -------
        new index (of same type and class...etc)


        Examples
        --------
        >>> idx = MultiIndex.from_tuples([(1, u'one'), (1, u'two'),
                                          (2, u'one'), (2, u'two')],
                                          names=['foo', 'bar'])
        >>> idx.set_levels([['a','b'], [1,2]])
        MultiIndex(levels=[[u'a', u'b'], [1, 2]],
                   labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
                   names=[u'foo', u'bar'])
        >>> idx.set_levels(['a','b'], level=0)
        MultiIndex(levels=[[u'a', u'b'], [u'one', u'two']],
                   labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
                   names=[u'foo', u'bar'])
        >>> idx.set_levels(['a','b'], level='bar')
        MultiIndex(levels=[[1, 2], [u'a', u'b']],
                   labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
                   names=[u'foo', u'bar'])
        >>> idx.set_levels([['a','b'], [1,2]], level=[0,1])
        MultiIndex(levels=[[u'a', u'b'], [1, 2]],
                   labels=[[0, 0, 1, 1], [0, 1, 0, 1]],
                   names=[u'foo', u'bar'])
        """
        ...
    
    __set_levels = ...
    levels = ...
    def _get_labels(self):
        ...
    
    def _set_labels(self, labels, level: Optional[Any] = ..., copy: bool = ..., validate: bool = ..., verify_integrity: bool = ...):
        ...
    
    def set_labels(self, labels, level: Optional[Any] = ..., inplace: bool = ..., verify_integrity: bool = ...):
        """
        Set new labels on MultiIndex. Defaults to returning
        new index.

        Parameters
        ----------
        labels : sequence or list of sequence
            new labels to apply
        level : int, level name, or sequence of int/level names (default None)
            level(s) to set (None for all levels)
        inplace : bool
            if True, mutates in place
        verify_integrity : bool (default True)
            if True, checks that levels and labels are compatible

        Returns
        -------
        new index (of same type and class...etc)

        Examples
        --------
        >>> idx = MultiIndex.from_tuples([(1, u'one'), (1, u'two'),
                                          (2, u'one'), (2, u'two')],
                                          names=['foo', 'bar'])
        >>> idx.set_labels([[1,0,1,0], [0,0,1,1]])
        MultiIndex(levels=[[1, 2], [u'one', u'two']],
                   labels=[[1, 0, 1, 0], [0, 0, 1, 1]],
                   names=[u'foo', u'bar'])
        >>> idx.set_labels([1,0,1,0], level=0)
        MultiIndex(levels=[[1, 2], [u'one', u'two']],
                   labels=[[1, 0, 1, 0], [0, 1, 0, 1]],
                   names=[u'foo', u'bar'])
        >>> idx.set_labels([0,0,1,1], level='bar')
        MultiIndex(levels=[[1, 2], [u'one', u'two']],
                   labels=[[0, 0, 1, 1], [0, 0, 1, 1]],
                   names=[u'foo', u'bar'])
        >>> idx.set_labels([[1,0,1,0], [0,0,1,1]], level=[0,1])
        MultiIndex(levels=[[1, 2], [u'one', u'two']],
                   labels=[[1, 0, 1, 0], [0, 0, 1, 1]],
                   names=[u'foo', u'bar'])
        """
        ...
    
    __set_labels = ...
    labels = ...
    def copy(self, names: Optional[Any] = ..., dtype: Optional[Any] = ..., levels: Optional[Any] = ..., labels: Optional[Any] = ..., deep: bool = ..., _set_identity: bool = ..., **kwargs):
        """
        Make a copy of this object. Names, dtype, levels and labels can be
        passed and will be set on new copy.

        Parameters
        ----------
        names : sequence, optional
        dtype : numpy dtype or pandas type, optional
        levels : sequence, optional
        labels : sequence, optional

        Returns
        -------
        copy : MultiIndex

        Notes
        -----
        In most cases, there should be no functional difference from using
        ``deep``, but if ``deep`` is passed it will attempt to deepcopy.
        This could be potentially expensive on large MultiIndex objects.
        """
        ...
    
    def __array__(self, dtype: Optional[Any] = ...):
        """ the array interface, return my values """
        ...
    
    def view(self, cls: Optional[Any] = ...):
        """ this is defined as a copy with the same identity """
        ...
    
    def _shallow_copy_with_infer(self, values: Optional[Any] = ..., **kwargs):
        ...
    
    @Appender(_index_shared_docs['__contains__'] % _index_doc_kwargs)
    def __contains__(self, key):
        ...
    
    contains = ...
    @Appender(_index_shared_docs['_shallow_copy'])
    def _shallow_copy(self, values: Optional[Any] = ..., **kwargs):
        ...
    
    @cache_readonly
    def dtype(self):
        ...
    
    def _is_memory_usage_qualified(self):
        """ return a boolean if we need a qualified .info display """
        ...
    
    @Appender(Index.memory_usage.__doc__)
    def memory_usage(self, deep: bool = ...):
        ...
    
    @cache_readonly
    def nbytes(self):
        """ return the number of bytes in the underlying data """
        ...
    
    def _nbytes(self, deep: bool = ...):
        """
        return the number of bytes in the underlying data
        deeply introspect the level data if deep=True

        include the engine hashtable

        *this is in internal routine*

        """
        ...
    
    def _format_attrs(self):
        """
        Return a list of tuples of the (attr,formatted_value)
        """
        ...
    
    def _format_space(self):
        ...
    
    def _format_data(self, name: Optional[Any] = ...):
        ...
    
    def __len__(self):
        ...
    
    def _get_names(self):
        ...
    
    def _set_names(self, names, level: Optional[Any] = ..., validate: bool = ...):
        """
        sets names on levels. WARNING: mutates!

        Note that you generally want to set this *after* changing levels, so
        that it only acts on copies
        """
        ...
    
    names = ...
    def _reference_duplicate_name(self, name):
        """
        Returns True if the name refered to in self.names is duplicated.
        """
        ...
    
    def _format_native_types(self, na_rep=..., **kwargs):
        ...
    
    @Appender(_index_shared_docs['_get_grouper_for_level'])
    def _get_grouper_for_level(self, mapper, level):
        ...
    
    @property
    def _constructor(self):
        ...
    
    @cache_readonly
    def inferred_type(self):
        ...
    
    @staticmethod
    def _from_elements(values, labels: Optional[Any] = ..., levels: Optional[Any] = ..., names: Optional[Any] = ..., sortorder: Optional[Any] = ...):
        ...
    
    def _get_level_number(self, level):
        ...
    
    _tuples = ...
    @cache_readonly
    def _engine(self):
        ...
    
    @property
    def values(self):
        ...
    
    @property
    def _is_v1(self):
        ...
    
    @property
    def _is_v2(self):
        ...
    
    @property
    def _has_complex_internals(self):
        ...
    
    @cache_readonly
    def is_monotonic(self):
        """
        return if the index is monotonic increasing (only equal or
        increasing) values.
        """
        ...
    
    @cache_readonly
    def is_monotonic_increasing(self):
        """
        return if the index is monotonic increasing (only equal or
        increasing) values.
        """
        ...
    
    @cache_readonly
    def is_monotonic_decreasing(self):
        """
        return if the index is monotonic decreasing (only equal or
        decreasing) values.
        """
        ...
    
    @cache_readonly
    def is_unique(self):
        ...
    
    @cache_readonly
    def _have_mixed_levels(self):
        """ return a boolean list indicated if we have mixed levels """
        ...
    
    @cache_readonly
    def _inferred_type_levels(self):
        """ return a list of the inferred types, one for each level """
        ...
    
    @cache_readonly
    def _hashed_values(self):
        """ return a uint64 ndarray of my hashed values """
        ...
    
    def _hashed_indexing_key(self, key):
        """
        validate and return the hash for the provided key

        *this is internal for use for the cython routines*

        Paramters
        ---------
        key : string or tuple

        Returns
        -------
        np.uint64

        Notes
        -----
        we need to stringify if we have mixed levels

        """
        ...
    
    @Appender(base._shared_docs['duplicated'] % _index_doc_kwargs)
    def duplicated(self, keep=...):
        ...
    
    def fillna(self, value: Optional[Any] = ..., downcast: Optional[Any] = ...):
        """
        fillna is not implemented for MultiIndex
        """
        ...
    
    @Appender(_index_shared_docs['dropna'])
    def dropna(self, how=...):
        ...
    
    def get_value(self, series, key):
        ...
    
    def _get_level_values(self, level):
        """
        Return vector of label values for requested level,
        equal to the length of the index

        **this is an internal method**

        Parameters
        ----------
        level : int level

        Returns
        -------
        values : ndarray
        """
        ...
    
    def get_level_values(self, level):
        """
        Return vector of label values for requested level,
        equal to the length of the index.

        Parameters
        ----------
        level : int or str
            ``level`` is either the integer position of the level in the
            MultiIndex, or the name of the level.

        Returns
        -------
        values : Index
            ``values`` is a level of this MultiIndex converted to
            a single :class:`Index` (or subclass thereof).

        Examples
        ---------

        Create a MultiIndex:

        >>> mi = pd.MultiIndex.from_arrays((list('abc'), list('def')))
        >>> mi.names = ['level_1', 'level_2']

        Get level values by supplying level as either integer or name:

        >>> mi.get_level_values(0)
        Index(['a', 'b', 'c'], dtype='object', name='level_1')
        >>> mi.get_level_values('level_2')
        Index(['d', 'e', 'f'], dtype='object', name='level_2')
        """
        ...
    
    def format(self, space=..., sparsify: Optional[Any] = ..., adjoin: bool = ..., names: bool = ..., na_rep: Optional[Any] = ..., formatter: Optional[Any] = ...):
        ...
    
    def _to_safe_for_reshape(self):
        """ convert to object if we are a categorical """
        ...
    
    def to_frame(self, index: bool = ...):
        """
        Create a DataFrame with the levels of the MultiIndex as columns.

        .. versionadded:: 0.20.0

        Parameters
        ----------
        index : boolean, default True
            Set the index of the returned DataFrame as the original MultiIndex.

        Returns
        -------
        DataFrame : a DataFrame containing the original MultiIndex data.
        """
        ...
    
    def to_hierarchical(self, n_repeat, n_shuffle=...):
        """
        Return a MultiIndex reshaped to conform to the
        shapes given by n_repeat and n_shuffle.

        Useful to replicate and rearrange a MultiIndex for combination
        with another Index with n_repeat items.

        Parameters
        ----------
        n_repeat : int
            Number of times to repeat the labels on self
        n_shuffle : int
            Controls the reordering of the labels. If the result is going
            to be an inner level in a MultiIndex, n_shuffle will need to be
            greater than one. The size of each label must divisible by
            n_shuffle.

        Returns
        -------
        MultiIndex

        Examples
        --------
        >>> idx = MultiIndex.from_tuples([(1, u'one'), (1, u'two'),
                                          (2, u'one'), (2, u'two')])
        >>> idx.to_hierarchical(3)
        MultiIndex(levels=[[1, 2], [u'one', u'two']],
                   labels=[[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                           [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]])
        """
        ...
    
    @property
    def is_all_dates(self):
        ...
    
    def is_lexsorted(self):
        """
        Return True if the labels are lexicographically sorted
        """
        ...
    
    @cache_readonly
    def lexsort_depth(self):
        ...
    
    @classmethod
    def from_arrays(cls, arrays, sortorder: Optional[Any] = ..., names: Optional[Any] = ...):
        """
        Convert arrays to MultiIndex

        Parameters
        ----------
        arrays : list / sequence of array-likes
            Each array-like gives one level's value for each data point.
            len(arrays) is the number of levels.
        sortorder : int or None
            Level of sortedness (must be lexicographically sorted by that
            level)

        Returns
        -------
        index : MultiIndex

        Examples
        --------
        >>> arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
        >>> MultiIndex.from_arrays(arrays, names=('number', 'color'))

        See Also
        --------
        MultiIndex.from_tuples : Convert list of tuples to MultiIndex
        MultiIndex.from_product : Make a MultiIndex from cartesian product
                                  of iterables
        """
        ...
    
    @classmethod
    def from_tuples(cls, tuples, sortorder: Optional[Any] = ..., names: Optional[Any] = ...):
        """
        Convert list of tuples to MultiIndex

        Parameters
        ----------
        tuples : list / sequence of tuple-likes
            Each tuple is the index of one row/column.
        sortorder : int or None
            Level of sortedness (must be lexicographically sorted by that
            level)

        Returns
        -------
        index : MultiIndex

        Examples
        --------
        >>> tuples = [(1, u'red'), (1, u'blue'),
                      (2, u'red'), (2, u'blue')]
        >>> MultiIndex.from_tuples(tuples, names=('number', 'color'))

        See Also
        --------
        MultiIndex.from_arrays : Convert list of arrays to MultiIndex
        MultiIndex.from_product : Make a MultiIndex from cartesian product
                                  of iterables
        """
        ...
    
    @classmethod
    def from_product(cls, iterables, sortorder: Optional[Any] = ..., names: Optional[Any] = ...):
        """
        Make a MultiIndex from the cartesian product of multiple iterables

        Parameters
        ----------
        iterables : list / sequence of iterables
            Each iterable has unique labels for each level of the index.
        sortorder : int or None
            Level of sortedness (must be lexicographically sorted by that
            level).
        names : list / sequence of strings or None
            Names for the levels in the index.

        Returns
        -------
        index : MultiIndex

        Examples
        --------
        >>> numbers = [0, 1, 2]
        >>> colors = [u'green', u'purple']
        >>> MultiIndex.from_product([numbers, colors],
                                     names=['number', 'color'])
        MultiIndex(levels=[[0, 1, 2], [u'green', u'purple']],
                   labels=[[0, 0, 1, 1, 2, 2], [0, 1, 0, 1, 0, 1]],
                   names=[u'number', u'color'])

        See Also
        --------
        MultiIndex.from_arrays : Convert list of arrays to MultiIndex
        MultiIndex.from_tuples : Convert list of tuples to MultiIndex
        """
        ...
    
    def _sort_levels_monotonic(self):
        """
        .. versionadded:: 0.20.0

        This is an *internal* function.

        create a new MultiIndex from the current to monotonically sorted
        items IN the levels. This does not actually make the entire MultiIndex
        monotonic, JUST the levels.

        The resulting MultiIndex will have the same outward
        appearance, meaning the same .values and ordering. It will also
        be .equals() to the original.

        Returns
        -------
        MultiIndex

        Examples
        --------

        >>> i = pd.MultiIndex(levels=[['a', 'b'], ['bb', 'aa']],
                              labels=[[0, 0, 1, 1], [0, 1, 0, 1]])
        >>> i
        MultiIndex(levels=[['a', 'b'], ['bb', 'aa']],
                   labels=[[0, 0, 1, 1], [0, 1, 0, 1]])

        >>> i.sort_monotonic()
        MultiIndex(levels=[['a', 'b'], ['aa', 'bb']],
                   labels=[[0, 0, 1, 1], [1, 0, 1, 0]])

        """
        ...
    
    def remove_unused_levels(self):
        """
        create a new MultiIndex from the current that removing
        unused levels, meaning that they are not expressed in the labels

        The resulting MultiIndex will have the same outward
        appearance, meaning the same .values and ordering. It will also
        be .equals() to the original.

        .. versionadded:: 0.20.0

        Returns
        -------
        MultiIndex

        Examples
        --------
        >>> i = pd.MultiIndex.from_product([range(2), list('ab')])
        MultiIndex(levels=[[0, 1], ['a', 'b']],
                   labels=[[0, 0, 1, 1], [0, 1, 0, 1]])


        >>> i[2:]
        MultiIndex(levels=[[0, 1], ['a', 'b']],
                   labels=[[1, 1], [0, 1]])

        The 0 from the first level is not represented
        and can be removed

        >>> i[2:].remove_unused_levels()
        MultiIndex(levels=[[1], ['a', 'b']],
                   labels=[[0, 0], [0, 1]])

        """
        ...
    
    @property
    def nlevels(self):
        ...
    
    @property
    def levshape(self):
        ...
    
    def __reduce__(self):
        """Necessary for making this object picklable"""
        ...
    
    def __setstate__(self, state):
        """Necessary for making this object picklable"""
        self.sortorder = ...
    
    def __getitem__(self, key):
        ...
    
    @Appender(_index_shared_docs['take'] % _index_doc_kwargs)
    def take(self, indices, axis=..., allow_fill: bool = ..., fill_value: Optional[Any] = ..., **kwargs):
        ...
    
    def _assert_take_fillable(self, values, indices, allow_fill: bool = ..., fill_value: Optional[Any] = ..., na_value: Optional[Any] = ...):
        """ Internal method to handle NA filling of take """
        ...
    
    def append(self, other):
        """
        Append a collection of Index options together

        Parameters
        ----------
        other : Index or list/tuple of indices

        Returns
        -------
        appended : Index
        """
        ...
    
    def argsort(self, *args, **kwargs):
        ...
    
    @deprecate_kwarg(old_arg_name='n', new_arg_name='repeats')
    def repeat(self, repeats, *args, **kwargs):
        ...
    
    def where(self, cond, other: Optional[Any] = ...):
        ...
    
    def drop(self, labels, level: Optional[Any] = ..., errors=...):
        """
        Make new MultiIndex with passed list of labels deleted

        Parameters
        ----------
        labels : array-like
            Must be a list of tuples
        level : int or level name, default None

        Returns
        -------
        dropped : MultiIndex
        """
        ...
    
    def _drop_from_level(self, labels, level):
        ...
    
    def droplevel(self, level=...):
        """
        Return Index with requested level removed. If MultiIndex has only 2
        levels, the result will be of Index type not MultiIndex.

        Parameters
        ----------
        level : int/level name or list thereof

        Notes
        -----
        Does not check if result index is unique or not

        Returns
        -------
        index : Index or MultiIndex
        """
        ...
    
    def swaplevel(self, i=..., j=...):
        """
        Swap level i with level j. Do not change the ordering of anything

        Parameters
        ----------
        i, j : int, string (can be mixed)
            Level of index to be swapped. Can pass level name as string.

        Returns
        -------
        swapped : MultiIndex

        .. versionchanged:: 0.18.1

           The indexes ``i`` and ``j`` are now optional, and default to
           the two innermost levels of the index.

        """
        ...
    
    def reorder_levels(self, order):
        """
        Rearrange levels using input order. May not drop or duplicate levels

        Parameters
        ----------
        """
        ...
    
    def __getslice__(self, i, j):
        ...
    
    def _get_labels_for_sorting(self):
        """
        we categorizing our labels by using the
        available catgories (all, not just observed)
        excluding any missing ones (-1); this is in preparation
        for sorting, where we need to disambiguate that -1 is not
        a valid valid
        """
        ...
    
    def sortlevel(self, level=..., ascending: bool = ..., sort_remaining: bool = ...):
        """
        Sort MultiIndex at the requested level. The result will respect the
        original ordering of the associated factor at that level.

        Parameters
        ----------
        level : list-like, int or str, default 0
            If a string is given, must be a name of the level
            If list-like must be names or ints of levels.
        ascending : boolean, default True
            False to sort in descending order
            Can also be a list to specify a directed ordering
        sort_remaining : sort by the remaining levels after level.

        Returns
        -------
        sorted_index : pd.MultiIndex
            Resulting index
        indexer : np.ndarray
            Indices of output values in original index

        """
        ...
    
    def _convert_listlike_indexer(self, keyarr, kind: Optional[Any] = ...):
        """
        Parameters
        ----------
        keyarr : list-like
            Indexer to convert.

        Returns
        -------
        tuple (indexer, keyarr)
            indexer is an ndarray or None if cannot convert
            keyarr are tuple-safe keys
        """
        ...
    
    @Appender(_index_shared_docs['get_indexer'] % _index_doc_kwargs)
    def get_indexer(self, target, method: Optional[Any] = ..., limit: Optional[Any] = ..., tolerance: Optional[Any] = ...):
        ...
    
    @Appender(_index_shared_docs['get_indexer_non_unique'] % _index_doc_kwargs)
    def get_indexer_non_unique(self, target):
        ...
    
    def reindex(self, target, method: Optional[Any] = ..., level: Optional[Any] = ..., limit: Optional[Any] = ..., tolerance: Optional[Any] = ...):
        """
        Create index with target's values (move/add/delete values as necessary)

        Returns
        -------
        new_index : pd.MultiIndex
            Resulting index
        indexer : np.ndarray or None
            Indices of output values in original index

        """
        ...
    
    def get_slice_bound(self, label, side, kind):
        ...
    
    def slice_locs(self, start: Optional[Any] = ..., end: Optional[Any] = ..., step: Optional[Any] = ..., kind: Optional[Any] = ...):
        """
        For an ordered MultiIndex, compute the slice locations for input
        labels.

        The input labels can be tuples representing partial levels, e.g. for a
        MultiIndex with 3 levels, you can pass a single value (corresponding to
        the first level), or a 1-, 2-, or 3-tuple.

        Parameters
        ----------
        start : label or tuple, default None
            If None, defaults to the beginning
        end : label or tuple
            If None, defaults to the end
        step : int or None
            Slice step
        kind : string, optional, defaults None

        Returns
        -------
        (start, end) : (int, int)

        Notes
        -----
        This method only works if the MultiIndex is properly lex-sorted. So,
        if only the first 2 levels of a 3-level MultiIndex are lexsorted,
        you can only pass two levels to ``.slice_locs``.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([list('abbd'), list('deff')],
        ...                                names=['A', 'B'])

        Get the slice locations from the beginning of 'b' in the first level
        until the end of the multiindex:

        >>> mi.slice_locs(start='b')
        (1, 4)

        Like above, but stop at the end of 'b' in the first level and 'f' in
        the second level:

        >>> mi.slice_locs(start='b', end=('b', 'f'))
        (1, 3)

        See Also
        --------
        MultiIndex.get_loc : Get location for a label or a tuple of labels.
        MultiIndex.get_locs : Get location for a label/slice/list/mask or a
                              sequence of such.
        """
        ...
    
    def _partial_tup_index(self, tup, side=...):
        ...
    
    def get_loc(self, key, method: Optional[Any] = ...):
        """
        Get location for a label or a tuple of labels as an integer, slice or
        boolean mask.

        Parameters
        ----------
        key : label or tuple of labels (one for each level)
        method : None

        Returns
        -------
        loc : int, slice object or boolean mask
            If the key is past the lexsort depth, the return may be a
            boolean mask array, otherwise it is always a slice or int.

        Examples
        ---------
        >>> mi = pd.MultiIndex.from_arrays([list('abb'), list('def')])

        >>> mi.get_loc('b')
        slice(1, 3, None)

        >>> mi.get_loc(('b', 'e'))
        1

        Notes
        ------
        The key cannot be a slice, list of same-level labels, a boolean mask,
        or a sequence of such. If you want to use those, use
        :meth:`MultiIndex.get_locs` instead.

        See also
        --------
        Index.get_loc : get_loc method for (single-level) index.
        MultiIndex.slice_locs : Get slice location given start label(s) and
                                end label(s).
        MultiIndex.get_locs : Get location for a label/slice/list/mask or a
                              sequence of such.
        """
        ...
    
    def get_loc_level(self, key, level=..., drop_level: bool = ...):
        """
        Get both the location for the requested label(s) and the
        resulting sliced index.

        Parameters
        ----------
        key : label or sequence of labels
        level : int/level name or list thereof, optional
        drop_level : bool, default True
            if ``False``, the resulting index will not drop any level.

        Returns
        -------
        loc : A 2-tuple where the elements are:
              Element 0: int, slice object or boolean array
              Element 1: The resulting sliced multiindex/index. If the key
              contains all levels, this will be ``None``.

        Examples
        --------
        >>> mi = pd.MultiIndex.from_arrays([list('abb'), list('def')],
        ...                                names=['A', 'B'])

        >>> mi.get_loc_level('b')
        (slice(1, 3, None), Index(['e', 'f'], dtype='object', name='B'))

        >>> mi.get_loc_level('e', level='B')
        (array([False,  True, False], dtype=bool),
        Index(['b'], dtype='object', name='A'))

        >>> mi.get_loc_level(['b', 'e'])
        (1, None)

        See Also
        ---------
        MultiIndex.get_loc  : Get location for a label or a tuple of labels.
        MultiIndex.get_locs : Get location for a label/slice/list/mask or a
                              sequence of such
        """
        ...
    
    def _get_level_indexer(self, key, level=..., indexer: Optional[Any] = ...):
        ...
    
    def get_locs(self, seq):
        """
        Get location for a given label/slice/list/mask or a sequence of such as
        an array of integers.

        Parameters
        ----------
        seq : label/slice/list/mask or a sequence of such
           You should use one of the above for each level.
           If a level should not be used, set it to ``slice(None)``.

        Returns
        -------
        locs : array of integers suitable for passing to iloc

        Examples
        ---------
        >>> mi = pd.MultiIndex.from_arrays([list('abb'), list('def')])

        >>> mi.get_locs('b')
        array([1, 2], dtype=int64)

        >>> mi.get_locs([slice(None), ['e', 'f']])
        array([1, 2], dtype=int64)

        >>> mi.get_locs([[True, False, True], slice('e', 'f')])
        array([2], dtype=int64)

        See also
        --------
        MultiIndex.get_loc : Get location for a label or a tuple of labels.
        MultiIndex.slice_locs : Get slice location given start label(s) and
                                end label(s).
        """
        ...
    
    def truncate(self, before: Optional[Any] = ..., after: Optional[Any] = ...):
        """
        Slice index between two labels / tuples, return new MultiIndex

        Parameters
        ----------
        before : label or tuple, can be partial. Default None
            None defaults to start
        after : label or tuple, can be partial. Default None
            None defaults to end

        Returns
        -------
        truncated : MultiIndex
        """
        ...
    
    def equals(self, other):
        """
        Determines if two MultiIndex objects have the same labeling information
        (the levels themselves do not necessarily have to be the same)

        See also
        --------
        equal_levels
        """
        ...
    
    def equal_levels(self, other):
        """
        Return True if the levels of both MultiIndex objects are the same

        """
        ...
    
    def union(self, other):
        """
        Form the union of two MultiIndex objects, sorting if possible

        Parameters
        ----------
        other : MultiIndex or array / Index of tuples

        Returns
        -------
        Index

        >>> index.union(index2)
        """
        ...
    
    def intersection(self, other):
        """
        Form the intersection of two MultiIndex objects, sorting if possible

        Parameters
        ----------
        other : MultiIndex or array / Index of tuples

        Returns
        -------
        Index
        """
        ...
    
    def difference(self, other):
        """
        Compute sorted set difference of two MultiIndex objects

        Returns
        -------
        diff : MultiIndex
        """
        ...
    
    @Appender(_index_shared_docs['astype'])
    def astype(self, dtype, copy: bool = ...):
        ...
    
    def _convert_can_do_setop(self, other):
        ...
    
    def insert(self, loc, item):
        """
        Make new MultiIndex inserting new item at location

        Parameters
        ----------
        loc : int
        item : tuple
            Must be same length as number of levels in the MultiIndex

        Returns
        -------
        new_index : Index
        """
        ...
    
    def delete(self, loc):
        """
        Make new index with passed location deleted

        Returns
        -------
        new_index : MultiIndex
        """
        ...
    
    get_major_bounds = ...
    __bounds = ...
    @property
    def _bounds(self):
        """
        Return or compute and return slice points for level 0, assuming
        sortedness
        """
        ...
    
    def _wrap_joined_index(self, joined, other):
        ...
    
    @Appender(Index.isin.__doc__)
    def isin(self, values, level: Optional[Any] = ...):
        ...
    


def _sparsify(label_list, start=..., sentinel=...):
    ...

def _get_na_rep(dtype):
    ...

