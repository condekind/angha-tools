"""
This type stub file was generated by pyright.
"""

import itertools
import logging
from typing import Any, Optional

"""

Conventions:

"constrain_x" means to constrain the variable with either
another kiwisolver variable, or a float.  i.e. `constrain_width(0.2)`
will set a constraint that the width has to be 0.2 and this constraint is
permanent - i.e. it will not be removed if it becomes obsolete.

"edit_x" means to set x to a value (just a float), and that this value can
change.  So `edit_width(0.2)` will set width to be 0.2, but `edit_width(0.3)`
will allow it to change to 0.3 later.  Note that these values are still just
"suggestions" in `kiwisolver` parlance, and could be over-ridden by
other constrains.

"""
_log = logging.getLogger(__name__)
def get_renderer(fig):
    ...

class LayoutBox(object):
    """
    Basic rectangle representation using kiwi solver variables
    """
    def __init__(self, parent: Optional[Any] = ..., name=..., tightwidth: bool = ..., tightheight: bool = ..., artist: Optional[Any] = ..., lower_left=..., upper_right=..., pos: bool = ..., subplot: bool = ..., h_pad: Optional[Any] = ..., w_pad: Optional[Any] = ...):
        self.parent = ...
        self.name = ...
        self.artist = ...
        self.pos = ...
        self.subplot = ...
        self.top = ...
        self.bottom = ...
        self.left = ...
        self.right = ...
        self.width = ...
        self.height = ...
        self.h_center = ...
        self.v_center = ...
        self.min_width = ...
        self.min_height = ...
        self.pref_width = ...
        self.pref_height = ...
        self.left_margin = ...
        self.right_margin = ...
        self.bottom_margin = ...
        self.top_margin = ...
        self.left_margin_min = ...
        self.right_margin_min = ...
        self.bottom_margin_min = ...
        self.top_margin_min = ...
        self.tightheight = ...
        self.tightwidth = ...
        self.children = ...
        self.subplotspec = ...
        self.h_pad = ...
        self.w_pad = ...
    
    def constrain_margins(self):
        """
        Only do this for pos.  This sets a variable distance
        margin between the position of the axes and the outer edge of
        the axes.

        Margins are variable because they change with the fogure size.

        Margin minimums are set to make room for axes decorations.  However,
        the margins can be larger if we are mathicng the position size to
        otehr axes.
        """
        ...
    
    def add_child(self, child):
        ...
    
    def remove_child(self, child):
        ...
    
    def add_constraints(self):
        ...
    
    def parent_constrain(self):
        ...
    
    def hard_constraints(self):
        ...
    
    def soft_constraints(self):
        ...
    
    def set_parent(self, parent):
        ''' replace the parent of this with the new parent
        '''
        self.parent = ...
    
    def constrain_geometry(self, left, bottom, right, top, strength=...):
        ...
    
    def constrain_same(self, other, strength=...):
        """
        Make the layoutbox have same position as other layoutbox
        """
        ...
    
    def constrain_left_margin(self, margin, strength=...):
        ...
    
    def edit_left_margin_min(self, margin):
        ...
    
    def constrain_right_margin(self, margin, strength=...):
        ...
    
    def edit_right_margin_min(self, margin):
        ...
    
    def constrain_bottom_margin(self, margin, strength=...):
        ...
    
    def edit_bottom_margin_min(self, margin):
        ...
    
    def constrain_top_margin(self, margin, strength=...):
        ...
    
    def edit_top_margin_min(self, margin):
        ...
    
    def get_rect(self):
        ...
    
    def update_variables(self):
        '''
        Update *all* the variables that are part of the solver this LayoutBox
        is created with
        '''
        ...
    
    def edit_height(self, height, strength=...):
        '''
        Set the height of the layout box.

        This is done as an editable variable so that the value can change
        due to resizing.
        '''
        ...
    
    def constrain_height(self, height, strength=...):
        '''
        Constrain the height of the layout box.  height is
        either a float or a layoutbox.height.
        '''
        ...
    
    def constrain_height_min(self, height, strength=...):
        ...
    
    def edit_width(self, width, strength=...):
        ...
    
    def constrain_width(self, width, strength=...):
        '''
        Constrain the width of the layout box.  `width` is
        either a float or a layoutbox.width.
        '''
        ...
    
    def constrain_width_min(self, width, strength=...):
        ...
    
    def constrain_left(self, left, strength=...):
        ...
    
    def constrain_bottom(self, bottom, strength=...):
        ...
    
    def constrain_right(self, right, strength=...):
        ...
    
    def constrain_top(self, top, strength=...):
        ...
    
    def _is_subplotspec_layoutbox(self):
        '''
        Helper to check if this layoutbox is the layoutbox of a
        subplotspec
        '''
        ...
    
    def _is_gridspec_layoutbox(self):
        '''
        Helper to check if this layoutbox is the layoutbox of a
        gridspec
        '''
        ...
    
    def find_child_subplots(self):
        '''
        Find children of this layout box that are subplots.  We want to line
        poss up, and this is an easy way to find them all.
        '''
        ...
    
    def layout_from_subplotspec(self, subspec, name=..., artist: Optional[Any] = ..., pos: bool = ...):
        '''  Make a layout box from a subplotspec. The layout box is
        constrained to be a fraction of the width/height of the parent,
        and be a fraction of the parent width/height from the left/bottom
        of the parent.  Therefore the parent can move around and the
        layout for the subplot spec should move with it.

        The parent is *usually* the gridspec that made the subplotspec.??
        '''
        ...
    
    def __repr__(self):
        ...
    


def hstack(boxes, padding=..., strength=...):
    '''
    Stack LayoutBox instances from left to right.
    `padding` is in figure-relative units.
    '''
    ...

def hpack(boxes, padding=..., strength=...):
    '''
    Stack LayoutBox instances from left to right.
    '''
    ...

def vstack(boxes, padding=..., strength=...):
    '''
    Stack LayoutBox instances from top to bottom
    '''
    ...

def vpack(boxes, padding=..., strength=...):
    '''
    Stack LayoutBox instances from top to bottom
    '''
    ...

def match_heights(boxes, height_ratios: Optional[Any] = ..., strength=...):
    '''
    Stack LayoutBox instances from top to bottom
    '''
    ...

def match_widths(boxes, width_ratios: Optional[Any] = ..., strength=...):
    '''
    Stack LayoutBox instances from top to bottom
    '''
    ...

def vstackeq(boxes, padding=..., height_ratios: Optional[Any] = ...):
    ...

def hstackeq(boxes, padding=..., width_ratios: Optional[Any] = ...):
    ...

def align(boxes, attr, strength=...):
    ...

def match_top_margins(boxes, levels=...):
    ...

def match_bottom_margins(boxes, levels=...):
    ...

def match_left_margins(boxes, levels=...):
    ...

def match_right_margins(boxes, levels=...):
    ...

def match_width_margins(boxes, levels=...):
    ...

def match_height_margins(boxes, levels=...):
    ...

def match_margins(boxes, levels=...):
    ...

_layoutboxobjnum = itertools.count()
def seq_id():
    '''
    Generate a short sequential id for layoutbox objects...
    '''
    ...

def print_children(lb):
    '''
    Print the children of the layoutbox
    '''
    ...

def nonetree(lb):
    '''
    Make all elements in this tree none...  This signals not to do any more
    layout.
    '''
    ...

def nonechildren(lb):
    ...

def print_tree(lb):
    '''
    Print the tree of layoutboxes
    '''
    ...

def plot_children(fig, box, level=..., printit: bool = ...):
    '''
    Simple plotting to show where boxes are
    '''
    ...

