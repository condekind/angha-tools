"""
This type stub file was generated by pyright.
"""

import six
import difflib
import os
from __future__ import absolute_import, division, print_function
from matplotlib import cbook
from matplotlib.testing import setup

if not os.path.exists(os.path.join(os.path.dirname(__file__), 'baseline_images')):
    ...
@cbook.deprecated("2.1")
def assert_str_equal(reference_str, test_str, format_str=...):
    """
    Assert the two strings are equal. If not, fail and print their
    diffs using difflib.

    """
    ...

