'''Document programs tend to specify printing ranges like this:
"1-3,5" prints pages 1, 2, 3 and 5.
This program is designed to do the same.

Similar to this:
http://texblog.org/2007/05/28/mulitple-reference-citation/
'''


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


def JoinSpans(spans):
    return ', '.join(map(str, spans))


def NumbersToSpans(numbers):
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


def NumbersToRangeText(numbers):
    return JoinSpans(NumbersToSpans(numbers))


def parse_numbers(numbersText):
    return list(map(int, numbersText.replace(' ', '').split(',')))


if __name__ == '__main__':
    EXAMPLE_NUMBERS = tuple(sorted([1, 2, 4, 5, 6, 10]))
    print(
        'Number span compression, for example the following numbers:' +
        '\n%r\nMay be represented as:\n%r\n' %
        (', '.join(
            map(str, EXAMPLE_NUMBERS)), NumbersToRangeText(EXAMPLE_NUMBERS)))
    numberText = input('Enter numbers to compress span: ')
    values = parse_numbers(numberText)
    print(NumbersToRangeText(values))
