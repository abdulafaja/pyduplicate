from pyduplicate.filesystem import FileSystem


class Copier(object):
    """
    Class responsible for save files into right destination
    """

    @classmethod
    def copy_file(cls, file, dest_path):
        FileSystem.file_copy(file, dest_path)

    @classmethod
    def copy_files(cls, files, dest_path):
        [cls.copy_file(file, dest_path) for file in files]
