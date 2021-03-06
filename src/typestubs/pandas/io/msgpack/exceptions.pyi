"""
This type stub file was generated by pyright.
"""

class UnpackException(Exception):
    ...


class BufferFull(UnpackException):
    ...


class OutOfData(UnpackException):
    ...


class UnpackValueError(UnpackException, ValueError):
    ...


class ExtraData(ValueError):
    def __init__(self, unpacked, extra):
        self.unpacked = ...
        self.extra = ...
    
    def __str__(self):
        ...
    


class PackException(Exception):
    ...


class PackValueError(PackException, ValueError):
    ...


