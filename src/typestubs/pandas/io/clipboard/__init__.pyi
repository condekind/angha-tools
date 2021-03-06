"""
This type stub file was generated by pyright.
"""

import platform
import os
import subprocess
from .clipboards import init_gtk_clipboard, init_klipper_clipboard, init_no_clipboard, init_osx_clipboard, init_qt_clipboard, init_xclip_clipboard, init_xsel_clipboard
from .windows import init_windows_clipboard

"""
Pyperclip

A cross-platform clipboard module for Python. (only handles plain text for now)
By Al Sweigart al@inventwithpython.com
BSD License

Usage:
  import pyperclip
  pyperclip.copy('The text to be copied to the clipboard.')
  spam = pyperclip.paste()

  if not pyperclip.copy:
    print("Copy functionality unavailable!")

On Windows, no additional modules are needed.
On Mac, the module uses pbcopy and pbpaste, which should come with the os.
On Linux, install xclip or xsel via package manager. For example, in Debian:
sudo apt-get install xclip

Otherwise on Linux, you will need the gtk or PyQt4 modules installed.

gtk and PyQt4 modules are not available for Python 3,
and this module does not work with PyGObject yet.
"""
__version__ = '1.5.27'
HAS_DISPLAY = os.getenv("DISPLAY", False)
CHECK_CMD = "where" if platform.system() == "Windows" else "which"
def _executable_exists(name):
    ...

def determine_clipboard():
    ...

def set_clipboard(clipboard):
    ...

__all__ = ["copy", "paste"]
clipboard_get = paste
clipboard_set = copy
