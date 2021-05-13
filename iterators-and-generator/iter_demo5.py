# create custom iterator


class Even:
    def __init__(self, max):
        self.num = 2
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


numbers = Even(10)

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))


