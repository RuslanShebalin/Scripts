import unittest
import random
import sorting

ARRAY_SIZE = 1000
MIN_VALUE = -10000
MAX_VALUE = 10000
NUMBER_EACH_TEST = 200


class TestSortMethods(unittest.TestCase):
    def test_hoar_sort(self):
        for i in range(NUMBER_EACH_TEST):
            sample_list = [
                random.randint(MIN_VALUE,
                               MAX_VALUE) for _ in range(ARRAY_SIZE)
            ]
            sorted_list = sample_list.copy()
            sorted_list.sort()
            sorting.sort_hoar(sample_list)
            self.assertEqual(sorted_list, sample_list)

    def test_shell_sort(self):
        for i in range(NUMBER_EACH_TEST):
            sample_list = [
                random.randint(MIN_VALUE,
                               MAX_VALUE) for _ in range(ARRAY_SIZE)
            ]
            sorted_list = sample_list.copy()
            sorted_list.sort()
            sorting.sort_shell(sample_list)
            self.assertEqual(sorted_list, sample_list)

    def test_piramid_sort(self):
        for i in range(NUMBER_EACH_TEST):
            sample_list = [
                random.randint(MIN_VALUE,
                               MAX_VALUE) for _ in range(ARRAY_SIZE)
            ]
            sorted_list = sample_list.copy()
            sorted_list.sort()
            sorting.sort_piramid(sample_list)
            self.assertEqual(sorted_list, sample_list)

    def test_introsort_sort(self):
        for i in range(NUMBER_EACH_TEST):
            sample_list = [
                random.randint(MIN_VALUE,
                               MAX_VALUE) for _ in range(ARRAY_SIZE)
            ]
            sorted_list = sample_list.copy()
            sorted_list.sort()
            sorting.sort_introsort(sample_list)
            self.assertEqual(sorted_list, sample_list)
