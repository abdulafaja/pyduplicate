from pyduplicate.filesystem import FileSystem
from pyduplicate.hasher import Hasher


class File(object):
    """
    Class which represent file.
    It has file last modification time, path to it and hashed content
    """
    __slots__ = ['_path', '_filename', '_modification_date', '_hash']

    def __init__(self, file_path):
        self._path = file_path
        self._filename = FileSystem.filename(self._path)
        self._modification_date = FileSystem.file_last_modification_date(self._path)
        self._hash = Hasher.hash_file_first_line(self._path)

    def __hash__(self):
        return self._hash

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __unicode__(self):
        return '{}'.format(self.filename)

    @property
    def filename(self):
        return self._filename

    @property
    def formatted_modification_date(self):
        return self._modification_date.strftime("%Y/%d")

    @property
    def filepath(self):
        return self._path

    @staticmethod
    def compare(object, other):
        return object._modification_date < other._modification_date
