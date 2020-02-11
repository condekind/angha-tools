"""
This type stub file was generated by pyright.
"""

from .. import cbook
from .backend_agg import FigureCanvasAgg
from ._backend_tk import FigureCanvasTk, FigureManagerTk, NavigationToolbar2Tk, _BackendTk
from typing import Any, Optional

class FigureCanvasTkAgg(FigureCanvasAgg, FigureCanvasTk):
    def draw(self):
        ...
    
    def blit(self, bbox: Optional[Any] = ...):
        ...
    


@cbook.deprecated("2.2")
class FigureManagerTkAgg(FigureManagerTk):
    ...


@cbook.deprecated("2.2")
class NavigationToolbar2TkAgg(NavigationToolbar2Tk):
    ...


@_BackendTk.export
class _BackendTkAgg(_BackendTk):
    FigureCanvas = ...


