import os
import unittest

from pyduplicate.copier import Copier
from pyduplicate.exceptions import ArgumentException


class CopierTestCase(unittest.TestCase):
    def test_copy(self):
        dest = 'tests/copied'
        file = 'tests/copy_test_file'
        file_path = os.path.abspath(file)
        dest_path = os.path.abspath(dest)
        Copier.copy_file(file_path, dest_path)
        self.assertTrue(os.path.isfile(os.path.join(dest_path, os.path.basename(file))))

    def test_copy_dest_not_dir(self):
        dest = 'tests/copier'
        file = 'tests/copy_test_file'
        file_path = os.path.abspath(file)
        dest_path = os.path.abspath(dest)
        self.assertRaises(ArgumentException, Copier.copy_file, file_path, dest_path)
