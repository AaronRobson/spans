#!/usr/bin/python

import unittest

from spans import parse_numbers


class TestParseNumbers(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(parse_numbers(''), set())

    def test_comma_separated(self):
        self.assertEqual(parse_numbers('1,2'), {1, 2})

    def test_comma_space_separated(self):
        self.assertEqual(parse_numbers('3, 4'), {3, 4})

    def test_space_separated(self):
        self.assertEqual(parse_numbers('5 6'), {5, 6})

    def test_whitespace_separated(self):
        self.assertEqual(parse_numbers('7 \t \n 8'), {7, 8})

    def test_duplicates(self):
        self.assertEqual(parse_numbers('9,9'), {9})

    def test_incorrect_order(self):
        self.assertEqual(parse_numbers('11,10'), {10, 11})

    def test_range(self):
        self.assertEqual(parse_numbers('1-3'), {1, 2, 3})

    def test_ranges(self):
        self.assertEqual(parse_numbers('1-3, 5-6'), {1, 2, 3, 5, 6})

    def test_backwards_range(self):
        self.assertEqual(parse_numbers('3-1'), {1, 2, 3})
