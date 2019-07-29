#!/usr/bin/python

import unittest

from spans import inclusive_range


class TestInclusiveRange(unittest.TestCase):
    def test_forward(self):
        self.assertEqual(inclusive_range(5, 7), [5, 6, 7])
