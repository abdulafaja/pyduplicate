import os

from pyduplicate.exceptions import FileSystemException
from pyduplicate.logger import PyDuplicateLogger


class FileSystem(object):
    """
    Class to manage file system
    """
    @classmethod
    def listdir(cls, path='~/.'):
        """
        Get the list of files in directory under given path

        :param path: Path to the directory
        :type path: str
        :return: List of file names under repository
        :rtype: list
        """
        try:
            return os.listdir(path)
        except PermissionError as e:
            PyDuplicateLogger.exception(e)
            raise FileSystemException(e)
        except NotADirectoryError as e:
            PyDuplicateLogger.exception(e)
            raise FileSystemException(e)
