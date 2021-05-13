# Hierarchial Inheritance
# More than one class inherits from a class

class A:
    pass

class B(A):
    pass

class C(A):
    pass

print(
    issubclass(C, A) and issubclass(B, A)
)