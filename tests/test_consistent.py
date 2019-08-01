import unittest

from hypothesis import given
from hypothesis.strategies import sets, integers

from spans import encode, decode, simplify

set_of_integers_strategy = sets(integers())


class TestConsistent(unittest.TestCase):
    @given(set_of_integers_strategy)
    def test_decode_inverts_encode(self, values):
        self.assertEqual(decode(encode(values)), values)

    @given(set_of_integers_strategy)
    def test_encode_returns_simplest_result(self, values):
        numbers = encode(values)
        self.assertEqual(simplify(numbers), numbers)
