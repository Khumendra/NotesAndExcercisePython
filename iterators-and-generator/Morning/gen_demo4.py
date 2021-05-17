# infinite stream of data with generator
# fibonacci Series: 0, 1, 1, 2, 3, 5, ...


def gen():
    n = 0
    n += 2
    yield n

    n += 2
    yield n

    n += 2
    yield n


n = gen()
print(dir(n))
print(*n)
