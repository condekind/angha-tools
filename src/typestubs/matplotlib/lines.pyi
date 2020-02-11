"""
This type stub file was generated by pyright.
"""

from . import docstring
from .artist import Artist, allow_rasterization
from .markers import MarkerStyle
from typing import Any, Optional

"""
This module contains all the 2D line class which can draw with a
variety of line styles, markers and colors.
"""
def _get_dash_pattern(style):
    """Convert linestyle -> dash pattern
    """
    ...

def _scale_dashes(offset, dashes, lw):
    ...

def segment_hits(cx, cy, x, y, radius):
    """
    Determine if any line segments are within radius of a
    point. Returns the list of line segments that are within that
    radius.
    """
    ...

def _mark_every_path(markevery, tpath, affine, ax_transform):
    """
    Helper function that sorts out how to deal the input
    `markevery` and returns the points where markers should be drawn.

    Takes in the `markevery` value and the line path and returns the
    sub-sampled path.
    """
    ...

class Line2D(Artist):
    """
    A line - the line can have both a solid linestyle connecting all
    the vertices, and a marker at each vertex.  Additionally, the
    drawing of the solid line is influenced by the drawstyle, e.g., one
    can create "stepped" lines in various styles.


    """
    lineStyles = ...
    _drawStyles_l = ...
    _drawStyles_s = ...
    drawStyles = ...
    drawStyleKeys = ...
    markers = ...
    filled_markers = ...
    fillStyles = ...
    zorder = ...
    validCap = ...
    validJoin = ...
    def __str__(self):
        ...
    
    def __init__(self, xdata, ydata, linewidth: Optional[Any] = ..., linestyle: Optional[Any] = ..., color: Optional[Any] = ..., marker: Optional[Any] = ..., markersize: Optional[Any] = ..., markeredgewidth: Optional[Any] = ..., markeredgecolor: Optional[Any] = ..., markerfacecolor: Optional[Any] = ..., markerfacecoloralt=..., fillstyle: Optional[Any] = ..., antialiased: Optional[Any] = ..., dash_capstyle: Optional[Any] = ..., solid_capstyle: Optional[Any] = ..., dash_joinstyle: Optional[Any] = ..., solid_joinstyle: Optional[Any] = ..., pickradius=..., drawstyle: Optional[Any] = ..., markevery: Optional[Any] = ..., **kwargs):
        """
        Create a :class:`~matplotlib.lines.Line2D` instance with *x*
        and *y* data in sequences *xdata*, *ydata*.

        The kwargs are :class:`~matplotlib.lines.Line2D` properties:

        %(Line2D)s

        See :meth:`set_linestyle` for a decription of the line styles,
        :meth:`set_marker` for a description of the markers, and
        :meth:`set_drawstyle` for a description of the draw styles.

        """
        self.verticalOffset = ...
        self.pickradius = ...
        self.ind_offset = ...
    
    def contains(self, mouseevent):
        """
        Test whether the mouse event occurred on the line.  The pick
        radius determines the precision of the location test (usually
        within five points of the value).  Use
        :meth:`~matplotlib.lines.Line2D.get_pickradius` or
        :meth:`~matplotlib.lines.Line2D.set_pickradius` to view or
        modify it.

        Returns *True* if any values are within the radius along with
        ``{'ind': pointlist}``, where *pointlist* is the set of points
        within the radius.

        TODO: sort returned indices by distance
        """
        ...
    
    def get_pickradius(self):
        """return the pick radius used for containment tests"""
        ...
    
    def set_pickradius(self, d):
        """Set the pick radius used for containment tests.

        .. ACCEPTS: float distance in points

        Parameters
        ----------
        d : float
            Pick radius, in points.
        """
        self.pickradius = ...
    
    def get_fillstyle(self):
        """
        return the marker fillstyle
        """
        ...
    
    def set_fillstyle(self, fs):
        """
        Set the marker fill style; 'full' means fill the whole marker.
        'none' means no filling; other options are for half-filled markers.

        ACCEPTS: ['full' | 'left' | 'right' | 'bottom' | 'top' | 'none']
        """
        self.stale = ...
    
    def set_markevery(self, every):
        """Set the markevery property to subsample the plot when using markers.

        e.g., if `every=5`, every 5-th marker will be plotted.

        ACCEPTS: [None | int | length-2 tuple of int | slice |
        list/array of int | float | length-2 tuple of float]

        Parameters
        ----------
        every: None | int | length-2 tuple of int | slice | list/array of int \
| float | length-2 tuple of float
            Which markers to plot.

            - every=None, every point will be plotted.
            - every=N, every N-th marker will be plotted starting with
              marker 0.
            - every=(start, N), every N-th marker, starting at point
              start, will be plotted.
            - every=slice(start, end, N), every N-th marker, starting at
              point start, upto but not including point end, will be plotted.
            - every=[i, j, m, n], only markers at points i, j, m, and n
              will be plotted.
            - every=0.1, (i.e. a float) then markers will be spaced at
              approximately equal distances along the line; the distance
              along the line between markers is determined by multiplying the
              display-coordinate distance of the axes bounding-box diagonal
              by the value of every.
            - every=(0.5, 0.1) (i.e. a length-2 tuple of float), the
              same functionality as every=0.1 is exhibited but the first
              marker will be 0.5 multiplied by the
              display-cordinate-diagonal-distance along the line.

        Notes
        -----
        Setting the markevery property will only show markers at actual data
        points.  When using float arguments to set the markevery property
        on irregularly spaced data, the markers will likely not appear evenly
        spaced because the actual data points do not coincide with the
        theoretical spacing between markers.

        When using a start offset to specify the first marker, the offset will
        be from the first data point which may be different from the first
        the visible data point if the plot is zoomed in.

        If zooming in on a plot when using float arguments then the actual
        data points that have markers will change because the distance between
        markers is always determined from the display-coordinates
        axes-bounding-box-diagonal regardless of the actual axes data limits.

        """
        ...
    
    def get_markevery(self):
        """return the markevery setting"""
        ...
    
    def set_picker(self, p):
        """Sets the event picker details for the line.

        ACCEPTS: float distance in points or callable pick function
        ``fn(artist, event)``
        """
        ...
    
    def get_window_extent(self, renderer):
        ...
    
    @Artist.axes.setter
    def axes(self, ax):
        ...
    
    def set_data(self, *args):
        """
        Set the x and y data

        ACCEPTS: 2D array (rows are x, y) or two 1D arrays
        """
        ...
    
    def recache_always(self):
        ...
    
    def recache(self, always: bool = ...):
        ...
    
    def _transform_path(self, subslice: Optional[Any] = ...):
        """
        Puts a TransformedPath instance at self._transformed_path;
        all invalidation of the transform is then handled by the
        TransformedPath instance.
        """
        ...
    
    def _get_transformed_path(self):
        """
        Return the :class:`~matplotlib.transforms.TransformedPath` instance
        of this line.
        """
        ...
    
    def set_transform(self, t):
        """
        set the Transformation instance used by this artist

        ACCEPTS: a :class:`matplotlib.transforms.Transform` instance
        """
        self.stale = ...
    
    def _is_sorted(self, x):
        """return True if x is sorted in ascending order"""
        ...
    
    @allow_rasterization
    def draw(self, renderer):
        """draw the Line with `renderer` unless visibility is False"""
        self.ind_offset = ...
        self.stale = ...
    
    def get_antialiased(self):
        ...
    
    def get_color(self):
        ...
    
    def get_drawstyle(self):
        ...
    
    def get_linestyle(self):
        ...
    
    def get_linewidth(self):
        ...
    
    def get_marker(self):
        ...
    
    def get_markeredgecolor(self):
        ...
    
    def get_markeredgewidth(self):
        ...
    
    def _get_markerfacecolor(self, alt: bool = ...):
        ...
    
    def get_markerfacecolor(self):
        ...
    
    def get_markerfacecoloralt(self):
        ...
    
    def get_markersize(self):
        ...
    
    def get_data(self, orig: bool = ...):
        """
        Return the xdata, ydata.

        If *orig* is *True*, return the original data.
        """
        ...
    
    def get_xdata(self, orig: bool = ...):
        """
        Return the xdata.

        If *orig* is *True*, return the original data, else the
        processed data.
        """
        ...
    
    def get_ydata(self, orig: bool = ...):
        """
        Return the ydata.

        If *orig* is *True*, return the original data, else the
        processed data.
        """
        ...
    
    def get_path(self):
        """
        Return the :class:`~matplotlib.path.Path` object associated
        with this line.
        """
        ...
    
    def get_xydata(self):
        """
        Return the *xy* data as a Nx2 numpy array.
        """
        ...
    
    def set_antialiased(self, b):
        """
        Set whether to use antialiased rendering.

        Parameters
        ----------
        b : bool
            .. ACCEPTS: bool
        """
        ...
    
    def set_color(self, color):
        """
        Set the color of the line

        ACCEPTS: any matplotlib color
        """
        self.stale = ...
    
    def set_drawstyle(self, drawstyle):
        """
        Set the drawstyle of the plot

        'default' connects the points with lines. The steps variants
        produce step-plots. 'steps' is equivalent to 'steps-pre' and
        is maintained for backward-compatibility.

        ACCEPTS: ['default' | 'steps' | 'steps-pre' | 'steps-mid' |
                  'steps-post']
        """
        ...
    
    def set_linewidth(self, w):
        """
        Set the line width in points

        ACCEPTS: float value in points
        """
        ...
    
    def _split_drawstyle_linestyle(self, ls):
        '''Split drawstyle from linestyle string

        If `ls` is only a drawstyle default to returning a linestyle
        of '-'.

        Parameters
        ----------
        ls : str
            The linestyle to be processed

        Returns
        -------
        ret_ds : str or None
            If the linestyle string does not contain a drawstyle prefix
            return None, otherwise return it.

        ls : str
            The linestyle with the drawstyle (if any) stripped.
        '''
        ...
    
    def set_linestyle(self, ls):
        """
        Set the linestyle of the line (also accepts drawstyles,
        e.g., ``'steps--'``)


        ===========================   =================
        linestyle                     description
        ===========================   =================
        ``'-'`` or ``'solid'``        solid line
        ``'--'`` or  ``'dashed'``     dashed line
        ``'-.'`` or  ``'dashdot'``    dash-dotted line
        ``':'`` or ``'dotted'``       dotted line
        ``'None'``                    draw nothing
        ``' '``                       draw nothing
        ``''``                        draw nothing
        ===========================   =================

        'steps' is equivalent to 'steps-pre' and is maintained for
        backward-compatibility.

        Alternatively a dash tuple of the following form can be provided::

            (offset, onoffseq),

        where ``onoffseq`` is an even length tuple of on and off ink
        in points.


        ACCEPTS: ['solid' | 'dashed', 'dashdot', 'dotted' |
                   (offset, on-off-dash-seq) |
                   ``'-'`` | ``'--'`` | ``'-.'`` | ``':'`` | ``'None'`` |
                   ``' '`` | ``''``]

        .. seealso::

            :meth:`set_drawstyle`
               To set the drawing style (stepping) of the plot.

        Parameters
        ----------
        ls : { ``'-'``,  ``'--'``, ``'-.'``, ``':'``} and more see description
            The line style.
        """
        ...
    
    @docstring.dedent_interpd
    def set_marker(self, marker):
        """
        Set the line marker

        ACCEPTS: :mod:`A valid marker style <matplotlib.markers>`

        Parameters
        ----------

        marker: marker style
            See `~matplotlib.markers` for full description of possible
            argument

        """
        self.stale = ...
    
    def set_markeredgecolor(self, ec):
        """
        Set the marker edge color

        ACCEPTS: any matplotlib color
        """
        ...
    
    def set_markeredgewidth(self, ew):
        """
        Set the marker edge width in points

        ACCEPTS: float value in points
        """
        ...
    
    def set_markerfacecolor(self, fc):
        """
        Set the marker face color.

        ACCEPTS: any matplotlib color
        """
        ...
    
    def set_markerfacecoloralt(self, fc):
        """
        Set the alternate marker face color.

        ACCEPTS: any matplotlib color
        """
        ...
    
    def set_markersize(self, sz):
        """
        Set the marker size in points

        ACCEPTS: float
        """
        ...
    
    def set_xdata(self, x):
        """
        Set the data np.array for x

        ACCEPTS: 1D array
        """
        self.stale = ...
    
    def set_ydata(self, y):
        """
        Set the data np.array for y

        ACCEPTS: 1D array
        """
        self.stale = ...
    
    def set_dashes(self, seq):
        """
        Set the dash sequence, sequence of dashes with on off ink in
        points.  If seq is empty or if seq = (None, None), the
        linestyle will be set to solid.

        ACCEPTS: sequence of on/off ink in points
        """
        ...
    
    def update_from(self, other):
        """copy properties from other to self"""
        ...
    
    def _get_rgba_face(self, alt: bool = ...):
        ...
    
    def _get_rgba_ln_color(self, alt: bool = ...):
        ...
    
    def set_aa(self, val):
        'alias for set_antialiased'
        ...
    
    def set_c(self, val):
        'alias for set_color'
        ...
    
    def set_ls(self, val):
        """alias for set_linestyle"""
        ...
    
    def set_lw(self, val):
        """alias for set_linewidth"""
        ...
    
    def set_mec(self, val):
        """alias for set_markeredgecolor"""
        ...
    
    def set_mew(self, val):
        """alias for set_markeredgewidth"""
        ...
    
    def set_mfc(self, val):
        """alias for set_markerfacecolor"""
        ...
    
    def set_mfcalt(self, val):
        """alias for set_markerfacecoloralt"""
        ...
    
    def set_ms(self, val):
        """alias for set_markersize"""
        ...
    
    def get_aa(self):
        """alias for get_antialiased"""
        ...
    
    def get_c(self):
        """alias for get_color"""
        ...
    
    def get_ls(self):
        """alias for get_linestyle"""
        ...
    
    def get_lw(self):
        """alias for get_linewidth"""
        ...
    
    def get_mec(self):
        """alias for get_markeredgecolor"""
        ...
    
    def get_mew(self):
        """alias for get_markeredgewidth"""
        ...
    
    def get_mfc(self):
        """alias for get_markerfacecolor"""
        ...
    
    def get_mfcalt(self, alt: bool = ...):
        """alias for get_markerfacecoloralt"""
        ...
    
    def get_ms(self):
        """alias for get_markersize"""
        ...
    
    def set_dash_joinstyle(self, s):
        """
        Set the join style for dashed linestyles
        ACCEPTS: ['miter' | 'round' | 'bevel']
        """
        ...
    
    def set_solid_joinstyle(self, s):
        """
        Set the join style for solid linestyles
        ACCEPTS: ['miter' | 'round' | 'bevel']
        """
        ...
    
    def get_dash_joinstyle(self):
        """
        Get the join style for dashed linestyles
        """
        ...
    
    def get_solid_joinstyle(self):
        """
        Get the join style for solid linestyles
        """
        ...
    
    def set_dash_capstyle(self, s):
        """
        Set the cap style for dashed linestyles

        ACCEPTS: ['butt' | 'round' | 'projecting']
        """
        ...
    
    def set_solid_capstyle(self, s):
        """
        Set the cap style for solid linestyles

        ACCEPTS: ['butt' | 'round' |  'projecting']
        """
        ...
    
    def get_dash_capstyle(self):
        """
        Get the cap style for dashed linestyles
        """
        ...
    
    def get_solid_capstyle(self):
        """
        Get the cap style for solid linestyles
        """
        ...
    
    def is_dashed(self):
        'return True if line is dashstyle'
        ...
    


class VertexSelector(object):
    """
    Manage the callbacks to maintain a list of selected vertices for
    :class:`matplotlib.lines.Line2D`. Derived classes should override
    :meth:`~matplotlib.lines.VertexSelector.process_selected` to do
    something with the picks.

    Here is an example which highlights the selected verts with red
    circles::

        import numpy as np
        import matplotlib.pyplot as plt
        import matplotlib.lines as lines

        class HighlightSelected(lines.VertexSelector):
            def __init__(self, line, fmt='ro', **kwargs):
                lines.VertexSelector.__init__(self, line)
                self.markers, = self.axes.plot([], [], fmt, **kwargs)

            def process_selected(self, ind, xs, ys):
                self.markers.set_data(xs, ys)
                self.canvas.draw()

        fig, ax = plt.subplots()
        x, y = np.random.rand(2, 30)
        line, = ax.plot(x, y, 'bs-', picker=5)

        selector = HighlightSelected(line)
        plt.show()

    """
    def __init__(self, line):
        """
        Initialize the class with a :class:`matplotlib.lines.Line2D`
        instance.  The line should already be added to some
        :class:`matplotlib.axes.Axes` instance and should have the
        picker property set.
        """
        self.axes = ...
        self.line = ...
        self.canvas = ...
        self.cid = ...
        self.ind = ...
    
    def process_selected(self, ind, xs, ys):
        """
        Default "do nothing" implementation of the
        :meth:`process_selected` method.

        *ind* are the indices of the selected vertices.  *xs* and *ys*
        are the coordinates of the selected vertices.
        """
        ...
    
    def onpick(self, event):
        """When the line is picked, update the set of selected indices."""
        ...
    


lineStyles = Line2D._lineStyles
lineMarkers = MarkerStyle.markers
drawStyles = Line2D.drawStyles
fillStyles = MarkerStyle.fillstyles
