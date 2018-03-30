#!/usr/bin/python

import unittest

import spans


class TestSpans(unittest.TestCase):

    def setUp(self):
        self._givenNumbers1 = (1,)
        self._givenNumbers3_4 = (3,4,)
        self._givenNumbers = self._givenNumbers1 + self._givenNumbers3_4

        self._s1 = spans.Span(*self._givenNumbers1)
        self._s3_4 = spans.Span(*self._givenNumbers3_4)

    def testSpanObject(self):
        self.assertEqual(self._s1.start, self._givenNumbers1[0])
        self.assertEqual(self._s3_4.start, self._givenNumbers3_4[0])

        self.assertEqual(self._s1.finish, self._givenNumbers1[0])
        self.assertEqual(self._s3_4.finish, self._givenNumbers3_4[1])

        self.assertTrue(self._s1.single)
        self.assertFalse(self._s3_4.single)

        self.assertEqual(self._s1.arguments, self._givenNumbers1)
        self.assertEqual(self._s3_4.arguments, self._givenNumbers3_4)

        self.assertEqual(self._s1, self._s1)
        self.assertNotEqual(self._s1, self._s3_4)
        self.assertEqual(self._s3_4, self._s3_4)

        self.assertEqual(repr(self._s1), 'Span(%s)' % (str(self._givenNumbers1[0])))
        self.assertEqual(repr(self._s3_4), 'Span(%s)' % (str(self._givenNumbers3_4[0]) + ', ' + str(self._givenNumbers3_4[1])))

        self.assertEqual(str(self._s1), str(self._givenNumbers1[0]))
        self.assertEqual(str(self._s3_4), str(self._givenNumbers3_4[0]) + '-' + str(self._givenNumbers3_4[1]))

        self.assertEqual(tuple(iter(spans.Span(5,7))), (5,6,7,))

    def testJoinSpans(self):
        self.assertEqual(spans.JoinSpans([self._s1]), str(self._givenNumbers1[0]))
        self.assertEqual(spans.JoinSpans([self._s1, self._s3_4]), str(self._givenNumbers1[0]) + ', ' + str(self._givenNumbers3_4[0]) + '-' + str(self._givenNumbers3_4[1]))

    def testNumbersToSpans(self):
        self.assertEqual(tuple(spans.NumbersToSpans(self._givenNumbers1)), (self._s1,))
        self.assertEqual(tuple(spans.NumbersToSpans(self._givenNumbers3_4)), (self._s3_4,))
        self.assertEqual(tuple(spans.NumbersToSpans(self._givenNumbers)), (self._s1, self._s3_4,))

    def testNumbersToRangeText(self):
        self.assertEqual(spans.NumbersToRangeText(self._givenNumbers1), '1')
        self.assertEqual(spans.NumbersToRangeText(self._givenNumbers3_4), '3-4')
        self.assertEqual(spans.NumbersToRangeText(self._givenNumbers), '1, 3-4')

    def testExample(self):
        self.assertEqual(spans.NumbersToRangeText([1,2,4,5,6,10]), '1-2, 4-6, 10')


if __name__ == "__main__":
    unittest.main()