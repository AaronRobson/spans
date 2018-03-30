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

def Test():
    _givenNumbers1 = (1,)
    _givenNumbers3_4 = (3,4,)
    _givenNumbers = _givenNumbers1 + _givenNumbers3_4

    _s1 = Span(*_givenNumbers1)
    _s3_4 = Span(*_givenNumbers3_4)

    def TestSpanObject():
        assert _s1.start == _givenNumbers1[0]
        assert _s3_4.start == _givenNumbers3_4[0]

        assert _s1.finish == _givenNumbers1[0]
        assert _s3_4.finish == _givenNumbers3_4[1]

        assert _s1.single
        assert not _s3_4.single

        assert _s1.arguments == _givenNumbers1
        assert _s3_4.arguments == _givenNumbers3_4

        assert _s1 == _s1
        assert _s1 != _s3_4
        assert _s3_4 == _s3_4

        assert repr(_s1) == 'Span(%s)' % (str(_givenNumbers1[0]))
        assert repr(_s3_4) == 'Span(%s)' % (str(_givenNumbers3_4[0]) + ', ' + str(_givenNumbers3_4[1]))

        assert str(_s1) == str(_givenNumbers1[0])
        assert str(_s3_4) == str(_givenNumbers3_4[0]) + '-' + str(_givenNumbers3_4[1])

        assert tuple(iter(Span(5,7))) == (5,6,7,)

    def TestJoinSpans():
        assert JoinSpans([_s1]) == str(_givenNumbers1[0])
        assert JoinSpans([_s1, _s3_4]) == str(_givenNumbers1[0]) + ', ' + str(_givenNumbers3_4[0]) + '-' + str(_givenNumbers3_4[1])

    def TestNumbersToSpans():
        assert tuple(NumbersToSpans(_givenNumbers1)) == (_s1,)
        assert tuple(NumbersToSpans(_givenNumbers3_4)) == (_s3_4,)
        assert tuple(NumbersToSpans(_givenNumbers)) == (_s1,_s3_4,)

    def TestNumbersToRangeText():
        assert NumbersToRangeText(_givenNumbers1) == '1'
        assert NumbersToRangeText(_givenNumbers3_4) == '3-4'
        assert NumbersToRangeText(_givenNumbers) == '1, 3-4'

    TestSpanObject()
    TestJoinSpans()
    TestNumbersToSpans()
    TestNumbersToRangeText()

Test()

if __name__ == '__main__':
    EXAMPLE_NUMBERS = tuple(sorted([1,2,4,5,6,10]))
    print('The following numbers:\n%r\nMay be represented as:\n%r\n' % (EXAMPLE_NUMBERS, NumbersToRangeText(EXAMPLE_NUMBERS)))
