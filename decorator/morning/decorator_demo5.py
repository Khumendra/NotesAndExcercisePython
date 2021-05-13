# Passing function as Argument to other function


def add_one(number):
    return number + 1


def function(func):
    number = 5
    return func(number)


print(
    function(add_one)
)
