'''It is how Printing of ranges and individual pages of a document can be specified in applications.
For instance:
"1-3,5" would print pages (1,2,3,5,).

Similar to this
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
            #Must therefore be a different type of object.
            return False

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, ', '.join(self.argumentsAsStrings))

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

if __name__ == '__main__':
    EXAMPLE_NUMBERS = tuple(sorted([1,2,4,5,6,10]))
    print('Number span compression for example the following numbers:\n%r\nMay be represented as:\n%r\n' % (', '.join(map(str, EXAMPLE_NUMBERS)), NumbersToRangeText(EXAMPLE_NUMBERS)))
    values = list(map(int, input('Enter numbers to compress span: ').replace(' ', '').split(',')))
    print(NumbersToRangeText(values))
