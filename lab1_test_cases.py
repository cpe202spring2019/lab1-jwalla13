import unittest
from lab1 import *


# A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        # Tests with input None
        with self.assertRaises(ValueError):
            max_list_iter(None)

        # Tests with empty list
        self.assertEqual(max_list_iter([]), None)

        # Tests with input of incorrect data type
        with self.assertRaises(ValueError):
            max_list_iter(7)

        # Tests with input that doesn't contain integers
        with self.assertRaises(ValueError):
            max_list_iter([[1, 2, 3], 7, 2.7])

        # Tests function with correct data entry
        self.assertEqual(max_list_iter([1, 4, 7, -1]), 7)

    def test_reverse_rec(self):
        # Tests a basic reversal of a list with positive integers
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])

        # Tests reversal with input of None
        with self.assertRaises(ValueError):
            reverse_rec(None)

        # Tests reversal with incorrect data type input
        with self.assertRaises(ValueError):
            reverse_rec(7)

        # Tests reversal with list that does not contain integers
        with self.assertRaises(ValueError):
            reverse_rec([[1, 2], 7, 2.3])

        # Tests reversal with empty list input
        self.assertEqual(reverse_rec([]), [])

    def test_bin_search(self):
        # Tests correct data entry where target is less than starting point
        list_val = [0, 1, 2, 3, 4, 7, 8, 9, 10]
        self.assertEqual(bin_search(2, 0, len(list_val) - 1, list_val), 2)

        # Tests correct data entry where target is at starting point
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)

        # Tests correct data entry where target is greater than starting point
        self.assertEqual(bin_search(8, 0, len(list_val) - 1, list_val), 6)

        #Tests when number is not found and it is low
        self.assertEqual(bin_search(-1, 0, len(list_val) - 1, list_val), None)

        #Tests when number is not found and it is high
        self.assertEqual(bin_search(12, 0, len(list_val) - 1, list_val), None)

        #Tests when target number is the highest in the list
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)

        # Tests input None
        nList = None
        with self.assertRaises(ValueError):
            bin_search(4, 0, 7, nList)

        # Tests input of wrong data type
        with self.assertRaises(ValueError):
            bin_search(4, 0, 7, 8)

        # Tests input of list that does not contain integers
        with self.assertRaises(ValueError):
            bin_search(4, 0, 7, [2.7, 3.1, [1, 2]])


if __name__ == "__main__":
    unittest.main()
