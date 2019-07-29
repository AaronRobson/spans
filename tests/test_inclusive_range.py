#!/usr/bin/python

import unittest

from spans import inclusive_range


class TestInclusiveRange(unittest.TestCase):
    def test_single(self):
        self.assertEqual(inclusive_range(3), [3])

    def test_forward(self):
        self.assertEqual(inclusive_range(5, 7), [5, 6, 7])

    def test_backward(self):
        self.assertEqual(inclusive_range(10, 8), [8, 9, 10])
