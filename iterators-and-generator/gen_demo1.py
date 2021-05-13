def gen_even_number(max):
    n = 2

    while n <= max:
        yield n
        n += 2


numbers = gen_even_number(3)
# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

for x in numbers:
    print(x)