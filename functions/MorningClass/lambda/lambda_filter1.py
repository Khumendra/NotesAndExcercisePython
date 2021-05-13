items = [
    ('Apple', 10),
    ('Orange', 20),

    ('Lemon', 30),
    ('Mango', 40),
    
    ('Cold Drink', 50),
    ('Biscuits', 60),
    ('Books', 70),

]
filter_expression = lambda item: item[1] <= 30

filtered_object = filter(filter_expression, items)
print(
    *list(filtered_object),
    # sep='\n'
    )

