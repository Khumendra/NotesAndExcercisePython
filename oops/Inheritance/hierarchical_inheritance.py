class A(object):
    pass


class B(A):
    pass


class C(A):
    pass


print(
    issubclass(B, A) and issubclass(C, A)
)
