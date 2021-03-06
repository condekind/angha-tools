"""
This type stub file was generated by pyright.
"""

import pandas.core.base as base
import pandas.core.indexes.base as ibase
from pandas.util._decorators import Appender, cache_readonly
from pandas.core.indexes.base import Index, _index_shared_docs
from pandas.core import accessor
from typing import Any, Optional

_index_doc_kwargs = dict(ibase._index_doc_kwargs)
class CategoricalIndex(Index, accessor.PandasDelegate):
    """

    Immutable Index implementing an ordered, sliceable set. CategoricalIndex
    represents a sparsely populated Index with an underlying Categorical.

    Parameters
    ----------
    data : array-like or Categorical, (1-dimensional)
    categories : optional, array-like
        categories for the CategoricalIndex
    ordered : boolean,
        designating if the categories are ordered
    copy : bool
        Make a copy of input ndarray
    name : object
        Name to be stored in the index

    See Also
    --------
    Categorical, Index
    """
    _typ = ...
    _engine_type = ...
    _attributes = ...
    def __new__(cls, data: Optional[Any] = ..., categories: Optional[Any] = ..., ordered: Optional[Any] = ..., dtype: Optional[Any] = ..., copy: bool = ..., name: Optional[Any] = ..., fastpath: bool = ..., **kwargs):
        ...
    
    def _create_from_codes(self, codes, categories: Optional[Any] = ..., ordered: Optional[Any] = ..., name: Optional[Any] = ...):
        """
        *this is an internal non-public method*

        create the correct categorical from codes

        Parameters
        ----------
        codes : new codes
        categories : optional categories, defaults to existing
        ordered : optional ordered attribute, defaults to existing
        name : optional name attribute, defaults to existing

        Returns
        -------
        CategoricalIndex
        """
        ...
    
    @staticmethod
    def _create_categorical(self, data, categories: Optional[Any] = ..., ordered: Optional[Any] = ..., dtype: Optional[Any] = ...):
        """
        *this is an internal non-public method*

        create the correct categorical from data and the properties

        Parameters
        ----------
        data : data for new Categorical
        categories : optional categories, defaults to existing
        ordered : optional ordered attribute, defaults to existing
        dtype : CategoricalDtype, defaults to existing

        Returns
        -------
        Categorical
        """
        ...
    
    @classmethod
    def _simple_new(cls, values, name: Optional[Any] = ..., categories: Optional[Any] = ..., ordered: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs):
        ...
    
    @Appender(_index_shared_docs['_shallow_copy'])
    def _shallow_copy(self, values: Optional[Any] = ..., categories: Optional[Any] = ..., ordered: Optional[Any] = ..., dtype: Optional[Any] = ..., **kwargs):
        ...
    
    def _is_dtype_compat(self, other):
        """
        *this is an internal non-public method*

        provide a comparison between the dtype of self and other (coercing if
        needed)

        Raises
        ------
        TypeError if the dtypes are not compatible
        """
        ...
    
    def equals(self, other):
        """
        Determines if two CategorialIndex objects contain the same elements.
        """
        ...
    
    @property
    def _formatter_func(self):
        ...
    
    def _format_attrs(self):
        """
        Return a list of tuples of the (attr,formatted_value)
        """
        ...
    
    @property
    def inferred_type(self):
        ...
    
    @property
    def values(self):
        """ return the underlying data, which is a Categorical """
        ...
    
    def get_values(self):
        """ return the underlying data as an ndarray """
        ...
    
    def tolist(self):
        ...
    
    @property
    def codes(self):
        ...
    
    @property
    def categories(self):
        ...
    
    @property
    def ordered(self):
        ...
    
    def _reverse_indexer(self):
        ...
    
    @Appender(_index_shared_docs['__contains__'] % _index_doc_kwargs)
    def __contains__(self, key):
        ...
    
    @Appender(_index_shared_docs['contains'] % _index_doc_kwargs)
    def contains(self, key):
        ...
    
    def __array__(self, dtype: Optional[Any] = ...):
        """ the array interface, return my values """
        ...
    
    @Appender(_index_shared_docs['astype'])
    def astype(self, dtype, copy: bool = ...):
        ...
    
    @cache_readonly
    def _isnan(self):
        """ return if each value is nan"""
        ...
    
    @Appender(ibase._index_shared_docs['fillna'])
    def fillna(self, value, downcast: Optional[Any] = ...):
        ...
    
    def argsort(self, *args, **kwargs):
        ...
    
    @cache_readonly
    def _engine(self):
        ...
    
    @cache_readonly
    def is_unique(self):
        ...
    
    @property
    def is_monotonic_increasing(self):
        ...
    
    @property
    def is_monotonic_decreasing(self):
        ...
    
    @Appender(base._shared_docs['unique'] % _index_doc_kwargs)
    def unique(self):
        ...
    
    @Appender(base._shared_docs['duplicated'] % _index_doc_kwargs)
    def duplicated(self, keep=...):
        ...
    
    def _to_safe_for_reshape(self):
        """ convert to object if we are a categorical """
        ...
    
    def get_loc(self, key, method: Optional[Any] = ...):
        """
        Get integer location, slice or boolean mask for requested label.

        Parameters
        ----------
        key : label
        method : {None}
            * default: exact matches only.

        Returns
        -------
        loc : int if unique index, slice if monotonic index, else mask

        Examples
        ---------
        >>> unique_index = pd.CategoricalIndex(list('abc'))
        >>> unique_index.get_loc('b')
        1

        >>> monotonic_index = pd.CategoricalIndex(list('abbc'))
        >>> monotonic_index.get_loc('b')
        slice(1, 3, None)

        >>> non_monotonic_index = p.dCategoricalIndex(list('abcb'))
        >>> non_monotonic_index.get_loc('b')
        array([False,  True, False,  True], dtype=bool)
        """
        ...
    
    def get_value(self, series, key):
        """
        Fast lookup of value from 1-dimensional ndarray. Only use this if you
        know what you're doing
        """
        ...
    
    def _can_reindex(self, indexer):
        """ always allow reindexing """
        ...
    
    @Appender(_index_shared_docs['where'])
    def where(self, cond, other: Optional[Any] = ...):
        ...
    
    def reindex(self, target, method: Optional[Any] = ..., level: Optional[Any] = ..., limit: Optional[Any] = ..., tolerance: Optional[Any] = ...):
        """
        Create index with target's values (move/add/delete values as necessary)

        Returns
        -------
        new_index : pd.Index
            Resulting index
        indexer : np.ndarray or None
            Indices of output values in original index

        """
        ...
    
    def _reindex_non_unique(self, target):
        """ reindex from a non-unique; which CategoricalIndex's are almost
        always
        """
        ...
    
    @Appender(_index_shared_docs['get_indexer'] % _index_doc_kwargs)
    def get_indexer(self, target, method: Optional[Any] = ..., limit: Optional[Any] = ..., tolerance: Optional[Any] = ...):
        ...
    
    @Appender(_index_shared_docs['get_indexer_non_unique'] % _index_doc_kwargs)
    def get_indexer_non_unique(self, target):
        ...
    
    @Appender(_index_shared_docs['_convert_scalar_indexer'])
    def _convert_scalar_indexer(self, key, kind: Optional[Any] = ...):
        ...
    
    @Appender(_index_shared_docs['_convert_list_indexer'])
    def _convert_list_indexer(self, keyarr, kind: Optional[Any] = ...):
        ...
    
    @Appender(_index_shared_docs['_convert_arr_indexer'])
    def _convert_arr_indexer(self, keyarr):
        ...
    
    @Appender(_index_shared_docs['_convert_index_indexer'])
    def _convert_index_indexer(self, keyarr):
        ...
    
    @Appender(_index_shared_docs['take'] % _index_doc_kwargs)
    def take(self, indices, axis=..., allow_fill: bool = ..., fill_value: Optional[Any] = ..., **kwargs):
        ...
    
    def is_dtype_equal(self, other):
        ...
    
    take_nd = ...
    def map(self, mapper):
        """Apply mapper function to its categories (not codes).

        Parameters
        ----------
        mapper : callable
            Function to be applied. When all categories are mapped
            to different categories, the result will be a CategoricalIndex
            which has the same order property as the original. Otherwise,
            the result will be a Index.

        Returns
        -------
        applied : CategoricalIndex or Index

        """
        ...
    
    def delete(self, loc):
        """
        Make new Index with passed location(-s) deleted

        Returns
        -------
        new_index : Index
        """
        ...
    
    def insert(self, loc, item):
        """
        Make new Index inserting new item at location. Follows
        Python list.append semantics for negative values

        Parameters
        ----------
        loc : int
        item : object

        Returns
        -------
        new_index : Index

        Raises
        ------
        ValueError if the item is not in the categories

        """
        ...
    
    def _concat(self, to_concat, name):
        ...
    
    def _concat_same_dtype(self, to_concat, name):
        """
        Concatenate to_concat which has the same class
        ValueError if other is not in the categories
        """
        ...
    
    def _codes_for_groupby(self, sort):
        """ Return a Categorical adjusted for groupby """
        ...
    
    @classmethod
    def _add_comparison_methods(cls):
        """ add in comparison methods """
        ...
    
    def _delegate_method(self, name, *args, **kwargs):
        """ method delegation to the ._values """
        ...
    
    @classmethod
    def _add_accessors(cls):
        """ add in Categorical accessor methods """
        ...
    


