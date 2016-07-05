from pyduplicate.exceptions import FileSystemException
from pyduplicate.logger import PyDuplicateLogger


class Hasher(object):

    @classmethod
    def hash_file_first_line(cls, filepath):
        """
        Create a hash of file content
        :param filepath: Path to the file
        :type filepath: str
        :return: File's content hash
        :rtype: int
        """
        try:
            with open(filepath) as file:
                first_line_hash = hash(file.readline(1))
            return first_line_hash
        except FileNotFoundError as e:
            PyDuplicateLogger.exception(e)
            raise FileSystemException(e)
        except PermissionError as e:
            PyDuplicateLogger.exception(e)
            raise FileSystemException(e)
