def upper_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


@upper_decorator
def say_hi():
    return "Hello There!"


# decorate = upper_decorator(function=say_hi)
print(
    say_hi()
)
