"""
This type stub file was generated by pyright.
"""

"""
Common helper methods used in different submodules of pandas.io.formats
"""
def get_level_lengths(levels, sentinel=...):
    """For each index in each level the function returns lengths of indexes.

    Parameters
    ----------
    levels : list of lists
        List of values on for level.
    sentinel : string, optional
        Value which states that no new index starts on there.

    Returns
    ----------
    Returns list of maps. For each level returns map of indexes (key is index
    in row and value is length of index).
    """
    ...

