from pyduplicate.exceptions import FileSystemException
from pyduplicate.filesystem import FileSystem


class Loader(object):
    """
    Loader class which is responsible for load files from given path
    """
    def __init__(self):
        self._files = []

    @property
    def files(self):
        return self._files

    def _append_file(self, file):
        self._files.append(file)

    def load_files(self, path):
        """
        Function loads files from given path and create an instance of each of it

        :param path: Path to the directory from which files will be loaded
        :type path: str
        :return: None
        :rtype: None
        """
        try:
            for file in FileSystem.listdir(path):
                self._append_file(file)
        except FileSystemException:
            raise
