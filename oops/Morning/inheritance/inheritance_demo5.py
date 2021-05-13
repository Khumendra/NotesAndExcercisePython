# Hybrid Inheritance


class A:
    message = "Message from A."


class B(A):
    message = "Message from B."


class C(A):
    message = "Message from C."

# order
class D(B, C):
    pass


obj_d = D()

print(
    obj_d.message
)
