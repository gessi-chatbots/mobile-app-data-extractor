from unittest import TestCase

from utils import flatten_dict, combine_fields, combine_dicts


class Test(TestCase):
    def test_flatten_dict(self):
        dict_test = {'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]}
        flattened = {'a': 1, 'd': [6, 7, 8], 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5}
        flat = flatten_dict(dict_test)
        self.assertDictEqual(flat, flattened)

    def test_combine_fields(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'d': 1, 'e': 3, 'f': 3}
        keys = [('a', 'd'), ('b', 'e'), ('c', 'f')]
        dict_final = {'a': 1, 'b': [2, 3], 'c': 3}
        result = combine_fields(dict1, dict2, keys)
        self.assertDictEqual(result, dict_final)

    def test_combine_fields_sep(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'d': 1, 'e': 3, 'f': 3}
        keys = [('a', 'd'), ('b', 'e'), ('c', 'f')]
        dict_final = {'a': 1, 'b': [2, 3], 'c': 3}
        result = combine_fields(dict1, dict2, keys)
        self.assertDictEqual(result, dict_final)

    def test_combine_fields_disjoint(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'d': 1, 'e': 3, 'f': 3}
        keys = [('g', 'h')]
        dict_final = {}
        result = combine_fields(dict1, dict2, keys)
        self.assertDictEqual(result, dict_final)

    def test_combine_dicts(self):
        dict1 = {'a': 1, 'b': 2, 'c': 3}
        dict2 = {'d': 1, 'e': 3, 'f': 3}
        keys = [('a', 'e')]
        dict_final = {'a': [1, 3], 'b': 2, 'c': 3, 'd': 1, 'f': 3}
        result = combine_dicts(dict1, dict2, keys)
        self.assertDictEqual(result,dict_final)

