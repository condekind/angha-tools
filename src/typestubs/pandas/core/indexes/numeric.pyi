"""
This type stub file was generated by pyright.
"""

from pandas.core.indexes.base import Index, _index_shared_docs
from pandas.util._decorators import Appender, cache_readonly
from typing import Any, Optional

_num_index_shared_docs = dict()
class NumericIndex(Index):
    """
    Provide numeric type operations

    This is an abstract class

    """
    _is_numeric_dtype = ...
    def __new__(cls, data: Optional[Any] = ..., dtype: Optional[Any] = ..., copy: bool = ..., name: Optional[Any] = ..., fastpath: bool = ...):
        ...
    
    @Appender(_index_shared_docs['_maybe_cast_slice_bound'])
    def _maybe_cast_slice_bound(self, label, side, kind):
        ...
    
    def _convert_for_op(self, value):
        """ Convert value to be insertable to ndarray """
        ...
    
    def _convert_tolerance(self, tolerance, target):
        ...
    
    @classmethod
    def _assert_safe_casting(cls, data, subarr):
        """
        Subclasses need to override this only if the process of casting data
        from some accepted dtype to the internal dtype(s) bears the risk of
        truncation (e.g. float to int).
        """
        ...
    
    @property
    def is_all_dates(self):
        """
        Checks that all the labels are datetime objects
        """
        ...
    


_int64_descr_args = dict(klass='Int64Index', ltype='integer', dtype='int64', extra='')
class Int64Index(NumericIndex):
    __doc__ = ...
    _typ = ...
    _arrmap = ...
    _left_indexer_unique = ...
    _left_indexer = ...
    _inner_indexer = ...
    _outer_indexer = ...
    _can_hold_na = ...
    _engine_type = ...
    _default_dtype = ...
    @property
    def inferred_type(self):
        ...
    
    @property
    def asi8(self):
        ...
    
    @Appender(_index_shared_docs['_convert_scalar_indexer'])
    def _convert_scalar_indexer(self, key, kind: Optional[Any] = ...):
        ...
    
    def _wrap_joined_index(self, joined, other):
        ...
    
    @classmethod
    def _assert_safe_casting(cls, data, subarr):
        """
        Ensure incoming data can be represented as ints.
        """
        ...
    


_uint64_descr_args = dict(klass='UInt64Index', ltype='unsigned integer', dtype='uint64', extra='')
class UInt64Index(NumericIndex):
    __doc__ = ...
    _typ = ...
    _arrmap = ...
    _left_indexer_unique = ...
    _left_indexer = ...
    _inner_indexer = ...
    _outer_indexer = ...
    _can_hold_na = ...
    _na_value = ...
    _engine_type = ...
    _default_dtype = ...
    @property
    def inferred_type(self):
        ...
    
    @property
    def asi8(self):
        ...
    
    @Appender(_index_shared_docs['_convert_scalar_indexer'])
    def _convert_scalar_indexer(self, key, kind: Optional[Any] = ...):
        ...
    
    @Appender(_index_shared_docs['_convert_arr_indexer'])
    def _convert_arr_indexer(self, keyarr):
        ...
    
    @Appender(_index_shared_docs['_convert_index_indexer'])
    def _convert_index_indexer(self, keyarr):
        ...
    
    def _wrap_joined_index(self, joined, other):
        ...
    
    @classmethod
    def _assert_safe_casting(cls, data, subarr):
        """
        Ensure incoming data can be represented as uints.
        """
        ...
    


_float64_descr_args = dict(klass='Float64Index', dtype='float64', ltype='float', extra='')
class Float64Index(NumericIndex):
    __doc__ = ...
    _typ = ...
    _engine_type = ...
    _arrmap = ...
    _left_indexer_unique = ...
    _left_indexer = ...
    _inner_indexer = ...
    _outer_indexer = ...
    _default_dtype = ...
    @property
    def inferred_type(self):
        ...
    
    @Appender(_index_shared_docs['astype'])
    def astype(self, dtype, copy: bool = ...):
        ...
    
    @Appender(_index_shared_docs['_convert_scalar_indexer'])
    def _convert_scalar_indexer(self, key, kind: Optional[Any] = ...):
        ...
    
    @Appender(_index_shared_docs['_convert_slice_indexer'])
    def _convert_slice_indexer(self, key, kind: Optional[Any] = ...):
        ...
    
    def _format_native_types(self, na_rep=..., float_format: Optional[Any] = ..., decimal=..., quoting: Optional[Any] = ..., **kwargs):
        ...
    
    def get_value(self, series, key):
        """ we always want to get an index value, never a value """
        ...
    
    def equals(self, other):
        """
        Determines if two Index objects contain the same elements.
        """
        ...
    
    def __contains__(self, other):
        ...
    
    @Appender(_index_shared_docs['get_loc'])
    def get_loc(self, key, method: Optional[Any] = ..., tolerance: Optional[Any] = ...):
        ...
    
    @cache_readonly
    def is_unique(self):
        ...
    
    @Appender(Index.isin.__doc__)
    def isin(self, values, level: Optional[Any] = ...):
        ...
    


