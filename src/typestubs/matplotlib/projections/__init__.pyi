"""
This type stub file was generated by pyright.
"""

import six
from __future__ import absolute_import, division, print_function, unicode_literals
from .geo import AitoffAxes, HammerAxes, LambertAxes, MollweideAxes
from .polar import PolarAxes
from matplotlib import axes
from typing import Any, Optional

class ProjectionRegistry(object):
    """
    Manages the set of projections available to the system.
    """
    def __init__(self):
        ...
    
    def register(self, *projections):
        """
        Register a new set of projection(s).
        """
        ...
    
    def get_projection_class(self, name):
        """
        Get a projection class from its *name*.
        """
        ...
    
    def get_projection_names(self):
        """
        Get a list of the names of all projections currently
        registered.
        """
        ...
    


projection_registry = ProjectionRegistry()
def register_projection(cls):
    ...

def get_projection_class(projection: Optional[Any] = ...):
    """
    Get a projection class from its name.

    If *projection* is None, a standard rectilinear projection is
    returned.
    """
    ...

def process_projection_requirements(figure, *args, **kwargs):
    """
    Handle the args/kwargs to for add_axes/add_subplot/gca,
    returning::

        (axes_proj_class, proj_class_kwargs, proj_stack_key)

    Which can be used for new axes initialization/identification.

    .. note:: **kwargs** is modified in place.

    """
    ...

def get_projection_names():
    """
    Get a list of acceptable projection names.
    """
    ...

