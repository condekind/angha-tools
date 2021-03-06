"""
This type stub file was generated by pyright.
"""

"""
Interaction with scipy.sparse matrices.

Currently only includes SparseSeries.to_coo helpers.
"""
def _check_is_partition(parts, whole):
    ...

def _to_ijv(ss, row_levels=..., column_levels=..., sort_labels: bool = ...):
    """ For arbitrary (MultiIndexed) SparseSeries return
    (v, i, j, ilabels, jlabels) where (v, (i, j)) is suitable for
    passing to scipy.sparse.coo constructor. """
    ...

def _sparse_series_to_coo(ss, row_levels=..., column_levels=..., sort_labels: bool = ...):
    """ Convert a SparseSeries to a scipy.sparse.coo_matrix using index
    levels row_levels, column_levels as the row and column
    labels respectively. Returns the sparse_matrix, row and column labels.
    """
    ...

def _coo_to_sparse_series(A, dense_index: bool = ...):
    """ Convert a scipy.sparse.coo_matrix to a SparseSeries.
    Use the defaults given in the SparseSeries constructor.
    """
    ...

