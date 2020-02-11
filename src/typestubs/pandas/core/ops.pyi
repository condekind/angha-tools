"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""
Arithmetic operations for PandasObjects

This is not a public API.
"""
def _create_methods(arith_method, comp_method, bool_method, use_numexpr, special: bool = ..., default_axis=..., have_divmod: bool = ...):
    ...

def add_methods(cls, new_methods, force, select, exclude):
    ...

def add_special_arithmetic_methods(cls, arith_method: Optional[Any] = ..., comp_method: Optional[Any] = ..., bool_method: Optional[Any] = ..., use_numexpr: bool = ..., force: bool = ..., select: Optional[Any] = ..., exclude: Optional[Any] = ..., have_divmod: bool = ...):
    """
    Adds the full suite of special arithmetic methods (``__add__``,
    ``__sub__``, etc.) to the class.

    Parameters
    ----------
    arith_method : function (optional)
        factory for special arithmetic methods, with op string:
        f(op, name, str_rep, default_axis=None, fill_zeros=None, **eval_kwargs)
    comp_method : function (optional)
        factory for rich comparison - signature: f(op, name, str_rep)
    bool_method : function (optional)
        factory for boolean methods - signature: f(op, name, str_rep)
    use_numexpr : bool, default True
        whether to accelerate with numexpr, defaults to True
    force : bool, default False
        if False, checks whether function is defined **on ``cls.__dict__``**
        before defining if True, always defines functions on class base
    select : iterable of strings (optional)
        if passed, only sets functions with names in select
    exclude : iterable of strings (optional)
        if passed, will not set functions with names in exclude
    have_divmod : bool, (optional)
        should a divmod method be added? this method is special because it
        returns a tuple of cls instead of a single element of type cls
    """
    ...

def add_flex_arithmetic_methods(cls, flex_arith_method, flex_comp_method: Optional[Any] = ..., flex_bool_method: Optional[Any] = ..., use_numexpr: bool = ..., force: bool = ..., select: Optional[Any] = ..., exclude: Optional[Any] = ...):
    """
    Adds the full suite of flex arithmetic methods (``pow``, ``mul``, ``add``)
    to the class.

    Parameters
    ----------
    flex_arith_method : function
        factory for special arithmetic methods, with op string:
        f(op, name, str_rep, default_axis=None, fill_zeros=None, **eval_kwargs)
    flex_comp_method : function, optional,
        factory for rich comparison - signature: f(op, name, str_rep)
    use_numexpr : bool, default True
        whether to accelerate with numexpr, defaults to True
    force : bool, default False
        if False, checks whether function is defined **on ``cls.__dict__``**
        before defining if True, always defines functions on class base
    select : iterable of strings (optional)
        if passed, only sets functions with names in select
    exclude : iterable of strings (optional)
        if passed, will not set functions with names in exclude
    """
    ...

class _Op(object):
    """
    Wrapper around Series arithmetic operations.
    Generally, you should use classmethod ``_Op.get_op`` as an entry point.

    This validates and coerces lhs and rhs depending on its dtype and
    based on op. See _TimeOp also.

    Parameters
    ----------
    left : Series
        lhs of op
    right : object
        rhs of op
    name : str
        name of op
    na_op : callable
        a function which wraps op
    """
    fill_value = ...
    wrap_results = ...
    dtype = ...
    def __init__(self, left, right, name, na_op):
        self.left = ...
        self.right = ...
        self.name = ...
        self.na_op = ...
        self.lvalues = ...
        self.rvalues = ...
    
    @classmethod
    def get_op(cls, left, right, name, na_op):
        """
        Get op dispatcher, returns _Op or _TimeOp.

        If ``left`` and ``right`` are appropriate for datetime arithmetic with
        operation ``name``, processes them and returns a ``_TimeOp`` object
        that stores all the required values.  Otherwise, it will generate
        either a ``_Op``, indicating that the operation is performed via
        normal numpy path.
        """
        ...
    


class _TimeOp(_Op):
    """
    Wrapper around Series datetime/time/timedelta arithmetic operations.
    Generally, you should use classmethod ``_Op.get_op`` as an entry point.
    """
    fill_value = ...
    def __init__(self, left, right, name, na_op):
        self.is_offset_lhs = ...
        self.is_timedelta_lhs = ...
        self.is_datetime64_lhs = ...
        self.is_datetime64tz_lhs = ...
        self.is_datetime_lhs = ...
        self.is_integer_lhs = ...
        self.is_floating_lhs = ...
        self.is_offset_rhs = ...
        self.is_datetime64_rhs = ...
        self.is_datetime64tz_rhs = ...
        self.is_datetime_rhs = ...
        self.is_timedelta_rhs = ...
        self.is_integer_rhs = ...
        self.is_floating_rhs = ...
    
    def _validate(self, lvalues, rvalues, name):
        ...
    
    def _convert_to_array(self, values, name: Optional[Any] = ..., other: Optional[Any] = ...):
        """converts values to ndarray"""
        ...
    
    def _convert_for_datetime(self, lvalues, rvalues):
        ...
    
    def _is_offset(self, arr_or_obj):
        """ check if obj or all elements of list-like is DateOffset """
        ...
    


def _align_method_SERIES(left, right, align_asobject: bool = ...):
    """ align lhs and rhs Series """
    ...

def _construct_result(left, result, index, name, dtype):
    ...

def _construct_divmod_result(left, result, index, name, dtype):
    """divmod returns a tuple of like indexed series instead of a single series.
    """
    ...

def _arith_method_SERIES(op, name, str_rep, fill_zeros: Optional[Any] = ..., default_axis: Optional[Any] = ..., construct_result=..., **eval_kwargs):
    """
    Wrapper function for Series arithmetic operations, to avoid
    code duplication.
    """
    ...

def _comp_method_OBJECT_ARRAY(op, x, y):
    ...

def _comp_method_SERIES(op, name, str_rep, masker: bool = ...):
    """
    Wrapper function for Series arithmetic operations, to avoid
    code duplication.
    """
    ...

def _bool_method_SERIES(op, name, str_rep):
    """
    Wrapper function for Series arithmetic operations, to avoid
    code duplication.
    """
    ...

_op_descriptions = { 'add': { 'op': '+','desc': 'Addition','reversed': False,'reverse': 'radd' },'sub': { 'op': '-','desc': 'Subtraction','reversed': False,'reverse': 'rsub' },'mul': { 'op': '*','desc': 'Multiplication','reversed': False,'reverse': 'rmul' },'mod': { 'op': '%','desc': 'Modulo','reversed': False,'reverse': 'rmod' },'pow': { 'op': '**','desc': 'Exponential power','reversed': False,'reverse': 'rpow' },'truediv': { 'op': '/','desc': 'Floating division','reversed': False,'reverse': 'rtruediv' },'floordiv': { 'op': '//','desc': 'Integer division','reversed': False,'reverse': 'rfloordiv' },'divmod': { 'op': 'divmod','desc': 'Integer division and modulo','reversed': False,'reverse': None },'eq': { 'op': '==','desc': 'Equal to','reversed': False,'reverse': None },'ne': { 'op': '!=','desc': 'Not equal to','reversed': False,'reverse': None },'lt': { 'op': '<','desc': 'Less than','reversed': False,'reverse': None },'le': { 'op': '<=','desc': 'Less than or equal to','reversed': False,'reverse': None },'gt': { 'op': '>','desc': 'Greater than','reversed': False,'reverse': None },'ge': { 'op': '>=','desc': 'Greater than or equal to','reversed': False,'reverse': None } }
_op_names = list(_op_descriptions.keys())
_flex_doc_SERIES = """
%s of series and other, element-wise (binary operator `%s`).

Equivalent to ``%s``, but with support to substitute a fill_value for
missing data in one of the inputs.

Parameters
----------
other : Series or scalar value
fill_value : None or float value, default None (NaN)
    Fill missing (NaN) values with this value. If both Series are
    missing, the result will be missing
level : int or name
    Broadcast across a level, matching Index values on the
    passed MultiIndex level

Returns
-------
result : Series

See also
--------
Series.%s
"""
def _flex_method_SERIES(op, name, str_rep, default_axis: Optional[Any] = ..., fill_zeros: Optional[Any] = ..., **eval_kwargs):
    ...

series_flex_funcs = dict(flex_arith_method=_flex_method_SERIES, flex_comp_method=_flex_method_SERIES)
series_special_funcs = dict(arith_method=_arith_method_SERIES, comp_method=_comp_method_SERIES, bool_method=_bool_method_SERIES, have_divmod=True)
_arith_doc_FRAME = """
Binary operator %s with support to substitute a fill_value for missing data in
one of the inputs

Parameters
----------
other : Series, DataFrame, or constant
axis : {0, 1, 'index', 'columns'}
    For Series input, axis to match Series index on
fill_value : None or float value, default None
    Fill missing (NaN) values with this value. If both DataFrame locations are
    missing, the result will be missing
level : int or name
    Broadcast across a level, matching Index values on the
    passed MultiIndex level

Notes
-----
Mismatched indices will be unioned together

Returns
-------
result : DataFrame
"""
_flex_doc_FRAME = """
%s of dataframe and other, element-wise (binary operator `%s`).

Equivalent to ``%s``, but with support to substitute a fill_value for
missing data in one of the inputs.

Parameters
----------
other : Series, DataFrame, or constant
axis : {0, 1, 'index', 'columns'}
    For Series input, axis to match Series index on
fill_value : None or float value, default None
    Fill missing (NaN) values with this value. If both DataFrame
    locations are missing, the result will be missing
level : int or name
    Broadcast across a level, matching Index values on the
    passed MultiIndex level

Notes
-----
Mismatched indices will be unioned together

Returns
-------
result : DataFrame

See also
--------
DataFrame.%s
"""
def _align_method_FRAME(left, right, axis):
    """ convert rhs to meet lhs dims if input is list, tuple or np.ndarray """
    ...

def _arith_method_FRAME(op, name, str_rep: Optional[Any] = ..., default_axis=..., fill_zeros: Optional[Any] = ..., **eval_kwargs):
    ...

def _flex_comp_method_FRAME(op, name, str_rep: Optional[Any] = ..., default_axis=..., masker: bool = ...):
    ...

def _comp_method_FRAME(func, name, str_rep, masker: bool = ...):
    ...

frame_flex_funcs = dict(flex_arith_method=_arith_method_FRAME, flex_comp_method=_flex_comp_method_FRAME)
frame_special_funcs = dict(arith_method=_arith_method_FRAME, comp_method=_comp_method_FRAME, bool_method=_arith_method_FRAME)
def _arith_method_PANEL(op, name, str_rep: Optional[Any] = ..., fill_zeros: Optional[Any] = ..., default_axis: Optional[Any] = ..., **eval_kwargs):
    ...

def _comp_method_PANEL(op, name, str_rep: Optional[Any] = ..., masker: bool = ...):
    ...

panel_special_funcs = dict(arith_method=_arith_method_PANEL, comp_method=_comp_method_PANEL, bool_method=_arith_method_PANEL)
