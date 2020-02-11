"""
This type stub file was generated by pyright.
"""

"""
A wx API adapter to hide differences between wxPython classic and phoenix.

It is assumed that the user code is selecting what version it wants to use,
here we just ensure that it meets the minimum required by matplotlib.

For an example see embedding_in_wx2.py
"""
missingwx = "Matplotlib backend_wx and backend_wxagg require wxPython>=2.9"
if wx_version < str("2.9"):
    ...
if is_phoenix:
    fontweights = { 100: wx.FONTWEIGHT_LIGHT,200: wx.FONTWEIGHT_LIGHT,300: wx.FONTWEIGHT_LIGHT,400: wx.FONTWEIGHT_NORMAL,500: wx.FONTWEIGHT_NORMAL,600: wx.FONTWEIGHT_NORMAL,700: wx.FONTWEIGHT_BOLD,800: wx.FONTWEIGHT_BOLD,900: wx.FONTWEIGHT_BOLD,'ultralight': wx.FONTWEIGHT_LIGHT,'light': wx.FONTWEIGHT_LIGHT,'normal': wx.FONTWEIGHT_NORMAL,'medium': wx.FONTWEIGHT_NORMAL,'semibold': wx.FONTWEIGHT_NORMAL,'bold': wx.FONTWEIGHT_BOLD,'heavy': wx.FONTWEIGHT_BOLD,'ultrabold': wx.FONTWEIGHT_BOLD,'black': wx.FONTWEIGHT_BOLD }
    fontangles = { 'italic': wx.FONTSTYLE_ITALIC,'normal': wx.FONTSTYLE_NORMAL,'oblique': wx.FONTSTYLE_SLANT }
    fontnames = { 'Sans': wx.FONTFAMILY_SWISS,'Roman': wx.FONTFAMILY_ROMAN,'Script': wx.FONTFAMILY_SCRIPT,'Decorative': wx.FONTFAMILY_DECORATIVE,'Modern': wx.FONTFAMILY_MODERN,'Courier': wx.FONTFAMILY_MODERN,'courier': wx.FONTFAMILY_MODERN }
    dashd_wx = { 'solid': wx.PENSTYLE_SOLID,'dashed': wx.PENSTYLE_SHORT_DASH,'dashdot': wx.PENSTYLE_DOT_DASH,'dotted': wx.PENSTYLE_DOT }
    BitmapFromBuffer = wx.Bitmap.FromBufferRGBA
    EmptyBitmap = wx.Bitmap
    EmptyImage = wx.Image
    Cursor = wx.Cursor
    EventLoop = wx.GUIEventLoop
    NamedColour = wx.Colour
    StockCursor = wx.Cursor
else:
    fontweights = { 100: wx.LIGHT,200: wx.LIGHT,300: wx.LIGHT,400: wx.NORMAL,500: wx.NORMAL,600: wx.NORMAL,700: wx.BOLD,800: wx.BOLD,900: wx.BOLD,'ultralight': wx.LIGHT,'light': wx.LIGHT,'normal': wx.NORMAL,'medium': wx.NORMAL,'semibold': wx.NORMAL,'bold': wx.BOLD,'heavy': wx.BOLD,'ultrabold': wx.BOLD,'black': wx.BOLD }
    fontangles = { 'italic': wx.ITALIC,'normal': wx.NORMAL,'oblique': wx.SLANT }
    fontnames = { 'Sans': wx.SWISS,'Roman': wx.ROMAN,'Script': wx.SCRIPT,'Decorative': wx.DECORATIVE,'Modern': wx.MODERN,'Courier': wx.MODERN,'courier': wx.MODERN }
    dashd_wx = { 'solid': wx.SOLID,'dashed': wx.SHORT_DASH,'dashdot': wx.DOT_DASH,'dotted': wx.DOT }
    BitmapFromBuffer = wx.BitmapFromBufferRGBA
    EmptyBitmap = wx.EmptyBitmap
    EmptyImage = wx.EmptyImage
    Cursor = wx.StockCursor
    EventLoop = wx.EventLoop
    NamedColour = wx.NamedColour
    StockCursor = wx.StockCursor
def _AddTool(parent, wx_ids, text, bmp, tooltip_text):
    ...

