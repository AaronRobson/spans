#!/usr/bin/python

import unittest

from spans import produce_parser


class TestProduceParser(unittest.TestCase):

    def setUp(self):
        parser = produce_parser()
        self.f = parser.parse_args

    def test_empty(self):
        self.assertEqual(self.f([]).values, [])

    def test_single(self):
        self.assertEqual(self.f(['1']).values, ['1'])

    def test_double(self):
        self.assertEqual(self.f(['1', '2']).values, ['1', '2'])

    def test_range(self):
        self.assertEqual(self.f(['1-3']).values, ['1-3'])
