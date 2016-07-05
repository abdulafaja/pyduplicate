from multiprocessing import Pool

from pyduplicate.exceptions import FileSystemException
from pyduplicate.file import File
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

    def _create_file_instance(self, file_abs_path):
        file = File(file_abs_path)
        self._append_file(file)
        return file

    def _load_files_multiprocess(self, path):
        with Pool() as p:
            self._files = p.map(self._create_file_instance, FileSystem.listdir(path))

    def _load_files_list_comprehension(self, path):
        [self._create_file_instance(file_abs_path) for file_abs_path in FileSystem.listdir(path)]

    def load_files(self, path, multiprocess=True):
        """
        Function loads files from given path and create an instance of each of it

        :param path: Path to the directory from which files will be loaded
        :type path: str
        :return: None
        :rtype: None
        """
        try:
            if multiprocess:
                self._load_files_multiprocess(path)
            else:
                self._load_files_list_comprehension(path)
        except FileSystemException:
            raise
