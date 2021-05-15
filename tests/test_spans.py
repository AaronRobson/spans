#!/usr/bin/python

import unittest

from spans import Span, join_spans, numbers_to_spans

_given_numbers_1 = (1,)
_given_numbers_3_4 = (3, 4)
_given_numbers = _given_numbers_1 + _given_numbers_3_4

_s1 = Span(*_given_numbers_1)
_s3_4 = Span(*_given_numbers_3_4)


class TestSpans(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(_s1.start, _given_numbers_1[0])
        self.assertEqual(_s1.finish, _given_numbers_1[0])
        self.assertEqual(_s1.arguments, _given_numbers_1)

    def test_range_of_numbers(self):
        self.assertEqual(_s3_4.start, _given_numbers_3_4[0])
        self.assertEqual(_s3_4.finish, _given_numbers_3_4[1])
        self.assertEqual(_s3_4.arguments, _given_numbers_3_4)

    def test_equality(self):
        self.assertEqual(_s1, _s1)
        self.assertNotEqual(_s1, _s3_4)
        self.assertEqual(_s3_4, _s3_4)
        self.assertNotEqual(_s1, 'other object example')

    def test_repr(self):
        self.assertEqual(
            repr(_s1),
            'Span(%s)' % (str(_given_numbers_1[0])))
        self.assertEqual(
            repr(_s3_4),
            'Span(%s)' % (
                str(_given_numbers_3_4[0]) +
                ', ' +
                str(_given_numbers_3_4[1])))

    def test_str(self):
        self.assertEqual(str(_s1), str(_given_numbers_1[0]))
        self.assertEqual(
            str(_s3_4),
            str(_given_numbers_3_4[0]) + '-' +
            str(_given_numbers_3_4[1]))


class TestJoinSpans(unittest.TestCase):
    def test(self):
        self.assertEqual(
            join_spans([_s1]), str(_given_numbers_1[0]))
        self.assertEqual(
            join_spans([_s1, _s3_4]),
            str(_given_numbers_1[0]) + ', ' +
            str(_given_numbers_3_4[0]) + '-' +
            str(_given_numbers_3_4[1]))


class TestNumbersToSpans(unittest.TestCase):
    def test(self):
        self.assertEqual(
            tuple(numbers_to_spans(_given_numbers_1)), (_s1,))
        self.assertEqual(
            tuple(numbers_to_spans(_given_numbers_3_4)), (_s3_4,))
        self.assertEqual(
            tuple(numbers_to_spans(_given_numbers)),
            (_s1, _s3_4,))
