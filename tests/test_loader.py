import os
import unittest

from pyduplicate.loader import Loader


class LoaderTests(unittest.TestCase):
    def test_load_files(self):
        test_files_dir = 'tests/loader_test_files'

        loader = Loader()
        loader.load_files(path=test_files_dir)
        self.assertEqual(len(os.listdir(test_files_dir)), len(loader.files))
