'''Document programs tend to specify printing ranges like this:
"1-3,5" prints pages 1, 2, 3 and 5.
This program is designed to do the same.

Similar to this:
http://texblog.org/2007/05/28/mulitple-reference-citation/
'''

import argparse


class Span:
    def __init__(self, start, finish=None):
        if finish is None:
            finish = start

        self.start = start
        self.finish = finish

    @property
    def single(self):
        return self.start == self.finish

    @property
    def arguments(self):
        sequence = [self.start]
        if not self.single:
            sequence += [self.finish]

        return tuple(sequence)

    @property
    def argumentsAsStrings(self):
        return map(str, self.arguments)

    def __eq__(self, other):
        try:
            return self.arguments == other.arguments
        except AttributeError:
            # Must therefore be a different type of object.
            return False

    def __repr__(self):
        return '%s(%s)' % (
            self.__class__.__name__,
            ', '.join(self.argumentsAsStrings))

    def __str__(self):
        return '-'.join(self.argumentsAsStrings)

    def __iter__(self):
        return iter(range(self.start, self.finish+1))


def join_spans(spans):
    return ', '.join(map(str, spans))


def numbers_to_spans(numbers):
    sequence = sorted(set(numbers))

    currentSpan = None
    lastSent = None
    for number in sequence:
        if currentSpan is None:
            currentSpan = Span(number)
        elif currentSpan.finish + 1 == number:
            currentSpan.finish += 1
        else:
            yield currentSpan
            lastSent = currentSpan
            currentSpan = Span(number)

    if (currentSpan is not None) and (currentSpan != lastSent):
        yield currentSpan


def numbers_to_range_text(numbers):
    return join_spans(numbers_to_spans(numbers))


def parse_numbers(numbersText):
    numbersText = numbersText.replace(',', ' ')
    output = set()
    for section in numbersText.split():
        if section.startswith('-'):
            try:
                range_separator_index = section[1:].index('-') + 1
            except ValueError:
                range_separator_index = None
        else:
            try:
                range_separator_index = section.index('-')
            except ValueError:
                range_separator_index = None

        if range_separator_index is None:
            output.add(int(section))
        else:
            first = int(section[:range_separator_index])
            second = int(section[range_separator_index + 1:])
            lower = min(first, second)
            higher = max(first, second)
            output.update(set(range(lower, higher + 1)))
    return output


def produce_parser():
    example_input = '1 2 4 5 6 10'
    example_output = numbers_to_range_text(parse_numbers(example_input))
    example_text = ('example:\n\n$ python spans.py ' +
                    example_input + '\n' + example_output)

    parser = argparse.ArgumentParser(
        description='pass numbers to convert into spans.',
        epilog=example_text,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'numbers', type=int, nargs='*',
        help='a list of numbers')
    return parser


if __name__ == '__main__':
    parser = produce_parser()
    args = parser.parse_args()
    print(numbers_to_range_text(args.numbers))
