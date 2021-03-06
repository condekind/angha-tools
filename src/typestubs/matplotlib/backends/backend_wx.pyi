"""
This type stub file was generated by pyright.
"""

import wx
from matplotlib.backend_bases import FigureCanvasBase, FigureManagerBase, GraphicsContextBase, NavigationToolbar2, RendererBase, TimerBase, _Backend, _has_pil, cursors
from matplotlib import backend_tools, cbook
from typing import Any, Optional

"""
 A wxPython backend for matplotlib, based (very heavily) on
 backend_template.py and backend_gtk.py

 Author: Jeremy O'Donoghue (jeremy@o-donoghue.com)

 Derived from original copyright work by John Hunter
 (jdhunter@ace.bsd.uchicago.edu)

 Copyright (C) Jeremy O'Donoghue & John Hunter, 2003-4

 License: This work is licensed under a PSF compatible license. A copy
 should be included with this source code.

"""
_DEBUG = 5
if _DEBUG < 5:
    ...
_DEBUG_lvls = { 1: 'Low ',2: 'Med ',3: 'High',4: 'Error' }
def DEBUG_MSG(string, lvl=..., o: Optional[Any] = ...):
    ...

def debug_on_error(type, value, tb):
    """Code due to Thomas Heller - published in Python Cookbook (O'Reilley)"""
    ...

class fake_stderr(object):
    """
    Wx does strange things with stderr, as it makes the assumption that
    there is probably no console. This redirects stderr to the console, since
    we know that there is one!
    """
    def write(self, msg):
        ...
    


PIXELS_PER_INCH = 75
IDLE_DELAY = 5
def error_msg_wx(msg, parent: Optional[Any] = ...):
    """
    Signal an error condition -- in a GUI, popup a error dialog
    """
    ...

def raise_msg_to_str(msg):
    """msg is a return arg from a raise.  Join with new lines."""
    ...

class TimerWx(TimerBase):
    '''
    Subclass of :class:`backend_bases.TimerBase` that uses WxTimer events.

    Attributes
    ----------
    interval : int
        The time between timer events in milliseconds. Default is 1000 ms.
    single_shot : bool
        Boolean flag indicating whether this timer should operate as single
        shot (run once and then stop). Defaults to False.
    callbacks : list
        Stores list of (func, args) tuples that will be called upon timer
        events. This list can be manipulated directly, or the functions
        `add_callback` and `remove_callback` can be used.

    '''
    def __init__(self, parent, *args, **kwargs):
        self.parent = ...
    
    def _timer_start(self):
        ...
    
    def _timer_stop(self):
        ...
    
    def _timer_set_interval(self):
        ...
    
    def _timer_set_single_shot(self):
        ...
    
    def _on_timer(self, *args):
        ...
    


class RendererWx(RendererBase):
    """
    The renderer handles all the drawing primitives using a graphics
    context instance that controls the colors/styles. It acts as the
    'renderer' instance used by many classes in the hierarchy.
    """
    fontweights = ...
    fontangles = ...
    fontnames = ...
    def __init__(self, bitmap, dpi):
        """
        Initialise a wxWindows renderer instance.
        """
        self.width = ...
        self.height = ...
        self.bitmap = ...
        self.fontd = ...
        self.dpi = ...
        self.gc = ...
    
    def flipy(self):
        ...
    
    def offset_text_height(self):
        ...
    
    def get_text_width_height_descent(self, s, prop, ismath):
        """
        get the width and height in display coords of the string s
        with FontPropertry prop
        """
        ...
    
    def get_canvas_width_height(self):
        'return the canvas width and height in display coords'
        ...
    
    def handle_clip_rectangle(self, gc):
        ...
    
    @staticmethod
    def convert_path(gfx_ctx, path, transform):
        ...
    
    def draw_path(self, gc, path, transform, rgbFace: Optional[Any] = ...):
        ...
    
    def draw_image(self, gc, x, y, im):
        ...
    
    def draw_text(self, gc, x, y, s, prop, angle, ismath: bool = ..., mtext: Optional[Any] = ...):
        ...
    
    def new_gc(self):
        """
        Return an instance of a GraphicsContextWx, and sets the current gc copy
        """
        self.gc = ...
    
    def get_gc(self):
        """
        Fetch the locally cached gc.
        """
        ...
    
    def get_wx_font(self, s, prop):
        """
        Return a wx font.  Cache instances in a font dictionary for
        efficiency
        """
        ...
    
    def points_to_pixels(self, points):
        """
        convert point measures to pixes using dpi and the pixels per
        inch of the display
        """
        ...
    


class GraphicsContextWx(GraphicsContextBase):
    """
    The graphics context provides the color, line styles, etc...

    This class stores a reference to a wxMemoryDC, and a
    wxGraphicsContext that draws to it.  Creating a wxGraphicsContext
    seems to be fairly heavy, so these objects are cached based on the
    bitmap object that is passed in.

    The base GraphicsContext stores colors as a RGB tuple on the unit
    interval, e.g., (0.5, 0.0, 1.0).  wxPython uses an int interval, but
    since wxPython colour management is rather simple, I have not chosen
    to implement a separate colour manager class.
    """
    _capd = ...
    _joind = ...
    _cache = ...
    def __init__(self, bitmap, renderer):
        self.bitmap = ...
        self.dc = ...
        self.gfx_ctx = ...
        self.renderer = ...
    
    def select(self):
        """
        Select the current bitmap into this wxDC instance
        """
        ...
    
    def unselect(self):
        """
        Select a Null bitmasp into this wxDC instance
        """
        ...
    
    def set_foreground(self, fg, isRGBA: Optional[Any] = ...):
        """
        Set the foreground color.  fg can be a matlab format string, a
        html hex color string, an rgb unit tuple, or a float between 0
        and 1.  In the latter case, grayscale is used.
        """
        ...
    
    def set_linewidth(self, w):
        """
        Set the line width.
        """
        ...
    
    def set_capstyle(self, cs):
        """
        Set the capstyle as a string in ('butt', 'round', 'projecting')
        """
        ...
    
    def set_joinstyle(self, js):
        """
        Set the join style to be one of ('miter', 'round', 'bevel')
        """
        ...
    
    @cbook.deprecated("2.1")
    def set_linestyle(self, ls):
        """
        Set the line style to be one of
        """
        ...
    
    def get_wxcolour(self, color):
        """return a wx.Colour from RGB format"""
        ...
    


class _FigureCanvasWxBase(FigureCanvasBase, wx.Panel):
    """
    The FigureCanvas contains the figure and does event handling.

    In the wxPython backend, it is derived from wxPanel, and (usually) lives
    inside a frame instantiated by a FigureManagerWx. The parent window
    probably implements a wx.Sizer to control the displayed control size - but
    we give a hint as to our preferred minimum size.
    """
    keyvald = ...
    def __init__(self, parent, id, figure):
        """
        Initialise a FigureWx instance.

        - Initialise the FigureCanvasBase and wxPanel parents.
        - Set event handlers for:
          EVT_SIZE  (Resize event)
          EVT_PAINT (Paint event)
        """
        self.bitmap = ...
        self.macros = ...
    
    def Destroy(self, *args, **kwargs):
        ...
    
    def Copy_to_Clipboard(self, event: Optional[Any] = ...):
        "copy bitmap of canvas to system clipboard"
        ...
    
    def draw_idle(self):
        """
        Delay rendering until the GUI is idle.
        """
        ...
    
    def new_timer(self, *args, **kwargs):
        """
        Creates a new backend-specific subclass of
        :class:`backend_bases.Timer`. This is useful for getting periodic
        events through the backend's native event loop. Implemented only
        for backends with GUIs.

        Other Parameters
        ----------------
        interval : scalar
            Timer interval in milliseconds
        callbacks : list
            Sequence of (func, args, kwargs) where ``func(*args, **kwargs)``
            will be executed by the timer every *interval*.

        """
        ...
    
    def flush_events(self):
        ...
    
    def start_event_loop(self, timeout=...):
        """
        Start an event loop.  This is used to start a blocking event
        loop so that interactive functions, such as ginput and
        waitforbuttonpress, can wait for events.  This should not be
        confused with the main GUI event loop, which is always running
        and has nothing to do with this.

        This call blocks until a callback function triggers
        stop_event_loop() or *timeout* is reached.  If *timeout* is
        <=0, never timeout.

        Raises RuntimeError if event loop is already running.
        """
        ...
    
    def stop_event_loop(self, event: Optional[Any] = ...):
        """
        Stop an event loop.  This is used to stop a blocking event
        loop so that interactive functions, such as ginput and
        waitforbuttonpress, can wait for events.

        """
        ...
    
    def _get_imagesave_wildcards(self):
        'return the wildcard string for the filesave dialog'
        ...
    
    def gui_repaint(self, drawDC: Optional[Any] = ..., origin=...):
        """
        Performs update of the displayed image on the GUI canvas, using the
        supplied wx.PaintDC device context.

        The 'WXAgg' backend sets origin accordingly.
        """
        ...
    
    filetypes = ...
    def print_figure(self, filename, *args, **kwargs):
        ...
    
    def _onPaint(self, evt):
        """
        Called when wxPaintEvt is generated
        """
        ...
    
    def _onSize(self, evt):
        """
        Called when wxEventSize is generated.

        In this application we attempt to resize to fit the window, so it
        is better to take the performance hit and redraw the whole window.
        """
        self.bitmap = ...
    
    def _get_key(self, evt):
        ...
    
    def _onKeyDown(self, evt):
        """Capture key press."""
        ...
    
    def _onKeyUp(self, evt):
        """Release key."""
        ...
    
    def _set_capture(self, capture: bool = ...):
        """control wx mouse capture """
        ...
    
    def _onCaptureLost(self, evt):
        """Capture changed or lost"""
        ...
    
    def _onRightButtonDown(self, evt):
        """Start measuring on an axis."""
        ...
    
    def _onRightButtonDClick(self, evt):
        """Start measuring on an axis."""
        ...
    
    def _onRightButtonUp(self, evt):
        """End measuring on an axis."""
        ...
    
    def _onLeftButtonDown(self, evt):
        """Start measuring on an axis."""
        ...
    
    def _onLeftButtonDClick(self, evt):
        """Start measuring on an axis."""
        ...
    
    def _onLeftButtonUp(self, evt):
        """End measuring on an axis."""
        ...
    
    def _onMiddleButtonDown(self, evt):
        """Start measuring on an axis."""
        ...
    
    def _onMiddleButtonDClick(self, evt):
        """Start measuring on an axis."""
        ...
    
    def _onMiddleButtonUp(self, evt):
        """End measuring on an axis."""
        ...
    
    def _onMouseWheel(self, evt):
        """Translate mouse wheel events into matplotlib events"""
        ...
    
    def _onMotion(self, evt):
        """Start measuring on an axis."""
        ...
    
    def _onLeave(self, evt):
        """Mouse has left the window."""
        ...
    
    def _onEnter(self, evt):
        """Mouse has entered the window."""
        ...
    


class FigureCanvasWx(_FigureCanvasWxBase):
    def draw(self, drawDC: Optional[Any] = ...):
        """
        Render the figure using RendererWx instance renderer, or using a
        previously defined renderer if none is specified.
        """
        self.renderer = ...
    
    def print_bmp(self, filename, *args, **kwargs):
        ...
    
    if not _has_pil:
        def print_jpeg(self, filename, *args, **kwargs):
            ...
        
        print_jpg = ...
    def print_pcx(self, filename, *args, **kwargs):
        ...
    
    def print_png(self, filename, *args, **kwargs):
        ...
    
    if not _has_pil:
        def print_tiff(self, filename, *args, **kwargs):
            ...
        
        print_tif = ...
    def print_xpm(self, filename, *args, **kwargs):
        ...
    
    def _print_image(self, filename, filetype, *args, **kwargs):
        self.bitmap = ...
        self.bitmap = ...
    


class FigureFrameWx(wx.Frame):
    def __init__(self, num, fig):
        self.num = ...
        self.canvas = ...
        self.sizer = ...
        self.toolbar = ...
        self.figmgr = ...
    
    def _get_toolbar(self, statbar):
        ...
    
    def get_canvas(self, fig):
        ...
    
    def get_figure_manager(self):
        ...
    
    def _onClose(self, evt):
        ...
    
    def GetToolBar(self):
        """Override wxFrame::GetToolBar as we don't have managed toolbar"""
        ...
    
    def Destroy(self, *args, **kwargs):
        ...
    


class FigureManagerWx(FigureManagerBase):
    """
    This class contains the FigureCanvas and GUI frame

    It is instantiated by GcfWx whenever a new figure is created. GcfWx is
    responsible for managing multiple instances of FigureManagerWx.

    Attributes
    ----------
    canvas : `FigureCanvas`
        a FigureCanvasWx(wx.Panel) instance
    window : wxFrame
        a wxFrame instance - wxpython.org/Phoenix/docs/html/Frame.html

    """
    def __init__(self, canvas, num, frame):
        self.frame = ...
        self.window = ...
        self.tb = ...
        self.toolbar = ...
    
    def show(self):
        ...
    
    def destroy(self, *args):
        ...
    
    def get_window_title(self):
        ...
    
    def set_window_title(self, title):
        ...
    
    def resize(self, width, height):
        'Set the canvas size in pixels'
        ...
    


_NTB_AXISMENU = wx.NewId()
_NTB_AXISMENU_BUTTON = wx.NewId()
_NTB_X_PAN_LEFT = wx.NewId()
_NTB_X_PAN_RIGHT = wx.NewId()
_NTB_X_ZOOMIN = wx.NewId()
_NTB_X_ZOOMOUT = wx.NewId()
_NTB_Y_PAN_UP = wx.NewId()
_NTB_Y_PAN_DOWN = wx.NewId()
_NTB_Y_ZOOMIN = wx.NewId()
_NTB_Y_ZOOMOUT = wx.NewId()
_NTB_SAVE = wx.NewId()
_NTB_CLOSE = wx.NewId()
def _load_bitmap(filename):
    """
    Load a bitmap file from the backends/images subdirectory in which the
    matplotlib library is installed. The filename parameter should not
    contain any path information as this is determined automatically.

    Returns a wx.Bitmap object
    """
    ...

class MenuButtonWx(wx.Button):
    """
    wxPython does not permit a menu to be incorporated directly into a toolbar.
    This class simulates the effect by associating a pop-up menu with a button
    in the toolbar, and managing this as though it were a menu.
    """
    def __init__(self, parent):
        ...
    
    def Destroy(self):
        ...
    
    def _onMenuButton(self, evt):
        """Handle menu button pressed."""
        ...
    
    def _handleSelectAllAxes(self, evt):
        """Called when the 'select all axes' menu item is selected."""
        ...
    
    def _handleInvertAxesSelected(self, evt):
        """Called when the invert all menu item is selected"""
        ...
    
    def _onMenuItemSelected(self, evt):
        """Called whenever one of the specific axis menu items is selected"""
        ...
    
    def updateAxes(self, maxAxis):
        """Ensures that there are entries for max_axis axes in the menu
        (selected by default)."""
        ...
    
    def getActiveAxes(self):
        """Return a list of the selected axes."""
        ...
    
    def updateButtonText(self, lst):
        """Update the list of selected axes in the menu button."""
        ...
    


cursord = { cursors.MOVE: wx.CURSOR_HAND,cursors.HAND: wx.CURSOR_HAND,cursors.POINTER: wx.CURSOR_ARROW,cursors.SELECT_REGION: wx.CURSOR_CROSS,cursors.WAIT: wx.CURSOR_WAIT }
@cbook.deprecated("2.2")
class SubplotToolWX(wx.Frame):
    def __init__(self, targetfig):
        ...
    


class NavigationToolbar2Wx(NavigationToolbar2, wx.ToolBar):
    def __init__(self, canvas):
        self.canvas = ...
        self.statbar = ...
        self.prevZoomRect = ...
        self.retinaFix = ...
    
    def get_canvas(self, frame, fig):
        ...
    
    def _init_toolbar(self):
        self.wx_ids = ...
    
    def zoom(self, *args):
        ...
    
    def pan(self, *args):
        ...
    
    def configure_subplots(self, evt):
        ...
    
    def save_figure(self, *args):
        ...
    
    def set_cursor(self, cursor):
        ...
    
    @cbook.deprecated("2.1", alternative="canvas.draw_idle")
    def dynamic_update(self):
        ...
    
    def press(self, event):
        ...
    
    def release(self, event):
        ...
    
    def draw_rubberband(self, event, x0, y0, x1, y1):
        ...
    
    def set_status_bar(self, statbar):
        self.statbar = ...
    
    def set_message(self, s):
        ...
    
    def set_history_buttons(self):
        ...
    


@cbook.deprecated("2.2", alternative="NavigationToolbar2Wx")
class Toolbar(NavigationToolbar2Wx):
    ...


class StatusBarWx(wx.StatusBar):
    """
    A status bar is added to _FigureFrame to allow measurements and the
    previously selected scroll function to be displayed as a user
    convenience.
    """
    def __init__(self, parent):
        ...
    
    def set_function(self, string):
        ...
    


class SaveFigureWx(backend_tools.SaveFigureBase):
    def trigger(self, *args):
        ...
    


class SetCursorWx(backend_tools.SetCursorBase):
    def set_cursor(self, cursor):
        ...
    


if 'wxMac' not in wx.PlatformInfo:
    class RubberbandWx(backend_tools.RubberbandBase):
        def __init__(self, *args, **kwargs):
            self.wxoverlay = ...
        
        def draw_rubberband(self, x0, y0, x1, y1):
            ...
        
        def remove_rubberband(self):
            self.wxoverlay = ...
        
    
    
else:
    class RubberbandWx(backend_tools.RubberbandBase):
        def __init__(self, *args, **kwargs):
            ...
        
        def draw_rubberband(self, x0, y0, x1, y1):
            ...
        
        def remove_rubberband(self, dc: Optional[Any] = ...):
            ...
        
    
    
class PrintoutWx(wx.Printout):
    """
    Simple wrapper around wx Printout class -- all the real work
    here is scaling the matplotlib canvas bitmap to the current
    printer's definition.
    """
    def __init__(self, canvas, width=..., margin=..., title=...):
        self.canvas = ...
        self.width = ...
        self.margin = ...
    
    def HasPage(self, page):
        ...
    
    def GetPageInfo(self):
        ...
    
    def OnPrintPage(self, page):
        ...
    


@_Backend.export
class _BackendWx(_Backend):
    FigureCanvas = ...
    FigureManager = ...
    _frame_class = ...
    @staticmethod
    def trigger_manager_draw(manager):
        ...
    
    @classmethod
    def new_figure_manager(cls, num, *args, **kwargs):
        ...
    
    @classmethod
    def new_figure_manager_given_figure(cls, num, figure):
        ...
    
    @staticmethod
    def mainloop():
        ...
    


