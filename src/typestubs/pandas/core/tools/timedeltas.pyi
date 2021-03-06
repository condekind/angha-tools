"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""
timedelta support tools
"""
def to_timedelta(arg, unit=..., box: bool = ..., errors=...):
    """
    Convert argument to timedelta

    Parameters
    ----------
    arg : string, timedelta, list, tuple, 1-d array, or Series
    unit : unit of the arg (D,h,m,s,ms,us,ns) denote the unit, which is an
        integer/float number
    box : boolean, default True
        - If True returns a Timedelta/TimedeltaIndex of the results
        - if False returns a np.timedelta64 or ndarray of values of dtype
          timedelta64[ns]
    errors : {'ignore', 'raise', 'coerce'}, default 'raise'
        - If 'raise', then invalid parsing will raise an exception
        - If 'coerce', then invalid parsing will be set as NaT
        - If 'ignore', then invalid parsing will return the input

    Returns
    -------
    ret : timedelta64/arrays of timedelta64 if parsing succeeded

    Examples
    --------

    Parsing a single string to a Timedelta:

    >>> pd.to_timedelta('1 days 06:05:01.00003')
    Timedelta('1 days 06:05:01.000030')
    >>> pd.to_timedelta('15.5us')
    Timedelta('0 days 00:00:00.000015')

    Parsing a list or array of strings:

    >>> pd.to_timedelta(['1 days 06:05:01.00003', '15.5us', 'nan'])
    TimedeltaIndex(['1 days 06:05:01.000030', '0 days 00:00:00.000015', NaT],
                   dtype='timedelta64[ns]', freq=None)

    Converting numbers by specifying the `unit` keyword argument:

    >>> pd.to_timedelta(np.arange(5), unit='s')
    TimedeltaIndex(['00:00:00', '00:00:01', '00:00:02',
                    '00:00:03', '00:00:04'],
                   dtype='timedelta64[ns]', freq=None)
    >>> pd.to_timedelta(np.arange(5), unit='d')
    TimedeltaIndex(['0 days', '1 days', '2 days', '3 days', '4 days'],
                   dtype='timedelta64[ns]', freq=None)

    See also
    --------
    pandas.DataFrame.astype : Cast argument to a specified dtype.
    pandas.to_datetime : Convert argument to datetime.
    """
    ...

_unit_map = { 'Y': 'Y','y': 'Y','W': 'W','w': 'W','D': 'D','d': 'D','days': 'D','Days': 'D','day': 'D','Day': 'D','M': 'M','H': 'h','h': 'h','m': 'm','T': 'm','S': 's','s': 's','L': 'ms','MS': 'ms','ms': 'ms','US': 'us','us': 'us','NS': 'ns','ns': 'ns' }
def _validate_timedelta_unit(arg):
    """ provide validation / translation for timedelta short units """
    ...

def _coerce_scalar_to_timedelta_type(r, unit=..., box: bool = ..., errors=...):
    """Convert string 'r' to a timedelta object."""
    ...

def _convert_listlike(arg, unit=..., box: bool = ..., errors=..., name: Optional[Any] = ...):
    """Convert a list of objects to a timedelta index object."""
    ...

