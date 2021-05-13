def greet():
    return "Hello"


print(
    # greet()
)

# hello = greet()
hello = greet
# print(
#     # hello,
#     hello()
# )

del greet

# function are object that can be passed into other object
print(
    # greet(),
    hello()
)
