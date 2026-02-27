class NumberCollection:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self._generator()

    def _generator(self):
        current = self.start
        while current <= self.end:
            yield current
            current += 1

numbers = NumberCollection(1, 5)
for num in numbers:
    print(num)