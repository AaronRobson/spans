#!/usr/bin/python

import unittest

from spans import produce_parser


class TestProduceParser(unittest.TestCase):

    def setUp(self):
        parser = produce_parser()
        self.f = parser.parse_args

    def test_empty(self):
        self.assertEqual(self.f([]).numbers, [])

    def test_single(self):
        self.assertEqual(self.f(['1']).numbers, [1])

    def test_double(self):
        self.assertEqual(self.f(['1', '2']).numbers, [1, 2])
