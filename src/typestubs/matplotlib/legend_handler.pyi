"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""
This module defines default legend handlers.

It is strongly encouraged to have read the :doc:`legend guide
</tutorials/intermediate/legend_guide>` before this documentation.

Legend handlers are expected to be a callable object with a following
signature. ::

    legend_handler(legend, orig_handle, fontsize, handlebox)

Where *legend* is the legend itself, *orig_handle* is the original
plot, *fontsize* is the fontsize in pixels, and *handlebox* is a
OffsetBox instance. Within the call, you should create relevant
artists (using relevant properties from the *legend* and/or
*orig_handle*) and add them into the handlebox. The artists needs to
be scaled according to the fontsize (note that the size is in pixel,
i.e., this is dpi-scaled value).

This module includes definition of several legend handler classes
derived from the base class (HandlerBase) with the following method::

    def legend_artist(self, legend, orig_handle, fontsize, handlebox):

"""
def update_from_first_child(tgt, src):
    ...

class HandlerBase(object):
    """
    A Base class for default legend handlers.

    The derived classes are meant to override *create_artists* method, which
    has a following signature.::

      def create_artists(self, legend, orig_handle,
                         xdescent, ydescent, width, height, fontsize,
                         trans):

    The overridden method needs to create artists of the given
    transform that fits in the given dimension (xdescent, ydescent,
    width, height) that are scaled by fontsize if necessary.

    """
    def __init__(self, xpad=..., ypad=..., update_func: Optional[Any] = ...):
        ...
    
    def _update_prop(self, legend_handle, orig_handle):
        ...
    
    def _default_update_prop(self, legend_handle, orig_handle):
        ...
    
    def update_prop(self, legend_handle, orig_handle, legend):
        ...
    
    def adjust_drawing_area(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize):
        ...
    
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        """
        Return the artist that this HandlerBase generates for the given
        original artist/handle.

        Parameters
        ----------
        legend : :class:`matplotlib.legend.Legend` instance
            The legend for which these legend artists are being created.
        orig_handle : :class:`matplotlib.artist.Artist` or similar
            The object for which these legend artists are being created.
        fontsize : float or int
            The fontsize in pixels. The artists being created should
            be scaled according to the given fontsize.
        handlebox : :class:`matplotlib.offsetbox.OffsetBox` instance
            The box which has been created to hold this legend entry's
            artists. Artists created in the `legend_artist` method must
            be added to this handlebox inside this method.

        """
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        ...
    


class HandlerNpoints(HandlerBase):
    """
    A legend handler that shows *numpoints* points in the legend entry.
    """
    def __init__(self, marker_pad=..., numpoints: Optional[Any] = ..., **kw):
        """
        Parameters
        ----------
        marker_pad : float
            Padding between points in legend entry.

        numpoints : int
            Number of points to show in legend entry.

        Notes
        -----
        Any other keyword arguments are given to `HandlerBase`.
        """
        ...
    
    def get_numpoints(self, legend):
        ...
    
    def get_xdata(self, legend, xdescent, ydescent, width, height, fontsize):
        ...
    


class HandlerNpointsYoffsets(HandlerNpoints):
    """
    A legend handler that shows *numpoints* in the legend, and allows them to
    be individually offest in the y-direction.
    """
    def __init__(self, numpoints: Optional[Any] = ..., yoffsets: Optional[Any] = ..., **kw):
        """
        Parameters
        ----------
        numpoints : int
            Number of points to show in legend entry.

        yoffsets : array of floats
            Length *numpoints* list of y offsets for each point in
            legend entry.

        Notes
        -----
        Any other keyword arguments are given to `HandlerNpoints`.
        """
        ...
    
    def get_ydata(self, legend, xdescent, ydescent, width, height, fontsize):
        ...
    


class HandlerLine2D(HandlerNpoints):
    """
    Handler for `.Line2D` instances.
    """
    def __init__(self, marker_pad=..., numpoints: Optional[Any] = ..., **kw):
        """
        Parameters
        ----------
        marker_pad : float
            Padding between points in legend entry.

        numpoints : int
            Number of points to show in legend entry.

        Notes
        -----
        Any other keyword arguments are given to `HandlerNpoints`.
        """
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        ...
    


class HandlerPatch(HandlerBase):
    """
    Handler for `.Patch` instances.
    """
    def __init__(self, patch_func: Optional[Any] = ..., **kw):
        """
        Parameters
        ----------
        patch_func : callable, optional
            The function that creates the legend key artist.
            *patch_func* should have the signature::

                def patch_func(legend=legend, orig_handle=orig_handle,
                               xdescent=xdescent, ydescent=ydescent,
                               width=width, height=height, fontsize=fontsize)

            Subsequently the created artist will have its ``update_prop`` method
            called and the appropriate transform will be applied.

        Notes
        -----
        Any other keyword arguments are given to `HandlerBase`.
        """
        ...
    
    def _create_patch(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize):
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        ...
    


class HandlerLineCollection(HandlerLine2D):
    """
    Handler for `.LineCollection` instances.
    """
    def get_numpoints(self, legend):
        ...
    
    def _default_update_prop(self, legend_handle, orig_handle):
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        ...
    


class HandlerRegularPolyCollection(HandlerNpointsYoffsets):
    """
    Handler for `.RegularPolyCollections`.
    """
    def __init__(self, yoffsets: Optional[Any] = ..., sizes: Optional[Any] = ..., **kw):
        ...
    
    def get_numpoints(self, legend):
        ...
    
    def get_sizes(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize):
        ...
    
    def update_prop(self, legend_handle, orig_handle, legend):
        ...
    
    def create_collection(self, orig_handle, sizes, offsets, transOffset):
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        ...
    


class HandlerPathCollection(HandlerRegularPolyCollection):
    """
    Handler for `.PathCollections`, which are used by `~.Axes.scatter`.
    """
    def create_collection(self, orig_handle, sizes, offsets, transOffset):
        ...
    


class HandlerCircleCollection(HandlerRegularPolyCollection):
    """
    Handler for `.CircleCollections`.
    """
    def create_collection(self, orig_handle, sizes, offsets, transOffset):
        ...
    


class HandlerErrorbar(HandlerLine2D):
    """
    Handler for Errorbars.
    """
    def __init__(self, xerr_size=..., yerr_size: Optional[Any] = ..., marker_pad=..., numpoints: Optional[Any] = ..., **kw):
        ...
    
    def get_err_size(self, legend, xdescent, ydescent, width, height, fontsize):
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        ...
    


class HandlerStem(HandlerNpointsYoffsets):
    """
    Handler for plots produced by `~.Axes.stem`.
    """
    def __init__(self, marker_pad=..., numpoints: Optional[Any] = ..., bottom: Optional[Any] = ..., yoffsets: Optional[Any] = ..., **kw):
        """
        Parameters
        ----------
        marker_pad : float
            Padding between points in legend entry. Default is 0.3.

        numpoints : int, optional
            Number of points to show in legend entry.

        bottom : float, optional

        yoffsets : array of floats, optional
            Length *numpoints* list of y offsets for each point in
            legend entry.

        Notes
        -----
        Any other keyword arguments are given to `HandlerNpointsYoffsets`.
        """
        ...
    
    def get_ydata(self, legend, xdescent, ydescent, width, height, fontsize):
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        ...
    


class HandlerTuple(HandlerBase):
    """
    Handler for Tuple.

    Additional kwargs are passed through to `HandlerBase`.

    Parameters
    ----------
    ndivide : int, optional
        The number of sections to divide the legend area into. If None,
        use the length of the input tuple. Default is 1.


    pad : float, optional
        If None, fall back to ``legend.borderpad`` as the default.
        In units of fraction of font size. Default is None.
    """
    def __init__(self, ndivide=..., pad: Optional[Any] = ..., **kwargs):
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        ...
    


class HandlerPolyCollection(HandlerBase):
    """
    Handler for `.PolyCollection` used in `~.Axes.fill_between` and `~.Axes.stackplot`.
    """
    def _update_prop(self, legend_handle, orig_handle):
        ...
    
    def create_artists(self, legend, orig_handle, xdescent, ydescent, width, height, fontsize, trans):
        ...
    


