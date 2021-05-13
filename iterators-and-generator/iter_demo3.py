numbers = [1, 2, 3]
value = iter(numbers)
# print(value)

item1 = next(value)
print(item1)


item2 = next(value)
print(item2)


item3 = next(value)
print(item3)

# StopIteration
item4 = next(value)
print(item4)


