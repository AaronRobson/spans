'''Document programs tend to specify printing ranges like this:
"1-3,5" prints pages 1, 2, 3 and 5.
This program is designed to do the same.

Similar to this:
http://texblog.org/2007/05/28/mulitple-reference-citation/
'''

import argparse
from typing import Tuple, Iterator, Sequence, Set, Optional, Any


def encode(numbers: Set[int]) -> str:
    return join_spans(numbers_to_spans(numbers))


def decode(text: str) -> Set[int]:
    text = text.replace(',', ' ')
    output = set()
    for section in text.split():
        starts_with_minus = section.startswith('-')
        try:
            range_separator_index = section.index('-', int(starts_with_minus))
        except ValueError:
            output.add(int(section))
        else:
            first = int(section[:range_separator_index])
            second = int(section[range_separator_index + 1:])
            output.update(set(inclusive_range(first, second)))
    return output


def simplify(text: str) -> str:
    '''Reduce to its simplest form.'''
    return encode(decode(text))


def inclusive_range(first: int, second: Optional[int] = None) -> Sequence[int]:
    if second is None:
        second = first

    lower = min(first, second)
    higher = max(first, second)
    return list(range(lower, higher + 1))


class Span:
    def __init__(self, start: int, finish: Optional[int] = None) -> None:
        if finish is None:
            finish = start

        self.start = start
        self.finish = finish

    @property
    def arguments(self) -> Tuple[int, ...]:
        sequence = [self.start]
        if self.start != self.finish:
            sequence += [self.finish]

        return tuple(sequence)

    @property
    def arguments_as_strings(self) -> Iterator[str]:
        return map(str, self.arguments)

    def __eq__(self, other: Any) -> bool:
        try:
            return self.arguments == other.arguments
        except AttributeError:
            # Must therefore be a different type of object.
            return False

    def __repr__(self) -> str:
        return '%s(%s)' % (
            self.__class__.__name__,
            ', '.join(self.arguments_as_strings))

    def __str__(self) -> str:
        return '-'.join(self.arguments_as_strings)


def join_spans(spans: Sequence[Span]) -> str:
    return ', '.join(map(str, spans))


def numbers_to_spans(numbers: Set[int]):
    sequence = sorted(set(numbers))

    current_span = None
    last_sent = None
    for number in sequence:
        if current_span is None:
            current_span = Span(number)
        elif current_span.finish + 1 == number:
            current_span.finish += 1
        else:
            yield current_span
            last_sent = current_span
            current_span = Span(number)

    if (current_span is not None) and (current_span != last_sent):
        yield current_span


def produce_parser():
    example_input_sequence = ('1', '2', '3', '5-7', '10')
    example_input = ' '.join(example_input_sequence)
    example_output = simplify(example_input)
    example_text = ('example:\n\n$ python spans.py ' +
                    example_input + '\n' + example_output)

    parser = argparse.ArgumentParser(
        description='pass numbers to convert into spans.',
        epilog=example_text,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'values', type=str, nargs='*',
        help='a list of numbers and ranges of numbers')
    return parser


if __name__ == '__main__':
    parser = produce_parser()
    args = parser.parse_args()
    print(simplify(' '.join(args.values)))
