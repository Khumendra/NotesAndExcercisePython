def even_gen():
    n = 0

    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n


numbers = even_gen()
print(next(numbers))
print(next(numbers))
print(next(numbers))
