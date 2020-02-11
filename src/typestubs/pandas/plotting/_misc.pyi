"""
This type stub file was generated by pyright.
"""

from pandas.util._decorators import deprecate_kwarg
from typing import Any, Optional

def scatter_matrix(frame, alpha=..., figsize: Optional[Any] = ..., ax: Optional[Any] = ..., grid: bool = ..., diagonal=..., marker=..., density_kwds: Optional[Any] = ..., hist_kwds: Optional[Any] = ..., range_padding=..., **kwds):
    """
    Draw a matrix of scatter plots.

    Parameters
    ----------
    frame : DataFrame
    alpha : float, optional
        amount of transparency applied
    figsize : (float,float), optional
        a tuple (width, height) in inches
    ax : Matplotlib axis object, optional
    grid : bool, optional
        setting this to True will show the grid
    diagonal : {'hist', 'kde'}
        pick between 'kde' and 'hist' for
        either Kernel Density Estimation or Histogram
        plot in the diagonal
    marker : str, optional
        Matplotlib marker type, default '.'
    hist_kwds : other plotting keyword arguments
        To be passed to hist function
    density_kwds : other plotting keyword arguments
        To be passed to kernel density estimate plot
    range_padding : float, optional
        relative extension of axis range in x and y
        with respect to (x_max - x_min) or (y_max - y_min),
        default 0.05
    kwds : other plotting keyword arguments
        To be passed to scatter function

    Examples
    --------
    >>> df = DataFrame(np.random.randn(1000, 4), columns=['A','B','C','D'])
    >>> scatter_matrix(df, alpha=0.2)
    """
    ...

def _get_marker_compat(marker):
    ...

def radviz(frame, class_column, ax: Optional[Any] = ..., color: Optional[Any] = ..., colormap: Optional[Any] = ..., **kwds):
    """RadViz - a multivariate data visualization algorithm

    Parameters:
    -----------
    frame: DataFrame
    class_column: str
        Column name containing class names
    ax: Matplotlib axis object, optional
    color: list or tuple, optional
        Colors to use for the different classes
    colormap : str or matplotlib colormap object, default None
        Colormap to select colors from. If string, load colormap with that name
        from matplotlib.
    kwds: keywords
        Options to pass to matplotlib scatter plotting method

    Returns:
    --------
    ax: Matplotlib axis object
    """
    ...

@deprecate_kwarg(old_arg_name='data', new_arg_name='frame')
def andrews_curves(frame, class_column, ax: Optional[Any] = ..., samples=..., color: Optional[Any] = ..., colormap: Optional[Any] = ..., **kwds):
    """
    Generates a matplotlib plot of Andrews curves, for visualising clusters of
    multivariate data.

    Andrews curves have the functional form:

    f(t) = x_1/sqrt(2) + x_2 sin(t) + x_3 cos(t) +
           x_4 sin(2t) + x_5 cos(2t) + ...

    Where x coefficients correspond to the values of each dimension and t is
    linearly spaced between -pi and +pi. Each row of frame then corresponds to
    a single curve.

    Parameters:
    -----------
    frame : DataFrame
        Data to be plotted, preferably normalized to (0.0, 1.0)
    class_column : Name of the column containing class names
    ax : matplotlib axes object, default None
    samples : Number of points to plot in each curve
    color: list or tuple, optional
        Colors to use for the different classes
    colormap : str or matplotlib colormap object, default None
        Colormap to select colors from. If string, load colormap with that name
        from matplotlib.
    kwds: keywords
        Options to pass to matplotlib plotting method

    Returns:
    --------
    ax: Matplotlib axis object

    """
    ...

def bootstrap_plot(series, fig: Optional[Any] = ..., size=..., samples=..., **kwds):
    """Bootstrap plot.

    Parameters:
    -----------
    series: Time series
    fig: matplotlib figure object, optional
    size: number of data points to consider during each sampling
    samples: number of times the bootstrap procedure is performed
    kwds: optional keyword arguments for plotting commands, must be accepted
        by both hist and plot

    Returns:
    --------
    fig: matplotlib figure
    """
    ...

@deprecate_kwarg(old_arg_name='colors', new_arg_name='color')
@deprecate_kwarg(old_arg_name='data', new_arg_name='frame', stacklevel=3)
def parallel_coordinates(frame, class_column, cols: Optional[Any] = ..., ax: Optional[Any] = ..., color: Optional[Any] = ..., use_columns: bool = ..., xticks: Optional[Any] = ..., colormap: Optional[Any] = ..., axvlines: bool = ..., axvlines_kwds: Optional[Any] = ..., sort_labels: bool = ..., **kwds):
    """Parallel coordinates plotting.

    Parameters
    ----------
    frame: DataFrame
    class_column: str
        Column name containing class names
    cols: list, optional
        A list of column names to use
    ax: matplotlib.axis, optional
        matplotlib axis object
    color: list or tuple, optional
        Colors to use for the different classes
    use_columns: bool, optional
        If true, columns will be used as xticks
    xticks: list or tuple, optional
        A list of values to use for xticks
    colormap: str or matplotlib colormap, default None
        Colormap to use for line colors.
    axvlines: bool, optional
        If true, vertical lines will be added at each xtick
    axvlines_kwds: keywords, optional
        Options to be passed to axvline method for vertical lines
    sort_labels: bool, False
        Sort class_column labels, useful when assigning colors

        .. versionadded:: 0.20.0

    kwds: keywords
        Options to pass to matplotlib plotting method

    Returns
    -------
    ax: matplotlib axis object

    Examples
    --------
    >>> from pandas import read_csv
    >>> from pandas.tools.plotting import parallel_coordinates
    >>> from matplotlib import pyplot as plt
    >>> df = read_csv('https://raw.github.com/pandas-dev/pandas/master'
                      '/pandas/tests/data/iris.csv')
    >>> parallel_coordinates(df, 'Name', color=('#556270',
                             '#4ECDC4', '#C7F464'))
    >>> plt.show()
    """
    ...

def lag_plot(series, lag=..., ax: Optional[Any] = ..., **kwds):
    """Lag plot for time series.

    Parameters:
    -----------
    series: Time series
    lag: lag of the scatter plot, default 1
    ax: Matplotlib axis object, optional
    kwds: Matplotlib scatter method keyword arguments, optional

    Returns:
    --------
    ax: Matplotlib axis object
    """
    ...

def autocorrelation_plot(series, ax: Optional[Any] = ..., **kwds):
    """Autocorrelation plot for time series.

    Parameters:
    -----------
    series: Time series
    ax: Matplotlib axis object, optional
    kwds : keywords
        Options to pass to matplotlib plotting method

    Returns:
    -----------
    ax: Matplotlib axis object
    """
    ...

