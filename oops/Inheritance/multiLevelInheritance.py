class A:
    x = 1


class B(A):
    pass


class C(B):
    pass


cobj = C()

print(cobj.x)
