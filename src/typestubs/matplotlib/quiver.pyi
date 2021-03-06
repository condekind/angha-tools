"""
This type stub file was generated by pyright.
"""

import matplotlib.collections as mcollections
import matplotlib.artist as martist
from matplotlib.artist import allow_rasterization
from matplotlib import docstring
from typing import Any, Optional

"""
Support for plotting vector fields.

Presently this contains Quiver and Barb. Quiver plots an arrow in the
direction of the vector, with the size of the arrow related to the
magnitude of the vector.

Barbs are like quiver in that they point along a vector, but
the magnitude of the vector is given schematically by the presence of barbs
or flags on the barb.

This will also become a home for things such as standard
deviation ellipses, which can and will be derived very easily from
the Quiver code.
"""
_quiver_doc = """
Plot a 2-D field of arrows.

Call signatures::

  quiver(U, V, **kw)
  quiver(U, V, C, **kw)
  quiver(X, Y, U, V, **kw)
  quiver(X, Y, U, V, C, **kw)

*U* and *V* are the arrow data, *X* and *Y* set the location of the
arrows, and *C* sets the color of the arrows. These arguments may be 1-D or
2-D arrays or sequences.

If *X* and *Y* are absent, they will be generated as a uniform grid.
If *U* and *V* are 2-D arrays and *X* and *Y* are 1-D, and if ``len(X)`` and
``len(Y)`` match the column and row dimensions of *U*, then *X* and *Y* will be
expanded with :func:`numpy.meshgrid`.

The default settings auto-scales the length of the arrows to a reasonable size.
To change this behavior see the *scale* and *scale_units* kwargs.

The defaults give a slightly swept-back arrow; to make the head a
triangle, make *headaxislength* the same as *headlength*. To make the
arrow more pointed, reduce *headwidth* or increase *headlength* and
*headaxislength*. To make the head smaller relative to the shaft,
scale down all the head parameters. You will probably do best to leave
minshaft alone.

*linewidths* and *edgecolors* can be used to customize the arrow
outlines.

Parameters
----------
X : 1D or 2D array, sequence, optional
    The x coordinates of the arrow locations
Y : 1D or 2D array, sequence, optional
    The y coordinates of the arrow locations
U : 1D or 2D array or masked array, sequence
    The x components of the arrow vectors
V : 1D or 2D array or masked array, sequence
    The y components of the arrow vectors
C : 1D or 2D array, sequence, optional
    The arrow colors
units : [ 'width' | 'height' | 'dots' | 'inches' | 'x' | 'y' | 'xy' ]
    The arrow dimensions (except for *length*) are measured in multiples of
    this unit.

    'width' or 'height': the width or height of the axis

    'dots' or 'inches': pixels or inches, based on the figure dpi

    'x', 'y', or 'xy': respectively *X*, *Y*, or :math:`\\sqrt{X^2 + Y^2}`
    in data units

    The arrows scale differently depending on the units.  For
    'x' or 'y', the arrows get larger as one zooms in; for other
    units, the arrow size is independent of the zoom state.  For
    'width or 'height', the arrow size increases with the width and
    height of the axes, respectively, when the window is resized;
    for 'dots' or 'inches', resizing does not change the arrows.
angles : [ 'uv' | 'xy' ], array, optional
    Method for determining the angle of the arrows. Default is 'uv'.

    'uv': the arrow axis aspect ratio is 1 so that
    if *U*==*V* the orientation of the arrow on the plot is 45 degrees
    counter-clockwise from the horizontal axis (positive to the right).

    'xy': arrows point from (x,y) to (x+u, y+v).
    Use this for plotting a gradient field, for example.

    Alternatively, arbitrary angles may be specified as an array
    of values in degrees, counter-clockwise from the horizontal axis.

    Note: inverting a data axis will correspondingly invert the
    arrows only with ``angles='xy'``.
scale : None, float, optional
    Number of data units per arrow length unit, e.g., m/s per plot width; a
    smaller scale parameter makes the arrow longer. Default is *None*.

    If *None*, a simple autoscaling algorithm is used, based on the average
    vector length and the number of vectors. The arrow length unit is given by
    the *scale_units* parameter
scale_units : [ 'width' | 'height' | 'dots' | 'inches' | 'x' | 'y' | 'xy' ], \
None, optional
    If the *scale* kwarg is *None*, the arrow length unit. Default is *None*.

    e.g. *scale_units* is 'inches', *scale* is 2.0, and
    ``(u,v) = (1,0)``, then the vector will be 0.5 inches long.

    If *scale_units* is 'width'/'height', then the vector will be half the
    width/height of the axes.

    If *scale_units* is 'x' then the vector will be 0.5 x-axis
    units. To plot vectors in the x-y plane, with u and v having
    the same units as x and y, use
    ``angles='xy', scale_units='xy', scale=1``.
width : scalar, optional
    Shaft width in arrow units; default depends on choice of units,
    above, and number of vectors; a typical starting value is about
    0.005 times the width of the plot.
headwidth : scalar, optional
    Head width as multiple of shaft width, default is 3
headlength : scalar, optional
    Head length as multiple of shaft width, default is 5
headaxislength : scalar, optional
    Head length at shaft intersection, default is 4.5
minshaft : scalar, optional
    Length below which arrow scales, in units of head length. Do not
    set this to less than 1, or small arrows will look terrible!
    Default is 1
minlength : scalar, optional
    Minimum length as a multiple of shaft width; if an arrow length
    is less than this, plot a dot (hexagon) of this diameter instead.
    Default is 1.
pivot : [ 'tail' | 'mid' | 'middle' | 'tip' ], optional
    The part of the arrow that is at the grid point; the arrow rotates
    about this point, hence the name *pivot*.
color : [ color | color sequence ], optional
    This is a synonym for the
    :class:`~matplotlib.collections.PolyCollection` facecolor kwarg.
    If *C* has been set, *color* has no effect.

Notes
-----
Additional :class:`~matplotlib.collections.PolyCollection`
keyword arguments:

%(PolyCollection)s

See Also
--------
quiverkey : Add a key to a quiver plot
""" % docstring.interpd.params
_quiverkey_doc = """
Add a key to a quiver plot.

Call signature::

  quiverkey(Q, X, Y, U, label, **kw)

Arguments:

  *Q*:
    The Quiver instance returned by a call to quiver.

  *X*, *Y*:
    The location of the key; additional explanation follows.

  *U*:
    The length of the key

  *label*:
    A string with the length and units of the key

Keyword arguments:

  *angle* = 0
    The angle of the key arrow. Measured in degrees anti-clockwise from the
    x-axis.

  *coordinates* = [ 'axes' | 'figure' | 'data' | 'inches' ]
    Coordinate system and units for *X*, *Y*: 'axes' and 'figure' are
    normalized coordinate systems with 0,0 in the lower left and 1,1
    in the upper right; 'data' are the axes data coordinates (used for
    the locations of the vectors in the quiver plot itself); 'inches'
    is position in the figure in inches, with 0,0 at the lower left
    corner.

  *color*:
    overrides face and edge colors from *Q*.

  *labelpos* = [ 'N' | 'S' | 'E' | 'W' ]
    Position the label above, below, to the right, to the left of the
    arrow, respectively.

  *labelsep*:
    Distance in inches between the arrow and the label.  Default is
    0.1

  *labelcolor*:
    defaults to default :class:`~matplotlib.text.Text` color.

  *fontproperties*:
    A dictionary with keyword arguments accepted by the
    :class:`~matplotlib.font_manager.FontProperties` initializer:
    *family*, *style*, *variant*, *size*, *weight*

Any additional keyword arguments are used to override vector
properties taken from *Q*.

The positioning of the key depends on *X*, *Y*, *coordinates*, and
*labelpos*.  If *labelpos* is 'N' or 'S', *X*, *Y* give the position
of the middle of the key arrow.  If *labelpos* is 'E', *X*, *Y*
positions the head, and if *labelpos* is 'W', *X*, *Y* positions the
tail; in either of these two cases, *X*, *Y* is somewhere in the
middle of the arrow+label key object.
"""
class QuiverKey(martist.Artist):
    """ Labelled arrow for use as a quiver plot scale key."""
    halign = ...
    valign = ...
    pivot = ...
    def __init__(self, Q, X, Y, U, label, **kw):
        self.Q = ...
        self.X = ...
        self.Y = ...
        self.U = ...
        self.angle = ...
        self.coord = ...
        self.color = ...
        self.label = ...
        self.labelsep = ...
        self.labelpos = ...
        self.labelcolor = ...
        self.fontproperties = ...
        self.kw = ...
        self.text = ...
        self.zorder = ...
    
    def remove(self):
        """
        Overload the remove method
        """
        ...
    
    def _init(self):
        ...
    
    def _text_x(self, x):
        ...
    
    def _text_y(self, y):
        ...
    
    @allow_rasterization
    def draw(self, renderer):
        self.stale = ...
    
    def _set_transform(self):
        ...
    
    def set_figure(self, fig):
        ...
    
    def contains(self, mouseevent):
        ...
    
    quiverkey_doc = ...


def _parse_args(*args):
    ...

def _check_consistent_shapes(*arrays):
    ...

class Quiver(mcollections.PolyCollection):
    """
    Specialized PolyCollection for arrows.

    The only API method is set_UVC(), which can be used
    to change the size, orientation, and color of the
    arrows; their locations are fixed when the class is
    instantiated.  Possibly this method will be useful
    in animations.

    Much of the work in this class is done in the draw()
    method so that as much information as possible is available
    about the plot.  In subsequent draw() calls, recalculation
    is limited to things that might have changed, so there
    should be no performance penalty from putting the calculations
    in the draw() method.
    """
    _PIVOT_VALS = ...
    @docstring.Substitution(_quiver_doc)
    def __init__(self, ax, *args, **kw):
        """
        The constructor takes one required argument, an Axes
        instance, followed by the args and kwargs described
        by the following pylab interface documentation:
        %s
        """
        self.ax = ...
        self.X = ...
        self.Y = ...
        self.XY = ...
        self.N = ...
        self.scale = ...
        self.headwidth = ...
        self.headlength = ...
        self.headaxislength = ...
        self.minshaft = ...
        self.minlength = ...
        self.units = ...
        self.scale_units = ...
        self.angles = ...
        self.width = ...
        self.color = ...
        self.pivot = ...
        self.transform = ...
        self.polykw = ...
        self.keyvec = ...
        self.keytext = ...
    
    def remove(self):
        """
        Overload the remove method
        """
        ...
    
    def _init(self):
        """
        Initialization delayed until first draw;
        allow time for axes setup.
        """
        ...
    
    def get_datalim(self, transData):
        ...
    
    @allow_rasterization
    def draw(self, renderer):
        self.stale = ...
    
    def set_UVC(self, U, V, C: Optional[Any] = ...):
        self.U = ...
        self.V = ...
        self.Umask = ...
        self.stale = ...
    
    def _dots_per_unit(self, units):
        """
        Return a scale factor for converting from units to pixels
        """
        ...
    
    def _set_transform(self):
        """
        Sets the PolygonCollection transform to go
        from arrow width units to pixels.
        """
        ...
    
    def _angles_lengths(self, U, V, eps=...):
        ...
    
    def _make_verts(self, U, V, angles):
        ...
    
    def _h_arrows(self, length):
        """ length is in arrow width units """
        ...
    
    quiver_doc = ...


_barbs_doc = r"""
Plot a 2-D field of barbs.

Call signatures::

  barb(U, V, **kw)
  barb(U, V, C, **kw)
  barb(X, Y, U, V, **kw)
  barb(X, Y, U, V, C, **kw)

Arguments:

  *X*, *Y*:
    The x and y coordinates of the barb locations
    (default is head of barb; see *pivot* kwarg)

  *U*, *V*:
    Give the x and y components of the barb shaft

  *C*:
    An optional array used to map colors to the barbs

All arguments may be 1-D or 2-D arrays or sequences. If *X* and *Y*
are absent, they will be generated as a uniform grid.  If *U* and *V*
are 2-D arrays but *X* and *Y* are 1-D, and if ``len(X)`` and ``len(Y)``
match the column and row dimensions of *U*, then *X* and *Y* will be
expanded with :func:`numpy.meshgrid`.

*U*, *V*, *C* may be masked arrays, but masked *X*, *Y* are not
supported at present.

Keyword arguments:

  *length*:
    Length of the barb in points; the other parts of the barb
    are scaled against this.
    Default is 7.

  *pivot*: [ 'tip' | 'middle' | float ]
    The part of the arrow that is at the grid point; the arrow rotates
    about this point, hence the name *pivot*.  Default is 'tip'. Can
    also be a number, which shifts the start of the barb that many
    points from the origin.

  *barbcolor*: [ color | color sequence ]
    Specifies the color all parts of the barb except any flags.  This
    parameter is analogous to the *edgecolor* parameter for polygons,
    which can be used instead. However this parameter will override
    facecolor.

  *flagcolor*: [ color | color sequence ]
    Specifies the color of any flags on the barb.  This parameter is
    analogous to the *facecolor* parameter for polygons, which can be
    used instead. However this parameter will override facecolor.  If
    this is not set (and *C* has not either) then *flagcolor* will be
    set to match *barbcolor* so that the barb has a uniform color. If
    *C* has been set, *flagcolor* has no effect.

  *sizes*:
    A dictionary of coefficients specifying the ratio of a given
    feature to the length of the barb. Only those values one wishes to
    override need to be included.  These features include:

        - 'spacing' - space between features (flags, full/half barbs)

        - 'height' - height (distance from shaft to top) of a flag or
          full barb

        - 'width' - width of a flag, twice the width of a full barb

        - 'emptybarb' - radius of the circle used for low magnitudes

  *fill_empty*:
    A flag on whether the empty barbs (circles) that are drawn should
    be filled with the flag color.  If they are not filled, they will
    be drawn such that no color is applied to the center.  Default is
    False

  *rounding*:
    A flag to indicate whether the vector magnitude should be rounded
    when allocating barb components.  If True, the magnitude is
    rounded to the nearest multiple of the half-barb increment.  If
    False, the magnitude is simply truncated to the next lowest
    multiple.  Default is True

  *barb_increments*:
    A dictionary of increments specifying values to associate with
    different parts of the barb. Only those values one wishes to
    override need to be included.

        - 'half' - half barbs (Default is 5)

        - 'full' - full barbs (Default is 10)

        - 'flag' - flags (default is 50)

  *flip_barb*:
    Either a single boolean flag or an array of booleans.  Single
    boolean indicates whether the lines and flags should point
    opposite to normal for all barbs.  An array (which should be the
    same size as the other data arrays) indicates whether to flip for
    each individual barb.  Normal behavior is for the barbs and lines
    to point right (comes from wind barbs having these features point
    towards low pressure in the Northern Hemisphere.)  Default is
    False

Barbs are traditionally used in meteorology as a way to plot the speed
and direction of wind observations, but can technically be used to
plot any two dimensional vector quantity.  As opposed to arrows, which
give vector magnitude by the length of the arrow, the barbs give more
quantitative information about the vector magnitude by putting slanted
lines or a triangle for various increments in magnitude, as show
schematically below::

 :     /\    \\
 :    /  \    \\
 :   /    \    \    \\
 :  /      \    \    \\
 : ------------------------------

.. note the double \\ at the end of each line to make the figure
.. render correctly

The largest increment is given by a triangle (or "flag"). After those
come full lines (barbs). The smallest increment is a half line.  There
is only, of course, ever at most 1 half line.  If the magnitude is
small and only needs a single half-line and no full lines or
triangles, the half-line is offset from the end of the barb so that it
can be easily distinguished from barbs with a single full line.  The
magnitude for the barb shown above would nominally be 65, using the
standard increments of 50, 10, and 5.

linewidths and edgecolors can be used to customize the barb.
Additional :class:`~matplotlib.collections.PolyCollection` keyword
arguments:

%(PolyCollection)s
""" % docstring.interpd.params
class Barbs(mcollections.PolyCollection):
    '''
    Specialized PolyCollection for barbs.

    The only API method is :meth:`set_UVC`, which can be used to
    change the size, orientation, and color of the arrows.  Locations
    are changed using the :meth:`set_offsets` collection method.
    Possibly this method will be useful in animations.

    There is one internal function :meth:`_find_tails` which finds
    exactly what should be put on the barb given the vector magnitude.
    From there :meth:`_make_barbs` is used to find the vertices of the
    polygon to represent the barb based on this information.
    '''
    @docstring.interpd
    def __init__(self, ax, *args, **kw):
        """
        The constructor takes one required argument, an Axes
        instance, followed by the args and kwargs described
        by the following pylab interface documentation:
        %(barbs_doc)s
        """
        self.sizes = ...
        self.fill_empty = ...
        self.barb_increments = ...
        self.rounding = ...
        self.flip = ...
        self.x = ...
        self.y = ...
    
    def _find_tails(self, mag, rounding: bool = ..., half=..., full=..., flag=...):
        '''
        Find how many of each of the tail pieces is necessary.  Flag
        specifies the increment for a flag, barb for a full barb, and half for
        half a barb. Mag should be the magnitude of a vector (i.e., >= 0).

        This returns a tuple of:

            (*number of flags*, *number of barbs*, *half_flag*, *empty_flag*)

        *half_flag* is a boolean whether half of a barb is needed,
        since there should only ever be one half on a given
        barb. *empty_flag* flag is an array of flags to easily tell if
        a barb is empty (too low to plot any barbs/flags.
        '''
        ...
    
    def _make_barbs(self, u, v, nflags, nbarbs, half_barb, empty_flag, length, pivot, sizes, fill_empty, flip):
        '''
        This function actually creates the wind barbs.  *u* and *v*
        are components of the vector in the *x* and *y* directions,
        respectively.

        *nflags*, *nbarbs*, and *half_barb*, empty_flag* are,
        *respectively, the number of flags, number of barbs, flag for
        *half a barb, and flag for empty barb, ostensibly obtained
        *from :meth:`_find_tails`.

        *length* is the length of the barb staff in points.

        *pivot* specifies the point on the barb around which the
        entire barb should be rotated.  Right now, valid options are
        'tip' and 'middle'. Can also be a number, which shifts the start
        of the barb that many points from the origin.

        *sizes* is a dictionary of coefficients specifying the ratio
        of a given feature to the length of the barb. These features
        include:

            - *spacing*: space between features (flags, full/half
               barbs)

            - *height*: distance from shaft of top of a flag or full
               barb

            - *width* - width of a flag, twice the width of a full barb

            - *emptybarb* - radius of the circle used for low
               magnitudes

        *fill_empty* specifies whether the circle representing an
        empty barb should be filled or not (this changes the drawing
        of the polygon).

        *flip* is a flag indicating whether the features should be flipped to
        the other side of the barb (useful for winds in the southern
        hemisphere).

        This function returns list of arrays of vertices, defining a polygon
        for each of the wind barbs.  These polygons have been rotated to
        properly align with the vector direction.
        '''
        ...
    
    def set_UVC(self, U, V, C: Optional[Any] = ...):
        self.u = ...
        self.v = ...
        self.stale = ...
    
    def set_offsets(self, xy):
        """
        Set the offsets for the barb polygons.  This saves the offsets passed
        in and actually sets version masked as appropriate for the existing
        U/V data. *offsets* should be a sequence.

        ACCEPTS: sequence of pairs of floats
        """
        self.x = ...
        self.y = ...
        self.stale = ...
    
    barbs_doc = ...


