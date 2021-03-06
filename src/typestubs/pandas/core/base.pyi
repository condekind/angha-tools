"""
This type stub file was generated by pyright.
"""

from pandas.util._decorators import Appender, Substitution, cache_readonly, deprecate_kwarg
from pandas.core.accessor import DirNamesMixin
from typing import Any, Optional

"""
Base and utility classes for pandas objects.
"""
_shared_docs = dict()
_indexops_doc_kwargs = dict(klass='IndexOpsMixin', inplace='', unique='IndexOpsMixin', duplicated='IndexOpsMixin')
class StringMixin(object):
    """implements string methods so long as object defines a `__unicode__`
    method.

    Handles Python2/3 compatibility transparently.
    """
    def __unicode__(self):
        ...
    
    def __str__(self):
        """
        Return a string representation for a particular Object

        Invoked by str(df) in both py2/py3.
        Yields Bytestring in Py2, Unicode String in py3.
        """
        ...
    
    def __bytes__(self):
        """
        Return a string representation for a particular object.

        Invoked by bytes(obj) in py3 only.
        Yields a bytestring in both py2/py3.
        """
        ...
    
    def __repr__(self):
        """
        Return a string representation for a particular object.

        Yields Bytestring in Py2, Unicode String in py3.
        """
        ...
    


class PandasObject(StringMixin, DirNamesMixin):
    """baseclass for various pandas objects"""
    @property
    def _constructor(self):
        """class constructor (for this class it's just `__class__`"""
        ...
    
    def __unicode__(self):
        """
        Return a string representation for a particular object.

        Invoked by unicode(obj) in py2 only. Yields a Unicode String in both
        py2/py3.
        """
        ...
    
    def _reset_cache(self, key: Optional[Any] = ...):
        """
        Reset cached properties. If ``key`` is passed, only clears that key.
        """
        ...
    
    def __sizeof__(self):
        """
        Generates the total memory usage for a object that returns
        either a value or Series of values
        """
        ...
    


class NoNewAttributesMixin(object):
    """Mixin which prevents adding new attributes.

    Prevents additional attributes via xxx.attribute = "something" after a
    call to `self.__freeze()`. Mainly used to prevent the user from using
    wrong attributes on a accessor (`Series.cat/.str/.dt`).

    If you really want to add a new attribute at a later time, you need to use
    `object.__setattr__(self, key, value)`.
    """
    def _freeze(self):
        """Prevents setting additional attributes"""
        ...
    
    def __setattr__(self, key, value):
        ...
    


class GroupByError(Exception):
    ...


class DataError(GroupByError):
    ...


class SpecificationError(GroupByError):
    ...


class SelectionMixin(object):
    """
    mixin implementing the selection & aggregation interface on a group-like
    object sub-classes need to define: obj, exclusions
    """
    _selection = ...
    _internal_names = ...
    _internal_names_set = ...
    _builtin_table = ...
    _cython_table = ...
    @property
    def _selection_name(self):
        """
        return a name for myself; this would ideally be called
        the 'name' property, but we cannot conflict with the
        Series.name property which can be set
        """
        ...
    
    @property
    def _selection_list(self):
        ...
    
    @cache_readonly
    def _selected_obj(self):
        ...
    
    @cache_readonly
    def ndim(self):
        ...
    
    @cache_readonly
    def _obj_with_exclusions(self):
        ...
    
    def __getitem__(self, key):
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
    
    def aggregate(self, func, *args, **kwargs):
        ...
    
    agg = ...
    def _try_aggregate_string_function(self, arg, *args, **kwargs):
        """
        if arg is a string, then try to operate on it:
        - try to find a function (or attribute) on ourselves
        - try to find a numpy function
        - raise

        """
        ...
    
    def _aggregate(self, arg, *args, **kwargs):
        """
        provide an implementation for the aggregators

        Parameters
        ----------
        arg : string, dict, function
        *args : args to pass on to the function
        **kwargs : kwargs to pass on to the function

        Returns
        -------
        tuple of result, how

        Notes
        -----
        how can be a string describe the required post-processing, or
        None if not required
        """
        ...
    
    def _aggregate_multiple_funcs(self, arg, _level, _axis):
        ...
    
    def _shallow_copy(self, obj: Optional[Any] = ..., obj_type: Optional[Any] = ..., **kwargs):
        """ return a new object with the replacement attributes """
        ...
    
    def _is_cython_func(self, arg):
        """ if we define an internal function for this argument, return it """
        ...
    
    def _is_builtin_func(self, arg):
        """
        if we define an builtin function for this argument, return it,
        otherwise return the arg
        """
        ...
    


class GroupByMixin(object):
    """ provide the groupby facilities to the mixed object """
    @staticmethod
    def _dispatch(name, *args, **kwargs):
        """ dispatch to apply """
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
    


class IndexOpsMixin(object):
    """ common ops mixin to support a unified inteface / docs for Series /
    Index
    """
    __array_priority__ = ...
    def transpose(self, *args, **kwargs):
        """ return the transpose, which is by definition self """
        ...
    
    T = ...
    @property
    def shape(self):
        """ return a tuple of the shape of the underlying data """
        ...
    
    @property
    def ndim(self):
        """ return the number of dimensions of the underlying data,
        by definition 1
        """
        ...
    
    def item(self):
        """ return the first element of the underlying data as a python
        scalar
        """
        ...
    
    @property
    def data(self):
        """ return the data pointer of the underlying data """
        ...
    
    @property
    def itemsize(self):
        """ return the size of the dtype of the item of the underlying data """
        ...
    
    @property
    def nbytes(self):
        """ return the number of bytes in the underlying data """
        ...
    
    @property
    def strides(self):
        """ return the strides of the underlying data """
        ...
    
    @property
    def size(self):
        """ return the number of elements in the underlying data """
        ...
    
    @property
    def flags(self):
        """ return the ndarray.flags for the underlying data """
        ...
    
    @property
    def base(self):
        """ return the base object if the memory of the underlying data is
        shared
        """
        ...
    
    @property
    def _values(self):
        """ the internal implementation """
        ...
    
    @property
    def empty(self):
        ...
    
    def max(self):
        """ The maximum value of the object """
        ...
    
    def argmax(self, axis: Optional[Any] = ...):
        """
        return a ndarray of the maximum argument indexer

        See also
        --------
        numpy.ndarray.argmax
        """
        ...
    
    def min(self):
        """ The minimum value of the object """
        ...
    
    def argmin(self, axis: Optional[Any] = ...):
        """
        return a ndarray of the minimum argument indexer

        See also
        --------
        numpy.ndarray.argmin
        """
        ...
    
    def tolist(self):
        """
        Return a list of the values.

        These are each a scalar type, which is a Python scalar
        (for str, int, float) or a pandas scalar
        (for Timestamp/Timedelta/Interval/Period)

        See Also
        --------
        numpy.ndarray.tolist
        """
        ...
    
    def __iter__(self):
        """
        Return an iterator of the values.

        These are each a scalar type, which is a Python scalar
        (for str, int, float) or a pandas scalar
        (for Timestamp/Timedelta/Interval/Period)
        """
        ...
    
    @cache_readonly
    def hasnans(self):
        """ return if I have any nans; enables various perf speedups """
        ...
    
    def _reduce(self, op, name, axis=..., skipna: bool = ..., numeric_only: Optional[Any] = ..., filter_type: Optional[Any] = ..., **kwds):
        """ perform the reduction type operation if we can """
        ...
    
    def value_counts(self, normalize: bool = ..., sort: bool = ..., ascending: bool = ..., bins: Optional[Any] = ..., dropna: bool = ...):
        """
        Returns object containing counts of unique values.

        The resulting object will be in descending order so that the
        first element is the most frequently-occurring element.
        Excludes NA values by default.

        Parameters
        ----------
        normalize : boolean, default False
            If True then the object returned will contain the relative
            frequencies of the unique values.
        sort : boolean, default True
            Sort by values
        ascending : boolean, default False
            Sort in ascending order
        bins : integer, optional
            Rather than count values, group them into half-open bins,
            a convenience for pd.cut, only works with numeric data
        dropna : boolean, default True
            Don't include counts of NaN.

        Returns
        -------
        counts : Series
        """
        ...
    
    @Appender(_shared_docs['unique'] % _indexops_doc_kwargs)
    def unique(self):
        ...
    
    def nunique(self, dropna: bool = ...):
        """
        Return number of unique elements in the object.

        Excludes NA values by default.

        Parameters
        ----------
        dropna : boolean, default True
            Don't include NaN in the count.

        Returns
        -------
        nunique : int
        """
        ...
    
    @property
    def is_unique(self):
        """
        Return boolean if values in the object are unique

        Returns
        -------
        is_unique : boolean
        """
        ...
    
    @property
    def is_monotonic(self):
        """
        Return boolean if values in the object are
        monotonic_increasing

        .. versionadded:: 0.19.0

        Returns
        -------
        is_monotonic : boolean
        """
        ...
    
    is_monotonic_increasing = ...
    @property
    def is_monotonic_decreasing(self):
        """
        Return boolean if values in the object are
        monotonic_decreasing

        .. versionadded:: 0.19.0

        Returns
        -------
        is_monotonic_decreasing : boolean
        """
        ...
    
    def memory_usage(self, deep: bool = ...):
        """
        Memory usage of my values

        Parameters
        ----------
        deep : bool
            Introspect the data deeply, interrogate
            `object` dtypes for system-level memory consumption

        Returns
        -------
        bytes used

        Notes
        -----
        Memory usage does not include memory consumed by elements that
        are not components of the array if deep=False or if used on PyPy

        See Also
        --------
        numpy.ndarray.nbytes
        """
        ...
    
    def factorize(self, sort: bool = ..., na_sentinel=...):
        """
        Encode the object as an enumerated type or categorical variable

        Parameters
        ----------
        sort : boolean, default False
            Sort by values
        na_sentinel: int, default -1
            Value to mark "not found"

        Returns
        -------
        labels : the indexer to the original array
        uniques : the unique Index
        """
        ...
    
    @Substitution(klass='IndexOpsMixin')
    @Appender(_shared_docs['searchsorted'])
    @deprecate_kwarg(old_arg_name='key', new_arg_name='value')
    def searchsorted(self, value, side=..., sorter: Optional[Any] = ...):
        ...
    
    @Appender(_shared_docs['drop_duplicates'] % _indexops_doc_kwargs)
    def drop_duplicates(self, keep=..., inplace: bool = ...):
        ...
    
    @Appender(_shared_docs['duplicated'] % _indexops_doc_kwargs)
    def duplicated(self, keep=...):
        ...
    
    def _update_inplace(self, result, **kwargs):
        ...
    


