import os

from pyduplicate.exceptions import FileSystemException
from pyduplicate.logger import PyDuplicateLogger


class FileSystem(object):
    @classmethod
    def listdir(cls, path='~/.'):
        try:
            return os.listdir(path)
        except PermissionError as e:
            PyDuplicateLogger.exception(e)
            raise FileSystemException(e)
        except NotADirectoryError as e:
            PyDuplicateLogger.exception(e)
            raise FileSystemException(e)
