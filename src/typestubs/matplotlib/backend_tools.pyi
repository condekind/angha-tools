"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""
Abstract base classes define the primitives for Tools.
These tools are used by `matplotlib.backend_managers.ToolManager`

:class:`ToolBase`
    Simple stateless tool

:class:`ToolToggleBase`
    Tool that has two states, only one Toggle tool can be
    active at any given time for the same
    `matplotlib.backend_managers.ToolManager`
"""
class Cursors(object):
    """Simple namespace for cursor reference"""
    ...


cursors = Cursors()
_views_positions = 'viewpos'
class ToolBase(object):
    """
    Base tool class

    A base tool, only implements `trigger` method or not method at all.
    The tool is instantiated by `matplotlib.backend_managers.ToolManager`

    Attributes
    ----------
    toolmanager: `matplotlib.backend_managers.ToolManager`
        ToolManager that controls this Tool
    figure: `FigureCanvas`
        Figure instance that is affected by this Tool
    name: String
        Used as **Id** of the tool, has to be unique among tools of the same
        ToolManager
    """
    default_keymap = ...
    description = ...
    image = ...
    def __init__(self, toolmanager, name):
        ...
    
    @property
    def figure(self):
        ...
    
    @figure.setter
    def figure(self, figure):
        ...
    
    @property
    def canvas(self):
        ...
    
    @property
    def toolmanager(self):
        ...
    
    def set_figure(self, figure):
        """
        Assign a figure to the tool

        Parameters
        ----------
        figure: `Figure`
        """
        ...
    
    def trigger(self, sender, event, data: Optional[Any] = ...):
        """
        Called when this tool gets used

        This method is called by
        `matplotlib.backend_managers.ToolManager.trigger_tool`

        Parameters
        ----------
        event: `Event`
            The Canvas event that caused this tool to be called
        sender: object
            Object that requested the tool to be triggered
        data: object
            Extra data
        """
        ...
    
    @property
    def name(self):
        """Tool Id"""
        ...
    
    def destroy(self):
        """
        Destroy the tool

        This method is called when the tool is removed by
        `matplotlib.backend_managers.ToolManager.remove_tool`
        """
        ...
    


class ToolToggleBase(ToolBase):
    """
    Toggleable tool

    Every time it is triggered, it switches between enable and disable

    Parameters
    ----------
    ``*args``
        Variable length argument to be used by the Tool
    ``**kwargs``
        `toggled` if present and True, sets the initial state of the Tool
        Arbitrary keyword arguments to be consumed by the Tool
    """
    radio_group = ...
    cursor = ...
    default_toggled = ...
    def __init__(self, *args, **kwargs):
        ...
    
    def trigger(self, sender, event, data: Optional[Any] = ...):
        """Calls `enable` or `disable` based on `toggled` value"""
        ...
    
    def enable(self, event: Optional[Any] = ...):
        """
        Enable the toggle tool

        `trigger` calls this method when `toggled` is False
        """
        ...
    
    def disable(self, event: Optional[Any] = ...):
        """
        Disable the toggle tool

        `trigger` call this method when `toggled` is True.

        This can happen in different circumstances

        * Click on the toolbar tool button
        * Call to `matplotlib.backend_managers.ToolManager.trigger_tool`
        * Another `ToolToggleBase` derived tool is triggered
          (from the same `ToolManager`)
        """
        ...
    
    @property
    def toggled(self):
        """State of the toggled tool"""
        ...
    
    def set_figure(self, figure):
        ...
    


class SetCursorBase(ToolBase):
    """
    Change to the current cursor while inaxes

    This tool, keeps track of all `ToolToggleBase` derived tools, and calls
    set_cursor when a tool gets triggered
    """
    def __init__(self, *args, **kwargs):
        ...
    
    def set_figure(self, figure):
        ...
    
    def _tool_trigger_cbk(self, event):
        ...
    
    def _add_tool(self, tool):
        """set the cursor when the tool is triggered"""
        ...
    
    def _add_tool_cbk(self, event):
        """Process every newly added tool"""
        ...
    
    def _set_cursor_cbk(self, event):
        ...
    
    def set_cursor(self, cursor):
        """
        Set the cursor

        This method has to be implemented per backend
        """
        ...
    


class ToolCursorPosition(ToolBase):
    """
    Send message with the current pointer position

    This tool runs in the background reporting the position of the cursor
    """
    def __init__(self, *args, **kwargs):
        ...
    
    def set_figure(self, figure):
        ...
    
    def send_message(self, event):
        """Call `matplotlib.backend_managers.ToolManager.message_event`"""
        ...
    


class RubberbandBase(ToolBase):
    """Draw and remove rubberband"""
    def trigger(self, sender, event, data):
        """Call `draw_rubberband` or `remove_rubberband` based on data"""
        ...
    
    def draw_rubberband(self, *data):
        """
        Draw rubberband

        This method must get implemented per backend
        """
        ...
    
    def remove_rubberband(self):
        """
        Remove rubberband

        This method should get implemented per backend
        """
        ...
    


class ToolQuit(ToolBase):
    """Tool to call the figure manager destroy method"""
    description = ...
    default_keymap = ...
    def trigger(self, sender, event, data: Optional[Any] = ...):
        ...
    


class ToolQuitAll(ToolBase):
    """Tool to call the figure manager destroy method"""
    description = ...
    default_keymap = ...
    def trigger(self, sender, event, data: Optional[Any] = ...):
        ...
    


class ToolEnableAllNavigation(ToolBase):
    """Tool to enable all axes for toolmanager interaction"""
    description = ...
    default_keymap = ...
    def trigger(self, sender, event, data: Optional[Any] = ...):
        ...
    


class ToolEnableNavigation(ToolBase):
    """Tool to enable a specific axes for toolmanager interaction"""
    description = ...
    default_keymap = ...
    def trigger(self, sender, event, data: Optional[Any] = ...):
        ...
    


class _ToolGridBase(ToolBase):
    """Common functionality between ToolGrid and ToolMinorGrid."""
    _cycle = ...
    def trigger(self, sender, event, data: Optional[Any] = ...):
        ...
    
    @staticmethod
    def _get_uniform_grid_state(ticks):
        """
        Check whether all grid lines are in the same visibility state.

        Returns True/False if all grid lines are on or off, None if they are
        not all in the same state.
        """
        ...
    


class ToolGrid(_ToolGridBase):
    """Tool to toggle the major grids of the figure"""
    description = ...
    default_keymap = ...
    def _get_next_grid_states(self, ax):
        ...
    


class ToolMinorGrid(_ToolGridBase):
    """Tool to toggle the major and minor grids of the figure"""
    description = ...
    default_keymap = ...
    def _get_next_grid_states(self, ax):
        ...
    


class ToolFullScreen(ToolToggleBase):
    """Tool to toggle full screen"""
    description = ...
    default_keymap = ...
    def enable(self, event):
        ...
    
    def disable(self, event):
        ...
    


class AxisScaleBase(ToolToggleBase):
    """Base Tool to toggle between linear and logarithmic"""
    def trigger(self, sender, event, data: Optional[Any] = ...):
        ...
    
    def enable(self, event):
        ...
    
    def disable(self, event):
        ...
    


class ToolYScale(AxisScaleBase):
    """Tool to toggle between linear and logarithmic scales on the Y axis"""
    description = ...
    default_keymap = ...
    def set_scale(self, ax, scale):
        ...
    


class ToolXScale(AxisScaleBase):
    """Tool to toggle between linear and logarithmic scales on the X axis"""
    description = ...
    default_keymap = ...
    def set_scale(self, ax, scale):
        ...
    


class ToolViewsPositions(ToolBase):
    """
    Auxiliary Tool to handle changes in views and positions

    Runs in the background and should get used by all the tools that
    need to access the figure's history of views and positions, e.g.

    * `ToolZoom`
    * `ToolPan`
    * `ToolHome`
    * `ToolBack`
    * `ToolForward`
    """
    def __init__(self, *args, **kwargs):
        self.views = ...
        self.positions = ...
        self.home_views = ...
    
    def add_figure(self, figure):
        """Add the current figure to the stack of views and positions"""
        ...
    
    def clear(self, figure):
        """Reset the axes stack"""
        ...
    
    def update_view(self):
        """
        Update the view limits and position for each axes from the current
        stack position. If any axes are present in the figure that aren't in
        the current stack position, use the home view limits for those axes and
        don't update *any* positions.
        """
        ...
    
    def push_current(self, figure: Optional[Any] = ...):
        """
        Push the current view limits and position onto their respective stacks
        """
        ...
    
    def _axes_pos(self, ax):
        """
        Return the original and modified positions for the specified axes

        Parameters
        ----------
        ax : (matplotlib.axes.AxesSubplot)
        The axes to get the positions for

        Returns
        -------
        limits : (tuple)
        A tuple of the original and modified positions
        """
        ...
    
    def update_home_views(self, figure: Optional[Any] = ...):
        """
        Make sure that self.home_views has an entry for all axes present in the
        figure
        """
        ...
    
    def refresh_locators(self):
        """Redraw the canvases, update the locators"""
        ...
    
    def home(self):
        """Recall the first view and position from the stack"""
        ...
    
    def back(self):
        """Back one step in the stack of views and positions"""
        ...
    
    def forward(self):
        """Forward one step in the stack of views and positions"""
        ...
    


class ViewsPositionsBase(ToolBase):
    """Base class for `ToolHome`, `ToolBack` and `ToolForward`"""
    _on_trigger = ...
    def trigger(self, sender, event, data: Optional[Any] = ...):
        ...
    


class ToolHome(ViewsPositionsBase):
    """Restore the original view lim"""
    description = ...
    image = ...
    default_keymap = ...
    _on_trigger = ...


class ToolBack(ViewsPositionsBase):
    """Move back up the view lim stack"""
    description = ...
    image = ...
    default_keymap = ...
    _on_trigger = ...


class ToolForward(ViewsPositionsBase):
    """Move forward in the view lim stack"""
    description = ...
    image = ...
    default_keymap = ...
    _on_trigger = ...


class ConfigureSubplotsBase(ToolBase):
    """Base tool for the configuration of subplots"""
    description = ...
    image = ...


class SaveFigureBase(ToolBase):
    """Base tool for figure saving"""
    description = ...
    image = ...
    default_keymap = ...


class ZoomPanBase(ToolToggleBase):
    """Base class for `ToolZoom` and `ToolPan`"""
    def __init__(self, *args):
        self.base_scale = ...
        self.scrollthresh = ...
        self.lastscroll = ...
    
    def enable(self, event):
        """Connect press/release events and lock the canvas"""
        ...
    
    def disable(self, event):
        """Release the canvas and disconnect press/release events"""
        ...
    
    def trigger(self, sender, event, data: Optional[Any] = ...):
        ...
    
    def scroll_zoom(self, event):
        self.lastscroll = ...
    


class ToolZoom(ZoomPanBase):
    """Zoom to rectangle"""
    description = ...
    image = ...
    default_keymap = ...
    cursor = ...
    radio_group = ...
    def __init__(self, *args):
        ...
    
    def _cancel_action(self):
        ...
    
    def _press(self, event):
        """the _press mouse button in zoom to rect mode callback"""
        ...
    
    def _switch_on_zoom_mode(self, event):
        ...
    
    def _switch_off_zoom_mode(self, event):
        ...
    
    def _mouse_move(self, event):
        """the drag callback in zoom mode"""
        ...
    
    def _release(self, event):
        """the release mouse button callback in zoom to rect mode"""
        ...
    


class ToolPan(ZoomPanBase):
    """Pan axes with left mouse, zoom with right"""
    default_keymap = ...
    description = ...
    image = ...
    cursor = ...
    radio_group = ...
    def __init__(self, *args):
        ...
    
    def _cancel_action(self):
        ...
    
    def _press(self, event):
        ...
    
    def _release(self, event):
        ...
    
    def _mouse_move(self, event):
        ...
    


default_tools = { 'home': ToolHome,'back': ToolBack,'forward': ToolForward,'zoom': ToolZoom,'pan': ToolPan,'subplots': 'ToolConfigureSubplots','save': 'ToolSaveFigure','grid': ToolGrid,'grid_minor': ToolMinorGrid,'fullscreen': ToolFullScreen,'quit': ToolQuit,'quit_all': ToolQuitAll,'allnav': ToolEnableAllNavigation,'nav': ToolEnableNavigation,'xscale': ToolXScale,'yscale': ToolYScale,'position': ToolCursorPosition,_views_positions: ToolViewsPositions,'cursor': 'ToolSetCursor','rubberband': 'ToolRubberband' }
default_toolbar_tools = [['navigation', ['home', 'back', 'forward']], ['zoompan', ['pan', 'zoom', 'subplots']], ['io', ['save']]]
def add_tools_to_manager(toolmanager, tools=...):
    """
    Add multiple tools to `ToolManager`

    Parameters
    ----------
    toolmanager: ToolManager
        `backend_managers.ToolManager` object that will get the tools added
    tools : {str: class_like}, optional
        The tools to add in a {name: tool} dict, see `add_tool` for more
        info.
    """
    ...

def add_tools_to_container(container, tools=...):
    """
    Add multiple tools to the container.

    Parameters
    ----------
    container: Container
        `backend_bases.ToolContainerBase` object that will get the tools added
    tools : list, optional
        List in the form
        [[group1, [tool1, tool2 ...]], [group2, [...]]]
        Where the tools given by tool1, and tool2 will display in group1.
        See `add_tool` for details.
    """
    ...

