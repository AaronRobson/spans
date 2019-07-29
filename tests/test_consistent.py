import unittest

from hypothesis import given
from hypothesis.strategies import sets, integers

from spans import encode, decode


class TestConsistent(unittest.TestCase):
    @given(sets(integers()))
    def test_numbers_to_spans_and_back_should_be_the_same(self, values):
        self.assertEqual(decode(encode(values)), values)
