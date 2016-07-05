class PyDuplicateException(Exception):
    """
    Base PyDuplicate exception class
    """
    pass


class FileSystemException(PyDuplicateException):
    """
    Exception raised by file system class.
    """
    pass
