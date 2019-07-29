import unittest

from spans import encode


class TestNumbersToRangeText(unittest.TestCase):
    def test_no_number(self):
        self.assertEqual(encode(set()), '')

    def test_single_number(self):
        self.assertEqual(encode({1}), '1')

    def test_adjacent_pair(self):
        self.assertEqual(encode({3, 4}), '3-4')

    def test_non_adjacent_pair(self):
        self.assertEqual(
            encode({1, 2, 3}),
            '1-3')

    def test_complex(self):
        self.assertEqual(
            encode({1, 2, 4, 5, 6, 10}),
            '1-2, 4-6, 10')
