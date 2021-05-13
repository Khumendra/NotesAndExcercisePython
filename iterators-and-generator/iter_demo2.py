numbers = [1, 2, 3]

value = numbers.__iter__()


print(value.__next__()) #1
print(value.__next__()) #2
print(value.__next__()) #3

# StopIteration
print(value.__next__())
