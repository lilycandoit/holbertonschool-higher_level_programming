#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for the max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_all_negative(self):
        self.assertEqual(max_integer([-10, -5, -2]), -2)

    def test_mixed_items(self):
        self.assertEqual(max_integer([-1, 0, 10, -20]), 10)

    def test_duplicates(self):
        self.assertEqual(max_integer([5, 1, 5, 3]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_at_start(self):
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 9, 2]), 9)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 9]), 9)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 500000, 999999]), 1000000)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_mixed_integers_and_floats(self):
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_string_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["a", "z", "m"]), "z")


if __name__ == "__main__":
    unittest.main()
