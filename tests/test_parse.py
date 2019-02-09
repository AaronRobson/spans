#!/usr/bin/python

import unittest

from spans import parse_numbers


class TestParseNumbers(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(parse_numbers(''), [])

    def test_comma_separated(self):
        self.assertEqual(parse_numbers('1,2'), [1, 2])

    def test_comma_space_separated(self):
        self.assertEqual(parse_numbers('3, 4'), [3, 4])

    def test_space_separated(self):
        self.assertEqual(parse_numbers('5 6'), [5, 6])

    def test_whitespace_separated(self):
        self.assertEqual(parse_numbers('7 \t \n 8'), [7, 8])
