import os
import unittest

from pyduplicate.exceptions import FileSystemException
from pyduplicate.loader import Loader


class LoaderTests(unittest.TestCase):
    def setUp(self):
        self.loader = Loader()

    def test_load_files(self):
        test_files_dir = 'tests/loader_test_files'

        self.loader.load_files(path=test_files_dir)
        self.assertEqual(len(os.listdir(test_files_dir)), len(self.loader.files))

    def test_load_files_from_file(self):
        test_files_not_dir = 'tests/not_directory'

        self.assertRaises(FileSystemException, self.loader.load_files, test_files_not_dir)

    def test_load_files_from_unavailable_directory(self):
        test_files_not_dir = 'tests/denied_directory'

        self.assertRaises(FileSystemException, self.loader.load_files, test_files_not_dir)

    def test_load_files_from_not_existing_directory(self):
        test_dir_not_exists = 'tests/not_existed_directory'

        self.assertRaises(FileSystemException, self.loader.load_files, test_dir_not_exists)
