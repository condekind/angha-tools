"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""
Table Schema builders

http://specs.frictionlessdata.io/json-table-schema/
"""
def as_json_table_type(x):
    """
    Convert a NumPy / pandas type to its corresponding json_table.

    Parameters
    ----------
    x : array or dtype

    Returns
    -------
    t : str
        the Table Schema data types

    Notes
    -----
    This table shows the relationship between NumPy / pandas dtypes,
    and Table Schema dtypes.

    ==============  =================
    Pandas type     Table Schema type
    ==============  =================
    int64           integer
    float64         number
    bool            boolean
    datetime64[ns]  datetime
    timedelta64[ns] duration
    object          str
    categorical     any
    =============== =================
    """
    ...

def set_default_names(data):
    """Sets index names to 'index' for regular, or 'level_x' for Multi"""
    ...

def make_field(arr, dtype: Optional[Any] = ...):
    ...

def build_table_schema(data, index: bool = ..., primary_key: Optional[Any] = ..., version: bool = ...):
    """
    Create a Table schema from ``data``.

    Parameters
    ----------
    data : Series, DataFrame
    index : bool, default True
        Whether to include ``data.index`` in the schema.
    primary_key : bool or None, default True
        column names to designate as the primary key.
        The default `None` will set `'primaryKey'` to the index
        level or levels if the index is unique.
    version : bool, default True
        Whether to include a field `pandas_version` with the version
        of pandas that generated the schema.

    Returns
    -------
    schema : dict

    Examples
    --------
    >>> df = pd.DataFrame(
    ...     {'A': [1, 2, 3],
    ...      'B': ['a', 'b', 'c'],
    ...      'C': pd.date_range('2016-01-01', freq='d', periods=3),
    ...     }, index=pd.Index(range(3), name='idx'))
    >>> build_table_schema(df)
    {'fields': [{'name': 'idx', 'type': 'integer'},
    {'name': 'A', 'type': 'integer'},
    {'name': 'B', 'type': 'string'},
    {'name': 'C', 'type': 'datetime'}],
    'pandas_version': '0.20.0',
    'primaryKey': ['idx']}

    Notes
    -----
    See `_as_json_table_type` for conversion types.
    Timedeltas as converted to ISO8601 duration format with
    9 decimal places after the secnods field for nanosecond precision.

    Categoricals are converted to the `any` dtype, and use the `enum` field
    constraint to list the allowed values. The `ordered` attribute is included
    in an `ordered` field.
    """
    ...

