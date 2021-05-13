# lambda within user-defined function
# lambda param : expression


def add(num1):
    return lambda num2: num1 + num2


two = add(10)
print(two(20))

