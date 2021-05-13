
def even_gen(max):
    n = 2
    while n <= max:
        yield n
        n += 2
numbers = even_gen(4)
print(next(numbers))
print(next(numbers))
print(next(numbers))