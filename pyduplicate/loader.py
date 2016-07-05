from pyduplicate.exceptions import PermissionDeniedException
from pyduplicate.filesystem import FileSystem


class Loader(object):
    def __init__(self):
        self._files = []

    @property
    def files(self):
        return self._files

    def _append_file(self, file):
        self._files.append(file)

    def load_files(self, path):
        try:
            for file in FileSystem.listdir(path):
                self._append_file(file)
        except PermissionDeniedException as e:
            raise PermissionDeniedException(e)
