"""
This type stub file was generated by pyright.
"""

import re
import sys
from matplotlib.backend_bases import FigureCanvasBase, FigureManagerBase, GraphicsContextBase, RendererBase, _Backend
from typing import Any, Optional

system_fonts = []
if sys.platform.startswith('win'):
    ...
else:
    ...
def get_texcommand():
    """Get chosen TeX system from rc."""
    ...

def get_fontspec():
    """Build fontspec preamble from rc."""
    ...

def get_preamble():
    """Get LaTeX preamble from rc."""
    ...

latex_pt_to_in = 1 / 72.27
latex_in_to_pt = 1 / latex_pt_to_in
mpl_pt_to_in = 1 / 72
mpl_in_to_pt = 1 / mpl_pt_to_in
NO_ESCAPE = r"(?<!\\)(?:\\\\)*"
re_mathsep = re.compile(NO_ESCAPE + r"\$")
re_escapetext = re.compile(NO_ESCAPE + "([_^$%])")
repl_escapetext = lambda m: "\\" + m.group(1)
re_mathdefault = re.compile(NO_ESCAPE + r"(\\mathdefault)")
repl_mathdefault = lambda m: m.group(0)[: - len(m.group(1))]
def common_texification(text):
    """
    Do some necessary and/or useful substitutions for texts to be included in
    LaTeX documents.
    """
    ...

def writeln(fh, line):
    ...

def _font_properties_str(prop):
    ...

def make_pdf_to_png_converter():
    """
    Returns a function that converts a pdf file to a png file.
    """
    ...

class LatexError(Exception):
    def __init__(self, message, latex_output=...):
        self.latex_output = ...
    


class LatexManagerFactory(object):
    previous_instance = ...
    @staticmethod
    def get_latex_manager():
        ...
    


class LatexManager(object):
    """
    The LatexManager opens an instance of the LaTeX application for
    determining the metrics of text elements. The LaTeX environment can be
    modified by setting fonts and/or a custem preamble in the rc parameters.
    """
    _unclean_instances = ...
    @staticmethod
    def _build_latex_header():
        ...
    
    @staticmethod
    def _cleanup_remaining_instances():
        ...
    
    def _stdin_writeln(self, s):
        ...
    
    def _expect(self, s):
        ...
    
    def _expect_prompt(self):
        ...
    
    def __init__(self):
        self.tmpdir = ...
        self.texcommand = ...
        self.latex_header = ...
        self.latex = ...
        self.latex_stdin_utf8 = ...
        self.str_cache = ...
    
    def _cleanup(self):
        ...
    
    def __del__(self):
        ...
    
    def get_width_height_descent(self, text, prop):
        """
        Get the width, total height and descent for a text typesetted by the
        current LaTeX environment.
        """
        ...
    


class RendererPgf(RendererBase):
    def __init__(self, figure, fh, dummy: bool = ...):
        """
        Creates a new PGF renderer that translates any drawing instruction
        into text commands to be interpreted in a latex pgfpicture environment.

        Attributes
        ----------
        figure : `matplotlib.figure.Figure`
            Matplotlib figure to initialize height, width and dpi from.
        fh : file-like
            File handle for the output of the drawing commands.

        """
        self.dpi = ...
        self.fh = ...
        self.figure = ...
        self.image_counter = ...
        self.latexManager = ...
    
    def draw_markers(self, gc, marker_path, marker_trans, path, trans, rgbFace: Optional[Any] = ...):
        ...
    
    def draw_path(self, gc, path, transform, rgbFace: Optional[Any] = ...):
        ...
    
    def _print_pgf_clip(self, gc):
        ...
    
    def _print_pgf_path_styles(self, gc, rgbFace):
        ...
    
    def _print_pgf_path(self, gc, path, transform, rgbFace: Optional[Any] = ...):
        ...
    
    def _pgf_path_draw(self, stroke: bool = ..., fill: bool = ...):
        ...
    
    def option_scale_image(self):
        """
        pgf backend supports affine transform of image.
        """
        ...
    
    def option_image_nocomposite(self):
        """
        return whether to generate a composite image from multiple images on
        a set of axes
        """
        ...
    
    def draw_image(self, gc, x, y, im, transform: Optional[Any] = ...):
        ...
    
    def draw_tex(self, gc, x, y, s, prop, angle, ismath=..., mtext: Optional[Any] = ...):
        ...
    
    def draw_text(self, gc, x, y, s, prop, angle, ismath: bool = ..., mtext: Optional[Any] = ...):
        ...
    
    def get_text_width_height_descent(self, s, prop, ismath):
        ...
    
    def flipy(self):
        ...
    
    def get_canvas_width_height(self):
        ...
    
    def points_to_pixels(self, points):
        ...
    
    def new_gc(self):
        ...
    


class GraphicsContextPgf(GraphicsContextBase):
    ...


class TmpDirCleaner(object):
    remaining_tmpdirs = ...
    @staticmethod
    def add(tmpdir):
        ...
    
    @staticmethod
    def cleanup_remaining_tmpdirs():
        ...
    


class FigureCanvasPgf(FigureCanvasBase):
    filetypes = ...
    def get_default_filetype(self):
        ...
    
    def _print_pgf_to_fh(self, fh, *args, **kwargs):
        ...
    
    def print_pgf(self, fname_or_fh, *args, **kwargs):
        """
        Output pgf commands for drawing the figure so it can be included and
        rendered in latex documents.
        """
        ...
    
    def _print_pdf_to_fh(self, fh, *args, **kwargs):
        ...
    
    def print_pdf(self, fname_or_fh, *args, **kwargs):
        """
        Use LaTeX to compile a Pgf generated figure to PDF.
        """
        ...
    
    def _print_png_to_fh(self, fh, *args, **kwargs):
        ...
    
    def print_png(self, fname_or_fh, *args, **kwargs):
        """
        Use LaTeX to compile a pgf figure to pdf and convert it to png.
        """
        ...
    
    def get_renderer(self):
        ...
    


class FigureManagerPgf(FigureManagerBase):
    def __init__(self, *args):
        ...
    


@_Backend.export
class _BackendPgf(_Backend):
    FigureCanvas = ...
    FigureManager = ...


def _cleanup_all():
    ...

