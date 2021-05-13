class A:
    x = 1


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


dobj = D()
print(dobj.x)
