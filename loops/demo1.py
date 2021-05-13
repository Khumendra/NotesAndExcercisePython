# for x in range(1, 11):
#     print(x)


# number = 5

# for i in range(number):
#     print("x"*i)


# iterators

# string
# name = "Khumendra"

# for x in name:
#     print(x, end='')

# Looping over list

# fruits = ['apple', 'banana', 'mango']

# for f in fruits:
#     print(f)

# list comprehension
# number = [x for x in range(10)]
# print(number)


# loop over tuple
# number = tuple(x for x in range(10))
# print(number)


# loop over set
fruits = {'mango', 'banana', 'apple'}
# values = { x for x in fruits }
# print(values)

# li = []
# for f in fruits:
#     li.append(f)

# print(li)


# Loop over the dictionary

di = {
    'name': 'Vikash',
    'age': 21,
    'phone': '09876543211'
}
 
# for x in di:
#     print(x, di[x])

# for x in di.values():
#     print(x)

for x, y in di.items():
    print(x, y)