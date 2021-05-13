items = [
    ('Product1', 10), 
    ('Product2', 11), 
    ('Product3', 12), 
]

x  = filter(lambda item: item[1] >= 11, items)

print(
    list(x)
)