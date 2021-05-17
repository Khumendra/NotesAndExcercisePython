# infinite stream of data with generator
# fibonacci Series: 0, 1, 1, 2, 3, 5, ...


def gen_fib():
    n1 = 0
    n2 = 1

    while True:
        yield n1
        n1, n2 = (n2, n1 + n2)


seq = gen_fib()

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
