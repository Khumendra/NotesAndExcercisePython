# print price of all items


items = [
    ('product1', 10),
    ('product2', 20),
    ('product3', 30),
]


# price = []

# for item in items:
#     price.append(item[1])

# map(fun, iterable)

x = lambda item : item[1]

price= map(x, items)


print(list(price))


# for p in price:
#     print(p)


# map(fun, iterables) -------> map object
# you can loop over map object
# or list()