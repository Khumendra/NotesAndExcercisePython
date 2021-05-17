def even(max):
    n = 2
    while n <= max:
        yield n
        n += 2


number = even(10)
print(number.__next__())
print(number.__next__())
print(number.__next__())
print(number.__next__())
print(number.__next__())
# exception
print(number.__next__())