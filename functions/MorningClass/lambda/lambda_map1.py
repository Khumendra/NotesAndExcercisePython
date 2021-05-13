# print price of all items


items = [
    ('Apple', 10),
    ('Orange', 20),
    ('Lemon', 30),
]


price = []

# for i in items:
#     # print(i)
#     price.append(i[1])

# print(    price )

func = lambda i : i[0]


product = map(func, items)
print(
    *list(product), sep=', '
    )
