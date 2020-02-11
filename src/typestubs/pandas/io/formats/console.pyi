"""
This type stub file was generated by pyright.
"""

"""
Internal module for console introspection
"""
_initial_defencoding = None
def detect_console_encoding():
    """
    Try to find the most capable encoding supported by the console.
    slighly modified from the way IPython handles the same issue.
    """
    ...

def get_console_size():
    """Return console size as tuple = (width, height).

    Returns (None,None) in non-interactive session.
    """
    ...

