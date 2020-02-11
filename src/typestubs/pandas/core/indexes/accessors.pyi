"""
This type stub file was generated by pyright.
"""

from pandas.core.accessor import PandasDelegate
from pandas.core.base import NoNewAttributesMixin, PandasObject
from typing import Any, Optional

"""
datetimelike delegation
"""
def is_datetimelike(data):
    """
    return a boolean if we can be successfully converted to a datetimelike
    """
    ...

def maybe_to_datetimelike(data, copy: bool = ...):
    """
    return a DelegatedClass of a Series that is datetimelike
      (e.g. datetime64[ns],timedelta64[ns] dtype or a Series of Periods)
    raise TypeError if this is not possible.

    Parameters
    ----------
    data : Series
    copy : boolean, default False
           copy the input data

    Returns
    -------
    DelegatedClass

    """
    ...

class Properties(PandasDelegate, PandasObject, NoNewAttributesMixin):
    def __init__(self, values, index, name, orig: Optional[Any] = ...):
        self.values = ...
        self.index = ...
        self.name = ...
        self.orig = ...
    
    def _delegate_property_get(self, name):
        ...
    
    def _delegate_property_set(self, name, value, *args, **kwargs):
        ...
    
    def _delegate_method(self, name, *args, **kwargs):
        ...
    


class DatetimeProperties(Properties):
    """
    Accessor object for datetimelike properties of the Series values.

    Examples
    --------
    >>> s.dt.hour
    >>> s.dt.second
    >>> s.dt.quarter

    Returns a Series indexed like the original Series.
    Raises TypeError if the Series does not contain datetimelike values.
    """
    def to_pydatetime(self):
        ...
    
    @property
    def freq(self):
        ...
    


class TimedeltaProperties(Properties):
    """
    Accessor object for datetimelike properties of the Series values.

    Examples
    --------
    >>> s.dt.hours
    >>> s.dt.seconds

    Returns a Series indexed like the original Series.
    Raises TypeError if the Series does not contain datetimelike values.
    """
    def to_pytimedelta(self):
        ...
    
    @property
    def components(self):
        """
        Return a dataframe of the components (days, hours, minutes,
        seconds, milliseconds, microseconds, nanoseconds) of the Timedeltas.

        Returns
        -------
        a DataFrame

        """
        ...
    
    @property
    def freq(self):
        ...
    


class PeriodProperties(Properties):
    """
    Accessor object for datetimelike properties of the Series values.

    Examples
    --------
    >>> s.dt.hour
    >>> s.dt.second
    >>> s.dt.quarter

    Returns a Series indexed like the original Series.
    Raises TypeError if the Series does not contain datetimelike values.
    """
    ...


class CombinedDatetimelikeProperties(DatetimeProperties, TimedeltaProperties):
    __doc__ = ...
    @classmethod
    def _make_accessor(cls, data):
        ...
    


