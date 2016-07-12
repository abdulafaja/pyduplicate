from os.path import join as os_join

from pyduplicate.argument_parser import ArgumentParser
from pyduplicate.copier import Copier
from pyduplicate.duplicate import DuplicateAnalyzer
from pyduplicate.file import File
from pyduplicate.filesystem import FileSystem
from pyduplicate.loader import Loader
from pyduplicate.logger import PyDuplicateLogger


def main():
    argument_parser = ArgumentParser()
    args = argument_parser.parse_args()

    loader = Loader()
    loader.load_files(args.source)
    unique, duplicated = DuplicateAnalyzer.split(loader.files, File.compare)
    FileSystem.create_dir(args.destination, 'duplicates')
    duplicated_path = os_join(args.destination, 'duplicates')
    [Copier.copy_file(file.filepath, duplicated_path) for file in duplicated]
    [FileSystem.create_dir(args.destination, file.formatted_modification_date, ignore_errors=True) for file in unique]
    [Copier.copy_file(file.filepath, os_join(args.destination, file.formatted_modification_date)) for file in unique]
    PyDuplicateLogger.debug("Successfully ended!")


if __name__ == "__main__":
    main()
