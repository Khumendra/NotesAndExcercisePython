# Operator Overloading
# print(10 + 20)
# a = 10
# b = 20
# print(int.__add__(a, b))
x = 10

print(x.__add__(20))


class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x


class B:
    def __init__(self, x):
        self.x = x

a = A(100)
b = B(200)

print(a + b)