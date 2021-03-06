"""
This type stub file was generated by pyright.
"""

from pandas.core.computation.check import _NUMEXPR_INSTALLED
from typing import Any, Optional

"""
Expressions
-----------

Offer fast expression evaluation through numexpr

"""
if _NUMEXPR_INSTALLED:
    ...
_TEST_MODE = None
_TEST_RESULT = None
_USE_NUMEXPR = _NUMEXPR_INSTALLED
_evaluate = None
_where = None
_ALLOWED_DTYPES = { 'evaluate': set(['int64', 'int32', 'float64', 'float32', 'bool']),'where': set(['int64', 'float64', 'bool']) }
_MIN_ELEMENTS = 10000
def set_use_numexpr(v: bool = ...):
    ...

def set_numexpr_threads(n: Optional[Any] = ...):
    ...

def _evaluate_standard(op, op_str, a, b, **eval_kwargs):
    """ standard evaluation """
    ...

def _can_use_numexpr(op, op_str, a, b, dtype_check):
    """ return a boolean if we WILL be using numexpr """
    ...

def _evaluate_numexpr(op, op_str, a, b, truediv: bool = ..., reversed: bool = ..., **eval_kwargs):
    ...

def _where_standard(cond, a, b):
    ...

def _where_numexpr(cond, a, b):
    ...

def _has_bool_dtype(x):
    ...

def _bool_arith_check(op_str, a, b, not_allowed=..., unsupported: Optional[Any] = ...):
    ...

def evaluate(op, op_str, a, b, use_numexpr: bool = ..., **eval_kwargs):
    """ evaluate and return the expression of the op on a and b

        Parameters
        ----------

        op :    the actual operand
        op_str: the string version of the op
        a :     left operand
        b :     right operand
        use_numexpr : whether to try to use numexpr (default True)
        """
    ...

def where(cond, a, b, use_numexpr: bool = ...):
    """ evaluate the where condition cond on a and b

        Parameters
        ----------

        cond : a boolean array
        a :    return if cond is True
        b :    return if cond is False
        use_numexpr : whether to try to use numexpr (default True)
        """
    ...

def set_test_mode(v: bool = ...):
    """
    Keeps track of whether numexpr  was used.  Stores an additional ``True``
    for every successful use of evaluate with numexpr since the last
    ``get_test_result``
    """
    ...

def _store_test_result(used_numexpr):
    ...

def get_test_result():
    """get test result and reset test_results"""
    ...

