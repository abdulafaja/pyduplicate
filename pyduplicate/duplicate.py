import copy


class DuplicateAnalyzer(object):
    """
    Class to find duplicates objects using it's hashes
    """

    @classmethod
    def _basic_split(cls, objects_list):
        unique = list(set(objects_list))
        rest = copy.deepcopy(objects_list)
        [rest.remove(obj) for obj in unique]
        return unique, rest

    @classmethod
    def _compare_func_split(cls, objects_list, compare_func):
        unique = []
        duplicate = []
        for object in objects_list:
            if object not in unique:
                unique.append(object)
            else:
                other = unique[unique.index(object)]
                unique.remove(other)
                if compare_func(object, other):
                    unique.append(other)
                    duplicate.append(object)
                else:
                    unique.append(object)
                    duplicate.append(other)
        return unique, duplicate

    @classmethod
    def split(cls, objects_list, compare_func=None):
        """
        Split objects list into two lists: one with unique objects and the second with duplicates.
        The first found object is move to the unique list - each other object which is it's duplicate is added to the
        'duplicate' list.
        Objects needs to be hashable and comparable.
        :param objects_list: List of objects to split
        :type objects_list: list
        :return: Two lists: first with unique objects and the second with duplicates
        :rtype: tuple
        """
        if not compare_func:
            return cls._basic_split(objects_list)
        return cls._compare_func_split(objects_list, compare_func)
