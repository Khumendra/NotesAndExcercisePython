
# Multiple Inheritance
# Multiple---> parent(A, B) classes ----> One Child Class


class A:
    pass


class B:
    pass


class C(A, B):
    pass


print(
    issubclass(C, A) and issubclass(C, B)
)
