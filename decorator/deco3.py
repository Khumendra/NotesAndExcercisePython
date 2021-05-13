# passing function as an argument

def func(x):
    return x + 1


def func2(func, x):
    result = func(x)
    return result


print(
    func2(func, 4)
)
