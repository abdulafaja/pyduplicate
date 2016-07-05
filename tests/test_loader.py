import os
import unittest

from pyduplicate.exceptions import FileSystemException
from pyduplicate.loader import Loader


class LoaderTests(unittest.TestCase):
    def test_load_files(self):
        test_files_dir = 'tests/loader_test_files'

        loader = Loader()
        loader.load_files(path=test_files_dir)
        self.assertEqual(len(os.listdir(test_files_dir)), len(loader.files))

    def test_load_files_from_file(self):
        test_files_not_dir = 'tests/not_directory'

        loader = Loader()
        self.assertRaises(FileSystemException, loader.load_files, test_files_not_dir)

    def test_load_files_from_unavailable_directory(self):
        test_files_not_dir = 'tests/denied_directory'

        loader = Loader()
        self.assertRaises(FileSystemException, loader.load_files, test_files_not_dir)
