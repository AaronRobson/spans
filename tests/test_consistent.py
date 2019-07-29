import unittest

from hypothesis import given
from hypothesis.strategies import sets, integers

from spans import encode, decode, simplify


class TestConsistent(unittest.TestCase):
    @given(sets(integers()))
    def test_decode_inverts_encode(self, values):
        self.assertEqual(decode(encode(values)), values)

    @given(sets(integers()))
    def test_encode_returns_simplest_result(self, values):
        numbers = encode(values)
        self.assertEqual(simplify(numbers), numbers)
