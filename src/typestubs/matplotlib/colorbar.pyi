"""
This type stub file was generated by pyright.
"""

import matplotlib.cm as cm
from matplotlib import docstring
from typing import Any, Optional

'''
Colorbar toolkit with two classes and a function:

    :class:`ColorbarBase`
        the base class with full colorbar drawing functionality.
        It can be used as-is to make a colorbar for a given colormap;
        a mappable object (e.g., image) is not needed.

    :class:`Colorbar`
        the derived class for use with images or contour plots.

    :func:`make_axes`
        a function for resizing an axes and adding a second axes
        suitable for a colorbar

The :meth:`~matplotlib.figure.Figure.colorbar` method uses :func:`make_axes`
and :class:`Colorbar`; the :func:`~matplotlib.pyplot.colorbar` function
is a thin wrapper over :meth:`~matplotlib.figure.Figure.colorbar`.

'''
make_axes_kw_doc = '''

    ============= ====================================================
    Property      Description
    ============= ====================================================
    *orientation* vertical or horizontal
    *fraction*    0.15; fraction of original axes to use for colorbar
    *pad*         0.05 if vertical, 0.15 if horizontal; fraction
                  of original axes between colorbar and new image axes
    *shrink*      1.0; fraction by which to multiply the size of the colorbar
    *aspect*      20; ratio of long to short dimensions
    *anchor*      (0.0, 0.5) if vertical; (0.5, 1.0) if horizontal;
                  the anchor point of the colorbar axes
    *panchor*     (1.0, 0.5) if vertical; (0.5, 0.0) if horizontal;
                  the anchor point of the colorbar parent axes. If
                  False, the parent axes' anchor will be unchanged
    ============= ====================================================

'''
colormap_kw_doc = '''

    ============  ====================================================
    Property      Description
    ============  ====================================================
    *extend*      [ 'neither' | 'both' | 'min' | 'max' ]
                  If not 'neither', make pointed end(s) for out-of-
                  range values.  These are set for a given colormap
                  using the colormap set_under and set_over methods.
    *extendfrac*  [ *None* | 'auto' | length | lengths ]
                  If set to *None*, both the minimum and maximum
                  triangular colorbar extensions with have a length of
                  5% of the interior colorbar length (this is the
                  default setting). If set to 'auto', makes the
                  triangular colorbar extensions the same lengths as
                  the interior boxes (when *spacing* is set to
                  'uniform') or the same lengths as the respective
                  adjacent interior boxes (when *spacing* is set to
                  'proportional'). If a scalar, indicates the length
                  of both the minimum and maximum triangular colorbar
                  extensions as a fraction of the interior colorbar
                  length. A two-element sequence of fractions may also
                  be given, indicating the lengths of the minimum and
                  maximum colorbar extensions respectively as a
                  fraction of the interior colorbar length.
    *extendrect*  bool
                  If *False* the minimum and maximum colorbar extensions
                  will be triangular (the default). If *True* the
                  extensions will be rectangular.
    *spacing*     [ 'uniform' | 'proportional' ]
                  Uniform spacing gives each discrete color the same
                  space; proportional makes the space proportional to
                  the data interval.
    *ticks*       [ None | list of ticks | Locator object ]
                  If None, ticks are determined automatically from the
                  input.
    *format*      [ None | format string | Formatter object ]
                  If None, the
                  :class:`~matplotlib.ticker.ScalarFormatter` is used.
                  If a format string is given, e.g., '%.3f', that is
                  used. An alternative
                  :class:`~matplotlib.ticker.Formatter` object may be
                  given instead.
    *drawedges*   bool
                  Whether to draw lines at color boundaries.
    ============  ====================================================

    The following will probably be useful only in the context of
    indexed colors (that is, when the mappable has norm=NoNorm()),
    or other unusual circumstances.

    ============   ===================================================
    Property       Description
    ============   ===================================================
    *boundaries*   None or a sequence
    *values*       None or a sequence which must be of length 1 less
                   than the sequence of *boundaries*. For each region
                   delimited by adjacent entries in *boundaries*, the
                   color mapped to the corresponding value in values
                   will be used.
    ============   ===================================================

'''
colorbar_doc = '''

Add a colorbar to a plot.

Function signatures for the :mod:`~matplotlib.pyplot` interface; all
but the first are also method signatures for the
:meth:`~matplotlib.figure.Figure.colorbar` method::

  colorbar(**kwargs)
  colorbar(mappable, **kwargs)
  colorbar(mappable, cax=cax, **kwargs)
  colorbar(mappable, ax=ax, **kwargs)

Parameters
----------
mappable :
    The :class:`~matplotlib.image.Image`,
    :class:`~matplotlib.contour.ContourSet`, etc. to
    which the colorbar applies; this argument is mandatory for the Figure
    :meth:`~matplotlib.figure.Figure.colorbar` method but optional for the
    pyplot :func:`~matplotlib.pyplot.colorbar` function, which sets the
    default to the current image.

cax : :class:`~matplotlib.axes.Axes` object, optional
    Axes into which the colorbar will be drawn.

ax : :class:`~matplotlib.axes.Axes`, list of Axes, optional
    Parent axes from which space for a new colorbar axes will be stolen.
    If a list of axes is given they will all be resized to make room for the
    colorbar axes.

use_gridspec : bool, optional
    If *cax* is ``None``, a new *cax* is created as an instance of
    Axes. If *ax* is an instance of Subplot and *use_gridspec* is ``True``,
    *cax* is created as an instance of Subplot using the
    grid_spec module.


Returns
-------
:class:`~matplotlib.colorbar.Colorbar` instance
    See also its base class, :class:`~matplotlib.colorbar.ColorbarBase`.
    Call the :meth:`~matplotlib.colorbar.ColorbarBase.set_label` method
    to label the colorbar.

Notes
-----
Additional keyword arguments are of two kinds:

  axes properties:
%s
  colorbar properties:
%s

If *mappable* is a :class:`~matplotlib.contours.ContourSet`, its *extend*
kwarg is included automatically.

The *shrink* kwarg provides a simple way to scale the colorbar with respect
to the axes. Note that if *cax* is specified it determines the size of the
colorbar and *shrink* and *aspect* kwargs are ignored.

For more precise control, you can manually specify the positions of
the axes objects in which the mappable and the colorbar are drawn.  In
this case, do not use any of the axes properties kwargs.

It is known that some vector graphics viewer (svg and pdf) renders white gaps
between segments of the colorbar. This is due to bugs in the viewers not
matplotlib. As a workaround the colorbar can be rendered with overlapping
segments::

    cbar = colorbar()
    cbar.solids.set_edgecolor("face")
    draw()

However this has negative consequences in other circumstances. Particularly
with semi transparent images (alpha < 1) and colorbar extensions and is not
enabled by default see (issue #1188).

''' % (make_axes_kw_doc, colormap_kw_doc)
def _set_ticks_on_axis_warn(*args, **kw):
    ...

class ColorbarBase(cm.ScalarMappable):
    '''
    Draw a colorbar in an existing axes.

    This is a base class for the :class:`Colorbar` class, which is the
    basis for the :func:`~matplotlib.pyplot.colorbar` function and the
    :meth:`~matplotlib.figure.Figure.colorbar` method, which are the
    usual ways of creating a colorbar.

    It is also useful by itself for showing a colormap.  If the *cmap*
    kwarg is given but *boundaries* and *values* are left as None,
    then the colormap will be displayed on a 0-1 scale. To show the
    under- and over-value colors, specify the *norm* as::

        colors.Normalize(clip=False)

    To show the colors versus index instead of on the 0-1 scale,
    use::

        norm=colors.NoNorm.

    Useful public methods are :meth:`set_label` and :meth:`add_lines`.

    Attributes
    ----------
    ax : Axes
        The `Axes` instance in which the colorbar is drawn.

    lines : list
        A list of `LineCollection` if lines were drawn, otherwise
        an empty list.

    dividers : LineCollection
        A LineCollection if *drawedges* is ``True``, otherwise ``None``.
    '''
    _slice_dict = ...
    n_rasterize = ...
    def __init__(self, ax, cmap: Optional[Any] = ..., norm: Optional[Any] = ..., alpha: Optional[Any] = ..., values: Optional[Any] = ..., boundaries: Optional[Any] = ..., orientation=..., ticklocation=..., extend=..., spacing=..., ticks: Optional[Any] = ..., format: Optional[Any] = ..., drawedges: bool = ..., filled: bool = ..., extendfrac: Optional[Any] = ..., extendrect: bool = ..., label=...):
        self.ax = ...
        self.alpha = ...
        self.values = ...
        self.boundaries = ...
        self.extend = ...
        self.spacing = ...
        self.orientation = ...
        self.drawedges = ...
        self.filled = ...
        self.extendfrac = ...
        self.extendrect = ...
        self.solids = ...
        self.lines = ...
        self.outline = ...
        self.patch = ...
        self.dividers = ...
        self.ticklocation = ...
    
    def _extend_lower(self):
        """Returns whether the lower limit is open ended."""
        ...
    
    def _extend_upper(self):
        """Returns whether the uper limit is open ended."""
        ...
    
    def _patch_ax(self):
        ...
    
    def draw_all(self):
        '''
        Calculate any free parameters based on the current cmap and norm,
        and do all the drawing.
        '''
        ...
    
    def config_axis(self):
        ...
    
    def update_ticks(self):
        """
        Force the update of the ticks and ticklabels. This must be
        called whenever the tick locator and/or tick formatter changes.
        """
        ...
    
    def set_ticks(self, ticks, update_ticks: bool = ...):
        """
        Set tick locations.

        Parameters
        ----------
        ticks : {None, sequence, :class:`~matplotlib.ticker.Locator` instance}
            If None, a default Locator will be used.

        update_ticks : {True, False}, optional
            If True, tick locations are updated immediately.  If False,
            use :meth:`update_ticks` to manually update the ticks.

        """
        self.stale = ...
    
    def get_ticks(self, minor: bool = ...):
        """Return the x ticks as a list of locations"""
        ...
    
    def set_ticklabels(self, ticklabels, update_ticks: bool = ...):
        """
        set tick labels. Tick labels are updated immediately unless
        update_ticks is *False*. To manually update the ticks, call
        *update_ticks* method explicitly.
        """
        self.stale = ...
    
    def _config_axes(self, X, Y):
        '''
        Make an axes patch and outline.
        '''
        self.outline = ...
        self.patch = ...
    
    def _set_label(self):
        self.stale = ...
    
    def set_label(self, label, **kw):
        '''
        Label the long axis of the colorbar
        '''
        ...
    
    def _outline(self, X, Y):
        '''
        Return *x*, *y* arrays of colorbar bounding polygon,
        taking orientation into account.
        '''
        ...
    
    def _edges(self, X, Y):
        '''
        Return the separator line segments; helper for _add_solids.
        '''
        ...
    
    def _add_solids(self, X, Y, C):
        '''
        Draw the colors using :meth:`~matplotlib.axes.Axes.pcolormesh`;
        optionally add separators.
        '''
        self.solids = ...
    
    def add_lines(self, levels, colors, linewidths, erase: bool = ...):
        '''
        Draw lines on the colorbar.

        *colors* and *linewidths* must be scalars or
        sequences the same length as *levels*.

        Set *erase* to False to add lines without first
        removing any previously added lines.
        '''
        self.stale = ...
    
    def _ticker(self):
        '''
        Return the sequence of ticks (colorbar data locations),
        ticklabels (strings), and the corresponding offset string.
        '''
        ...
    
    def _process_values(self, b: Optional[Any] = ...):
        '''
        Set the :attr:`_boundaries` and :attr:`_values` attributes
        based on the input boundaries and values.  Input boundaries
        can be *self.boundaries* or the argument *b*.
        '''
        ...
    
    def _find_range(self):
        '''
        Set :attr:`vmin` and :attr:`vmax` attributes to the first and
        last boundary excluding extended end boundaries.
        '''
        self.vmin = ...
        self.vmax = ...
    
    def _central_N(self):
        '''number of boundaries **before** extension of ends'''
        ...
    
    def _extended_N(self):
        '''
        Based on the colormap and extend variable, return the
        number of boundaries.
        '''
        ...
    
    def _get_extension_lengths(self, frac, automin, automax, default=...):
        '''
        Get the lengths of colorbar extensions.

        A helper method for _uniform_y and _proportional_y.
        '''
        ...
    
    def _uniform_y(self, N):
        '''
        Return colorbar data coordinates for *N* uniformly
        spaced boundaries, plus ends if required.
        '''
        ...
    
    def _proportional_y(self):
        '''
        Return colorbar data coordinates for the boundaries of
        a proportional colorbar.
        '''
        ...
    
    def _mesh(self):
        '''
        Return X,Y, the coordinate arrays for the colorbar pcolormesh.
        These are suitable for a vertical colorbar; swapping and
        transposition for a horizontal colorbar are done outside
        this function.
        '''
        ...
    
    def _locate(self, x):
        '''
        Given a set of color data values, return their
        corresponding colorbar data coordinates.
        '''
        ...
    
    def set_alpha(self, alpha):
        self.alpha = ...
    
    def remove(self):
        """
        Remove this colorbar from the figure
        """
        ...
    


class Colorbar(ColorbarBase):
    """
    This class connects a :class:`ColorbarBase` to a
    :class:`~matplotlib.cm.ScalarMappable` such as a
    :class:`~matplotlib.image.AxesImage` generated via
    :meth:`~matplotlib.axes.Axes.imshow`.

    It is not intended to be instantiated directly; instead,
    use :meth:`~matplotlib.figure.Figure.colorbar` or
    :func:`~matplotlib.pyplot.colorbar` to make your colorbar.

    """
    def __init__(self, ax, mappable, **kw):
        self.mappable = ...
    
    def on_mappable_changed(self, mappable):
        """
        Updates this colorbar to match the mappable's properties.

        Typically this is automatically registered as an event handler
        by :func:`colorbar_factory` and should not be called manually.

        """
        ...
    
    def add_lines(self, CS, erase: bool = ...):
        '''
        Add the lines from a non-filled
        :class:`~matplotlib.contour.ContourSet` to the colorbar.

        Set *erase* to False if these lines should be added to
        any pre-existing lines.
        '''
        ...
    
    def update_normal(self, mappable):
        '''
        update solid, lines, etc. Unlike update_bruteforce, it does
        not clear the axes.  This is meant to be called when the image
        or contour plot to which this colorbar belongs is changed.
        '''
        self.stale = ...
    
    def update_bruteforce(self, mappable):
        '''
        Destroy and rebuild the colorbar.  This is
        intended to become obsolete, and will probably be
        deprecated and then removed.  It is not called when
        the pyplot.colorbar function or the Figure.colorbar
        method are used to create the colorbar.

        '''
        self.outline = ...
        self.patch = ...
        self.solids = ...
        self.lines = ...
        self.dividers = ...
        self.cmap = ...
        self.norm = ...
    
    def remove(self):
        """
        Remove this colorbar from the figure.  If the colorbar was created with
        ``use_gridspec=True`` then restore the gridspec to its previous value.
        """
        ...
    


@docstring.Substitution(make_axes_kw_doc)
def make_axes(parents, location: Optional[Any] = ..., orientation: Optional[Any] = ..., fraction=..., shrink=..., aspect=..., **kw):
    '''
    Resize and reposition parent axes, and return a child
    axes suitable for a colorbar.

    Keyword arguments may include the following (with defaults):

        location : [None|'left'|'right'|'top'|'bottom']
            The position, relative to **parents**, where the colorbar axes
            should be created. If None, the value will either come from the
            given ``orientation``, else it will default to 'right'.

        orientation :  [None|'vertical'|'horizontal']
            The orientation of the colorbar. Typically, this keyword shouldn't
            be used, as it can be derived from the ``location`` keyword.

    %s

    Returns (cax, kw), the child axes and the reduced kw dictionary to be
    passed when creating the colorbar instance.
    '''
    ...

@docstring.Substitution(make_axes_kw_doc)
def make_axes_gridspec(parent, **kw):
    '''
    Resize and reposition a parent axes, and return a child axes
    suitable for a colorbar. This function is similar to
    make_axes. Prmary differences are

     * *make_axes_gridspec* only handles the *orientation* keyword
       and cannot handle the "location" keyword.

     * *make_axes_gridspec* should only be used with a subplot parent.

     * *make_axes* creates an instance of Axes. *make_axes_gridspec*
        creates an instance of Subplot.

     * *make_axes* updates the position of the
        parent. *make_axes_gridspec* replaces the grid_spec attribute
        of the parent with a new one.

    While this function is meant to be compatible with *make_axes*,
    there could be some minor differences.

    Keyword arguments may include the following (with defaults):

        *orientation*
            'vertical' or 'horizontal'

    %s

    All but the first of these are stripped from the input kw set.

    Returns (cax, kw), the child axes and the reduced kw dictionary to be
    passed when creating the colorbar instance.
    '''
    ...

class ColorbarPatch(Colorbar):
    """
    A Colorbar which is created using :class:`~matplotlib.patches.Patch`
    rather than the default :func:`~matplotlib.axes.pcolor`.

    It uses a list of Patch instances instead of a
    :class:`~matplotlib.collections.PatchCollection` because the
    latter does not allow the hatch pattern to vary among the
    members of the collection.
    """
    def __init__(self, ax, mappable, **kw):
        self.solids_patches = ...
    
    def _add_solids(self, X, Y, C):
        """
        Draw the colors using :class:`~matplotlib.patches.Patch`;
        optionally add separators.
        """
        self.solids_patches = ...
    


def colorbar_factory(cax, mappable, **kwargs):
    """
    Creates a colorbar on the given axes for the given mappable.

    Typically, for automatic colorbar placement given only a mappable use
    :meth:`~matplotlib.figure.Figure.colorbar`.

    """
    ...

