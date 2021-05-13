items = [
    ('product1', 10),
    ('product2', 20),
    ('product3', 30),
    ('product1', 40),
    ('product2', 50),
    ('product3', 60),
]

filter_expression = lambda item: item[1] >= 30


print(
    list(filter(filter_expression, items))
    )
