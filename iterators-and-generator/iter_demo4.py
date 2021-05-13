# Working with for loop
numbers = [1, 4, 5]

# for num in numbers:
#     print(num)


iter_obj = iter(numbers)

while True:
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration:
        break
