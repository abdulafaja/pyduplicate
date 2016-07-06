class PyDuplicateException(Exception):
    """
    Base PyDuplicate exception class
    """
    pass


class ArgumentException(PyDuplicateException):
    """
    Exception raised by function if wrong argument was passed
    """
    pass


class FileSystemException(PyDuplicateException):
    """
    Exception raised by file system class.
    """
    pass
