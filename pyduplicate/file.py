from pyduplicate.filesystem import FileSystem
from pyduplicate.hasher import Hasher


class File(object):
    """
    Class which represent file.
    It has file last modification time, path to it and hashed content
    """
    def __init__(self, file_path):
        self._path = file_path
        self._filename = FileSystem.filename(self._path)
        self._modification_date = FileSystem.file_last_modification_date(self._path)
        self._hash = Hasher.hash_file_first_line(self._path)

    def __hash__(self):
        return self._hash