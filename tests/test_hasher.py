import unittest

from pyduplicate.hasher import Hasher


class HasherTests(unittest.TestCase):
    def test_file_first_line_hash(self):
        filename = 'tests/not_directory'
        hash = Hasher.hash_file_first_line(filename)
        self.assertIsInstance(hash, int)
