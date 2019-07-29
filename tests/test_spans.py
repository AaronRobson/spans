#!/usr/bin/python

import unittest

from spans import Span, join_spans, numbers_to_spans

_givenNumbers1 = (1,)
_givenNumbers3_4 = (3, 4)
_givenNumbers = _givenNumbers1 + _givenNumbers3_4

_s1 = Span(*_givenNumbers1)
_s3_4 = Span(*_givenNumbers3_4)


class TestSpans(unittest.TestCase):

    def testSpanObject(self):
        self.assertEqual(_s1.start, _givenNumbers1[0])
        self.assertEqual(_s3_4.start, _givenNumbers3_4[0])

        self.assertEqual(_s1.finish, _givenNumbers1[0])
        self.assertEqual(_s3_4.finish, _givenNumbers3_4[1])

        self.assertTrue(_s1.single)
        self.assertFalse(_s3_4.single)

        self.assertEqual(_s1.arguments, _givenNumbers1)
        self.assertEqual(_s3_4.arguments, _givenNumbers3_4)

        self.assertEqual(_s1, _s1)
        self.assertNotEqual(_s1, _s3_4)
        self.assertEqual(_s3_4, _s3_4)

        self.assertEqual(
            repr(_s1),
            'Span(%s)' % (str(_givenNumbers1[0])))
        self.assertEqual(
            repr(_s3_4),
            'Span(%s)' % (
                str(_givenNumbers3_4[0]) +
                ', ' +
                str(_givenNumbers3_4[1])))

        self.assertEqual(str(_s1), str(_givenNumbers1[0]))
        self.assertEqual(
            str(_s3_4),
            str(_givenNumbers3_4[0]) + '-' +
            str(_givenNumbers3_4[1]))

        self.assertEqual(tuple(iter(Span(5, 7))), (5, 6, 7))


class TestJoinSpans(unittest.TestCase):
    def test(self):
        self.assertEqual(
            join_spans([_s1]), str(_givenNumbers1[0]))
        self.assertEqual(
            join_spans([_s1, _s3_4]),
            str(_givenNumbers1[0]) + ', ' +
            str(_givenNumbers3_4[0]) + '-' +
            str(_givenNumbers3_4[1]))


class TestNumbersToSpans(unittest.TestCase):
    def test(self):
        self.assertEqual(
            tuple(numbers_to_spans(_givenNumbers1)), (_s1,))
        self.assertEqual(
            tuple(numbers_to_spans(_givenNumbers3_4)), (_s3_4,))
        self.assertEqual(
            tuple(numbers_to_spans(_givenNumbers)),
            (_s1, _s3_4,))
