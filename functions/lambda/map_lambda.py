# lambda parameter: expression

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


print(
   list( map(lambda item: item[1], items))
)
