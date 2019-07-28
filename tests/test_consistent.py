import unittest

from hypothesis import given
from hypothesis.strategies import sets, integers

from spans import parse_numbers, numbers_to_range_text


class TestConsistent(unittest.TestCase):
    @given(sets(integers()))
    def test_numbers_to_spans_and_back_should_be_the_same(self, values):
        actual = parse_numbers(numbers_to_range_text(values))
        expected = values
        self.assertEqual(expected, actual)
