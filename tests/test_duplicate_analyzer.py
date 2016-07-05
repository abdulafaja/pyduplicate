import unittest

from pyduplicate.duplicate import DuplicateAnalyzer
from pyduplicate.file import File
from pyduplicate.loader import Loader


class TestObject(object):
    def __init__(self, number):
        self._number = number

    def __hash__(self):
        return self._number

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()


class CompareTestObject(TestObject):
    def __init__(self, number, comparision):
        super(CompareTestObject, self).__init__(number)
        self._comparision = comparision

    @property
    def comparision(self):
        return self._comparision

    @staticmethod
    def compare(object, other):
        return object.comparision < other.comparision


class DuplicateAnalyzerTests(unittest.TestCase):
    def setUp(self):
        self.int_list = [1, 1, 2, 2, 3, 3, 4, 4, 1, 1, 2, 2, 3, 3]

    def test_duplicate_analyzer_split(self):
        unique, duplicated = DuplicateAnalyzer.split(self.int_list)
        self.assertEqual(len(unique), 4)
        self.assertEqual(len(duplicated), len(self.int_list) - 4)

    def test_duplicate_analyzer_split_objects(self):
        objects = [TestObject(number) for number in self.int_list]
        unique, duplicated = DuplicateAnalyzer.split(objects)
        self.assertEqual(len(unique), 4)
        self.assertEqual(len(duplicated), len(self.int_list) - 4)

    def test_duplicate_analyzer_split_objects_compare(self):
        tuple_list = [(1, 1), (1, 2), (2, 1), (2, 3), (2, 2), (1, 0)]
        objects = [CompareTestObject(number, comparision) for number, comparision in tuple_list]
        unique, duplicated = DuplicateAnalyzer.split(objects, CompareTestObject.compare)
        self.assertEqual(len(unique), 2)
        self.assertEqual(len(duplicated), len(tuple_list) - 2)

    def test_duplicate_analyzer_files(self):
        path = 'tests/duplicate_analyzer_files'
        l = Loader()
        l.load_files(path)
        unique, duplicated = DuplicateAnalyzer.split(l.files, File.compare)
        self.assertEqual(unique[0].filename, 'newer')
        self.assertEqual(duplicated[0].filename, 'older')
