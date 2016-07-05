import datetime
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
        Get the list of files in directory under given path.
        Join the file names and path to directory.

        :param path: Path to the directory
        :type path: str
        :return: List of file under directory absolute paths
        :rtype: list
        """
        try:
            return [os.path.join(path, file) for file in os.listdir(path)]
        except PermissionError as e:
            PyDuplicateLogger.exception(e)
            raise FileSystemException(e)
        except NotADirectoryError as e:
            PyDuplicateLogger.exception(e)
            raise FileSystemException(e)
        except FileNotFoundError as e:
            PyDuplicateLogger.exception(e)
            raise FileSystemException(e)

    @classmethod
    def filename(cls, filepath):
        """
        Get the file name from given absolute path

        :param path: Path to the file
        :type path: str
        :return: Filename under given path
        :rtype: str
        """
        return os.path.basename(filepath)

    @classmethod
    def file_last_modification_date(cls, filepath):
        """
        Get the date of file last modification
        :param filepath: Path to the file
        :type filepath: str
        :return: Last modification date
        :rtype: datetime.date
        """
        try:
            timestamp = os.path.getmtime(filepath)
            return datetime.date.fromtimestamp(timestamp)
        except OSError as e:
            PyDuplicateLogger.exception(e)
            raise FileSystemException(e)