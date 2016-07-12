import datetime
import os
import shutil

from pyduplicate.exceptions import ArgumentException, FileSystemException
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
            raise ArgumentException(e)
        except FileNotFoundError as e:
            PyDuplicateLogger.exception(e)
            raise ArgumentException(e)

    @classmethod
    def filename(cls, filepath):
        """
        Get the file name from given absolute path

        :param filepath: Path to the file
        :type filepath: str
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

    @classmethod
    def file_copy(cls, filepath, dest_path):
        """
        Copy files to given destination path
        :param filepath: Path to the file which should be copied
        :type filepath: str
        :param dest_path: Destination path where file should be copied. It must be directory
        :type dest_path: str
        :return: None
        :rtype: None
        """
        if not os.path.isdir(dest_path):
            raise ArgumentException("Path has to be directory")
        shutil.copy2(filepath, dest_path)

    @classmethod
    def create_dir(cls, path, dir_name, ignore_errors=False):
        """
        Create a directory on given path with dir_name
        :param path: Path where directory is going to be created
        :type path: str
        :param dir_name: Directory name
        :type dir_name: str
        :return: None
        :rtype: None
        """
        try:
            os.makedirs(os.path.join(path, dir_name))
        except FileExistsError as e:
            PyDuplicateLogger.exception(e)
            if not ignore_errors:
                raise FileSystemException(e)
