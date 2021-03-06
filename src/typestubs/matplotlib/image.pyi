"""
This type stub file was generated by pyright.
"""

import logging
import matplotlib.artist as martist
import matplotlib.cm as cm
import matplotlib.cbook as cbook
import matplotlib._image as _image
from matplotlib.artist import allow_rasterization
from matplotlib._image import *
from typing import Any, Optional

"""
The image module supports basic image loading, rescaling and display
operations.

"""
_log = logging.getLogger(__name__)
_interpd_ = { 'none': _image.NEAREST,'nearest': _image.NEAREST,'bilinear': _image.BILINEAR,'bicubic': _image.BICUBIC,'spline16': _image.SPLINE16,'spline36': _image.SPLINE36,'hanning': _image.HANNING,'hamming': _image.HAMMING,'hermite': _image.HERMITE,'kaiser': _image.KAISER,'quadric': _image.QUADRIC,'catrom': _image.CATROM,'gaussian': _image.GAUSSIAN,'bessel': _image.BESSEL,'mitchell': _image.MITCHELL,'sinc': _image.SINC,'lanczos': _image.LANCZOS,'blackman': _image.BLACKMAN }
interpolations_names = set(_interpd_)
def composite_images(images, renderer, magnification=...):
    """
    Composite a number of RGBA images into one.  The images are
    composited in the order in which they appear in the `images` list.

    Parameters
    ----------
    images : list of Images
        Each must have a `make_image` method.  For each image,
        `can_composite` should return `True`, though this is not
        enforced by this function.  Each image must have a purely
        affine transformation with no shear.

    renderer : RendererBase instance

    magnification : float
        The additional magnification to apply for the renderer in use.

    Returns
    -------
    tuple : image, offset_x, offset_y
        Returns the tuple:

        - image: A numpy array of the same type as the input images.

        - offset_x, offset_y: The offset of the image (left, bottom)
          in the output figure.
    """
    ...

def _draw_list_compositing_images(renderer, parent, artists, suppress_composite: Optional[Any] = ...):
    """
    Draw a sorted list of artists, compositing images into a single
    image where possible.

    For internal matplotlib use only: It is here to reduce duplication
    between `Figure.draw` and `Axes.draw`, but otherwise should not be
    generally useful.
    """
    ...

def _rgb_to_rgba(A):
    """
    Convert an RGB image to RGBA, as required by the image resample C++
    extension.
    """
    ...

class _ImageBase(martist.Artist, cm.ScalarMappable):
    zorder = ...
    @property
    @cbook.deprecated("2.1")
    def _interpd(self):
        ...
    
    @property
    @cbook.deprecated("2.1")
    def _interpdr(self):
        ...
    
    @property
    @cbook.deprecated("2.1", alternative="mpl.image.interpolation_names")
    def iterpnames(self):
        ...
    
    def __str__(self):
        ...
    
    def __init__(self, ax, cmap: Optional[Any] = ..., norm: Optional[Any] = ..., interpolation: Optional[Any] = ..., origin: Optional[Any] = ..., filternorm=..., filterrad=..., resample: bool = ..., **kwargs):
        """
        interpolation and cmap default to their rc settings

        cmap is a colors.Colormap instance
        norm is a colors.Normalize instance to map luminance to 0-1

        extent is data axes (left, right, bottom, top) for making image plots
        registered with data plots.  Default is to label the pixel
        centers with the zero-based row and column indices.

        Additional kwargs are matplotlib.artist properties

        """
        self.origin = ...
        self.axes = ...
    
    def __getstate__(self):
        ...
    
    def get_size(self):
        """Get the numrows, numcols of the input image"""
        ...
    
    def set_alpha(self, alpha):
        """
        Set the alpha value used for blending - not supported on
        all backends

        ACCEPTS: float
        """
        ...
    
    def changed(self):
        """
        Call this whenever the mappable is changed so observers can
        update state
        """
        ...
    
    def _make_image(self, A, in_bbox, out_bbox, clip_bbox, magnification=..., unsampled: bool = ..., round_to_pixel_border: bool = ...):
        """
        Normalize, rescale and color the image `A` from the given
        in_bbox (in data space), to the given out_bbox (in pixel
        space) clipped to the given clip_bbox (also in pixel space),
        and magnified by the magnification factor.

        `A` may be a greyscale image (MxN) with a dtype of `float32`,
        `float64`, `uint16` or `uint8`, or an RGBA image (MxNx4) with
        a dtype of `float32`, `float64`, or `uint8`.

        If `unsampled` is True, the image will not be scaled, but an
        appropriate affine transformation will be returned instead.

        If `round_to_pixel_border` is True, the output image size will
        be rounded to the nearest pixel boundary.  This makes the
        images align correctly with the axes.  It should not be used
        in cases where you want exact scaling, however, such as
        FigureImage.

        Returns the resulting (image, x, y, trans), where (x, y) is
        the upper left corner of the result in pixel space, and
        `trans` is the affine transformation from the image to pixel
        space.
        """
        ...
    
    def make_image(self, renderer, magnification=..., unsampled: bool = ...):
        ...
    
    def _draw_unsampled_image(self, renderer, gc):
        """
        draw unsampled image. The renderer should support a draw_image method
        with scale parameter.
        """
        ...
    
    def _check_unsampled_image(self, renderer):
        """
        return True if the image is better to be drawn unsampled.
        The derived class needs to override it.
        """
        ...
    
    @allow_rasterization
    def draw(self, renderer, *args, **kwargs):
        self.stale = ...
    
    def contains(self, mouseevent):
        """
        Test whether the mouse event occurred within the image.
        """
        ...
    
    def write_png(self, fname):
        """Write the image to png file with fname"""
        ...
    
    def set_data(self, A):
        """
        Set the image array.

        ACCEPTS: numpy/PIL Image A

        Note that this function does *not* update the normalization used.
        """
        self.stale = ...
    
    def set_array(self, A):
        """
        Retained for backwards compatibility - use set_data instead

        ACCEPTS: numpy array A or PIL Image
        """
        ...
    
    def get_interpolation(self):
        """
        Return the interpolation method the image uses when resizing.

        One of 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36',
        'hanning', 'hamming', 'hermite', 'kaiser', 'quadric', 'catrom',
        'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos', or 'none'.

        """
        ...
    
    def set_interpolation(self, s):
        """
        Set the interpolation method the image uses when resizing.

        if None, use a value from rc setting. If 'none', the image is
        shown as is without interpolating. 'none' is only supported in
        agg, ps and pdf backends and will fall back to 'nearest' mode
        for other backends.

        .. ACCEPTS: ['nearest' | 'bilinear' | 'bicubic' | 'spline16' |
           'spline36' | 'hanning' | 'hamming' | 'hermite' | 'kaiser' |
           'quadric' | 'catrom' | 'gaussian' | 'bessel' | 'mitchell' |
           'sinc' | 'lanczos' | 'none' ]

        """
        self.stale = ...
    
    def can_composite(self):
        """
        Returns `True` if the image can be composited with its neighbors.
        """
        ...
    
    def set_resample(self, v):
        """
        Set whether or not image resampling is used.

        ACCEPTS: True|False
        """
        self.stale = ...
    
    def get_resample(self):
        """Return the image resample boolean."""
        ...
    
    def set_filternorm(self, filternorm):
        """
        Set whether the resize filter norms the weights -- see
        help for imshow

        ACCEPTS: 0 or 1
        """
        self.stale = ...
    
    def get_filternorm(self):
        """Return the filternorm setting."""
        ...
    
    def set_filterrad(self, filterrad):
        """
        Set the resize filter radius only applicable to some
        interpolation schemes -- see help for imshow

        ACCEPTS: positive float
        """
        self.stale = ...
    
    def get_filterrad(self):
        """Return the filterrad setting."""
        ...
    


class AxesImage(_ImageBase):
    def __str__(self):
        ...
    
    def __init__(self, ax, cmap: Optional[Any] = ..., norm: Optional[Any] = ..., interpolation: Optional[Any] = ..., origin: Optional[Any] = ..., extent: Optional[Any] = ..., filternorm=..., filterrad=..., resample: bool = ..., **kwargs):
        """
        interpolation and cmap default to their rc settings

        cmap is a colors.Colormap instance
        norm is a colors.Normalize instance to map luminance to 0-1

        extent is data axes (left, right, bottom, top) for making image plots
        registered with data plots.  Default is to label the pixel
        centers with the zero-based row and column indices.

        Additional kwargs are matplotlib.artist properties

        """
        ...
    
    def get_window_extent(self, renderer: Optional[Any] = ...):
        ...
    
    def make_image(self, renderer, magnification=..., unsampled: bool = ...):
        ...
    
    def _check_unsampled_image(self, renderer):
        """
        Return whether the image would be better drawn unsampled.
        """
        ...
    
    def set_extent(self, extent):
        """
        extent is data axes (left, right, bottom, top) for making image plots

        This updates ax.dataLim, and, if autoscaling, sets viewLim
        to tightly fit the image, regardless of dataLim.  Autoscaling
        state is not changed, so following this with ax.autoscale_view
        will redo the autoscaling in accord with dataLim.
        """
        self.stale = ...
    
    def get_extent(self):
        """Get the image extent: left, right, bottom, top"""
        ...
    
    def get_cursor_data(self, event):
        """Get the cursor data for a given event"""
        ...
    


class NonUniformImage(AxesImage):
    def __init__(self, ax, **kwargs):
        """
        kwargs are identical to those for AxesImage, except
        that 'nearest' and 'bilinear' are the only supported 'interpolation'
        options.
        """
        ...
    
    def _check_unsampled_image(self, renderer):
        """
        return False. Do not use unsampled image.
        """
        ...
    
    def make_image(self, renderer, magnification=..., unsampled: bool = ...):
        ...
    
    def set_data(self, x, y, A):
        """
        Set the grid for the pixel centers, and the pixel values.

          *x* and *y* are monotonic 1-D ndarrays of lengths N and M,
             respectively, specifying pixel centers

          *A* is an (M,N) ndarray or masked array of values to be
            colormapped, or a (M,N,3) RGB array, or a (M,N,4) RGBA
            array.
        """
        self.stale = ...
    
    def set_array(self, *args):
        ...
    
    def set_interpolation(self, s):
        """
        Parameters
        ----------
        s : str, None
            Either 'nearest', 'bilinear', or ``None``.
        """
        ...
    
    def get_extent(self):
        ...
    
    def set_filternorm(self, s):
        ...
    
    def set_filterrad(self, s):
        ...
    
    def set_norm(self, norm):
        ...
    
    def set_cmap(self, cmap):
        ...
    


class PcolorImage(AxesImage):
    """
    Make a pcolor-style plot with an irregular rectangular grid.

    This uses a variation of the original irregular image code,
    and it is used by pcolorfast for the corresponding grid type.
    """
    def __init__(self, ax, x: Optional[Any] = ..., y: Optional[Any] = ..., A: Optional[Any] = ..., cmap: Optional[Any] = ..., norm: Optional[Any] = ..., **kwargs):
        """
        cmap defaults to its rc setting

        cmap is a colors.Colormap instance
        norm is a colors.Normalize instance to map luminance to 0-1

        Additional kwargs are matplotlib.artist properties
        """
        ...
    
    def make_image(self, renderer, magnification=..., unsampled: bool = ...):
        ...
    
    def _check_unsampled_image(self, renderer):
        ...
    
    def set_data(self, x, y, A):
        """
        Set the grid for the rectangle boundaries, and the data values.

          *x* and *y* are monotonic 1-D ndarrays of lengths N+1 and M+1,
             respectively, specifying rectangle boundaries.  If None,
             they will be created as uniform arrays from 0 through N
             and 0 through M, respectively.

          *A* is an (M,N) ndarray or masked array of values to be
            colormapped, or a (M,N,3) RGB array, or a (M,N,4) RGBA
            array.

        """
        self.is_grayscale = ...
        self.stale = ...
    
    def set_array(self, *args):
        ...
    
    def get_cursor_data(self, event):
        """Get the cursor data for a given event"""
        ...
    


class FigureImage(_ImageBase):
    zorder = ...
    _interpolation = ...
    def __init__(self, fig, cmap: Optional[Any] = ..., norm: Optional[Any] = ..., offsetx=..., offsety=..., origin: Optional[Any] = ..., **kwargs):
        """
        cmap is a colors.Colormap instance
        norm is a colors.Normalize instance to map luminance to 0-1

        kwargs are an optional list of Artist keyword args
        """
        self.figure = ...
        self.ox = ...
        self.oy = ...
        self.magnification = ...
    
    def get_extent(self):
        """Get the image extent: left, right, bottom, top"""
        ...
    
    def make_image(self, renderer, magnification=..., unsampled: bool = ...):
        ...
    
    def set_data(self, A):
        """Set the image array."""
        self.stale = ...
    


class BboxImage(_ImageBase):
    """The Image class whose size is determined by the given bbox."""
    def __init__(self, bbox, cmap: Optional[Any] = ..., norm: Optional[Any] = ..., interpolation: Optional[Any] = ..., origin: Optional[Any] = ..., filternorm=..., filterrad=..., resample: bool = ..., interp_at_native: bool = ..., **kwargs):
        """
        cmap is a colors.Colormap instance
        norm is a colors.Normalize instance to map luminance to 0-1

        interp_at_native is a flag that determines whether or not
        interpolation should still be applied when the image is
        displayed at its native resolution.  A common use case for this
        is when displaying an image for annotational purposes; it is
        treated similarly to Photoshop (interpolation is only used when
        displaying the image at non-native resolutions).


        kwargs are an optional list of Artist keyword args

        """
        self.bbox = ...
        self.interp_at_native = ...
    
    def get_transform(self):
        ...
    
    def get_window_extent(self, renderer: Optional[Any] = ...):
        ...
    
    def contains(self, mouseevent):
        """Test whether the mouse event occurred within the image."""
        ...
    
    def make_image(self, renderer, magnification=..., unsampled: bool = ...):
        ...
    


def imread(fname, format: Optional[Any] = ...):
    """
    Read an image from a file into an array.

    *fname* may be a string path, a valid URL, or a Python
    file-like object.  If using a file object, it must be opened in binary
    mode.

    If *format* is provided, will try to read file of that type,
    otherwise the format is deduced from the filename.  If nothing can
    be deduced, PNG is tried.

    Return value is a :class:`numpy.array`.  For grayscale images, the
    return array is MxN.  For RGB images, the return value is MxNx3.
    For RGBA images the return value is MxNx4.

    matplotlib can only read PNGs natively, but if `PIL
    <http://www.pythonware.com/products/pil/>`_ is installed, it will
    use it to load the image and return an array (if possible) which
    can be used with :func:`~matplotlib.pyplot.imshow`. Note, URL strings
    may not be compatible with PIL. Check the PIL documentation for more
    information.
    """
    ...

def imsave(fname, arr, vmin: Optional[Any] = ..., vmax: Optional[Any] = ..., cmap: Optional[Any] = ..., format: Optional[Any] = ..., origin: Optional[Any] = ..., dpi=...):
    """
    Save an array as in image file.

    The output formats available depend on the backend being used.

    Parameters
    ----------
    fname : str or file-like
        Path string to a filename, or a Python file-like object.
        If *format* is *None* and *fname* is a string, the output
        format is deduced from the extension of the filename.
    arr : array-like
        An MxN (luminance), MxNx3 (RGB) or MxNx4 (RGBA) array.
    vmin, vmax: [ None | scalar ]
        *vmin* and *vmax* set the color scaling for the image by fixing the
        values that map to the colormap color limits. If either *vmin*
        or *vmax* is None, that limit is determined from the *arr*
        min/max value.
    cmap : matplotlib.colors.Colormap, optional
        For example, ``cm.viridis``.  If ``None``, defaults to the
        ``image.cmap`` rcParam.
    format : str
        One of the file extensions supported by the active backend.  Most
        backends support png, pdf, ps, eps and svg.
    origin : [ 'upper' | 'lower' ]
        Indicates whether the ``(0, 0)`` index of the array is in the
        upper left or lower left corner of the axes.  Defaults to the
        ``image.origin`` rcParam.
    dpi : int
        The DPI to store in the metadata of the file.  This does not affect the
        resolution of the output image.
    """
    ...

def pil_to_array(pilImage):
    """Load a PIL image and return it as a numpy array.

    Grayscale images are returned as ``(M, N)`` arrays.  RGB images are
    returned as ``(M, N, 3)`` arrays.  RGBA images are returned as ``(M, N,
    4)`` arrays.
    """
    ...

def thumbnail(infile, thumbfile, scale=..., interpolation=..., preview: bool = ...):
    """
    make a thumbnail of image in *infile* with output filename
    *thumbfile*.

      *infile* the image file -- must be PNG or Pillow-readable if you
         have `Pillow <http://python-pillow.org/>`_ installed

      *thumbfile*
        the thumbnail filename

      *scale*
        the scale factor for the thumbnail

      *interpolation*
        the interpolation scheme used in the resampling


      *preview*
        if True, the default backend (presumably a user interface
        backend) will be used which will cause a figure to be raised
        if :func:`~matplotlib.pyplot.show` is called.  If it is False,
        a pure image backend will be used depending on the extension,
        'png'->FigureCanvasAgg, 'pdf'->FigureCanvasPdf,
        'svg'->FigureCanvasSVG


    See examples/misc/image_thumbnail.py.

    .. htmlonly::

        :ref:`sphx_glr_gallery_misc_image_thumbnail_sgskip.py`

    Return value is the figure instance containing the thumbnail

    """
    ...

