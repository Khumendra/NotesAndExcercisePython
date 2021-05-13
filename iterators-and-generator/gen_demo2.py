# fibonacci series
# 0, 1, 1, 2, 3


def gen_fibonacci():
    n1 = 0
    n2 = 1
    while True:
        yield n1
        n1, n2 = (n2, n1 + n2)


seq = gen_fibonacci()
# print(next(seq), end=', ')
# print(next(seq), end=', ')
# print(next(seq), end=', ')
# print(next(seq), end=', ')
# print(next(seq), end=', ')
# print(next(seq), end=' ')
