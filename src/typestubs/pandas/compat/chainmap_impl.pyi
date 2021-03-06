"""
This type stub file was generated by pyright.
"""

from collections import MutableMapping
from typing import Any, Optional

def recursive_repr(fillvalue=...):
    'Decorator to make a repr function return fillvalue for a recursive call'
    ...

class ChainMap(MutableMapping):
    """ A ChainMap groups multiple dicts (or other mappings) together
    to create a single, updatable view.

    The underlying mappings are stored in a list.  That list is public and can
    be accessed / updated using the *maps* attribute.  There is no other state.

    Lookups search the underlying mappings successively until a key is found.
    In contrast, writes, updates, and deletions only operate on the first
    mapping.

    """
    def __init__(self, *maps):
        """Initialize a ChainMap by setting *maps* to the given mappings.
        If no mappings are provided, a single empty dictionary is used.

        """
        self.maps = ...
    
    def __missing__(self, key):
        ...
    
    def __getitem__(self, key):
        ...
    
    def get(self, key, default: Optional[Any] = ...):
        ...
    
    def __len__(self):
        ...
    
    def __iter__(self):
        ...
    
    def __contains__(self, key):
        ...
    
    def __bool__(self):
        ...
    
    @recursive_repr()
    def __repr__(self):
        ...
    
    @classmethod
    def fromkeys(cls, iterable, *args):
        'Create a ChainMap with a single dict created from the iterable.'
        ...
    
    def copy(self):
        """
        New ChainMap or subclass with a new copy of maps[0] and refs to
        maps[1:]
        """
        ...
    
    __copy__ = ...
    def new_child(self, m: Optional[Any] = ...):
        """
        New ChainMap with a new map followed by all previous maps. If no
        map is provided, an empty dict is used.
        """
        ...
    
    @property
    def parents(self):
        'New ChainMap from maps[1:].'
        ...
    
    def __setitem__(self, key, value):
        ...
    
    def __delitem__(self, key):
        ...
    
    def popitem(self):
        """
        Remove and return an item pair from maps[0]. Raise KeyError is maps[0]
        is empty.
        """
        ...
    
    def pop(self, key, *args):
        """
        Remove *key* from maps[0] and return its value. Raise KeyError if
        *key* not in maps[0].
        """
        ...
    
    def clear(self):
        'Clear maps[0], leaving maps[1:] intact.'
        ...
    


