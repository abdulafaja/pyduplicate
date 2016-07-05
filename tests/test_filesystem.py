import os
import unittest

from pyduplicate.loader import FileSystem


class FilesystemTests(unittest.TestCase):
    def test_filename(self):
        filename = 'not_directory'
        abs_path = os.path.abspath(filename)
        filesystem_filename = FileSystem.filename(abs_path)
        self.assertEqual(filename, filesystem_filename)