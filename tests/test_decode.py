#!/usr/bin/python

import unittest

from spans import decode


class TestDecode(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(decode(''), set())

    def test_comma_separated(self):
        self.assertEqual(decode('1,2'), {1, 2})

    def test_comma_space_separated(self):
        self.assertEqual(decode('3, 4'), {3, 4})

    def test_space_separated(self):
        self.assertEqual(decode('5 6'), {5, 6})

    def test_whitespace_separated(self):
        self.assertEqual(decode('7 \t \n 8'), {7, 8})

    def test_duplicates(self):
        self.assertEqual(decode('9,9'), {9})

    def test_incorrect_order(self):
        self.assertEqual(decode('11,10'), {10, 11})

    def test_range(self):
        self.assertEqual(decode('1-3'), {1, 2, 3})

    def test_ranges(self):
        self.assertEqual(decode('1-3, 5-6'), {1, 2, 3, 5, 6})

    def test_backwards_range(self):
        self.assertEqual(decode('3-1'), {1, 2, 3})

    def test_a_negative(self):
        self.assertEqual(decode('-3'), {-3})

    def test_two_negative_numbers(self):
        self.assertEqual(decode('-3--1'), {-3, -2, -1})

    def test_a_negative_and_a_positive(self):
        self.assertEqual(decode('-3-1'), {-3, -2, -1, 0, 1})

    def test_a_positive_and_a_negative(self):
        self.assertEqual(decode('3--1'), {-1, 0, 1, 2, 3})
