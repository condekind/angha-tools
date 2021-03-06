"""
This type stub file was generated by pyright.
"""

from .backend_cairo import FigureCanvasCairo
from .backend_wx import FigureFrameWx, _BackendWx, _FigureCanvasWxBase
from typing import Any, Optional

class FigureFrameWxCairo(FigureFrameWx):
    def get_canvas(self, fig):
        ...
    


class FigureCanvasWxCairo(_FigureCanvasWxBase, FigureCanvasCairo):
    """
    The FigureCanvas contains the figure and does event handling.

    In the wxPython backend, it is derived from wxPanel, and (usually) lives
    inside a frame instantiated by a FigureManagerWx. The parent window
    probably implements a wxSizer to control the displayed control size - but
    we give a hint as to our preferred minimum size.
    """
    def __init__(self, parent, id, figure):
        ...
    
    def draw(self, drawDC: Optional[Any] = ...):
        self.bitmap = ...
    


@_BackendWx.export
class _BackendWxCairo(_BackendWx):
    FigureCanvas = ...
    _frame_class = ...


